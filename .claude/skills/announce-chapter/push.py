#!/usr/bin/env python3
"""Push announcement files into the Typefully queue.

Usage:
    push.py announcements/01-the-frozen-brain.md [more files...]
    push.py --dry-run announcements/[0-9]*.md

Each file becomes one Typefully draft with X, LinkedIn, and Bluesky content,
planned into the next free queue slot. Planned drafts are inert: nothing is
published until you approve it inside Typefully. Flags:

    --dry-run     validate and print what would be sent, no network calls
    --unplanned   create the draft without a queue slot
    --publish-now publish immediately instead of planning (use sparingly)

Needs TYPEFULLY_API_KEY (Typefully -> Settings -> API). If the key can see
more than one social set, set TYPEFULLY_SOCIAL_SET_ID too; the script lists
the candidates when it can't choose.
"""

import json
import os
import re
import sys
import urllib.error
import urllib.request

API_BASE = "https://api.typefully.com/v2"
# Typefully platform keys for the sections we write, in file order.
PLATFORMS = {"X": "x", "LinkedIn": "linkedin", "Bluesky": "bluesky"}
# X wraps every link in t.co, which costs a flat 23 characters.
X_LINK_LEN = 23
X_LIMIT = 280
BSKY_LIMIT = 300


def parse_announcement(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        raise ValueError(f"{path}: missing frontmatter")
    meta = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, val = line.split(":", 1)
            meta[key.strip()] = val.strip()
    body = text[m.end():]
    sections = {}
    for name in PLATFORMS:
        sm = re.search(rf"^## {name}\n(.*?)(?=^## |\Z)", body, re.DOTALL | re.MULTILINE)
        if sm:
            sections[name] = sm.group(1).strip()
    return meta, sections


def x_length(post):
    return len(re.sub(r"https?://\S+", "x" * X_LINK_LEN, post))


def validate(path, meta, sections):
    errors = []
    for field in ("title", "url"):
        if not meta.get(field):
            errors.append(f"frontmatter is missing '{field}'")
    if not sections:
        errors.append("no '## X' / '## LinkedIn' / '## Bluesky' sections found")
    for name, post in sections.items():
        if meta.get("url") and meta["url"] not in post:
            errors.append(f"{name} post does not contain the chapter url")
    if "X" in sections and x_length(sections["X"]) > X_LIMIT:
        errors.append(f"X post is {x_length(sections['X'])} chars (limit {X_LIMIT}, links count as {X_LINK_LEN})")
    if "Bluesky" in sections and len(sections["Bluesky"]) > BSKY_LIMIT:
        errors.append(f"Bluesky post is {len(sections['Bluesky'])} chars (limit {BSKY_LIMIT})")
    if errors:
        for e in errors:
            print(f"  ERROR {path}: {e}", file=sys.stderr)
    return not errors


def build_payload(meta, sections, schedule):
    platforms = {
        PLATFORMS[name]: {"enabled": True, "posts": [{"text": post}]}
        for name, post in sections.items()
    }
    payload = {"draft_title": f"PRA book: {meta['title']}", "platforms": platforms}
    if schedule == "plan":
        payload["plan_at"] = "next-free-slot"
    elif schedule == "now":
        payload["publish_at"] = "now"
    return payload


def api(method, path, key, body=None):
    req = urllib.request.Request(
        API_BASE + path,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
        method=method,
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        print(f"  API {method} {path} failed: {e.code} {e.read().decode(errors='replace')}", file=sys.stderr)
        raise SystemExit(1)


def social_set_id(key):
    override = os.environ.get("TYPEFULLY_SOCIAL_SET_ID")
    if override:
        return override
    data = api("GET", "/social-sets", key)
    sets = data if isinstance(data, list) else next(
        (data[k] for k in ("results", "data", "social_sets") if isinstance(data.get(k), list)), None)
    if sets is None:
        raise SystemExit(f"unexpected /social-sets response: {json.dumps(data)[:400]}")
    if len(sets) == 1:
        return sets[0]["id"]
    listing = ", ".join(f"{s.get('name', '?')}={s['id']}" for s in sets)
    raise SystemExit(f"multiple social sets ({listing}); set TYPEFULLY_SOCIAL_SET_ID")


def main(argv):
    flags = {a for a in argv if a.startswith("--")}
    files = sorted(a for a in argv if not a.startswith("--"))
    unknown = flags - {"--dry-run", "--unplanned", "--publish-now"}
    if unknown or not files:
        print(__doc__, file=sys.stderr)
        return 2
    schedule = "now" if "--publish-now" in flags else "none" if "--unplanned" in flags else "plan"
    dry = "--dry-run" in flags

    parsed, ok = [], True
    for path in files:
        meta, sections = parse_announcement(path)
        ok &= validate(path, meta, sections)
        parsed.append((path, meta, sections))
    if not ok:
        return 1

    if dry:
        for path, meta, sections in parsed:
            counts = ", ".join(
                f"{n}={x_length(p) if n == 'X' else len(p)}" for n, p in sections.items())
            print(f"{path}: ok ({counts}, schedule={schedule})")
        return 0

    key = os.environ.get("TYPEFULLY_API_KEY")
    if not key:
        raise SystemExit("TYPEFULLY_API_KEY is not set (Typefully -> Settings -> API)")
    set_id = social_set_id(key)
    for path, meta, sections in parsed:
        draft = api("POST", f"/social-sets/{set_id}/drafts", key,
                    build_payload(meta, sections, schedule))
        print(f"{path}: draft {draft.get('id', '?')} {draft.get('status', '')}".rstrip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
