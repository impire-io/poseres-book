---
name: announce-chapter
description: Draft and queue the social announcement for a book chapter — X, LinkedIn, and Bluesky copy in the book's voice, written to announcements/, pushed as an inert planned draft into the Typefully queue. Use when a chapter lands, when asked to announce a chapter or the book, or to queue the backfill spotlights.
---

# Announce a chapter

Every released chapter gets one announcement file in `announcements/` holding
the post copy for X, LinkedIn, and Bluesky, and one Typefully draft planned
into the next free queue slot. Planned drafts are inert: the owner gives the
final go inside Typefully, so pushing is safe; the review that matters
happens on the file, here.

## 1. Identify the chapter

The argument is a chapter number or a path. Resolve it against
`src/SUMMARY.md`; the announcement file takes the chapter file's name:
`src/part-3-the-mechanism/09-wanting-things.md` →
`announcements/09-wanting-things.md`. Chapter pages are live at
`https://impire.io/poseres-book/<part-dir>/<chapter-file>.html`.

If an announcement file for the chapter already exists, this is a revision
pass: re-read it against the chapter and fix, don't duplicate.

## 2. Read before writing

In order: `STYLE.md` (the contract — it binds announcement copy in full),
`announcements/README.md` (the file format and platform limits),
`announcements/00-book-launch.md` (a worked example), then the chapter
itself, in full.

## 3. Draft

Write the announcement file. The hook is a sentence or image from the
chapter, quoted or lightly trimmed; every claim in a post must appear in the
chapter; the banned list applies with zero tolerance; at most one em dash
per file. X ≤ 280 characters with links counting 23; Bluesky ≤ 300 counting
everything; LinkedIn is 2–4 short paragraphs. Each post ends with the
chapter URL. No hashtags, no exclamation marks.

## 4. Check

```
.claude/skills/announce-chapter/push.py --dry-run announcements/<file>.md
```

validates structure and lengths. Then grep the file for the STYLE.md banned
list and reread the chapter's opening to confirm the hook is really the
chapter's own wording. Show the owner the copy for review.

## 5. Push

Once the file is approved (or when running the backfill queue):

```
.claude/skills/announce-chapter/push.py announcements/<file>.md
```

Needs `TYPEFULLY_API_KEY` (Typefully → Settings → API); set
`TYPEFULLY_SOCIAL_SET_ID` too if the key sees several social sets. The
draft lands planned in the next free queue slot with all three platforms
attached. The whole backfill goes up in chapter order with
`push.py announcements/[0-9]*.md`.

`--publish-now` exists for the rare "send it right now" ask; never use it
unprompted.
