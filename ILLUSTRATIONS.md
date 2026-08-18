# Illustration plan

The book's images, described in text for an external image program (or a
human illustrator) that has **no access to the book** — every description
below is self-contained. Nothing here is generated yet; this file is the
brief.

How to read an entry: **●** marks the core set (one per chapter plus the
cover — produce these first); **○** marks supporting images. *Place* quotes
the sentence the image should follow. Types: **scene** (a story moment),
**diagram** (a mechanism), **chart** (measured data drawn honestly).

Files go next to the chapter that uses them, numbered by chapter:
`src/<part>/figures/<NN>-<slug>.svg` (diagrams/charts, SVG preferred) or
`.png` (scenes), embedded as `![…](figures/<NN>-<slug>.png)`.

## SVG production spec (diagrams and charts)

The diagram/chart entries are built as hand-authored SVGs in this repo;
only the scenes and the cover go to an external image program. **Status:
all 44 diagram/chart figures are built and embedded** (39 chapter figures
2026-08-14 under `src/<part>/figures/`; 5 appendix figures under
`src/appendix/figures/` — 3 built 2026-08-16, 2 built 2026-08-18); the
11 scenes and the cover remain open.
Every SVG follows this spec so the set reads as one system:

- **Canvas**: `viewBox="0 0 1200 H"` (H chosen per figure, typically
  650–900; wide strips may run 1200×420). First element is the paper
  panel: `<rect x="1" y="1" width="1198" height="H-2" rx="14"
  fill="#f8f7fb" stroke="#e3e1ec" stroke-width="2"/>` — the panel is part
  of the image so figures read on the site's light *and* navy themes.
- **Padding**: keep 48px clear inside the panel edge; nothing overlaps —
  when in doubt, grow H rather than shrink type.
- **Palette (hex, fixed)**: ink `#1b1f2c`; dim text `#626779`; lines
  `#cbc8da`; faint grid `#e3e1ec`; white card fill `#ffffff`; warm amber
  (the system's act / the judged thing / the event-head series)
  `#c2410c`; world blue (the world, the grader, the frames series)
  `#0f62c4`; oracle gold (always dashed) `#96570a`; warning (taxed /
  penalized) `#be123c`; frozen wash `#e8edf5`; success green (only where
  an entry names a green check) `#15803d`. Muted greens `#a7c9a2` /
  `#7fae7a` are permitted solely for lawn/terrain vignettes.
- **Type**: sans labels
  `font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"`
  at 22px (captions 20px, headings 28px, weight 600); monospace for axis
  ticks, tallies, and data callouts
  `font-family="ui-monospace, 'SF Mono', Menlo, monospace"` at 20px.
  Break long labels with `<tspan x=… dy="1.3em">`.
- **Chart honesty rules** (from the entries): research charts get thin
  ink axes, monospace ticks, direct line labels — never legend boxes,
  never pass/fail badges; conceptual shape-curves carry no y-axis
  numbers; spreads are per-run dots, never a lone average.
- **No** external references, `<image>` elements, scripts, or CSS
  classes — inline presentation attributes only.
- **Files**: `src/<part>/figures/<NN>-<slug>.svg`, `NN` the two-digit
  chapter number. Embed in the chapter as
  `![<short title>](figures/<NN>-<slug>.svg)` on its own line, a blank
  line either side, directly after the paragraph containing the entry's
  placement quote.

## Art direction — one system

**Register.** Flat editorial vector line art on an off-white paper panel.
Every image carries its own paper background and a subtle border, so it
reads on the site's light *and* dark themes. Plain sans-serif labels,
sentence case. No mathematical notation anywhere — the technical lane of
the book lives in its prose boxes, and the art never duplicates it. Never:
glowing brains, circuit-board textures, ball-and-stick neural-network
hairballs, humanoid robots with faces. The popular picture of AI is what
the book argues against; the art must not smuggle it back in.

**The cast (all faceless).** Mood belongs to light and composition, never
to expressions — the book never attributes feeling to the system, and the
art holds that line.
- *The mower*: a small rounded domestic robot lawnmower, no brand, no eyes.
  Its tree trunk and lawn are the book's running everyman example.
- *The brain glyph*: a plain rounded rectangle on small legs, one accent
  color, no anatomy. "The system" whenever an abstract actor is needed.
- *The rover*: a small four-wheeled unit, five ray lines fanning forward,
  a front bumper bar, no camera eye. Chapters 5 and 12.
- *The bot*: a blocky grey-blue humanoid, two cubes tall, whose only
  feature is a single dark horizontal visor band (a band, not a face).
  Its world is a simple unbranded voxel landscape — flat grass, upright
  oak-log columns, a grey stone wall, a crafting table with a 3×3 grid.
  Never Minecraft branding or recognizable game characters, never a HUD.
- *The teacher is never a person*: praise and demonstration are translucent
  disembodied hands — a floating clapping pair with a small "well done"
  ribbon; guiding hands over the bot's own for a demonstration.

**Visual vocabulary** (established once, reused everywhere):
- *Knobs mean dimensions.* Identical small rotary dials with one indicator
  line, counted by eye. A **frame is always the rounded-rectangle control
  panel with dials**; its dial count is its dimension count. In population
  views panels may shrink to tiles, but a visible dial row stays — dial
  count is the canonical encoding, tile size only echoes it.
- *Frost means frozen.* Ice-crystal texture on a line, box, or padlock
  marks "learning switched off."
- *The bar is a physical object*: a horizontal line in charts, a balance
  weight, a low doorway lintel — three registers of the same idea, drawn
  recognizably related.
- *The triplet strip*: before → action → after as three boxes, the middle
  box always in the actor's warm accent.
- *The seam*: a vertical socket strip, engine on one side, worlds plugging
  in on the other.
- *The snapshot*: a file icon fed by a bold pause bar. Never an album,
  archive, or cloud.
- *Praise is a pulse, never a treat*: one sensor square lighting to 1.0
  for exactly one tick, with a narrow spike trace. Never food or coins.
- *The sensor strip*: a row of small squares for "everything the body
  senses"; point at one square to name one channel.
- *Reward tokens*: small coin-like sparks marking "this tick pays"; their
  absence marks a stretch that pays nothing.
- *The dashed empty slot*: an outcome that never arrived.
- *The oracle ghost*: a translucent dashed-frame duplicate of the scene,
  labeled as a peeked-at copy of the world.
- *The ring and the arrow*: a circle as a ceiling; an arrow whose length
  is magnitude and angle is direction.
- *The ugly-twin gallery*: circular portrait of the bot with one trait
  exaggerated, lowercase nameplate beneath.
- *The 24-pupil row*: 24 small circles, filled for pass, hollow for not,
  with a threshold marker.

**Palette** (fixed book-wide):
- Ink/black — the world's own truth.
- Warm amber — the system's own act or behavior; the thing being judged.
- Slate blue — the world, the grader, deployment.
- In data charts the series colors are fixed: frames slate blue, event
  head amber, truth ink, chance a dashed grey baseline, anything reading
  ground truth dashed gold, taxed/penalized arrows a reserved warning
  red-orange. Grey also carries "what should have happened."
- Cool blue-grey wash for anything frozen or deployed.

**Two chart voices, held apart.** Measured results use a plain
researcher's-plot style: thin axes, monospace tick labels, faint or no
gridlines, lines labeled directly (no legend boxes), no pass/fail badges —
and spreads shown as per-run dots, never a lone average (a constitutional
rule of the project). Conceptual shape-curves carry **no y-axis numbers**;
real values appear only as callouts on specific points. A reader should
tell at a glance whether a picture is measured or argued.

---

## Cover

### ● `cover-the-lawn-that-learned` — scene

**Show:** A single bird's-eye view of a green lawn filling the frame, one
dark circle slightly off-center for a tree trunk. Across the lawn run five
parallel mown stripes in slightly lighter green, read top to bottom like
lines on a page. The first stripe runs straight into the trunk and stops
dead, with a small impact mark. The second also stops at the trunk, a
small filled dot at the contact point. The third bends and grazes the
trunk's edge. The fourth curves around it with room to spare. The fifth
flows around the trunk in a clean, confident arc and continues to the
frame's edge, unbroken — and on this last stripe only, a small rounded
robot mower sits mid-path, mid-journey. No people, no text in the image,
no logos, no face on the mower. Title and author are typeset over the sky
of open lawn by the cover designer, not drawn into the scene.

**Serves:** The whole book in one picture — the same brain meeting the
same obstacle, and the path changing because it lived there — legible
before a single page is read, and quiet enough to survive as a thumbnail.

---

## Chapter 1 — The brain in the freezer

### 1.1 ● `mower-stuck-on-trunk` — scene

**Place:** after "It has been stuck on that trunk more times than I can
count. It will get stuck on it again tomorrow."

**Show:** A small domestic robot lawnmower (low, rounded, wheeled, no
brand markings, no face or eyes) wedged nose-first against the base of a
mature tree trunk in an ordinary suburban back lawn. The mower is tilted
very slightly upward where it has ridden onto a root; its rear wheels are
visibly spinning, throwing up a light spray of grass clippings and two
small motion arcs to show the spin. Behind it, a neatly mown path of
slightly lighter green curves across the lawn and runs dead straight into
the trunk, so the reader can read the whole approach at a glance.
Late-afternoon side light, long soft shadows, calm weather; the mood is
comic futility rather than alarm. The tree is healthy and undamaged, and
the mower is undamaged. Do NOT include: any person, any hand reaching in
to rescue it, any screen, app, phone, or user interface, any brand logo,
any anthropomorphic expression on the mower, any sparks, smoke, or sense
of danger.

**Serves:** Fixes the book's founding anecdote as a picture the reader
recalls every later time "the mower" is invoked; the straight-line
approach path silently makes the point that nothing about yesterday
changed today's route.

### 1.2 ○ `train-then-freeze-timeline` — diagram

**Place:** after "I call the copy that ships a "frozen brain": a snapshot
of what was learned, with the learning switched off."

**Show:** A single horizontal diagram read left to right, one continuous
baseline arrow spanning the full width. The left two-thirds is a pale
panel labeled "TRAINING — in the lab"; inside it a solid line labeled
"what the brain knows" climbs steadily upward, with small stacked-document
icons feeding into it from below labeled "examples". A bold vertical
divider crosses the whole figure, labeled "the copy that ships". The
right third is a pale blue-grey panel labeled "DEPLOYMENT — in the world";
there the same line runs perfectly flat to the right edge, drawn with a
faint frost/ice-crystal texture along it, and a small toggle-switch icon
sits just above it in the OFF position labeled "learning: off". At the far
right edge, three small arrows point inward at the flat line from outside
the panel, labeled "world changes", "task changes", "body changes", none
of which bend or disturb the flat line. Do NOT include: anatomical brain
imagery, a neural-network node-and-edge graphic, numbers or units on the
axes, a second "continuous learning" line, or any depiction of retraining.

**Serves:** Readers conflate "the model is running" with "the model is
learning"; this makes the shape of the split — rising, hard cut, then
permanently flat under pressure — the thing they remember.

### 1.3 ○ `mower-learns-in-a-week` — diagram

**Place:** after "By Friday it slides past without touching, and nobody
told it anything: no update was downloaded, no engineer was involved."

**Show:** A four-panel strip in one row, each panel a simple top-down view
of the same square patch of lawn with the same tree trunk drawn as a dark
circle slightly right of center. In each panel a dashed line traces the
mower's path in from the left, a small top-down mower silhouette at the
path's leading end. Panel labels across the top: "MON", "TUE", "WED",
"FRI". In MON the path runs straight into the circle and stops dead, with
a small impact burst. In TUE the path again stops at the circle, and a
small filled dot sits at the contact point labeled "noted". In WED the
path bends slightly outward and grazes the circle's edge. In FRI the path
curves cleanly around the circle and continues off the right edge of the
panel, unbroken. All four panels identical in scale, framing, and lawn
texture so only the path changes; flat near-diagrammatic style, the warm
accent used solely for the path. Do NOT include: any person, engineer,
laptop, download or wireless symbol, progress bar, speech bubble, thought
bubble, or reward/score indicator — nothing external intervened.

**Serves:** Converts "learning is its life" from a slogan into something
the reader can watch happen.

---

## Chapter 2 — Forget everything, or remember everything

### 2.1 ● `the-two-cliffs` — diagram

**Place:** after "Most of the field's history is people falling off one
cliff while backing away from the other."

**Show:** A wide side-on landscape: a narrow flat-topped ridge of rock in
the center with a sheer drop on each side, drawn symmetrically. Standing
on the ridge top is the brain glyph — a plain rounded-rectangle character
on small legs, one accent color, no face, no anatomical brain. The left
chasm is labeled "OVERWRITING" with the sub-label "nothing old survives";
far below in it, faint outlines of a whiteboard and scattered erased
marks. The right chasm is labeled "HOARDING" with the sub-label "nothing
is ever thrown away"; in it, a tall precarious tower of stacked boxes and
newspaper bundles rises partway up. A single dashed arrow on the ridge top
shows the character stepping backward away from the left edge and directly
toward the right edge. Muted earth tones for the rock, cool shadow in both
chasms. Do NOT include: real brain anatomy, labels naming algorithms or
companies, any human figure, or a safe third path/bridge — at this point
in the text there is no solution shown.

**Serves:** The two-cliffs framing carries the chapter and returns later;
one symmetric image makes the trap structural rather than rhetorical.

### 2.2 ○ `one-whiteboard-for-everything` — scene

**Place:** after "Learn enough Spanish on that board and one day you look
up and the French is gone."

**Show:** A close, slightly angled view of one ordinary wall-mounted
whiteboard filling most of the frame, densely covered edge to edge —
visibly no free space and no second board anywhere. Older writing is
present only as ghosted, half-erased grey traces beneath fresh dark
marker; the fresh layer is written straight over the old. On the left
third, the ghost traces are recognizably French vocabulary in a faded hand
(for example "le jardin", "nous avons"), and over them, sharp and new,
Spanish words ("el jardín", "nosotros"). A marker rests in the tray and a
dirty eraser sits beside it, smeared grey. Quiet, slightly claustrophobic
mood; ordinary lighting. Do NOT include: any person or hand, any second
whiteboard, notebook, filing cabinet, or backup of any kind, any computer
or screen, any lettering other than the French and Spanish fragments.

**Serves:** Gives catastrophic forgetting a physical cause — one surface,
no second surface — instead of an unexplained property of "numbers."

### 2.3 ○ `v3-population-runaway` — chart

**Place:** after "One new model per cycle, a clean straight line, no
plateau, no end."

**Show:** A plain, honest line chart in a working researcher's style, not
a marketing graphic. Horizontal axis labeled "cycle" with ticks at 0, 10,
20, 30; vertical axis labeled "number of models alive". One solid
accent-colored line rises in a perfectly straight diagonal from
bottom-left, gaining exactly one unit per cycle, and runs off the
top-right corner of the plot area rather than ending inside it — the
chart cannot contain it. A second line, dashed and grey, rises early and
flattens into a horizontal plateau, labeled "what a working eviction rule
should look like". A small callout with a leader line points at the solid
line: "v3: +1 per cycle, no plateau". Title above: "Prototype v3 —
population over 30 cycles". Thin axes, faint or no gridlines, no legend
box, monospace tick labels. Do NOT include: error bars, confidence bands,
additional series, any pass/fail badge, or a second panel.

**Serves:** Shows the actual shape of the failure the author says he can
still pull up; the runaway line escaping the frame does the argumentative
work. (Chapter 6's `population-breathes` answers this chart — axes, color,
and line weight must match between the two.)

---

## Chapter 3 — The question nobody answers

### 3.1 ● `the-knob-game` — diagram

**Place:** after "I'll call the knobs dimensions: the separate numbers
you'd need to pin down what state a thing is in."

**Show:** A row of four control panels, each a small rectangular faceplate
with physical rotary knobs, and above each panel a simple line-art icon of
the thing it controls. Left to right: (1) a playground swing, panel with
exactly 1 knob, caption "swing — 1"; (2) a small boat seen from above,
panel with exactly 3 knobs, caption "boat — 3"; (3) a quadcopter drone,
panel with 5 knobs, caption "drone — 5"; (4) a human hand, panel with many
small knobs packed in a grid that runs off the right edge of its
faceplate, caption "hand — 20+". Knobs are identical small dials with a
single position indicator, so the count is the only variable and countable
at a glance. Panels share size and baseline; flat two-color line art, the
accent on the knobs. One heading above the row: "How many knobs to
describe it completely?". Do NOT include: numeric readouts, sliders,
screens, wiring, labels naming individual knobs (no "x", "y", "angle"),
or any human figure beyond the hand icon.

**Serves:** "Dimensions" is the chapter's load-bearing term and its most
abstract; the knob row makes the count concrete before the text asks how a
brain could discover it. (This figure founds the book-wide knob
convention.)

### 3.2 ○ `few-knobs-behind-many-numbers` — diagram

**Place:** after "Finding the few knobs behind the many numbers is, I'd
argue, most of what understanding a world is."

**Show:** A left-to-right diagram in three stages. Far left: a single knob
dial in a small box labeled "the world's hidden state — 1 knob", the whole
box inside a dashed outline labeled "hidden". Center: a broad fan of
arrows spreading from that one knob into a large dense grid of small
squares rendered as a pixel field, labeled "what the senses receive — a
million pixels, 60 times a second"; the fan visibly widens, one source to
very many. Right: the brain glyph receiving the pixel grid, a question
mark inside it, captioned "how many knobs should I look for?". A single
long curved arrow runs backward from the brain glyph all the way to the
hidden knob box, labeled "must be inferred", drawn dashed to show it is
not given. Keep the visual weight lopsided: the pixel grid dominates, the
hidden knob is tiny. Do NOT include: equations or symbols (no z, x, f,
d), any neural-network diagram, or any indication of the correct answer
being revealed to the brain.

**Serves:** Resolves the chapter's central counterintuitive claim — the
sensory flood is bigger than the thing it describes — and shows exactly
which arrow is the hard one.

### 3.3 ○ `the-answer-was-one` — chart

**Place:** after "One knob for a twenty-knob world. One knob for fifty."

**Show:** A paired bar chart with four groups along the horizontal axis,
labeled "3", "20", "35", "50", under the axis title "world's true size
(knobs)". In each group, two bars: a grey bar ("true size") whose height
matches the group label, and an accent-colored bar ("size the engine
reported"). The grey bars step up dramatically; the accent bars are 3, 1,
1, 1 — in the first group the two match, in the rest the accent bar is a
barely visible stub beside a towering grey neighbor. Vertical axis
"knobs", ticks at 0, 10, 20, 30, 40, 50. One callout points at the three
stubs: "reported 1"; a light bracket groups the last three as "the new,
larger worlds". Plain research-plot styling matching 2.3. Do NOT include:
error bars, a trend line, a "FAIL" stamp or red X, additional world
sizes, or any explanation of the cause — the chapter leaves the cause
unresolved.

**Serves:** The failure's whole force is the gap between what the world
was and what the engine said; side-by-side bars make that gap
instantaneous.

---

## Chapter 4 — Before, action, after

### 4.1 ○ `spoon-drop-experiment` — scene

**Place:** after "By the fifth drop the adult has theories about the
baby's motives, and none of them are charitable."

**Show:** A warm domestic kitchen scene in loose ink line with light wash.
A baby sits in a wooden high chair at center, one arm extended over the
side of the tray, fingers just opened; a metal spoon is caught mid-fall
about a third of the way down, a small motion arc behind it. On the floor
below, four more spoons lie scattered where earlier drops landed, so the
reader can count five events. In the right third an adult bends
mid-retrieval, one hand reaching for a spoon, face patient — amused,
resigned, not angry. The baby looks down at the falling spoon with genuine
concentration, not mischief: a scientist watching an experiment. No
lettering, captions, speech bubbles, or diagram overlays. Do NOT add a
pet, a sibling, a phone, or branded packaging; do not make the adult look
angry.

**Serves:** Anchors the book's foundational abstraction in the concrete
anecdote it opens with, before any terminology arrives.

### 4.2 ● `triplet-anatomy` — diagram

**Place:** after "The triplet stream is the machine's own life, and my
claim is that it's enough."

**Show:** A horizontal three-panel diagram. Panel 1, headed "before":
a simple line drawing of a small hand gripping a spoon; caption "what I
sensed". Panel 2, headed "action", drawn in the warm accent to mark it as
the part that belongs to the actor: the same hand with fingers opened and
a small outward motion arc; caption "what I did". Panel 3, headed
"after": the empty hand at top and, below right, a small starburst with
three short radiating lines suggesting a clatter from the floor; caption
"what I sensed next". Two thick arrows run left-to-right between panels.
Below, a single bracket spans all three with the centered label "one
triplet". Do NOT draw a face, a full baby, or a floor; no numbers, sensor
readings, scores, or a reward symbol of any kind — the absence of a score
is deliberate.

**Serves:** The three-part shape the entire book rests on, pictured
separately from the story it came from. (Founds the triplet-strip
convention; the middle box is always the actor's accent color.)

### 4.3 ○ `watching-versus-meddling` — diagram

**Place:** after "Keep the rooster quiet for one morning and see whether
the sun still rises."

**Show:** Two panels side by side sharing one horizon line, the same
farmyard on two mornings. Left, headed "Watching": a rooster on a fence
post mid-crow, three small sound arcs at its beak, the sun halfway above
the horizon; beneath, "crow, then dawn — every single morning". Right,
headed "Meddling": same fence post and horizon, but the rooster is inside
a simple wooden crate, beak closed, a small crossed-out sound-arc symbol
beside it, while the sun rises exactly as before; beneath, "no crow —
dawn arrives anyway". Between panels, a vertical dashed divider with a
small hand icon pointing into the right panel, labeled "an act". Flat and
diagrammatic: no farmhouse, people, clouds, or clutter. The caged rooster
must not look distressed — the crate is an experimental control, not
cruelty.

**Serves:** Makes visible the one thing watching can never deliver — only
an intervention separates "causes" from "merely comes first."

---

## Chapter 5 — Not words, not pictures

### 5.1 ● `two-middles` — diagram

**Place:** after "You can't run the rooster experiment on a library. The
library can't be surprised by you."

**Show:** A stacked two-row comparison, each row the same three-box
left-to-right structure (before → middle → after). Top row, labeled "A
body that acts": box 1 shows a small four-wheeled rover facing a wall;
the middle box, in the warm accent, is labeled "act" and contains a
forward-arrow motor symbol; box 3 shows the same rover closer to the wall.
From the middle box a curved arrow loops upward into box 3, labeled "the
world replies to you". Bottom row, labeled "A reader of text": box 1 an
open book with grey squiggle lines for text; the middle box, plain grey,
labeled "guess"; box 3 the next page of the same book, already printed,
a small closed padlock in its corner labeled "fixed years ago". No curved
arrow connects the bottom middle to its box 3 — instead a short arrow
crossed out with a thin X, labeled "guessing differently changes
nothing". No real book titles, company names, logos, screens, or chat
interfaces; the rover has no face and no camera eye.

**Serves:** The whole chapter turns on one structural difference — act
versus guess — put in a single glance.

### 5.2 ○ `the-creek-checks` — scene

**Place:** after "Cold water settles the question in a way no amount of
fluent talking can undo."

**Show:** Two panels sharing one continuous creek. Left: a person stands
on the near bank, hands in pockets, relaxed, with a plain speech bubble:
"I can jump across that creek." — posture casual, the sentence costing
nothing. Right: the same person mid-jump-aftermath, arms out, landed
short, thigh-deep in the creek with a splash ring and a shocked wide-eyed
expression; no speech bubble at all. Simple current lines and rocks, a
little grass on the banks. Dryly comic, not humiliating — the joke is on
the sentence, not the person. Do NOT label the panels, add onlookers, or
put any text in the right panel; the silence is the point.

**Serves:** Dramatizes the chapter's cleanest test — a sentence comes out
smoothly whether or not it's true, and the world does not extend that
courtesy.

### 5.3 ○ `dictionary-loop` — diagram

**Place:** after "For a system made only of text, the loop has no exit.
There's nothing at the bottom."

**Show:** A circular diagram occupying most of the frame. Four boxes
around a ring, each a quoted word with a short definition, arrows running
clockwise: "water" — a clear liquid → "liquid" — a substance that flows →
"flow" — to move as a liquid does → "move" — to change position → back to
the first. The ring is flat grey, closed and airless, with a small label
at its empty center: "words pointing at words". Breaking out of the ring
from the "water" box, one arrow in the warm accent heads down and out to a
small vignette at the bottom: a bare foot stepping into water with a
splash ring, labeled "something that once splashed you". The escaping
arrow is the only warm-colored element on the page. Do NOT draw a physical
dictionary, book, computer, or brain; only one escape arrow.

**Serves:** The circularity argument is easy to nod along to and hard to
picture; the single escaping arrow makes it land.

---

## Chapter 6 — A head full of rival guessers

### 6.1 ● `frame-panel-and-pose` — diagram

**Place:** after "New sight, new pose, same frame."

**Show:** A diagram distinguishing a fixed control panel from its changing
settings. One physical control panel — a rounded rectangle with exactly
three labeled dials (1, 2, 3), each with a pointer needle — labeled "the
frame: three knobs (its bet about how many the world has)". Show this same
panel twice, stacked vertically, at two moments. Top: an incoming arrow
from a strip of ten unlabeled numbers in boxes, captioned "one sight: ten
sensor numbers"; the three needles at three particular angles; a small
readout beneath showing three numbers, captioned "the pose: where the
knobs point right now". Bottom: a different strip of ten numbers arrives,
the needles sit at visibly different angles, the readout shows three
different numbers. Between the instances, a vertical bracket labeled
"same panel, new setting". The panel outline must be identical in both —
same size, same three dials — only the needles move. Do NOT draw a head,
brain, robot, or neural-network graphic; do not vary the dial count.

**Serves:** Frame versus pose is the chapter's most slippery pair of
terms; panel-versus-needles settles it in one look.

### 6.2 ○ `frame-life-cycle` — diagram

**Place:** after "Same mechanism, one sign flipped, opposite fate."

**Show:** Four stations around a large clockwise ring, each a small
control-panel icon (rounded rectangle with a dial row) with a heading and
one line beneath. Top, "Born": a new panel appearing beside an existing
one — "spawned near the current best size — or on the spot, when no
existing frame can express a sight". Right, "Protected": a panel inside a
dotted-circle shield — "a fixed childhood: cannot be evicted no matter how
badly it scores". Bottom, "Judged": a panel on one side of a balance
scale, the other side holding a small weight labeled "the bar" —
"prediction error, plus rent for every knob". Left, "Evicted": a panel in
dashed outline, fading, an arrow leading off the ring — "deleted,
permanently". In the ring's center, a boxed rule in the warm accent:
"Nobody is ever edited. A new size means a new rival, not a resized
frame." with a small icon beneath: a three-dial and a four-dial panel
facing each other. Bottom right, outside the ring: "the more crowded the
head, the harsher the bar", with a short arrow showing the bar-weight
growing heavier as three extra panels crowd in. Do NOT add human figures,
gravestones, skulls, or death imagery beyond the fading dashed panel.

**Serves:** Four rules stated across four paragraphs become one system
shown as one loop; copy-don't-mutate in particular needs a picture.

### 6.3 ○ `population-breathes` — chart

**Place:** after "That number is negotiated, continuously, between the
spawn rate and the bar, and it holds while individual frames come and go."

**Show:** A clean line chart. X-axis "cycles", no tick values; y-axis
"number of frames alive", ticks at 0, 10, 20, 30. The main line, warm
accent, rises quickly over the first fifth then becomes a jagged sawtooth
band hovering between roughly 13 and 19 for the rest, never trending;
small upward ticks carry tiny "+" marks and downward ticks "−", with a
small key "+ spawn   − eviction". A horizontal shaded band across the
hovering region: "hovers in the teens — 15, 19 and 13 frames on three
runs of the same world". Behind it, pale dashed grey, a second line
climbing in a perfectly straight diagonal off the top, labeled "an
earlier version: one new frame per cycle, no plateau". One annotation
with a leader line to the hovering band: "no line of code says 'keep
about sixteen frames'". No legend box beyond the +/− key; no numeric
x-axis values. (Must visually rhyme with chart 2.3 — same axes, color,
line weight — because it is that chart's rebuttal.)

**Serves:** The self-limiting population is the chapter's climax; both
lines on one field do the argument's work.

---

## Chapter 7 — Never let it grade its own homework

### 7.1 ● `where-and-which` — diagram

**Place:** after "So v4 split the two roles: the gate still controls what
you learn from, and it no longer controls what you're graded on. *Which
events* count matters."

**Show:** Two columns, each a flaw on top and its repair below, separated
by a rule. Column A, headed "WHERE: in whose coordinates?". Top: ten
small numbered boxes labeled "what the sensors actually said" feed a
funnel labeled "squeeze", out of which drops a single value 0.41; beside
it a second identical funnel produces a predicted 0.41; the two values
meet at an equals sign with a green check, captioned "self-graded error:
0.36 — looks excellent". A grey shaded ellipse behind both funnels:
"everything the squeeze threw away is invisible to both sides". Bottom
(the repair): the predicted value expanded back out through a reversed
funnel into ten predicted boxes, compared against the ten actual boxes
with a two-headed arrow, captioned "honest error, measured against the
sensors: ~1.0 — no better than guessing". Column B, headed "WHICH: over
which moments?". Top: a strip of one hundred small tick marks for
consecutive moments, 23 filled in the warm accent, 77 hollow, captioned
"graded on only the 23% it agreed to map — the easy quarter of its
world". Bottom: the identical strip with all one hundred filled,
captioned "graded on every moment it was exposed to, mapped or declined".
No faces, characters, courtroom or exam imagery; strictly mechanical.

**Serves:** The two subtlest exploits in the book are the same trick
twice — a contestant controlling the measurement — obvious only side by
side.

### 7.2 ○ `crammed-then-tested` — scene

**Place:** after "Learning itself still runs on every step. Only the
*judging* moved."

**Show:** Two panels, same ink-and-wash style as the book's other scenes.
Left, headed "The old way": a student hunched at a desk, one hand holding
open a page of notes while the other fills in a test paper on the same
desk; the visible heading on the notes and on the test are identical, so
the reader notices they are the same material. A wall clock shows the two
events seconds apart. The student looks pleased. Right, headed "The pop
quiz": the same student stepping through a doorway into a completely
unfamiliar room — different furniture, different window — notes and bag
left visibly on the floor on the far side of the doorway, a quiz sheet
handed to them on arrival by an unseen hand entering from the frame edge.
Expression: caught off guard. Same panel size, clearly the same person.
Do NOT draw a teacher's face, readable body text beyond the two matching
headings, or any grade, score, or letter mark.

**Serves:** "Tested on material you crammed seconds ago" is the entire
fifth cheat; the exam-room framing makes a timing bug immediately
obvious.

### 7.3 ○ `honesty-needs-a-new-bar` — diagram

**Place:** after "Neither fix works without the other, and I have the
failed single-fix runs on record to prove it."

**Show:** Three panels, same setup each: a horizontal line as the bar and
a scatter of small dots above it for frames' honest scores, caption block
beneath. Panel 1, "Flattered scores, old bar": dots sit low, most below
the bar — "scores inflated by fresh practice — the wrong frames pass".
Panel 2, "Honest scores, old bar": the bar in exactly the same position,
but every dot now above it, none passing, small circular arrows
suggesting churn; caption in the warm accent: "0 frames ever mature —
newcomers churn endlessly, and the chosen size ratchets up to a median of
32.5". Panel 3, "Honest scores, recalibrated bar": the same high dots,
but the bar raised to meet them, bold, a small upward arrow beside it
labeled "bar × 2"; a handful of dots below it, one enlarged and labeled
"a long-lived resident"; caption "8 of 8 runs anchor at 7–11 knobs;
populations self-limit at 44–57 against a cap of 200". The bar's position
must be identical between panels 1 and 2 — only the scores moved. No
axes, gridlines, or legend; no generic error symbol on panel 2.

**Serves:** "The honest fix, alone, made things worse" is genuinely
counter-intuitive; the progression shows why honesty without a
recalibrated bar is just a different way to be wrong.

---

## Chapter 8 — The price of a dimension

### 8.1 ○ `patience-dose-response` — chart

**Place:** after "A dose–response curve like that is as close as this
kind of work gets to proof of mechanism."

**Show:** A small clean plot, four data points connected by a rising line
in the warm accent. X-axis "protected childhood (cycles)", exactly four
ticks: 2, 12, 24, 29. Y-axis "knobs the brain settled on", ticks 0, 5,
10, 15. Points at (2, 4.7), (12, 5.7), (24, 6.7), (29, 10.7), each value
printed above its marker. A horizontal dashed reference at y = 20 labeled
"the world's actual size: 20", well above all four points — the answer
climbing toward it without arriving. Beneath, one centered line: "turn
one dial, and the answer moves with it". Small, a figure inset, not a
full-page chart. No error bars, trend-line equation, legend, or extra
points.

**Serves:** Shows what "proof of mechanism" looks like — one constant
turned deliberately, one answer moving in step.

### 8.2 ○ `the-conveyor-and-the-empty-lounge` — scene

**Place:** after "and 'best_dim' was tracking the proposal generator, not
the world."

**Show:** An illustrated workshop cutaway, metaphor scene with diagram
labels. Left two-thirds: a long conveyor belt loops in a closed circle;
riding it are dozens of small unfinished control-panel units (rounded
rectangles with dials, some dials not yet fitted), each wrapped in a
dotted-line protective bubble. Above the belt: "29 juveniles — protected,
recycled faster than they can finish", and beside it smaller: "untouchable,
but still counted". On the right, a doorway with a deliberately low lintel
leads to a small side room; the doorway is labeled "the survival bar" —
one small unit ducks under easily, one visibly taller unit is stopped in
front of it. Through the doorway the room is completely empty: a couple of
chairs, no occupants, a wall sign "Mature frames: 0". From the crowded
conveyor a thin arrow to the lintel: "the crowd tightens the bar for
everyone else". Muted palette, the empty room in cooler tones. No faces,
arms, or expressions on the units; no human workers.

**Serves:** The two-caste diagnosis — a churning juvenile conveyor and an
empty adult niche — exposed a result that looked like success; it needs a
picture to be more than a phrase.

### 8.3 ● `no-elbow-and-the-price` — chart

**Place:** after "It is sitting exactly at the optimum of the trade it was
actually asked to make, and it holds that optimum stably at every scale
and every budget I've measured."

**Show:** Two stacked plots sharing one x-axis labeled "knobs
(dimensions)", 1 to about 30, ticks at 1, 10, 20, 30. Upper, headed "What
the errors actually do": y-axis "prediction error"; a single smooth curve
falling steeply then flattening, monotonic, no kink, corner, or elbow
anywhere. A vertical dashed line at x = 20 labeled "the world's true
size: 20 knobs", with a leader-line annotation where the curve crosses
it: "nothing happens here — no elbow to find". Lower, headed "What it
costs": y-axis "error + rent"; the same falling curve plus a straight
rising line (labeled "every knob charges a flat fee"), producing a
visible U with a clear minimum. Mark the minimum with a filled accent dot
annotated "the fee stops paying for itself here — the system lands at
10", plus a light shaded band spanning x = 8 to 12 labeled "measured
crossing: 8–12". No gridlines, legends, seed scatter, or extra curves.

**Serves:** The chapter's biggest reversal — "true size" leaves no
signature, and what's found instead is the price-optimal size — is a
claim about the shape of a curve, so the curve must be shown.

---

## Chapter 9 — Wanting things

### 9.1 ● `understanding-proposes-wanting-disposes` — diagram

**Place:** after "The two stay in the separate rooms chapter 4 promised."

**Show:** A left-to-right flow of how one action gets chosen, laid out as
two rooms with a wall between. Left room, headed "Understanding
(learns)": a stack of three control-panel icons labeled "frames",
receiving an arrow from a box "candidate actions: forward / turn left /
turn right", producing three small forecast cards each captioned "where
the world would land if I did this". A curved arrow labeled "experience"
enters this room from below and touches the frames. Right room, headed
"Wanting (does not learn)": the three forecast cards arrive into a sealed
box with a heavy double outline and a closed padlock, labeled "the drive:
scores each predicted outcome"; one arrow exits right into "the action
taken", which loops back around the whole diagram to "the world" and from
there to the "experience" arrow. Critical detail: the experience arrow
stops at the wall between rooms, a small crossed-out arrowhead against
the sealed box, noted "no path by which experience can change what it
wants". One line spans the base: "understanding proposes; wanting
disposes". No brain, human head, heart symbol, or emotion iconography —
the sealed box is a mechanism, not a feeling.

**Serves:** Readers are surprised the wanting part is the frozen part;
the blocked arrow is the whole justification in one graphic element.

### 9.2 ○ `thin-coverage-versus-deep-practice` — diagram

**Place:** after "Every hour of a finite life spent somewhere new is an
hour not spent getting good at something."

**Show:** Two identical bird's-eye maps of the same imaginary terrain side
by side — a grove, a pond, a rocky patch, an open field, a hillside,
rendered identically in both. Left, headed "Prefer whatever is new": a
single wandering path visits every region exactly once, a thin pale line,
single faint footprints in each region; caption "maximum coverage,
minimum depth". Right, headed "Prefer what you're getting good at": the
path loops repeatedly within two regions only, thick and dark from
repetition, those regions' ground visibly worn into packed trails while
the rest sit untouched and pale; caption "concentrated practice". Both
panels carry the same corner marker "one lifetime's worth of steps" —
identical budget, different distribution. No robot, rover, animal, or
person on either map — only paths and wear. No checkmarks or crosses
marking either as right or wrong.

**Serves:** Carries the chapter's central interpretation — novelty-seeking
spends a finite life as thinly as possible — undeniably.

### 9.3 ○ `frontier-three-signals` — diagram

**Place:** after "the frontier of improvement scores high."

**Show:** Three columns, each one kind of place: a scene vignette on top,
a small error-over-time plot in the middle, a score readout at the bottom.
Column 1, "Mastered": a smooth well-worn path; plot a flat line sitting
low; "score: 0". Column 2, "Unlearnable": an old television showing snowy
static; plot a flat line sitting high, jittering slightly, not
descending; "score: 0"; small note beneath: "endlessly new, and never
learnable". Column 3, "The frontier", in the warm accent: a path half
worn-in and half fading into rough ground; plot a line clearly descending
from high to low; "score: high". Label the shared middle-row y-axis once,
left of the whole figure: "prediction error over time". One line beneath
all three: "not 'is this new?' but 'am I getting better here?'". No
robot, face, or viewer figure; no checkmark or trophy on column 3.

**Serves:** The frontier drive is defined by what it rejects — two very
different places both scoring zero — and only a side-by-side makes clear
that "flat and mastered" and "flat and hopeless" are treated identically.

---

## Chapter 10 — The brain that almost stopped learning anyway

### 10.1 ● `two-curves-turn-together` — chart

**Place:** after "Honest error turns with it, at the same moment, and
never comes back."

**Show:** A single wide line chart, two curves sharing one horizontal axis
labeled "a component's life, in episodes", 0 at left to 9,600 at right.
Curve A, warm accent, labeled "how wrong its predictions are": starts
high, falls steeply, bottoms out about a fifth of the way across, then
turns and climbs steadily to end roughly twice its low point. Curve B,
cool accent, labeled "the total size of the numbers inside it": starts
mid-height, drifts gently down over the same early stretch, and turns
upward at exactly the same horizontal position as curve A, climbing
without leveling off. One vertical dashed line through both turning
points: "the turn: same moment, both curves". A small bracket under the
left region: "healthy: getting smaller, getting better"; under the right:
"rot: getting bigger, getting worse". No tick values on either vertical
axis (these are shapes, not a data plot), no gridlines, no legend box
(label curves inline at their right ends), no third curve, nothing
suggesting recovery.

**Serves:** The chapter's diagnosis rests on two numbers turning in
lockstep — a simultaneity claim prose can assert but a picture can show.

### 10.2 ○ `the-same-nudge-stops-working` — diagram

**Place:** after "It loses the ability to be gently changed."

**Show:** Two side-by-side panels, each the same flat S-shaped curve
(low-flat, steep middle, high-flat) on plain axes labeled in words only:
horizontal "what goes in", vertical "what comes out". Left panel, "small
numbers inside: a nudge changes the answer": a dot on the steep middle; a
short horizontal arrow nudges it and a matching tall vertical arrow shows
a large output change. Right panel, "bloated numbers inside: the same
nudge changes nothing": the dot far out on the flat upper shelf; an
identical-length horizontal nudge produces a barely visible vertical
stub. A small third inset below the right panel: the same dot with an
oversized arrow shooting clean past a small target marker, labeled "and
the step that used to tune it now overshoots". Both S-curves must be
geometrically identical — only the dot's position differs. No
mathematical notation (no sigma, tanh, formulas), no brain, neurons, or
connected-ball network, and no red-alert coloring on the right panel —
nothing is complaining.

**Serves:** "Saturate" and "loses the ability to be gently changed" are
the chapter's two hardest sentences, and both are one picture.

### 10.3 ○ `a-cap-not-a-freezer` — diagram

**Place:** after "What it cannot do is inflate."

**Show:** Two parts. Upper strip: three rejected repairs as small
crossed-out icons in a row, each with a red X and a caption: a padlock
frozen in a block of ice — "freeze it — that's a frozen brain again"; a
cluster of assorted arrows all shrinking toward a central dot including a
short healthy one — "shrink every number toward zero — punishes healthy
ones too"; a clock whose hands sweep while a stride-length marker beside
it dwindles — "slow its learning as it ages — freezing with extra steps".
Lower, larger part: the accepted repair as three sequential mini-panels
inside a shared ring: (1) a thin arrow from the circle's center, tip well
inside, "learning moves it — nothing happens"; (2) the arrow grown so its
tip pokes outside the circle, "learning pushes it past the ceiling"; (3)
the arrow pulled back so its tip rests exactly on the circle, pointing in
precisely the same direction as panel 2, "scaled back onto the ceiling:
same direction, shorter". The circle itself labeled "the ceiling: a
little above the size it was born at". The arrow's angle must be visibly
identical in panels 2 and 3; no pause or stop symbol anywhere in the
lower part; no age counter, clock, or timer in the accepted design.

**Serves:** The repair's entire claim is "magnitude only, direction
untouched, learning never paused" — the contrast with three
obvious-but-wrong fixes is what makes it land.

---

## Chapter 11 — No scrapbook required

### 11.1 ● `the-whole-estate` — diagram

**Place:** after "The population of frames: their sizes, their weights,
their running scores. That's the whole estate."

**Show:** A two-column comparison. Left column, headed "the usual
inventory", stacks three items: a box labeled "the model"; above it a
thick photo album, dog-eared, snapshots poking out, labeled "a scrapbook
of lived moments, re-studied forever"; above that scissors and a glue
stick labeled "a policy for what to paste in and what to tear out". A
vertical growth arrow beside the column shows the album thin at "day 1"
and fat at "day 1,000". Right column, headed "the whole estate": a loose
cluster of about twelve rounded panel tiles of visibly different sizes
(each with a small dial row); call out just one with three labels — "its
size", "the numbers inside it", "its running score" — the rest unlabeled.
Below the cluster, a short conveyor of small three-part markers sliding
into an open-bottomed chute, labeled "every observation: used in the
moment, then gone", with a tiny bracketed group of three still on the
belt: "a small window of recent ones, for bookkeeping". Under the right
column: "day 1 and day 1,000: the same size". The right column must
contain no stored images, database cylinders, cloud icons, or anything
resembling an archive of the past.

**Serves:** The chapter's claim is an inventory claim; readers from "AI
needs data" assume something is kept — both inventories side by side make
the absence visible.

### 11.2 ○ `paused-not-remembering` — diagram

**Place:** after "Two people can run the same mind forward from the same
moment and compare what happens."

**Show:** A horizontal lane left to right labeled "one run, learning
continuously", an irregular wiggling line with small evenly spaced tick
marks labeled once as "consolidation boundaries". At a tick a third of
the way across, a bold vertical pause bar, an arrow from it down to a
file icon labeled "every number inside every component, every score,
every counter, and the exact state of the random number generator". From
the file, two arrows fan to two plain boxes "machine A" and "machine B",
each continuing the lane forward. The two continuation wiggles are
exactly the same shape, a bracket spanning them: "byte-for-byte identical
to the run that never stopped". A caption band across the bottom: "a
snapshot is the brain paused, not the brain remembering". The file must
not be an album, memory chest, or cloud backup; no human figures, no
faces, no imagery of the past being retrieved or replayed.

**Serves:** Readers will read "snapshot" as "the memory it said it didn't
keep" — the distinction the chapter spends a section drawing.

### 11.3 ○ `sorting-is-a-mutation` — diagram

**Place:** after "The fix records the order as lived."

**Show:** Two horizontal rows of the same five tiles, each a rounded
rectangle of a different size carrying the same handwritten-looking
decimal number in both rows, joined by plus signs, ending in an equals
sign. Top row, "the order it was lived in": tiles in scrambled sizes.
Bottom row, "the order the snapshot wrote them: sorted by size": the
identical tiles smallest to largest. Each row ends in a long decimal
result; the two results are visually identical in every digit except the
very last, which differs. A magnifier over those two final digits with a
callout: "one ULP: the smallest step a computer's numbers can take".
Across the bottom, plain type: "sorting is a mutation". No tile's own
value may differ between rows — only the order changed. No crash symbols,
red warnings, or broken-machine imagery; every test up to this one had
passed.

**Serves:** "Addition order changes the last bit" is genuinely surprising
until the same numbers are seen in two orders.

---

## Chapter 12 — Watching it learn

### 12.1 ● `the-rover-page` — diagram

**Place:** after "You are watching the book's central argument happen in
well under five minutes."

**Show:** A simple browser window frame with two regions. Left two-thirds:
a flat top-down square walled arena containing exactly five dark
rectangular obstacles and one small wheeled rover (rounded chassis, nose
direction); five thin straight beams fan forward from the nose, each
stopping at the first wall or obstacle it meets; a faint dotted trail
behind the rover meanders without pattern. Four small callouts point at
the rover: "five-beam rangefinder", "compass", "position beacon",
"bumper". Right third: three stacked readouts, each a small line chart
with its name above: "prediction error", descending; "how many components
are alive", wobbling within a narrow horizontal band with 15 marked;
"best size", a staircase settling flat on 2 and staying. The rover must
not appear to pursue anything — no target marker, goal flag, planned
path, or exit — and no score, reward, or points display anywhere. No face
on the rover, no 3D, no photorealism.

**Serves:** The one chapter a reader can actually run; showing what
appears on screen tells them what to look for before they type the
command.

### 12.2 ○ `one-seam-many-worlds` — diagram

**Place:** after "The engine boots the world exactly once and learns from
one unbroken stream, with every mechanism from Parts 3 and 4 carried
over."

**Show:** A vertical socket strip down the center labeled "the body
interface: sensors in, actuators out". Left of it, a single plain box:
"the same engine, unchanged, in every case". Right of it, four connectors
plug in at different heights, each with a small illustration and label: a
top-down walled arena with a wheeled rover — "the demo rover"; a cart
with a balancing pole — "any Gymnasium game — CartPole and hundreds of
cousins, about fifty lines of adapter"; a wheeled robot with a spinning
lidar puck, an odometry wheel, and a camera — "a real robot over ROS2 —
every topic a sensor, every command channel an actuator"; a machine with
no reset button and a continuous stream line entering it — "a world that
cannot be reset — booted once, one unbroken stream". On the CartPole
connector, a coin-shaped token stamped "reward" stopped at a small
doorway, captioned "stays at the door". On the ROS2 connector, a new
small sensor being clipped onto the robot while it moves, captioned "snap
a sensor onto a running robot; the components resize without forgetting".
The reward token must never cross the doorway or reach the engine box,
and the engine box is drawn identically for all four — do not draw four
engines.

**Serves:** Four very different worlds hanging off one unchanged engine
is the section's claim; a reader who sees it once carries it into the
Minecraft chapter.

### 12.3 ○ `the-lidar-that-reported-infinity` — diagram

**Place:** after "The dashboard looked healthy; the numbers were garbage."

**Show:** A left-to-right flow in three stages. Left: a simulated
two-wheeled rover in a sparse room with an open doorway; one lidar beam
strikes a wall, tagged "3.4"; a second passes through the open doorway
and hits nothing, tagged "∞ (no hit)"; a third points at something far
too close, tagged "−∞ (below minimum range)". Middle: the tags travel
along a pipe into a row of four small accumulator boxes labeled "running
error statistics"; the "∞" tag enters the first box, and every box from
there rightward has flipped its contents to the word "nan", the flip
spreading visibly down the row. Right: a monitor panel with a green check
mark, the text "exit code: success", and beneath it the printed line "nan
early → nan late". A caption strip along the bottom: "the dashboard
looked healthy; the numbers were garbage". No alarm, red banner,
exclamation mark, crash, smoke, or error dialog anywhere — the entire
point is that nothing complained.

**Serves:** The chapter's warning about real sensors; the joke only works
visually when the green check sits beside the poisoned numbers.

---

## Chapter 13 — The log it put back

### 13.1 ● `the-log-in-its-hand` — scene

**Place:** after "One move away, once, for four minutes, on day four of
seventeen."

**Show:** A quiet scene in a blocky voxel world under late-afternoon
light. A grassy hillside is visibly rearranged: shallow one-block pits,
loose blocks of dirt set back down in odd places, scattered leaf litter,
a couple of small saplings planted where nothing planned them. The bot —
a simple blocky grey-blue humanoid, its only feature a single dark
horizontal visor band, no face or expression — stands alone near the
middle of the slope, holding a single cut oak log in one hand. Floating
beside it like a heads-up display, clean and slightly transparent, an
empty two-by-two grid of four square slots with an arrow pointing right
to a single empty output slot. Compose the log and the empty grid close
together so the gap between them reads as small. Mood still and slightly
melancholy, carried entirely by the light and the empty grid. Do NOT use
Minecraft branding or the recognizable Steve/Alex design; no other
creatures, players, buildings, torches, tools, crafting table, or planks
anywhere.

**Serves:** The image the whole book has been building toward — and the
reader needs to see how physically small the missed step was.

### 13.2 ○ `the-empty-counter` — diagram

**Place:** after "Zero. It pressed the take button a quarter of a million
times on an empty counter."

**Show:** A close-up schematic of a two-by-two grid of four square slots
with an arrow to a single output slot. The four input slots hold a jumble
forming no recipe: a block of dirt, a small sapling, a wheat seed, a
coiled leash. The output slot is empty, drawn with a faint dashed
outline. Right of it, a blocky hand presses a button labeled "take the
offer", repeat motion arcs behind the hand. Two small tallies beneath, in
plain type: "222,305 presses" and "0 steps with anything on offer". Reads
as a service counter with nobody behind it — restrained, not comic. The
output slot stays empty everywhere; no error message, rejection symbol,
red X, or buzzer (nothing ever told the bot it was wrong); the hand shows
no frustration, sweat, or cartoon anger.

**Serves:** A quarter of a million presses against a permanently empty
slot is the chapter's verdict; the picture makes the number felt.

### 13.3 ○ `why-it-walked-away` — diagram

**Place:** after "It ended because the era succeeded, and success is
precisely what this drive is built to leave."

**Show:** Two stacked panels sharing one horizontal axis labeled "time
spent digging". Upper, "how well it predicts what digging does": a curve
starting high, dropping steeply, flattening onto a low floor, the flat
part labeled "mastered: predicts it cleanly now". Lower, "how much the
drive wants to be here": a curve that is the steepness of the upper one —
high while the upper falls, sagging as it flattens, reaching zero exactly
where the upper levels off. A vertical dashed line through both panels at
that point: "the era ends"; from the lower panel's zero a curving arrow
leads off right into a soft undefined region labeled "somewhere else,
where prediction is still improving". Beneath both: "the drive scores a
place by whether its predictions there are still improving. Master
something, and there is nothing left improving." One final line, smaller:
"nothing anywhere in this design scores a log for being worth having."
Do NOT depict the bot breaking, tiring, or bored in a human way; no
reward numbers, trophies, or goal icons.

**Serves:** The central explanation is counterintuitive — the behavior
stopped because it succeeded — and seeing the second curve as the slope
of the first makes it obvious instead of paradoxical.

### 13.4 ○ `seventeen-days-in-one-strip` — chart *(optional)*

**Place:** after "But the digs stopped finishing. Motion without contact."

**Show:** A wide horizontal timeline bar spanning the image, left end
"step 0", right end "step 5,669,662 — seventeen days". A shaded band from
roughly one-sixth to one-third across: "four days of hands: 449 finished
digs, 1,077 blocks picked up". A single pin drops into that band slightly
past its middle: "one oak log, step 1,299,001, held four minutes, put
back". Right of the band, plain and unshaded: "3.7 million steps: nine
things picked up, all nine dropped nearby by a passing trader's llamas".
Below the main bar, two thin sub-lines on the same axis: "chose to dig",
ticking slightly upward late (mark "6.5%" over the shaded band, "9.4%"
over the plain region), and "digs that finished", dropping to hard flat
zero at the band's right edge and never lifting. A third thin line at the
bottom, "steps with anything on offer", flat on zero across the entire
width. Near the right end, a small visible gap breaking the bar: "57,219
steps lost — the disk filled up". No line may trend upward late except
"chose to dig"; no cause for the era ending may be annotated on the
timeline itself.

**Serves:** The chapter asks the reader to hold several million-step
landmarks at once; one strip replaces the mental arithmetic.

---

## Chapter 14 — Wanting follows expecting

### 14.1 ○ `statue-at-the-workshop` — scene

**Place:** after "What stood instead was a statue: a bot that stands
where the log is, knowing how to get it, and never starting."

**Show:** The bot (blocky, two cubes tall, grey-blue, single dark visor
band) stands in a clearing of a simple voxel landscape — flat grass,
square-edged terrain, blocky stone underfoot. The bot itself is rendered
as carved grey stone — veined, mossy at the ankles, on a low stone
plinth — while everything around it is in normal color. Within arm's
reach on its right, one upright oak-log column, bark intact, completely
undug; on its left, a waist-high crafting table with a 3×3 grid on top.
Above the bot, a thin-outlined thought bubble holds three small icons
joined by right-pointing arrows: a log, a stack of planks, two crossed
sticks — crisp, bright, fully formed, so the knowledge reads as intact.
Arms at its sides, feet half-sunk into a worn circle of bare earth
indicating long stillness. Mood: quiet, faintly comic, a monument to
not-doing. Do NOT show the log cracked or partly mined, tools in hands,
any human or animal, health/hunger bars, a HUD, on-screen text, or
Minecraft branding.

**Serves:** Readers assume the bot failed because it couldn't; this shows
it knew the whole chain, stood at its start, and never began — what the
chapter names "election."

### 14.2 ● `motivation-stack-and-twins` — diagram

**Place:** after "…a pure itch, a grinder who cannot quit; borrowed
goals, a sycophant; imagination, a dreamer."

**Show:** A vertical stack of six masonry-course slabs, widest at the
bottom, each resting on the one below; bottom to top exactly: "Budget —
life aimed at the calorie", "Deficits — hunger makes some things valuable
now", "Option-value — a log is money", "Completion itch — begun things
want finishing", "Borrowed goals — what the parent wants", "Imagination —
futures not yet lived". Right of each slab, a thin bracket points to a
small circular portrait of the same grey-blue bot exaggerated into one
failure, lowercase nameplate beneath, bottom to top: "the miser"
(clutching one tiny coin, hollow cheeks), "the monomaniac" (single
enormous eye locked on one apple), "the hoarder" (buried to the chest in
stacked logs), "the grinder" (swinging at a wall worn into a groove),
"the sycophant" (beaming up at a floating pair of clapping hands), "the
dreamer" (on its back watching cloud-castles). A single upward arrow
along the stack's left edge: "each layer exists to patch the failure of
the one below". Slabs in warm neutral tones, labels inside them; twin
portraits in a lighter tint reading as a side column. Do NOT number the
layers, draw any layer detachable or floating, add extra layers, connect
the twins to each other, or add commentary beyond the labels named.

**Serves:** This is the map the chapter says ordered the whole research
queue, and chapter 16 refers back to its bottom layer — the reader needs
one picture to return to. (Draw once at full detail; later chapters may
reuse it as a small greyed locator with one layer highlighted.)

### 14.3 ○ `the-cliff-the-frames-blur` — chart

**Place:** after "The head measured 0.0081 where the frames had measured
0.0612, the same channel read ten times finer than a single tick after
roughly 5,000 online updates from a cold start."

**Show:** A single line chart. X-axis "one dig: twelve ticks", marks 1 to
12; y-axis "how cracked the block is (0 to 1)". The true signal, solid
ink, climbs in eleven small even steps from 0 to near 1, then drops
vertically to 0 at tick 12, where a small log icon sits above the axis
labeled "the block breaks: cracks vanish, a log lands in the pocket".
Overlay two predictions: a thick soft blurred band in slate blue, "what
the frames predict — smooth, and it rounds the cliff away", rising gently
and sagging through the drop without reaching either extreme; and a thin
sharp amber line, "what the event head predicts — one model per action,
sharp at the jump", tracking the true line closely, vertical drop
included. Two callouts connect to their lines: "frames: typical error
0.0612" and "event head: typical error 0.0081". A dashed horizontal
bracket low on the chart: "one tick of digging is worth 0.083 — anything
blurrier than this cannot rank the steps". No robot, landscape, other
channels, gridlines, legend box, or axis numbers beyond ticks 1–12.

**Serves:** "The brain's model of its own progress was fog" is abstract
until the blurred line visibly fails to clear a bar drawn at one tick's
worth of progress.

---

## Chapter 15 — A label, not fuel

### 15.1 ○ `praise-arrives-as-a-number` — diagram

**Place:** after "The frames never got that far in forty-five."

**Show:** Two stacked bands sharing one horizontal time axis labeled
"ticks around one stick-craft". Top band: a strip of 33 small squares
labeled "everything the bot senses, 33 numbers"; 32 neutral grey, the
last outlined and labeled "channel 33: the teacher's well-done". Above
the strip floats a pair of translucent clapping hands — no body, no
face — with a small ribbon "well done" and a vertical arrow dropping into
the 33rd square at exactly the tick where a small crossed-sticks icon
sits on the axis; beneath the strip a narrow trace shows that channel
spiking to 1.0 on that one tick and flat 0.0 elsewhere, labeled "the
pulse: 1.0 on the tick, 0.0 otherwise". Bottom band: a line chart, x-axis
"how many approvals the pupil has seen, 1 to 45", y-axis "what the pupil
expects on the completion tick, 0 to 1". One sharp amber line, "event
head", rises steeply to 1.000 inside the first five approvals and stays
flat, a dot at approval five labeled "0.450 by the fifth"; a flat line
along zero, "event head, off the completion tick: 0.000"; a scatter of
twenty-four faint wandering slate-blue traces, "frames: one per pupil,
still a lottery at 45", several ending low and five dipping below zero
with the note "five pupils expected less praise at exactly the tick it
always came". Do NOT draw a teacher's body or face, a speech balloon with
dialogue, a food treat, a coin, or anything implying the bot consumes the
praise.

**Serves:** A lay reader pictures praise as a spoken word or a reward;
this shows one number on one wire, and puts the headline result beside
the old failure it overturned.

### 15.2 ● `the-post-approval-hangover` — diagram

**Place:** after "…so the bot avoids the loop that earned it."

**Show:** A closed circular loop of four rounded boxes joined by
clockwise arrows, labeled in order: "walk to the wood", "dig a log",
"craft planks", "craft sticks — the well-done lands here". A starburst
with a small ribbon "well done" sits on the fourth box. Every arrow
leaving the fourth box and continuing around the loop is drawn in the
warning color, carries a downward minus badge, and is tagged "predicts
the praise falling → taxed". From the fourth box a single pale dotted
arrow points outward, away from the circle, to a faded box "something the
bot has never tried", tagged "predicts nothing → untaxed"; the bot is
drawn mid-step on that outward arrow, leaning away, back to the loop.
Below the circle, a small inset trace shows the verdict channel spiking
to 1.0 at the craft tick and dropping to 0.0 after, labeled "the pulse
the head learned to expect — and learned to see decay". A caption strip
along the bottom: "the moment praise lands, every way back to it looks
like praise going away". Do NOT draw the bot as sad, ill, or drunk
despite the word hangover; no human figure, drink, bar, or reward object.

**Serves:** The sign flip is the chapter's least intuitive claim; seeing
the loop's own continuations become the penalized arrows makes it obvious
in one look.

### 15.3 ○ `the-log-hoarder` — scene

**Place:** after "At the higher doses behavior collapsed into log-hoarding
with zero sticks (one pupil stacked 100 logs; another, at the highest
dose, 156)."

**Show:** A portrait-style scene framed like a museum specimen card. The
bot stands in a voxel clearing, dwarfed by an enormous, absurdly neat
tower of stacked oak logs piled beside it — tall enough to run off the
top of the frame — both arms wrapped around the base of the stack. On the
ground beside it, a crafting table with an empty 3×3 grid, cobwebbed,
clearly untouched, carrying a single small tag "sticks: 0". At the far
edge, a translucent pair of clapping hands — no body, no face — hovers
dim and turned slightly away, a thin dashed line running from the bot
toward it that stops short and frays out. A lowercase nameplate along the
bottom: "the hoarder". Muted, slightly comic palette; the precision of
the stacking is the joke. Do NOT show planks or sticks anywhere, tools in
hands, a human figure, a HUD, an inventory grid, or any numbers besides
the two labels named.

**Serves:** Gives the abstract "70% tax on earning" a face, and continues
the ugly-twin gallery the chapter-14 map introduces.

---

## Chapter 16 — The steps, not the ingredients

### 16.1 ○ `a-label-with-nowhere-to-walk` — scene

**Place:** after "Dwell 100%: the bot stands in the wood loop, which pays
on almost every tick, and the walk to the wall pays nothing at all until
its final step."

**Show:** A wide side-on view of a simple voxel landscape. Left third:
the bot stands in a worn circle of bare earth beside an upright oak-log
column and a crafting table, small coin-like reward sparks scattered
thickly around its feet, annotated "pays on almost every tick". Right
edge: a tall grey stone wall face with a bright applause starburst above
it — translucent clapping hands, no body — and one single large coin
token at its base, annotated "pays only here, on the last step". Between
them, a wide expanse of flat grass drawn deliberately bare and slightly
desaturated, crossed by a dashed footpath with no tokens on it at all,
annotated "twelve demonstrations walked this, and nothing values the
walk". The bot faces the wall, clearly able to see the applause, but its
feet stay planted in the left circle while a faint dotted arrow starts
toward the wall and dissolves after two steps. Mood: comic stalemate —
the reward visible and unreachable the way a fridge is unreachable from a
sofa. Do NOT show cobblestone in the bot's possession, cracked stone, a
digging action, a human figure, a HUD, or any text beyond the three
annotations.

**Serves:** The label gate's failure is easy to misread as "the bot
didn't want the stone"; the picture shows the real cause — the ground in
between paid nothing.

### 16.2 ● `recipe-memory-and-the-pointer` — diagram

**Place:** after "…the subgoal is the next position in the recipe instead
of the final workshop, and the pointer advances when the bot gets within
a block."

**Show:** Two stacked registers. Top register, "what the demonstration
left behind: one recipe": a left-to-right filmstrip of eight square
frames joined edge to edge, each a simplified snapshot of what the bot
sensed along the taught walk: grass, grass, wall approaching, wall face,
wall face, digging, digging, and a final frame showing a cobblestone in
the pocket. The final frame is outlined brightly and carries a small
clapping-hands badge, "the applause, remembered inside the ending".
Bottom register: the same eight positions as footprints across a strip of
voxel ground running from a crafting table on the left to a grey stone
wall on the right; the bot stands on footprint three, a solid arrow from
it to footprint four labeled "the subgoal is the next step, not the far
end", a dashed circle one block wide around footprint four labeled
"pointer advances within a block". A thin vertical tie-line connects
filmstrip frame three to footprint three — the two registers are the same
sequence. Right of the filmstrip, a small boxed note: "two recipes
stored — wood, ending in sticks, no applause; stone, ending in
cobblestone, applause remembered. Pick the ending worth more." Filmstrip
in cool tones reading as memory; ground register in normal scene color.
Do NOT draw the bot digging or crafting in the bottom register; no map,
plan tree, search graph, checklist, or human figure.

**Serves:** The title claim is that the order was already sitting in the
teaching; a recipe is a remembered run of sensations with a pointer
walking it, not a plan somebody wrote.

### 16.3 ○ `the-stipend` — chart

**Place:** after "The frontier drive's median survival, measured: 4,250."

**Show:** One chart, two registers on a shared x-axis labeled "ticks of
one life, 0 to 5,000", marked only at 1,500, 3,000, and 4,250. Upper
register, a filled band labeled "the parent pays the bill": solid at full
height from 0 to 1,500, sloping in a straight line to nothing at 3,000,
empty after; the flat section annotated "childhood: costs covered", the
slope "weaning". Lower register: y-axis "energy, 1.0 down to 0 (0 is
death)", two lines labeled directly on the line. "A bot that never feeds
itself": flat at 1.0 through 1,500, bending down through the taper,
steepening after 3,000, reaching zero exactly at 4,250, a small marker
reading "predicted 4,250. measured 4,250." "A bot that works": dips
slightly during weaning then holds high with small saw-teeth, one tooth
annotated "+0.1, every time something lands in the pocket". Two distinct
line colors. Do NOT draw a robot, a parent figure, a skull or grave,
gridlines, or axis numbers other than 1,500 / 3,000 / 4,250.

**Serves:** Provisioning is not a softened world but a covered bill
fading on a schedule — and it lands the one prediction in the whole arc
that hit its number exactly.

---

## Appendix — The anatomy of a body

Appendix figures live in `src/appendix/figures/a<N>-<slug>.svg` (the
appendix has no chapter number; `a<N>` replaces `<NN>`). All three are
diagrams, built 2026-08-16. The counts they draw were verified against
the running body declaration (`c1_anatomy()`: 86 numbers, 13 acts), not
copied from prose.

### A.1 ● `the-anatomy-of-a-body` — diagram

**Place:** after "Here is the body the bot wears in Minecraft today,
grouped the way a doctor would group it:"

**Show:** The bot (the cast's blocky grey-blue figure, two cubes tall,
single dark visor band, no face) stands centered on a thin ground line
between two faint terrain blocks. Left column, in world blue: seven
sense groups with monospace eyebrow labels — EYES (glance ·32, blocks
·3, drops ·8), BALANCE (pose ·5), TASTE (aim ·9), GUT (vitals ·2, flood
·4), SKIN (env ·4), POCKETS (pocket ·4, hand ·7, grid ·7), FINGERTIPS
(mining ·1) — each with a two-line plain-words gloss, thin leader lines
to dots on the body. Right column: THE HEAD in ink ("empty on purpose —
the brain is not a body part"), then MOUTH (use held), HANDS (six item
acts), LEGS (five movement acts), and IDLE in warm amber, the acts
being the system's own. Monospace tallies top left and right: "IN — 86
numbers · 12 sense channels" / "OUT — 13 acts · one per tick". A full-
width bracket beneath captions it: "the survival body for Minecraft —
sensors in, actuators out, and no brain on the list". Do NOT give the
bot a face or anything inside the head — the emptiness is the claim;
the head and body fill is the frozen wash.

**Serves:** The first figure anywhere in the book that opens up a
single body and names its parts; the anchor for the appendix's
organ-by-organ walk.

### A.2 ● `what-crosses-the-seam` — diagram

**Place:** after "Categories are the brain's to form."

**Show:** Top: a horizontal strip of 86 small white squares outlined in
world blue — the sensor strip — with thin blue underbrackets grouping
them into the twelve named channels, monospace labels staggered on four
rows (pose ·5 … aim ·9). A thick ink arrow drops to a white engine card:
"the same engine, unchanged / the frames · the drive · the event head /
none of it lives in the body". A second arrow drops to a row of 13
white squares outlined in amber — the acts — labelled forward, back,
turn L, turn R, jump, dig, place, idle, swap, put, take, result, use
held. A thin blue return line runs up the right edge, labelled
vertically "the world answers", back into the strip. Beneath: "no names
cross the seam — things appear only as properties and an appearance
signature", then the bracket caption "a body is exactly two lists —
meaning is learned, not configured". No reward symbol anywhere — the
absence is deliberate.

**Serves:** The honest reduction behind A.1's organ words: what the
brain actually receives and returns, and the loop that is its only
feedback.

### A.3 ● `different-worlds-different-bodies` — diagram

**Place:** after "Ask for another world and you get another body:"

**Show:** Left: a white engine card ("the same engine, unchanged")
plugged into a tall frozen-wash socket strip labelled "the seam" —
the same seam motif as chapter 12's one-seam-many-worlds figure, which
this extends. Right: five bodies drawn as strips of small cells at one
shared scale, blue cells for numbers in, amber for acts out: CartPole
4 · 2, the demo rover 10 · 4, a ROS2 robot 12 · 4 (note: "snap on a new
sensor — the strip grows; the brain resizes without forgetting"), the
sample-field probe 16 · 7 (note: "nothing structural shared — same
engine, zero code changes, 24/24 bars"), and Minecraft's survival body
86 · 13, whose strip dwarfs the rest. Bracket caption: "different
worlds grow different bodies — the engine only learns two numbers: how
many senses, how many acts".

**Serves:** The world-dependence of anatomy made visible at a glance —
the length of the strip is the only thing the engine ever needs to
know.

## Appendix — The anatomy of a brain

The head-side sibling of the body appendix, same `a<N>` numbering.
Both figures built 2026-08-18; zone names verified against the running
code (`FrameStore`, `RecipeMemory`, `CompletionItchPolicy`) and the
record's design 0018 the same day.

### A.4 ● `the-anatomy-of-a-brain` — diagram

**Place:** after "here the parts share one picture, because a question
keeps arriving in different clothes: when the brain knows something,
where does that knowledge live?"

**Show:** Top left, in world blue: a slim observation bar ("86 numbers,
fixed order") with a blue arrow dropping into a large ink-outlined box
titled "THE BRAIN — one engine, every body". Beside the bar, dim: "some
of what streams in is knowledge kept at the seam: the palate's prices,
the flood of hunger". Inside the box, left: a white card "THE FRAME
STORE — small rival maps, born on demand, kept while they pay" holding
three small map·guess·learn cards and a trailing ellipsis, with a
nested amber-stroked card "EVENT HEAD — what will this act change?".
An ink arrow leads right to a white card "MOTIVATION — the posture,
this moment" listing in monospace: drive value, + κ · the itch, + β ·
the label, × κ_d · the deficit, + κ_c · commitment, with a nested
heavy-ink card "RECIPE MEMORY — taught steps, as themselves". A
frozen-wash bar spans the box's foot: "THE SNAPSHOT — every box above,
one file, restored byte for byte — the brain travels as an artifact".
An amber arrow exits the box upward to "OUT — ONE OF 13 ACTS". Caption
beneath the box: "nothing enters except as a sense; nothing inside is
ever finished".

**Serves:** The first picture anywhere of the whole head at once — the
anchor for the appendix's zone-by-zone walk, and the head-side answer
to A.1.

### A.5 ● `where-knowledge-lives` — diagram

**Place:** after "So the honest split: inside the brain live skills,
expectations, and one small shelf of taught steps, all plastic, all in
chapter 11's snapshot. Facts prefer to live outside."

**Show:** Two panels. Left, ink-stroked: "INSIDE THE BRAIN: SKILLS —
plastic · snapshotted · learned by living", stacking three cards:
FRAMES (how each corner of the world answers), EVENT HEAD
(amber-stroked; what each act will change), RECIPE MEMORY (heavy ink;
taught chains, the one shelf inside, grown by teaching alone). Right,
blue-stroked: "AT THE SEAM: FACTS — artifacts the world holds ·
sensed, never injected", holding one blue card "THE PALATE — a price
book / born all zeros, written by meals alone / gem 1.000 · crystal
0.100", then two short arrows: amber rightward "eating writes it (an
act like any other)", blue leftward "the worth sense reads it back",
and the line "copy the file: another brain can taste with it". Rule
centered beneath both panels, bold: "whatever the brain knows beyond
its body, it senses".

**Serves:** The book's one picture of the knowledge-and-skill split:
why this architecture keeps facts in artifacts a reader can inspect,
and skills in the learner that earned them.

## Set-aside ideas (if a chapter runs short on art)

- Ch 6: a trail worn into a field by footsteps that were never recorded —
  the no-scrapbook idea as landscape.
- Ch 8: a cartographer drawing a coastline with a limited supply of ink —
  the map sized to the mapmaker's budget, not the territory.
- Ch 14: a four-arm bar chart of election and chains (no itch 0/24, 0
  chains; itch on the brain's foggy signal 11/24, 5; itch on the oracle
  24/24, 6; itch on the event head 24/24, 13), captioned "the student
  beat its oracle".
- Ch 16: the time-machine distortion — the world's clock spun up ten
  times while the bot's own steps stretch: 17 brain steps to cross one
  block against 4 at normal speed.
- The oracle ghost's exit: wherever the last crutch disappears, the
  dashed translucent world-copy drawn greyed out and gone.
