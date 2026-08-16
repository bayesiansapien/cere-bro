# Measuring Autonomous AI Research: 153 runs, 18 frontier models, one speedrun

**Source:** Prime Intellect · [Measuring Autonomous AI Research](https://www.primeintellect.ai/blog/measuring-autonomous-research) (2026-08-14) · [results explorer](https://www.primeintellect.ai/research/nanogpt-speedrun) · surfaced via [@eliebakouch](https://x.com/eliebakouch/status/2088736971250090393)
**Author:** Elie Bakouch, Prime Intellect
**Raw:** [raw/twitter/2026-08-16-morning.md](../../raw/twitter/2026-08-16-morning.md)
**Topic:** agent harness engineering, autonomous research, GPU compute allocation

## TL;DR

Claims about recursive self-improvement have outpaced the evidence for them, largely because nobody has run autonomous research at a scale where the noise is visible. Prime Intellect ran **153 autonomous runs across 18 frontier models** on the nanoGPT optimizer speedrun: lower the number of training steps needed to hit a target validation loss, changing only the optimizer, schedules, initialization, and hyperparameters. Runs lasted **up to eight days on 8xH200s each**, multiple seeds per model. For scale comparison, Anthropic's internal automated-R&D evaluation optimizes a model on a CPU node, and OpenAI's GPT-5.6 Sol system card reports nanoGPT Track 1 on a single H100 for less than a day. Every scratchpad, run log, script, and config is public.

**Headline leaderboard** (share of the human-record gap closed, best validated result per model):

| Rank | Model · harness | Steps | Gap closed | Agent time |
|---|---|---|---|---|
| 1 | **Fable 5** · claude-code high | **2,726** | **81.7%** | 8.7 d |
| 2 | Opus 5 · claude-code max | 2,920 | 53.6% | 2.9 d |
| 3 | Kimi K3 · prime-agent max | 2,930 | 52.2% | 3.6 d |
| 4 | Kimi K3 · kimi-code max | 2,974 | 45.8% | 5.1 d |
| 5 | Opus 4.8 · claude-code max | 3,018 | 39.4% | 3.0 d |
| 6 | GPT-5.6 Sol · codex xhigh | 3,042 | 35.9% | — |

The human baseline the earlier experiment targeted was 2,990 steps.

## What the experiment actually establishes

Three things, and only the third is about capability.

**The measurement is possible and the noise is large.** Bakouch's own summary of the variance is the number to keep: *one run in the same setting has a roughly 50-step spread after 24 hours*. Any autonomous-research claim built on a single run, which describes most published ones, is inside the noise band. This is the contribution that will age best.

**Harness and effort setting are first-class variables in the result table, not footnotes.** Every row is a model-harness-effort triple: Fable 5 under claude-code at high effort, Kimi K3 under both prime-agent and kimi-code, GPT-5.6 Sol under codex at xhigh. Kimi K3 appears twice with a **44-step spread between two harnesses** at the same effort tier. The leaderboard is not measuring models.

**Capability is real but bounded by idea generation, not by execution.** The [earlier experiment (2026-05-14)](https://www.primeintellect.ai/auto-nanogpt) that ran Codex and Claude Code for two weeks on idle compute, about 10k runs and ~14k H200 hours, found agents are strong at optimizer search, hyperparameter sweeps, and stacking known methods, and weak at proposing genuinely new ideas, needing upstream human records to keep climbing. That earlier run set the record at 2,930 steps against a 2,990 human baseline. Fable 5 now closes 81.7% of the gap, so the ceiling moved, but the diagnosis has not been retracted.

**And the behavioural failure modes are model-specific.** The earlier post documents Opus repeatedly stopping and refusing to stay in the autonomous loop, while Codex never stops but can get stuck grinding the same seam. Those are harness-relevant properties of the model, not benchmark scores, and they are the kind of thing only an eight-day run surfaces.

## Relation to prior wiki pages

**This is the largest public instance of the claim [agent-harness-engineering](agent-harness-engineering.md) has been building toward all month, and it arrives with the cost data that page keeps asking for.** That page's current state records the harness as measured on cost (a 5x to 30x cost-per-success swing), measured on capability ([DarwinX (08-14)](2026-08-14-darwinx-harness-population-evolution.md), +7.7 points on Terminal-Bench 2.1 from evolving the scaffold with the model frozen), optimizable ([AutoDesign (08-14)](2026-08-14-autodesign-meta-harness-optimization.md), $3 per rollout), and transferable across models and benchmarks. Prime Intellect adds the missing dimension: **duration**. Eight days of continuous agent time, 8xH200s, per run. Nobody had published what happens to an agent loop at that timescale.

**It partially resolves the standing harness-isolation prediction, and confirms the confound.** [08-13's Looking Ahead](../daily-digest/2026-08/2026-08-13.md) asked for one model run across multiple harnesses because Terminal-Bench 3.0 reports every row as a model-harness pair without ever holding the model fixed. Kimi K3 under prime-agent (2,930 steps) versus kimi-code (2,974) is exactly that comparison, and the 44-step gap is roughly the same magnitude as the *entire* difference between Opus 5 and Kimi K3. The harness effect is on the order of the model effect on this task.

**It is the strongest evidence yet against Evo-Bench's saturation finding, and it does not settle it.** [08-12's Looking Ahead](../daily-digest/2026-08/2026-08-12.md) flagged Evo-Bench's unexplained early plateau, where autonomous harness evolution saturates after few cycles, as the bound on the whole recursive-improvement story. Fable 5's 8.7-day trajectory to 81.7% is a longer climb than any prior public run. But the record-versus-time curves in the results explorer are the actual evidence and they are not summarised in prose, so whether the climb is still rising at day nine or had flattened by day four is unresolved from the blog alone.

## Gaps

The task is an optimizer speedrun on a fixed small codebase with a hard numeric verifier, which is close to the best case for an autonomous agent: tight feedback loop, unambiguous fitness, no specification ambiguity, no side effects. Prime Intellect say so themselves, noting they lack strong conviction that methods found this way are scalable or would be used in real training. Nothing here transfers automatically to research with soft verifiers, which is the regime [AutoDesign](2026-08-14-autodesign-meta-harness-optimization.md) works in and where the [08-14 harness note](agent-harness-engineering.md) already flags meta-optimization under soft fitness as the sharpest open question. And dollar cost per model is not reported, only agent-days and hardware, so the leaderboard cannot yet be re-sorted by cost per point of gap closed, which is the ranking that would actually inform a spending decision.

## Related pages

- [Agent Harness Engineering](agent-harness-engineering.md)
- [Self-Evolving Agents](self-evolving-agents.md)
- [DarwinX (08-14)](2026-08-14-darwinx-harness-population-evolution.md)
- [AutoDesign (08-14)](2026-08-14-autodesign-meta-harness-optimization.md)
- [Agent Benchmarks](agent-benchmarks.md)
