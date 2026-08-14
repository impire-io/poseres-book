---
name: sync-from-pra
description: Check the book against the poseres (pra) repo — surface new journey/research material since SOURCES.lock, verify every chapter's "Draws on" citations, flag drifted snapshot numbers. Findings go to REVISIT.md; the lock is bumped when a pass completes. Use when asked to sync the book, check the book against the project, or after notable pra episodes land.
---

# Sync the book from the poseres repo

The book repo is downstream of the project repo
(github.com/impire-io/poseres, checked out locally as the pra repo). This
skill is the link: it finds what moved in the project since the book last
looked, and what the book claims that the project record no longer
supports. It **reports**; it does not rewrite chapters unless the owner
asks for drafts.

## 0. Locate the project repo

Try, in order: `../pra`, `../poseres` (siblings of this repo), then the
`PRA_REPO` environment variable. Verify with
`git -C <path> remote get-url origin` containing `impire-io/poseres`.
If none found, stop and ask where the checkout lives.

Do not fetch or pull it — sync against the checkout as it stands, and
report its HEAD so the owner knows what the pass saw.

## 1. Read the lock

`SOURCES.lock` at the repo root holds the poseres commit of the last
completed pass:

```
poseres <full-sha>
```

If the sha is unknown in the checkout, say so and continue with a
best-effort pass against HEAD (the lock may predate a history rewrite).

## 2. New material since the lock

```
git -C <pra> log --oneline --no-merges <lock-sha>..HEAD -- hq/04-JOURNEY hq/01-RESEARCH hq/02-DESIGN
```

For each new journey episode, research conclusion, or design doc:
read it, then judge against `outline.md` and the existing chapters
whether it is (a) new chapter material, (b) an update to a story a
chapter already tells, or (c) irrelevant to the book. Record (a) and (b)
in REVISIT.md; skip (c) silently.

## 3. Citation audit

Every chapter under `src/` opens with an HTML comment:

```html
<!-- Draws on: journey 0010 (positioning vs frozen intelligence);
     hq/01-RESEARCH/motivation-stack/README.md (G3 src closure). -->
```

For each chapter:

- Resolve every cited episode number to `hq/04-JOURNEY/<nnnn>-*.md` and
  every cited path, at the checkout's HEAD. A citation that no longer
  resolves is a finding (look for the renamed successor and name it).
- Where a chapter's central claim leans on the cited source, skim the
  source: if the record has since amended, reversed, or superseded the
  claim (later episodes often revise earlier ones), that is a finding.
  Cite the superseding episode.

## 4. Snapshot numbers

Chapters carry empirical numbers as snapshots, each with a comment noting
where it was measured. Re-check each number against its cited source at
HEAD. A number that drifted is a finding — report old vs new and the
source; do not silently edit the prose.

## 5. Report and bump the lock

Append one dated section to `REVISIT.md`:

```markdown
## Sync 2026-08-14 (poseres <short-sha>)

- [ ] ch 13: journey 0097 supersedes the c1c closing numbers — ...
- [ ] part 6 candidate: episode 0099 (native survival) — ...
```

One line per finding: chapter (or "candidate"), source, what moved.
If nothing moved, add the section anyway with "no drift found" — the
lock bump needs a witness.

Then update `SOURCES.lock` to the checkout's HEAD sha and commit the
book-repo changes (signed, as always). The lock only moves when the pass
ran to completion — a partial pass leaves it alone and says so.

## Boundaries

- Read-only toward the pra repo, always.
- Chapter prose changes are a separate, owner-driven step; this skill
  ends at REVISIT.md findings (drafts only when explicitly asked).
- STYLE.md governs any drafted text; read it first if drafting.
