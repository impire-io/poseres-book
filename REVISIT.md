# Revisit list

Working file, not part of the book. Cleared 2026-08-13 in a full
arbitration pass with Daan (rulings recorded in journey 0098); what
remains below is gated on future events, not on decisions.

## Publication gate (run before any release)

- [ ] **Numbers audit**: re-verify every empirical claim against the repo
  at publication date. All discrepancies found in the 2026-07-27 audit
  were fixed or arbitrated 2026-08-13; this item is about drift *after*
  that date (the record moves fast — journey is at 0097 while the book's
  chapters snapshot July–early August).
- [ ] **Audiobook regeneration**: every chapter changed on 2026-08-13
  (voice sweep + arbitration fixes); `audiobook/scripts/` regenerated
  2026-08-14 from the revised chapters, but the elevenlabs previews and
  epub still predate the sweep. Rebuild those before narration work.
- [ ] **Glossary + cross-reference final pass** once chapter numbering is
  frozen. (Part renumber done 2026-08-13: teachers are Part 6, the long
  run is Part 5; encoder/decoder/snapshot entries added.)
- [ ] **Reading-ease measurement** for ch 9–16 (target grade 6–8,
  mechanism chapters may run higher; ch 9 measured 9.2 on 2026-08-13).
- [ ] Mirror the Thousand Brains acknowledgment (`ACKNOWLEDGMENTS.md`,
  ruled 2026-08-13) into the audiobook front/back matter at production.
- [ ] Narration version of `00-a-note-before-we-start.md` (the intro is
  front matter; the audiobook's "A note before we start" currently
  covers editions only — merge or sequence the two at production).

## Waiting on the project, not on the book

- [ ] **Ch 4 worked triplet**: replace the constructed illustrative values
  with a real logged triplet from a pra-rover run (trivially dumpable;
  needs an actual run, not a decision).
- [ ] **Ch 16 endurance deciles**: the run was live at drafting; update
  the "still going as I write this" material when the reach arc's
  numbers are in. Part 6 gap: episodes 0074–0075 (brain-side hold, inert
  label, meter) are chapter material once the arc concludes.
- [ ] **E3.1 registration wording** (record discrepancy caught by the
  ch 16 writer): pillar/wall coordinates in the registration don't match
  the world file. Reconcile in an hq record-keeping commit — an hq task
  parked here so the book's audit trail stays whole.
- [ ] **Ch 5 length** (~870 words, shortest): reconsider once the full
  arc stands at final chapter count.

## Standing notes (decisions, recorded so they aren't relitigated)

- Voice rules of 2026-08-13 (STYLE.md "Told, not presented",
  "Verbs stay verbs"): book-wide sweep applied same day. The audit's
  paragraph-final-aphorism and fragment-triple flags (~150) were
  reviewed and deliberately retained as voice; only virtue
  announcements, bare chapter citations, and Daan's flagged fluency
  passages were rewritten.
- Terminology: **motivation** is the canonical word for what the drive
  encodes (glossary updated). Chapter titles keep their verbal forms
  ("Wanting things", "Wanting follows expecting") — titles are story,
  not terminology.
- best_dim in main text (ch 8, 12): kept — both are quoted instrument
  readouts. Bold cheat labels (ch 7) and "(motors forward!)" (ch 6):
  kept, codified in STYLE.md. Part intro pages: no.

## Sync 2026-09-27 (poseres 6966ffb)

Pass against the sibling checkout at HEAD 6966ffb (main, pushed and
released through ebae812 = v2.5.0; 6966ffb adds only the open research
topic the-arena-revival, nothing to read yet). Lock moved from 1c876502
(2026-08-14, journey 0098): 153 commits, episodes 0099–0123, designs
0013–0021 new, 0005/0008/0010/0011 amended. No trail doc under
hq/02-DESIGN/validate/ and no episode 0001–0098 changed, so ch 1–15's
cited numbers cannot have drifted; what moved is research folders
removed at graduation, new designs, and the new episodes. Items marked
(pre-lock) were already true at the last sync and were not on this list.

Candidates (new chapter material):

- [ ] part 6 close / part 7 opener candidate: episodes 0100–0106 (the palate, the last crack, native survival, distal senses, the flood) — released into Minecraft's own hunger economy the taught brain could see food, price it (palate A1 11/11), and still starve parked at a melon because the dig released its own hold at mining 0.97; the vote was a knife-edge re-fought every frame (release margins 0.00002–0.069 vs hold ≈0.008); commitment fixed it in a day (first eat step 333 vs the record's 1,119); the composition then lived two 100,501-step lives (99.3% / 98.1% fed, zero starvation) with the synthetic meter retired, and that body became the default (obs 86 / 13, v2.2.0). Closes ch 14's motivation map; ch 16's last line hands off to it.
- [ ] part 7 candidate: episodes 0109–0111 + 0113 (other bodies) — a second body made the world MORE predictable (−37.9% / −25.3% error), a two-melon larder made it lethal (below-12 1.000 vs solo 0.000), the peers sense bought nothing at any scarcity rung, and neither renewal rate nor separated patches opened a middle: the war is decided in the birth minute. Three registered nulls, one lesson ("a sense pays only where behavior has slack"); hold or write.
- [ ] part 7 candidate: episodes 0112, 0114, 0115, 0116 (the language road) — pays off ch 5's hook: flat actions starve at vocabulary scale (0/24 at A = 1024) while a product anchor predicts an untried act as well as a practiced one (0.0409 ≡ 0.0414); mobility priced by evidence absorbs exceptions (24/24 at 1.559×, pinned control fails 21/24); the kernel learns sequence worlds unmodified but a competence envelope binds, and the envelope is shared — the itch without incumbency +32%, then the frames hold the wall (R(4) 0.769 under the 2.0 line), confirming episode 0042's prediction.
- [ ] part 7 candidate: episodes 0117–0119 (compositional frames, the opaque world) — the owner set the gate as references between frames; the lab reversed it by its own condition (best variant +0.128 ± 0.138 SE against a tower that is a real rival, R(4) 1.231 vs 0.769); the wild made every shape indistinguishable (16 lives/arm: flat 41, tower 25, bind-pred 38 eats, all inside spread) with the feared lifecycle costs benign. A ch 6 hook: can rival guessers point at each other?
- [ ] part 7 candidate: episodes 0120–0123 (the long carry, the ladder) — the deciding arena built (N = 3 laps, chain ≈ 620–650 steps, 6× the probe world; aliased laps decode at chance 0.5039 vs 0.5036 ± 0.063; the day clock leaked the lap until pinned); zero chains in all 16 lives, flat and stage-sensing sibling alike; three gaps isolated (4,672 steps pressing a closed gate; 15 taught laps → 0 recipes; a sensed stage inert at selection) and shipped in two days as 045/046/047 (v2.3.0–v2.5.0, off by default, bit-exact off). Ends on a registered, unrun comparison as ch 16 does; the-arena-revival (opened 2026-09-27) is where it continues.
- [ ] fold-in, not a chapter: episodes 0107–0108 — design 0016 is the measured close of ch 14's map; provisioning graduated abandoned (native lives first-eat unaided within ~2k steps, so there is no stipend to wean).

Updates to existing chapters:

- [ ] ch 1: journey 0010's language non-goal — reversed (pre-lock, 0042) to a gated horizon, confirmed post-lock (0116, 0117); the prose already hedges.
- [ ] ch 5: episodes 0112–0116 ARE "the first measurements ... at the far end of the book" — nothing at the far end carries them yet.
- [ ] ch 6: episodes 0118–0119 — the flat population is now a measured default (a tower beats flat on the lab world, nothing beats the tower, nothing beats flat in the wild); 0112/design 0019 refutes the flat per-action transition at vocabulary scale (product anchor named, not shipped).
- [ ] ch 9: 0107/design 0016 places the drive as one layer of a measured stack; the survival stack runs frontier + itch + hold + commitment. "The shipped drive became competence" is imprecise — design 0007's default is `{curiosity: 1.0}`, competence is the measured recommendation (glossary too).
- [ ] ch 10 (pre-lock nuance): 0068 R3 — under cap 1.2 the no-rot clause fired on c1c (pred-err 0.101 → 0.164), qualified as an eviction-sweep regime change, not rot.
- [ ] ch 13 (pre-lock): 0078's mirrored map touches "dig at the block ahead" and the "digs stopped finishing" reading — the c1c record stands as measured; its sensed world was mirrored.
- [ ] ch 14: 0107/design 0016 measures the map the chapter calls "a judgment, not a measurement": filter = the world's hunger (0103); the deficit gate INVERTED live and is parked off (below-12 0.452 gated vs 0.007); the layer's real form is the flood — sensation beats valuation at the seam; G2 never ran.
- [ ] ch 14: "grinding twin ... carried forward" — superseded by 0101/design 0014: completion = itch begins + commitment finishes; the perseveration twin measured (517-frame dig lock) and closed by the intention boundary.
- [ ] ch 14: "both test worlds are paradise" — superseded by 0103/0104: the world's own hunger is the floor, the synthetic budget retired, the survival body the default.
- [ ] ch 14–16 (pre-lock): the lab "stand-in the rig can copy and restart" — 0097 deleted the FakeBridge estate at v2.0.0; the gate results stand, the instrument no longer exists in the code.
- [ ] ch 15: the closing open question (praise as want, E3.1) — 0107 files it as borrowed goals' twin; open as design, no longer the current edge. "Nothing in the shipped product holds position" — superseded (pre-lock) by 0077: feature 041 ships the hold over predicted positions; 0079 reads no drift over 25M steps.
- [ ] ch 16: "The run is still going as I write this" / "target fifty million" — superseded (pre-lock) by 0079 and C1D-LAB-RUN-PLAN.md "Readings — the run complete": closed by the amended goal rule at 75,359 chains / 25,003,001 steps; chains per fifth 15,187 / 15,540 / 15,298 / 14,518 / 14,816; dwell 99.976–99.981% per fifth; zero deaths; energy low 0.855 just past weaning; 500/500 segments with chains. Was on the waiting list; the record delivered it before the last lock and the chapter was never updated.
- [ ] ch 16: the meter and the stipend — 0103 retired the harness-meter layer (drain, pay, taper, stipend) for the world's own hunger; 0108 provisioning graduated abandoned.
- [ ] ch 16: dig flake "native to mineflayer" and "that is where the next chapter starts" — 0078 (pre-lock): the bridge's own `aheadColumn()` was mirrored and half-block-shifted since feature 027 (c1c mined its diagonal-rear neighbour for sixteen days; fix probes 20/20 + 20/20); 0093 B2′ ref/2×/5× 20/20, 10× 10/20, M* = 5; 0096 c1e closed ("the scenario was the tangent"); 0103 is the answer. No ch 17 exists.
- [ ] ch 16: "named successor: recombination" — delivered (pre-lock) by 0086/0087: fragments compose 24/24 with no splice, the ladder holds to depth four. In no chapter.
- [ ] ch 16: recipe memory "one recipe per finished item, the last demonstration" — amended by 0121–0123: place-keyed futility, process recipes (a gainless applauded demonstration stores the walked path), stage-conditional eligibility; design 0021 carries the ladder, design 0010 the mechanism.
- [ ] ch 16: Doc 0009's hold-drift reversal watch — closed unfired by 0079.
- [ ] appendix brain: the table says motivation and recipe memory are snapshotted — recipe.py: "policy-side state, deliberately not snapshot state in v1"; futility follows the recipe rule; snapshot.py carries only `policy_mode`. Pre-existing, not drift.
- [ ] appendix brain: "each dial defaults to the measured operating point of design 0015" — the code ships every 040–047 dial off (`label_beta` / `deficit_kappa` / `commit_kappa` / `event_head_eta` = 0.0); design 0011's column is "Measured point", not default. Pre-existing.
- [ ] appendix brain: dials list lacks `futility_k` / `futility_w` (0121), `stage_tolerance` (0123), and the RecipeMemory `process` door (0122).
- [ ] appendix body: no drift (obs 86 / 13 re-verified against the anatomy declaration order and the 027 adapter contract). Informational: the opt-in peers (94/13, 0110) and laps (0120) senses exist, not default.
- [ ] glossary: "the stipend" / "provisioning" — superseded (0103, 0108); "recipe memory ... from a demonstrated success" — amended (0122, process recipes); "competence drive — the shipped default" — imprecise (see ch 9).

Citations that no longer resolve:

- [ ] ch 14, 15, 16: `hq/01-RESEARCH/motivation-stack/README.md` — removed at 789fa8d (2026-08-16, graduation); successor episode 0107 + design 0016; G1/G1L/G3 in episodes 0070/0071; the G5 context rows ch 15 quotes (2,473 sticks; 179/117/77 vs 659; 100/156; 1,080; 0.450) exist only in `git show 789fa8d^:hq/01-RESEARCH/motivation-stack/README.md`; 0073 carries the headline subset.
- [ ] ch 16: `hq/01-RESEARCH/recipe-reach/README.md` — removed at 9a418d2 (pre-lock); successor episode 0077 + design 0010.
- [ ] ch 16: `hq/01-RESEARCH/fast-real-bridge/README.md` — removed at 59f9fa0 (pre-lock); successor episode 0093 + hq/02-DESIGN/validate/C1E-RUN-PLAN.md; the B1–B3 raw numbers only in `git show 59f9fa0^:…`.
- Every other cited episode (0001–0098), design doc, trail doc, spec and contract resolves at HEAD.

Numbers that drifted:

- [ ] ch 16: the c1d 1M-step row (3,236 chains at step 1,000,121, dwell 99.99%, energy 0.980) matches c1d-status.jsonl segment 20 exactly — but the run closed; see the c1d update above.
- [ ] ch 16: segment rate "501 steps/s at segment 1 to 80 by segment 28 ... not diagnosed" — record: 501 → 57 over 40 segments, diagnosed as snapshot-cadence suffocation (2,273 in-memory snapshots per segment), 753 after the fix (C1D-LAB-RUN-PLAN.md ops journal; 0079).
- [ ] ch 16: dig success 3/5, 4/5, 2/5, 4/5 — post-fix 20/20 + 20/20, drift 10/10 (0078); B2′ ref/2×/5× 20/20, 10× 10/20 (0093, C1E-RUN-PLAN.md).
- [ ] ch 16: β = 0.5 "the honest operating point" — 0080/0081 + design 0011 `label_beta`: 0.5 commands (selection monoculture 24/24, chains 18/24), 0.02 nudges, the cliff at 0.05–0.1 where the label crosses the drive band.
- Every other chapter's numbers re-verified with no drift (ch 1–15, both appendices, glossary). Not verifiable here: ch 13's "1,918 inventory changes" (S3-only); ch 15's context rows and ch 16's tick-rate table were checked against the removed READMEs' git history, not a live file.

Queued items (outline "what the record queues next" + the waiting list above):

- E3.1 (praise as want): delivered pre-lock (0075, told in ch 16); the design was never picked up; 0107 files it under borrowed goals. Closed as a queue item.
- The brain-side hold in the shipped product: delivered pre-lock (0077, feature 041); endurance read by 0079.
- G4, a world with a meter: delivered pre-lock (0075/0076); superseded by 0103 — the meter is retired for the world's own hunger.
- G2 option-value: still open (design 0016: never run; the palate covers the sensing half).
- Recombination: delivered pre-lock (0086/0087). c1d's five readings: delivered pre-lock (0079). c1e / B2′ dig reliability: delivered pre-lock (0078, 0093, 0096), answered by 0103. Recipe/label `src` builds: delivered (0077).
- Ch 4 worked triplet: still open (nothing in 0099–0123 touches pra-rover).
- Ch 16 endurance deciles: delivered by 0079 BEFORE the last lock; the chapter still says "still going". The sub-note "episodes 0074–0075 are chapter material" is stale — ch 16 already draws on 0074–0076.
- E3.1 registration wording: still open and changed shape — `motivation-stack/` was removed at graduation, so the hq fix annotates design 0016 or the run archive, not the README.
- Ch 5 length: still a book decision; the language arc (0112–0116) gives it concrete material.
