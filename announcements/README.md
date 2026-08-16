# Announcements

One file per release: the book launch, then one spotlight per chapter. Each
file holds the post copy for every platform we target, written once, reviewed
like any other text in this repo, and pushed into the Typefully queue by
`.claude/skills/announce-chapter/push.sh`.

The copy is part of the book. STYLE.md applies in full: the builder's voice,
the banned list, the em-dash budget, no invented facts. A post may only claim
what the chapter it links to actually says. The hook is a sentence from the
chapter itself, quoted or lightly trimmed, because the chapter's own voice is
the advertisement.

## File format

Files are named after the chapter file they announce: `01-the-frozen-brain.md`
points at `src/part-1-the-problem/01-the-frozen-brain.md`. The launch post is
`00-book-launch.md`.

```markdown
---
chapter: 01
title: The brain in the freezer
url: https://impire.io/poseres-book/part-1-the-problem/01-the-frozen-brain.html
---

## X

Post text, 280 characters or fewer (the URL counts as 23). Ends with the URL.

## LinkedIn

A few short paragraphs, same voice. Ends with the URL. No hashtag pile.

## Bluesky

Post text, 300 characters or fewer. Ends with the URL.
```

The push script parses the `## X` / `## LinkedIn` / `## Bluesky` headings
exactly; keep them as-is and put nothing else at that heading level.

## Queueing

Spotlights go out in chapter order. The book is an argument that builds, so
the drip reads as a serial: whoever joins at chapter 6 can walk back to
chapter 1 and catch up. Cadence lives in Typefully's queue slots (two per week
to start); the push script plans each draft into the next free slot rather
than timestamping it here.

New chapters join the same rhythm: land the chapter, run `/announce-chapter`,
review the file, push.
