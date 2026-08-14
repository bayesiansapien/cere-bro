# Agent Harness Engineering (Loop, Harness, Graph)

**Concept page.** The structured execution layer built *around* a foundation model that turns raw model capability into reliable long-horizon behavior. This page unifies the research thread and the practitioner thread, which have converged on the same claim from opposite directions: **the harness, not the model, is now the primary object of design, evaluation, and cost.**

*Provenance note: this page merges published research (digest sources) with a large cluster of practitioner articles surfaced via saved reading in 2026-08. Specific saved items are tracked in the private curation index; the durable knowledge and paper sources are recorded here.*

---

## The vocabulary (glossed once)

Three terms get mixed together constantly. They are layers, not synonyms:

- **Harness** — the whole scaffold around the model: context constructor, memory substrate, skill/tool routing, orchestration loop, and verification/governance. "Everything that isn't the weights."
- **Loop engineering** — designing the automated cycle (generate → critique → revise → act → verify) so the *system* prompts the model repeatedly, instead of a human prompting it by hand. The slogan: "the human should not be the loop."
- **Graph engineering** — the next layer up: wiring multiple agents, memory, and state into a structured graph. The practitioner framing: "loops make agents *think*; graphs make agents *remember* and coordinate."

Model-bound vs harness-bound is the key diagnostic: some tasks are limited by the model, others by the harness. **Smarter models do not make the harness matter less** — they raise the ceiling the harness has to reach.

---

## The core claim, and why it holds

Same model, same task, same prompt: move the work between two harnesses and **cost-per-success swings 5x to 30x** (omarsar0's preregistered benchmark, arXiv 2608.01347, surfaced 08-13). That single measurement is the empirical spine of the whole field: if the harness moves cost by more than an order of magnitude while the model is held fixed, then the harness is where the optimization budget belongs.

The same paper found a subtler result: prompt wording changes *where* effort goes, not just how much. "Try multiple approaches" inflates reasoning 2.4x–7.4x and spawns ~3 discarded solution branches for one implemented fix, with **no gain in success rate**. "Maximum certainty" instead triggers repeated verification (extra test runs, tool calls, turns, latency, context growth). The prompt is a cost dial most people turn blindly.

**Tier 1 intersection (efficiency):** this is a cost-optimization result, not just an agent-design result. Harness choice is a lever on serving cost, token spend, and latency — the same axis as KV-cache and inference work.

---

## How the idea evolved (the wiki's timeline)

1. **Code as Agent Harness** (arXiv 2605.18747, [summary 05-23](2026-05-23-code-as-agent-harness.md)) — the first strong articulation: code is the harness because it is executable, persistent, version-controlled, and compositional. Natural-language plans and raw tool-call sequences are none of these. Karpathy's Autoresearch (program.md + train.py + git log) is the canonical instance.
2. **Scaling the Harness** (arXiv 2605.26112, [summary 05-27](2026-05-27-scaling-the-harness.md)) — the position paper: *system* scaling, not model scaling, is the next bottleneck. Names the six harness components (foundation model, context constructor, memory substrate, skill-routing layer, orchestration loop, verification/governance) and calls for harness-level benchmarks measuring trajectory quality, memory hygiene, and context efficiency instead of one-shot task success.
3. **HarnessOpt-Bench** (08-07, per the [08-08 weekly](../daily-digest/2026-08/2026-08-08.md)) — made "can a model optimize its own harness" measurable. The benchmark for the self-improving-harness idea.
4. **The cost measurement** (omarsar0, arXiv 2608.01347, 08-13) — put the 5x–30x number on harness choice. Turned a design intuition into an efficiency fact.
5. **LongHorizon-Harness** (arXiv 2608.01964, Alibaba, 08-13) — the state-management mechanism: a Manage-Execute-Audit (MEA) loop keeps task state *outside* the execution context and updates it only on environment-verified facts, so wrong self-assessments stop propagating across long tasks. The rigorous answer to "how do you engineer the loop."
6. **The capability measurement** ([AI4AI at Test-Time](../inference-efficiency/2026-08-13-ai4ai-test-time-harness-transfer.md), arXiv 2608.12307, 08-13) — the twin of item 4. A strong *builder* model writes an inference-time harness for a weaker *target* model, refining it against a 5% validation split, and average target performance on four Theory-of-Mind benchmarks goes **0.49 → 0.91 with the target's weights never touched**. Harness choice moves accuracy by roughly 2x on a fixed model, the way it moves cost by 5x–30x.
7. **The safety statement** ([Agent Safety Should Be a Runtime Contract](2026-08-13-agent-safety-runtime-contract.md), arXiv 2608.11274, 08-13) — the harness is also where safety belongs, as a preventive face (sandboxes, permission gates, trajectory monitors) plus an **evidential face** (no task-complete claim without checkable proof: test runs, log captures, file diffs, citation grounding). Backed by a title-level audit of all 28,560 NeurIPS/ICML/ICLR 2023–2025 papers showing an **8x–12x imbalance between training-time and deployment-time safety publication**.

Running through all seven: **capability lives in the harness, not just the weights**, and the harness deserves to be designed, benchmarked, cost-optimized, and *governed* as a first-class object.

### What AI4AI adds to the mechanism story

The most useful part is not the headline number but the mechanism analysis, because it says what a harness is actually *for*. The gains do **not** come from the target reasoning more or sampling more widely, which is what a better prompt would produce. They come from three moves: **offloading unstable reasoning steps into deterministic code**, **routing per question type**, and **strict answer-format enforcement**. All three remove model discretion rather than adding model effort.

That is the same conclusion [Spark-to-Paper (08-13)](2026-08-13-spark-to-paper-composable-research-skills.md) reached independently in a different subfield: its first design principle is separating model-based judgment from deterministic operations that can be executed and checked, and its ablation shows fabrication detection rising from **14% for a single-pass draft to 92% with the full integrity stack**. Two papers, same board, different tasks, one conclusion: **the harness wins by taking decisions away from the model.** That is a sharper statement of the concept than "scaffolding helps," and it is falsifiable: a harness that improves results purely by giving the model more room should not show this signature.

---

## The practitioner convergence (2026-08, surfaced via saved reading)

Independently of the papers, a wave of practitioner writing landed on the identical thesis, with sharper operational language and proof points:

- **From prompting to loop engineering.** The consensus statement (attributed to senior engineers including OpenClaw's creator): "you shouldn't be prompting coding agents anymore; design the loop that prompts them." Proof point cited: one engineer shipping **259 merged PRs in a month**, the AI writing every one, never opening an editor.
- **The four loop types + the evaluator** (Claude-Code-specific loop-engineering guides), and "the four bills nobody warns you about" — the cost gotchas of running unattended loops. This is the practitioner rediscovery of Scaling-the-Harness's "context efficiency" concern.
- **Loop → Graph engineering.** The claimed frontier shift: once loops work, wire agents into graphs for memory and multi-agent coordination. Framed as "graphs make agents remember."
- **Model-bound vs harness-bound** entered practitioner vocabulary directly (an article by that name), matching the research diagnostic.
- **Market signal:** Forward Deployed Engineers reportedly command ~$1M/year and Anthropic $750k+ for harness/loop skill specifically. The industry is pricing the harness, not model access.

That research and practitioners reached the same frame in the same window is the strongest possible confirmation that this is a real structural shift, not a hype cycle.

---

## Relation to neighbouring concepts

- **[Agent memory](agent-memory.md)** — the memory substrate is one of the six harness components. The "RAG is a dead end / memory should be native to the model" turn (08-13) and the write→manage→read memory-engineering formalization are the memory layer of graph engineering.
- **[Self-evolving agents](self-evolving-agents.md)** — self-improving loops (agents that rewrite their own harness/skills) are harness engineering closing the loop on itself; HarnessOpt-Bench measures it.
- **Context engineering** — "delete 80% of the system prompt" (Anthropic/Cloudflare/Karpathy, 08-13) is the token-optimization face: the harness win is often in what you *stop* keeping in context.

---

## Industry has started pricing the harness directly (2026-08-13)

The market signal moved from salaries to product this week. **xAI shipped Grok 4.6 and stated that Grok 4.6 optimized the Grok Build harness for itself** ([@aksheyd](https://x.com/aksheyd/status/2087622695718662338)), and Hugging Face's Elie Bakouch, reading the model card, noted the model is **state of the art on an internal "inferenceEval" that measures optimization of xAI's own chat inference** ([@eliebakouch](https://x.com/eliebakouch/status/2087659219956928873)). Two of the capabilities a frontier lab chose to headline are the model improving its own scaffold and its own serving path.

That is the industrial instance of the research claim, and it lands the same week AI4AI measures strong-to-weak harness transfer and AutoWorldModel-Bench measures agents improving an external artifact under an unspecified objective in [63 of 64 sessions](2026-08-13-autoworldmodel-bench.md). The gap worth watching: xAI reports a self-optimized harness as a capability headline and publishes no cost-per-success number, which is precisely the measurement omarsar0's benchmark made the field's spine.

### The first public model-by-harness cost table (Terminal-Bench 3.0, 2026-08-13)

Terminal-Bench 3.0's leaderboard is the closest public artifact to the measurement this page keeps asking for, because **every row is a model-harness pair reported with token count and dollar cost alongside accuracy** ([screenshot](https://x.com/aksheyd/status/2087701375300026561)):

| Rank | Model | Agent harness | Resolution rate | Tokens | Cost | Cost / point |
|---|---|---|---|---|---|---|
| 1 | Opus 5 (max) | mini-SWE-agent | 42.7% ± 1.6% | 7.3B | $5.8k | ~$136 |
| 2 | GPT-5.6 Sol (max) | Codex | 34.6% ± 1.6% | 5.8B | $4.0k | ~$116 |
| 3 | Fable 5 (max) | Claude Code | 34.1% ± 1.7% | 3.6B | $6.5k | ~$191 |
| 4 | Grok 4.6 (high) | Grok Build | 26.5% ± 1.5% | 2.9B | $2.1k | ~$79 |
| 5 | Opus 4.8 (max) | Claude Code | 21.1% ± 1.6% | 5.2B | $5.2k | ~$246 |
| 6 | GPT-5.6 Terra (max) | Codex | 20.8% ± 1.4% | 7.0B | $2.5k | ~$120 |
| 7 | Grok 4.5 (xhigh) | Cursor CLI | 15.7% ± 1.5% | 1.2B | $766 | ~$49 |
| 8 | Sonnet 5 (max) | Claude Code | 14.6% ± 1.5% | 17.9B | $6.9k | ~$473 |
| 9 | GPT-5.6 Luna (max) | Codex | 14.3% ± 1.3% | 11.9B | $1.6k | ~$112 |
| 10 | GLM 5.2 (max) | Claude Code | 4.6% ± 1.0% | 3.3B | $3.4k | ~$739 |

Three readings. **Token spend does not track accuracy**: Sonnet 5 in Claude Code burns 17.9B tokens for 14.6% while Fable 5 in the *same* harness reaches 34.1% on 3.6B, a 5x token difference in the opposite direction from the score. **Ranking by cost-per-point reorders the table**, moving Grok 4.6 from fourth to second and dropping Fable 5 from third to seventh, which is the argument for reporting dollars-per-completed-task as the primary agentic metric. And **the grid is still not an ablation**: no model appears under two harnesses in the top ten, so the leaderboard shows harness variation is present without isolating it. Holding one model fixed across mini-SWE-agent, Codex, Claude Code, Grok Build and Cursor CLI remains the missing experiment, and it is now cheap enough that somebody should just run it.

---

## 2026-08-14: the harness stops being written and starts being optimized

One day after the cost and capability measurements landed, three things arrived together that change this page's central claim from *the harness is the object of design* to **the harness is the object of optimization**.

**[DarwinX](2026-08-14-darwinx-harness-population-evolution.md) (arXiv 2608.07545, Salesforce) makes harness search a population problem.** Model frozen, one evolution loop, about **+17 points average across four benchmarks**. Terminal-Bench 2.1 goes +7.7 to 83.2% on a matched base and 84.7% on a stronger one; TerminalWorld's held-out split hits 68.3%; WebArena-Infinity real-task pass@1 goes 43.5% → 93.0% audit-clean; and a Terminal-Bench harness **transfers unchanged to SWE-bench Verified**. Its diagnosis of prior work is the part that matters here: every self-improving harness in this wiki's timeline above is a **single lineage**, which is path-dependent and lets a local win silently regress another task. DarwinX's three fixes are a **preserve-and-extend contract** (admit a variant only if it extends coverage without regressing), an **archive of alternative lineages** for later recombination, and **one shared edit interface** for failure-derived, teacher-derived and self-derived evidence. Fitness comes from each benchmark's own verifier, so no gold solutions and no human picks winners.

This resolves the isolation experiment [08-13's Looking Ahead](../daily-digest/2026-08/2026-08-13.md) predicted for a 60-day window. The Terminal-Bench 3.0 table above shows harness variation exists but never holds a model fixed across two harnesses; DarwinX does exactly that on 2.1 and gets +7.7 points from the scaffold alone. Open problem 1 below is now half-answered: the swing is real at the frontier, though still not *predictable* in advance.

**[AutoDesign](2026-08-14-autodesign-meta-harness-optimization.md) (arXiv 2608.13560) supplies the missing price tag.** A meta-harness optimizer guides a code agent to rewrite its own harness from rollout feedback, aligned to human design priors. On the new PosterBench (100 papers, five disciplines) it scores 78.32, **beating the commercial Claude Design by 7.45 points**, and the learned DesignHarness dropped into **seven** other code-agent-model configurations lifts the average from 54.99 to 67.39. The number this page has been asking for since 08-13: **253 tool calls, 11 editing turns, 40 minutes, under $3**, fully autonomous. Harness optimization costs single-digit dollars per rollout.

Note what the pair does jointly. DarwinX optimizes against **hard verifiers** (a test either passes or does not) and reports no cost. AutoDesign optimizes against a **soft verifier** (a design rubric plus human preference) and reports full cost. Neither tests the other's regime, and whether meta-optimization degrades when fitness is soft is now the sharpest open question in this area.

**[DeepSeek Harness v0.1](../inference-efficiency/2026-08-14-deepseek-harness-kv-cache-economics.md) makes prefix stability a billing line.** DeepSeek open-sourced its agent harness under MIT (built on the Cordis meta-framework, where models, tools, skills, sessions, sandboxes, filesystems, loops, orchestration and UI are *all* plugins) on the same day it raised API prices with **cache-hit tokens repriced to roughly 6x**, plus a new peak/off-peak split at 50% below peak. Hugging Face's Elie Bakouch, reading the code, found the harness's organizing commitment is **first-class KV-cache-aware design: previously written history is never altered**; a change is expressed by appending a statement describing the modification rather than editing the prefix, because editing invalidates every cached token downstream. Bakouch also estimates **at least ~20% of the harness's own commits came from Codex worktrees**.

That is this page's Tier 1 efficiency claim arriving from the provider side. The 5x–30x cost-per-success swing was measured by varying harnesses at fixed prices; DeepSeek varied the prices at fixed harness design and reached the same conclusion. **Append-only history is now a cost property, not a latency nicety**, and it is cheap enough to implement that convergence across harnesses is likely within a quarter.

**[Ken Huang's Harness Engineering](2026-08-14-ken-huang-harness-engineering-patterns.md) supplies the governance half the research thread lacks.** His periodization (model as product → wrapper as product → **harness as product boundary**) is the industry statement of [Scaling the Harness](2026-05-27-scaling-the-harness.md)'s thesis, and his ten pattern families are a superset of that paper's six components with three additions research has not touched at all: **identity, data governance, and runtime steering**. His "hill climbing" family states the rule DarwinX independently implements: improvement is only safe when it is measured, bounded, and reversible. A security architect and a research team converged on the same admission rule within one day of each other.

**Updated state of knowledge.** The harness is measured on cost (5x–30x swing), measured on capability (0.49 → 0.91 at the small-model tier, +7.7 points at the frontier), **optimizable by population search and by meta-optimization**, **transferable across tasks, verifiers, base models and agent frameworks**, **priced by providers** through cache-hit economics, and now **has a governance taxonomy**. Five papers and one product release in six days. The gap that remains is the same one: nobody has put harness optimization and fine-tuning on a single cost axis for equal capability gain.

---

## Open problems (research angle)

0. **Harness optimization versus fine-tuning at matched cost.** Still unrun, and now more glaring: AutoDesign publishes $3 per rollout, DarwinX publishes no evolution budget, and no distillation paper publishes a comparable per-point cost. The first paper to put the two on one axis settles where a team should spend.
1. **A harness-quality metric that predicts the 5x–30x swing before you run.** omarsar0 measured the swing post-hoc; nobody can yet predict which harness wins for a given task class without a full benchmark. This is the single highest-value open experiment.
2. **Composing the pieces.** LongHorizon's state-outside-context, HarnessOpt's self-optimization, and graph-based memory are separate advances. A harness that manages state externally *and* self-optimizes *and* routes through a memory graph has not been built or benchmarked end-to-end.
3. **Where self-simulation of the loop diverges from reality** — the same self-judgment failure mode the reward-hacking thread keeps flagging. A confidently-wrong auditor breaks the MEA loop.
4. **Graph engineering lacks the research the loop layer now has.** The practitioner "graphs make agents remember" claim is mostly ahead of measured evidence. What a graph buys over a well-run loop is not yet quantified.

---

## Sources

**Research (digest):** [Code as Agent Harness](2026-05-23-code-as-agent-harness.md) · [Scaling the Harness](2026-05-27-scaling-the-harness.md) · omarsar0 harness benchmark ([arXiv 2608.01347](https://arxiv.org/abs/2608.01347)) · LongHorizon-Harness ([arXiv 2608.01964](https://arxiv.org/abs/2608.01964)) · HarnessOpt-Bench (08-08 weekly) · [AI4AI at Test-Time](../inference-efficiency/2026-08-13-ai4ai-test-time-harness-transfer.md) ([arXiv 2608.12307](https://arxiv.org/abs/2608.12307)) · [Agent Safety Should Be a Runtime Contract](2026-08-13-agent-safety-runtime-contract.md) ([arXiv 2608.11274](https://arxiv.org/abs/2608.11274)) · [Spark-to-Paper](2026-08-13-spark-to-paper-composable-research-skills.md) ([arXiv 2608.11924](https://arxiv.org/abs/2608.11924))

**Research (digest), 2026-08-14:** [DarwinX](2026-08-14-darwinx-harness-population-evolution.md) ([arXiv 2608.07545](https://arxiv.org/abs/2608.07545)) · [AutoDesign](2026-08-14-autodesign-meta-harness-optimization.md) ([arXiv 2608.13560](https://arxiv.org/abs/2608.13560))

**Industry / practitioner, 2026-08-14:** [DeepSeek Harness v0.1 and cache-hit repricing](../inference-efficiency/2026-08-14-deepseek-harness-kv-cache-economics.md) · [Ken Huang, Harness Engineering pattern language](2026-08-14-ken-huang-harness-engineering-patterns.md)

**Practitioner cluster (surfaced via saved reading, 2026-08):** ~12 articles on loop/harness/graph engineering, the dominant theme in the private curation index by a wide margin; synthesized in the [2026-08-13 Media Zone](../media-zone/2026-08/2026-08-13.md). Enumerated saves live in the private curation index.
