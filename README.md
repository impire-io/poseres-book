# The PRA book

A book about the Pose Resolution Architecture: why frozen models fail, what a
sensorimotor triplet is, and how a population of competing frames learns
structure nobody specified.

The project the book describes lives at
[impire-io/poseres](https://github.com/impire-io/poseres). This repo holds the
text, the audiobook kit, and the tooling that keeps the two in step.

Read `STYLE.md` before writing a single sentence. It is the contract.

## Layout

```
book.toml              mdBook config — `mdbook serve` to read locally
src/
  SUMMARY.md           the table of contents mdBook renders
  00-a-note-before-we-start.md
  part-1-the-problem/
    01-....md          one chapter per file, numbered for order
  part-2-the-triplet/
  part-3-the-mechanism/
  part-4-the-continuity-guarantee/
  part-5-the-long-run/
  part-6-teachers/
  GLOSSARY.md          every plain-words definition, in order of appearance
  ACKNOWLEDGMENTS.md
audiobook/             narration scripts, EPUB builder, ElevenLabs kit
STYLE.md               the writing contract — voice, two-lane rule, AI-tell bans
NOTES-ai-tells.md      research notes behind the style rules (not part of the book)
outline.md             the working outline (parts → chapters → beats)
REVISIT.md             open questions and drift found against the project record
SOURCES.lock           the poseres commit the book was last synced against
```

Chapter titles live in the file's H1, not the filename. Figures go in
`figures/` next to the chapter that uses them, as SVG where possible. New
chapters get an entry in `src/SUMMARY.md`.

## Working rules

- Chapters cite the project record: when a chapter tells a story from the
  poseres repo's `hq/04-JOURNEY/`, link the episode and commits it draws on in
  an HTML comment at the top of the file, so claims stay checkable as the code
  moves.
- Empirical numbers in the book are snapshots. Each one carries a comment
  noting where it was measured, so a later edition can re-verify or update.
- The `/sync-from-pra` skill (in `.claude/skills/`) checks the book against a
  sibling checkout of the poseres repo: new episodes since `SOURCES.lock`,
  citations that moved, numbers that drifted. Findings land in `REVISIT.md`.
- Every merged chapter passes the revision checklist at the bottom of
  `STYLE.md`.

## Building

```
mdbook serve    # read at http://localhost:3000
mdbook build    # static site in book/
```

Pushes to `main` deploy via GitHub Actions to GitHub Pages.

## Rights

© Daan Gerits. All rights reserved. The text is public to read; it is not
licensed for reuse, redistribution, or training.
