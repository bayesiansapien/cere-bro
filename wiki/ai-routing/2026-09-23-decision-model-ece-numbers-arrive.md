# Day eight of the decision-model boom: the calibration numbers finally arrive

**Source:** X home feed 2026-09-23, the dominant cluster (roughly 25 of 67 ranked posts) · [S1 Bench rankings](https://x.com/ItsCuthulhu/status/2102551440904397144) · [bench.jakecuth.com](http://bench.jakecuth.com) · [Lumma-fev-0.6B](https://x.com/FrontiersMind/status/2102490560229720488) · [Simon Willison's notes](https://simonwillison.net/2026/Sep/21/jev/) · [Tinker](https://x.com/tinkerapi/status/2102565243331490261)
**Raw:** [raw/twitter/feed/2026-09-23-morning-ranked.json](../../raw/twitter/feed/) (gitignored, local)

## TL;DR

A **decision model** (marketed as a "System One model") takes unstructured state plus a fixed option list and returns a typed choice with a probability in one forward pass, never generating natural language. [Jev](2026-09-16-jev-decision-only-model.md) is the hosted original, released 15 September. On [09-19](../daily-digest/2026-09/2026-09-19.md) this wiki predicted that a reliability diagram or expected-calibration-error figure would appear within 60 days and that the curve would look worse than the accuracy numbers implied. On [09-21](2026-09-21-jev-calibration-reckoning.md) a live trading run resolved the *direction* 58 days early while leaving the *measurement* owed, and the digest restated the prediction at 45 days with an explicit decision rule: **ECE under 5% closes the question in the vendors' favour; anything above 15% means every threshold gate shipped this month is decorative.**

**Today the measurement arrived.** A public leaderboard, S1 Bench, now reports **ECE as a first-class column** alongside macro accuracy, seconds per item and decisions per second, across 1,999 items and six subsets. The numbers land in the middle of the band the prediction drew, which is the least convenient possible outcome.

## The numbers on the board

From the published S1 Bench table (screenshot in today's feed, [bench.jakecuth.com](http://bench.jakecuth.com)):

| Entry | Macro acc | ECE | Notes |
|---|---|---|---|
| AutoJev 27B + calibration | 0.795 | **0.048** | best calibrated |
| AutoJev 27B + voting | 0.793 | 0.046 | |
| AutoJev 27B (plain) | 0.794 | 0.069 | local endpoint |
| **jev (hosted anchor)** | **0.775** | **0.076** | the reference product |
| simplejev-qwen38-27b | 0.758 | 0.121 | hosted API |
| djev / djev-full | 0.753 / 0.749 | 0.178 / 0.166 | diffusion variant |
| Decider 35B-A3B | 0.747 | 0.060 | |
| kev-4B / kev-9B | 0.732 | 0.100 / 0.087 | open clones |
| reflex-4b | 0.719 | 0.085 | 4B, CPU |

Several entries carry an explicit "trained on eval sources, not comparable" warning, which the board deserves credit for surfacing rather than burying.

## What this resolves, and what it does not

**Resolved: the measurement exists, 22 days ahead of the 45-day deadline.** The complaint this wiki logged repeatedly through the boom, that 160-plus public projects had produced not one reliability diagram or ECE figure, is now obsolete. ECE is a column on a public leaderboard with a fixed item set.

**Resolved against the strong version of the criticism.** The hosted model's **0.076 ECE is not the disaster the trading run implied.** A 7.6% expected calibration error is mediocre but usable: it means that on average, across confidence bins, the reported probability is off by about seven and a half points. That is well inside the "above 15% means decorative" failure line.

**Not resolved, and this is the important part: 0.076 sits in the dead zone between the two decision rules.** The prediction offered two clean outcomes and got neither. Under 5% would have vindicated the vendors; above 15% would have condemned the deployed threshold gates. Seven and a half points means a threshold set at 0.88 is really admitting somewhere around 0.80 to 0.95, which is fine for a content filter and dangerous for an automated refund. **The category's calibration is good enough that nobody has to stop, and bad enough that nobody should stop checking.**

**Directly explains the 09-21 trading anomaly.** The live run reported 85-88% confidence on nearly every one of 1,838 calls in a near-random domain. An aggregate ECE of 0.076 is fully compatible with catastrophic *per-domain* miscalibration, because ECE averages across an eval distribution and a market order book is nowhere in that distribution. **The board measures in-distribution calibration; the trading run measured out-of-distribution calibration; both results stand and they are not in conflict.** That is the single most useful thing on this page, and it is the caveat any practitioner setting a threshold needs: the 0.076 is not yours until you have measured it on your own traffic.

**The calibration column is now a competitive axis, and it is being optimized directly.** The two top entries are "AutoJev 27B + calibration" (ECE 0.048) and "+ voting" (0.046), both of which *beat the plain model's 0.069 while matching its accuracy*. Post-hoc calibration works, costs almost nothing, and the leaderboard now rewards it. This is exactly the outcome Hamel Husain and the OpenCode team argued for on 09-21 when they insisted the category should be called a classifier so it would inherit the classifier literature's measurement apparatus. **They were right, and the apparatus arrived within 48 hours of the argument.**

## The rest of the day-eight cluster

**The mechanism is now fully commoditized, and the last moat is training data.** Three separate items today: FrontiersMind shipped **Lumma-fev-0.6B**, a 0.6B decision model trained from its own from-scratch base, explicitly positioned "for routing, triage, moderation" with 4B and 9B promised; Tinker demonstrated that **any open LLM can serve the interface for $5 and ten minutes of fine-tuning**, on the observation that next-token prediction is already a probabilistic classifier; and Pydantic's Sydney Runkle reported using **semif**, an open alternative, in production to label incoming GitHub issues with one boolean question per label at a p>0.8 threshold, replacing a previous LLM classifier and running "much faster." That third one matters most: it is the first report on this wiki of a decision model *replacing a deployed LLM classifier in a real repo*, with the threshold stated and an explicit note that the author is "currently monitoring to make sure we're calibrated at the right threshold." Practitioner discipline arriving at the same time as the measurement.

**The ecosystem's shape is now clearly "gates inside somebody else's loop."** Today's repo lists (two large Chinese-language roundups, a 20-item skills list, a 10-item list) are dominated by: context sieves that judge each tool result before it enters context (`winnow`, `fast-jev-compaction`), per-turn model routers (`jev-codex-router`), browser-step choosers (`jev-ultrafast`), and CLI classifiers (`semdecide`). This confirms the [09-20 finding](2026-09-20-decision-primitive-finds-its-use.md) that the primitive's use is not the model-selection routing this page originally predicted. **It is context control.** The single most-starred item, `fast-jev-compaction`, scores every tool call and result in one fast request, drops the stale ones, and keeps everything retained verbatim, which is a direct attack on the lossy-compaction problem that [KVMEM](../inference-efficiency/2026-09-23-kvmem-paged-agent-memory.md) attacks from the cache side today.

**A grift layer has formed and should be discounted.** A visible fraction of today's cluster is engagement-farming: "x200 and x400 cheaper agentic loops," "99% of people pay 200x more," 14-page PDF lead magnets, and a trading-bot repo promoted on latency rather than profit. The ranker's reach-normalized score floats some of these; they carry no measurement and should be read as marketing.

## How this relates to what the wiki already knows

**It closes the loop the [09-18 entry](llm-routing.md) opened** when the decision primitive got its first independent numbers and the routing signal turned out to be transmissible. Eighteen days from product launch to a public leaderboard with a calibration column is fast even by this field's standards.

**It reinforces the 09-21 Global View claim that "a compressed output distribution looks healthy on every quality metric and has stopped carrying information."** The S1 Bench board is the counter-move: by publishing ECE next to accuracy, it makes the variance of the score visible rather than only its average, which is precisely the defence that entry called for. Three literatures shared that defect on 09-21 (decision models, distillation, AI-reviewed science). One of them now has an instrument.

## Gaps

One board, one operator, 1,999 items, six subsets, no published construction methodology for the item set, and several entries self-flagged as trained on eval sources. ECE itself is a blunt instrument: it is bin-dependent, it hides direction (over- versus under-confidence), and an aggregate ECE says nothing about the tail where automated actions actually fire. **No reliability diagram has been published yet, only the scalar.** And nothing here addresses the two mechanism-level defects reported on 09-21: non-determinism across identical prompts and sensitivity to option ordering. A model can post a respectable ECE and still return different numbers when you permute the option list.

## Related pages

- [llm-routing](llm-routing.md) · [Jev: the decision-only model](2026-09-16-jev-decision-only-model.md) · [the calibration reckoning (09-21)](2026-09-21-jev-calibration-reckoning.md)
- [the benchmark ladder and the routing tax (09-22)](2026-09-22-decision-model-benchmark-ladder-and-routing-tax.md)
- [constrained decoding (today)](../inference-efficiency/2026-09-23-constrained-decoding-production-blueprint.md) · [Jev-Mem](../agentic-systems/2026-09-22-jev-mem-system-one-agentic-memory.md)
