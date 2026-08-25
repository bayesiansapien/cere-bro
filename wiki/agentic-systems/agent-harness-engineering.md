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

*The open problem this creates.* If harnesses are portable, optimizable artifacts that lift arbitrary models, then the routable unit is the **model-harness pair**, as [A²E (08-11)](2026-08-11-harness-evolution-cluster.md) argued. [LLM Routing](../ai-routing/llm-routing.md) now records this as a standing gap with three supporting results and zero proposals: **no production router routes over harnesses, and no paper proposes it.**

---

## 2026-08-16: duration enters the measurement, and the cost axis spans three orders of magnitude

Two results extend this page along axes it had no data on, and a third supplies the small-model version of the substitution.

**[Measuring Autonomous AI Research](2026-08-16-measuring-autonomous-ai-research.md) (Prime Intellect) adds duration.** 153 autonomous runs across 18 frontier models on the nanoGPT optimizer speedrun, up to **8.7 days per run on 8xH200s**, all scratchpads and logs public. Every leaderboard row is a **model-harness-effort triple**: Fable 5 under claude-code at high effort closes 81.7% of the human-record gap at 2,726 steps; Opus 5 under claude-code max reaches 2,920 (53.6%); Kimi K3 appears twice, at 2,930 under prime-agent and 2,974 under kimi-code. **That 44-step spread between two harnesses running the same model is roughly the size of the entire gap between Opus 5 and Kimi K3**, which is the harness-isolation comparison [08-13's Looking Ahead](../daily-digest/2026-08/2026-08-13.md) asked for, arriving from an unexpected direction. Bakouch's variance note is the number to keep: **one run in the same setting has a ~50-step spread after 24 hours**, so single-run autonomous-research claims sit inside the noise. The earlier Prime Intellect experiment's diagnosis stands unretracted: agents are strong at optimizer search, hyperparameter sweeps and stacking known methods, and weak at generating new ideas, needing upstream human records to keep climbing.

**[Specification-first convergence](2026-08-16-specification-first-convergence.md) adds a stopping rule for tasks with no oracle.** An agent dismantled a core lifetime invariant across a **717,725-line production TypeScript codebase**, 189 files touched, with no human code review and no pre-existing test for the target behaviour. The protocol: the agent writes a formal specification, 14 refinement cycles audit the specification against the source, the specification is **frozen**, then 17 verification cycles audit the code against it. **201 defects corrected across 31 audit passes before a human ran the program.** Convergence criterion: **two consecutive verification passes returning zero findings.** Three days, **USD 2,430**. The freeze is the direct countermeasure to open problem 3 below, since the auditor is checking against a document it may no longer edit.

**Set the two published cost points side by side and the axis is visible for the first time.** [AutoDesign (08-14)](2026-08-14-autodesign-meta-harness-optimization.md) published **$3 per rollout** for 253 tool calls in 40 minutes. Specification-first publishes **$2,430 for three days** on one architectural refactor. Three orders of magnitude apart, both fully autonomous, both reported honestly. "What does agentic work cost" has no single answer, and any claim that does not name the task class is uninterpretable.

**[SKILLER](2026-08-16-skiller-language-level-rl-skills.md) supplies the cheap tier.** A strong model as actor and critic, the small-model agent system as environment, **every RL signal propagated as natural language**, producing executor-specific skills. Qwen3.5-9B gains 4.3 to 20.4 points, Qwen3.5-4B gains 1.8 to 13.3, and single-skill SkillsBench performance **matches strong closed models**. The paper's stated motivation is that skill-driven harnesses like Codex and OpenClaw are prohibitively expensive at closed-model prices, which is this page's cost thesis stated as a research problem rather than an observation. Parity is claimed on single-skill tasks only; composition is untested.

**Updated state of knowledge.** The harness is measured on cost (5x-30x swing; $3 to $2,430 per task depending on class), on capability (0.49 → 0.91 at the small tier, +7.7 to +17 points at the frontier, 81.7% of a human record over 8.7 days), and now on **duration and variance**. It is optimizable by population search and meta-optimization, transferable across tasks and base models, priced by providers through cache-hit economics, governed by a pattern taxonomy, and **manufacturable for small open models via natural-language RL**. What is still missing is unchanged: nobody has put harness work and fine-tuning on one cost axis for equal capability gain.

---

## 2026-08-25: the harness gets a cost curve, a reference implementation, and a 35B model at the frontier band

Three HuggingFace papers on one day, all treating the harness as the primary object, plus a fourth on the Kurate board. This is the densest single day this page has recorded.

**[Apodex 1.1](2026-08-25-apodex-1-1-environment-coordination-scaling.md) is the model-scale version of this page's thesis, and the day's top paper at 145 upvotes.** It names **working capability** (sustained, verifiable progress toward a real-world objective) as a category distinct from reasoning, constituted by state maintenance, failure recovery, and *verifiable delivery*. It develops that along two axes that are explicitly not parameter count: **Environment Scaling** (expanding the diversity and verifiability of executable file, search and code environments) and **Agentic Coordination Scaling** (training agents to decompose, delegate in parallel, integrate asynchronous results, replan). System side is a shared execution harness plus **AgentOS** maintaining task state and provenance across tools and agents, which makes provenance a first-class harness component exactly as [Scaling the Harness (05-27)](2026-05-27-scaling-the-harness.md) proposed. Result: a **35B** model and a locally deployable 35B Mini reach the leading performance band on finance, research, math, coding and search.

The parameter count next to the benchmark is the whole point. Every prior data point on this page lifted a *fixed* model with a better harness. Apodex trains model and environment together and lands at the frontier band from 35B, which is the strongest evidence here that **on verifiable professional work the marginal value of parameters is below the marginal value of environment and coordination**.

**But it entangles this page's open problem 0 rather than resolving it.** Harness optimization versus fine-tuning at matched cost is still unrun, and Apodex makes it harder to answer, not easier: environment-trained weights and an inference-time harness are both in the deliverable and the paper does not separate them. The ablation that would settle it (freeze the base and apply only harness plus AgentOS; then run the environment-trained weights under a plain ReAct loop) is the single most valuable missing experiment in the paper. Also unpriced: coordination scaling spends tokens on parallel delegation and replanning, and against the [AlphaSense finding (08-14)](../ai-industry/2026-08-14-alphasense-token-price-vs-task-cost.md) that task cost and token price can point opposite ways, a 35B model winning on quality could still lose on dollars per completed task. And "leading performance band" without per-benchmark deltas is not a checkable claim for a result whose entire content is a comparison.

**[Task-CoEvolve](2026-08-25-task-coevolve-adaptive-validation-selection.md) is the first result on this page about the efficiency of the harness search loop rather than the quality of its output.** [DarwinX (08-14)](2026-08-14-darwinx-harness-population-evolution.md) and [AutoDesign (08-14)](2026-08-14-autodesign-meta-harness-optimization.md) established that harness search works, by population selection and by meta-optimization respectively. Neither made it affordable. Task-CoEvolve observes that a validation set's informativeness **decays as the harness improves**: eventually the easy tasks are universally solved, the hard ones universally failed, and only a shrinking frontier band still separates candidates. It concentrates evaluation there by **variance-weighted sampling over past outcomes**, with the sampling distribution adapting as the harness evolves, then recovers comparable full-set scores from the biased sample with an **importance-weighted estimator**. That second piece is what makes the first usable: without it, each iteration measures a different subset and the search loop loses the ability to compare iteration k to k+1. Result: **80% fewer evaluations, matching full-set search's final quality**, on online text classification and Terminal-Bench 2.1 (the same benchmark DarwinX and AutoDesign used, so it is comparable).

This moves one side of open problem 0 by a large constant factor. AutoDesign published $3 per rollout, DarwinX published no evolution budget, no distillation paper published a comparable per-point cost. The comparison still has not been run, but harness search just got roughly five times cheaper, which changes the expected answer. **The likely hidden failure mode:** importance weighting is unbiased but its variance grows as sampling probabilities shrink, which is what aggressive concentration produces, so a noisy full-set estimate could cause the search to accept a worse harness. The paper does not discuss estimator variance, and only two task types back the 80% figure, which depends on the difficulty distribution having easy and impossible tails to skip.

**[Prime Agent](2026-08-25-prime-agent-self-improving-rlm-harness.md) supplies the reference implementation** and the cleanest one-line statement of why this page exists: it **prevents harness failures from becoming model failures**. Persistent IPython REPL under a Recursive Language Model abstraction, a Continual Harness preserving histories, memories, skills, prompts and subagent specs across trajectories, plus agent-to-agent coordination. ARC-AGI-3 RHAE Best@1 from **30% to 95.5%**. Open source.

**Fourth on the Kurate cs.AI board: [Agent Lightning v1.0: Towards Harnessed Agentic RL](https://arxiv.org/abs/2608.17528)** (He, Zhang, Zhou, Yang, Kang et al., ai_rating 7.0, the highest-rated item on that board). Four papers in one week putting the word harness in the thesis.

**Task-CoEvolve also extends the "schedule beats operator" pattern** this page's neighbours have tracked since 08-12. [LycheeMemory V2 (08-14)](../inference-efficiency/2026-08-14-lycheememory-v2-segment-consolidation.md) was recorded as the third instance after ICBQ block order (08-12) and ReOrder-OPD prompt order (08-13). Task-CoEvolve is the same shape: the harness-rewrite operator is unchanged and the entire gain comes from changing what gets measured when. And its disagreement-weighted sampling is the same statistical idea as [R2-OPD (08-25)](../inference-efficiency/2026-08-25-r2-opd-reasoning-progress-filtering.md), which suppresses distillation reward where a teacher ranking and a progress ranking disagree. Harness evaluation and distillation, one day, no shared authors, one principle.

**The counter-signal, and it should be read seriously.** Kurate cs.AI #14 is [On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification](https://arxiv.org/abs/2608.18066) (Ye, Li, Pruksachatkun, Zhang, Wu), arguing self-improvement gains are sensitive to variance, task arrival order, and underspecified objectives. Set that against Bakouch's 08-16 note that a single run in a fixed setting has a ~50-step spread after 24 hours, and against ARC-AGI-3 being near-saturated by two systems in one week (Prime Agent 95.5%, NVIDIA AVO 100%). The honest reading: **harness capability is real and its measured magnitude is not yet trustworthy.** A near-saturated benchmark cannot discriminate the thing everyone is now optimizing.

**[Meta-Harness](2026-08-25-meta-harness-code-space-optimization.md) closed a loop this page has been open on since it was created: the saved-reading thread got cited by the published literature.** Task-CoEvolve's related work opens with the six-fold same-benchmark gap from harness design alone, which is the Stanford and MIT Meta-Harness result surfaced through saved reading on 08-18. The optimizer design is two refusals of the standard recipe. **Full diagnostic trace access**: instead of a lossy scalar reward plus a short summary, an agentic proposer gets unrestricted filesystem access to raw execution logs and source code across all past iterations, up to 10M trace tokens, inspected with `grep` and `cat`. **Causal failure analysis in code space**: isolate the confounded regression, trace the downstream error back to the early context decision that caused it, rewrite the responsible executable Python function. The attribution argument is the substantive one: a scalar says a rollout was bad, it cannot say that turn 40 failed because turn 6 evicted the wrong file, and recovering that link requires the log to exist and be readable. Results: discovered context policies beat state-of-the-art agentic memory systems by **7.7 points at 4x fewer context tokens**, converging 10x faster, and a single discovered math-retrieval harness added **4.7 points on 200 IMO-level problems across five held-out frontier models** zero-shot. Unaccounted: the search cost. 10M trace tokens per proposal is expensive and "10x faster convergence" counts iterations, which is the wrong unit when the per-iteration bill rose.

**That transfer result crosses this page's own three-paper threshold.** [AI4AI at Test-Time (08-13)](../inference-efficiency/2026-08-13-ai4ai-test-time-harness-transfer.md) took a weaker target from 0.49 to 0.91 across four Theory-of-Mind benchmarks with the target frozen. [AutoDesign (08-14)](2026-08-14-autodesign-meta-harness-optimization.md) added 12.4 points across seven code-agent-model configurations. Meta-Harness adds five held-out frontier models on olympiad problems. Three independent results, twelve days, same structural claim: **a discovered harness is a portable artifact with standalone value, not per-model tuning residue.** That is a stronger statement than "harness choice matters," and it is what makes harness-as-product coherent.

**Industry reported the same cost number in the same week, which is the confirmation that matters most.** OpenAI's [Codex as a platform](https://developers.openai.com/blog/codex-as-a-platform) release (08-19) states outright that the harness, not the chat interface, is the primary reusable component, and reports that harness-level **retained reasoning plus context compaction moved GPT-5.6 Sol's ARC-AGI-3 score from 13.3% to 38.3% while cutting token consumption sixfold**. Meta-Harness reports 4x fewer context tokens at +7.7 points. A research group and a frontier vendor independently landing on 4x-6x token savings from the same architectural layer, in the same week, on partly the same benchmark, is the strongest cost evidence this page holds. Ken Huang's [reading of the open `codex-rs` repository](2026-08-14-ken-huang-harness-engineering-patterns.md) extracts a **token-budget subsystem with proactive compaction hooks** as one of nine supporting components, making token optimization an explicit architectural element rather than a tuning afterthought.

**[Thinkingbox (08-25)](2026-08-25-thinkingbox-stateful-reliability.md) aims the counter-signal at the metric rather than the method, and it is the sharper version of the Fragility critique.** Microsoft's 507 policy-conditioned stateful business workflows, evaluated against backend terminal state with executable checks that reject **extra** effects as well as wrong and missing ones, put the strongest model at **65.36% pass@1 and 25.25% pass^20**. Worse, many failures terminate cleanly having made valid state-changing tool calls, so response-level and tool-call-level signals are not proxies for completion. Set that beside Prime Agent's 95.5% **Best@1** the same day: both results can be true, and the honest joint reading is that **harness engineering has demonstrably raised the ceiling of what an agent can do while leaving open how often it does it.** Nobody has published a pass^k curve for a harness-optimized agent. That is now the single most conspicuous missing measurement on this page, and it is cheap to produce.

**Updated state of knowledge.** The harness is measured on cost (5x-30x swing; $3 to $2,430 per task by class; 4x-6x token reduction from context management, confirmed by research and vendor independently) and now on **the cost of finding one** (80% reducible). It is measured on capability (0.49 to 0.91 at the small tier, +7.7 to +17 at the frontier, 30% to 95.5% on ARC-AGI-3, 81.7% of a human record over 8.7 days) and now **at model scale**, with 35B reaching the frontier band when environment and coordination are scaled instead of parameters. It is optimizable by population search, meta-optimization, and now cheaply; transferable across tasks, verifiers, base models and frameworks; priced through cache-hit economics; governed by a pattern taxonomy; manufacturable for small open models via natural-language RL; and it has an open-source reference implementation. **What is still missing is unchanged and now conspicuous: nobody has put harness work and fine-tuning on one cost axis for equal capability gain, and the benchmark everyone is climbing is saturating.**

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
