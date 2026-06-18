# CEO-Bench: Can Agents Play the Long Game?

**TL;DR.** Most agent benchmarks test isolated, short-horizon skills (one SWE-bench bug, one customer-service turn). CEO-Bench tests the opposite: it simulates running a startup for 500 simulated days, and the agent manages pricing, marketing, budgeting, and the rest through a programmable Python interface, facing the same noisy, interconnected, changing environment a human CEO does. Success requires four capabilities together that current agents are rarely tested on jointly: navigating long horizons under uncertainty, acquiring information in noisy environments, adapting to a changing world, and orchestrating many moving parts toward one goal. The headline result is bleak: of state-of-the-art models, only Claude Opus 4.8 and GPT-5.5 finish above the $1M starting balance, and neither consistently turns a profit. The strongest agents write code that simulates customer cohorts to forecast cash and mines negotiation history for hidden preferences.

**Source:** HuggingFace · [arxiv 2606.18543](https://arxiv.org/abs/2606.18543) · arxiv-dated 2026-06-18

## What it is

A long-horizon agent benchmark structured as a 500-day business simulation. The agent operates a fictional company through a Python API, reading noisy interconnected business databases and translating signals into pricing, marketing, and budget decisions across many simulated days. It is explicitly designed to evaluate four capabilities as a bundle rather than in isolation: long-horizon planning under uncertainty, information acquisition in noise, adaptation to a non-stationary world, and multi-part orchestration toward a coherent objective.

The interesting behavioral finding is *how* the best agents succeed: they do not just answer queries, they write sophisticated code inside the environment, simulating customer cohorts to forecast future cash flow and data-mining negotiation transcripts to surface hidden customer preferences. Capability here looks like programming a model of the world, not prompting through it.

## Key findings

- Only **Claude Opus 4.8 and GPT-5.5** finish above the $1M starting balance; every other tested model ends underwater.
- Neither of the two survivors consistently turns a profit, so even the frontier is at the threshold, not above it.
- The strongest behavior is emergent tool-building: agents that simulate cohorts and mine history outperform agents that react turn-by-turn.
- The benchmark isolates sustained adaptive progress over time as a distinct axis, not reducible to single-task accuracy.

## Relation to prior wiki

- CEO-Bench extends the [agent-benchmarks](agent-benchmarks.md) page's hardest-frontier line, where realistic multi-step environments crater frontier agents (AdaPlanBench 06-06, best model 67.75% under accumulating hidden constraints; the 0–55% completion ceiling across the 05-07 cluster). It pushes further on the *time* axis: 500 days is far longer than the trajectories AgentLens (05-14) or SABER (06-06) graded, and the failure is economic rather than a pass/fail flag.
- It is the business-operations counterpart to the long-horizon planning gap, and a clean datapoint for the [CEO-as-orchestrator](multi-agent-systems.md) framing: the winning agents *orchestrate many decisions*, which is the single-agent version of the routing/orchestration thread (Conductor, SciOrch) applied to a business rather than a model pool.
- The "only Opus 4.8 and GPT-5.5 survive" result is a fresh capability-frontier marker that pairs with CEO-Bench's same-day company, and a counterweight to the open-weight catch-up narrative (GLM-5.2, DeepSeek V4): on sustained adaptive business operation, the gap to the two closed leaders is still wide.

## Research angle

The benchmark's most useful property is that it grades a *cumulative economic outcome* over 500 steps, which makes it a natural testbed for trajectory-level routing and for OPD-style credit assignment over very long horizons (the privileged-hindsight machinery of [PBSD](../inference-efficiency/2026-06-09-trd-trajectory-refined-distillation.md)/OPD-Evolver was built for exactly this sparse-final-reward-to-turn-credit problem). The open question: does a smaller model that *writes a good world-simulation tool* beat a larger model that reasons natively, the same harness-beats-scale pattern seen elsewhere this week? If so, CEO-Bench becomes an argument that long-game competence is a scaffolding problem, not a parameter problem.

## Gaps

A single simulated business domain, so generalization to other long-horizon settings is unmeasured. The simulator's fidelity is the load-bearing assumption, an agent could win by exploiting simulator artifacts rather than sound strategy, the long-horizon analogue of AgentLens "lucky passes," and the paper does not report an audit of that. Two-model survival is a thin signal; the gap between "above starting balance" and "consistently profitable" is where the real difficulty sits and is not yet decomposed.

Raw: `raw/huggingface/2026-06-18-ceo-bench-can-agents-play-the-long-game.md`
