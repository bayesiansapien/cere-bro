# EnvFactory: Scaling Tool-Use Agents via Executable Environments Synthesis and Robust RL

**Source:** HuggingFace Daily Papers 2026-05-20 · [arXiv 2605.18703](https://arxiv.org/abs/2605.18703) · [raw](../../raw/huggingface/2026-05-20-envfactory-scaling-tool-use-agents-via-executable-environmen.md)

## TL;DR

Equipping LLMs with tool-use via Agentic RL is bottlenecked by two problems: lack of scalable robust execution environments, and scarcity of realistic training data that captures implicit human reasoning. Existing approaches use costly real-world APIs, hallucination-prone LLM simulators, or synthetic environments that are single-turn or depend on pre-collected documents. Synthetic trajectories are often over-specified, resembling instruction sequences rather than natural human intents, which reduces their RL training value. EnvFactory autonomously explores and verifies stateful executable tool environments from authentic resources, and synthesizes natural multi-turn trajectories through topology-aware sampling and calibrated refinement to produce grounded queries with implicit intents. Using only 85 verified environments across 7 domains, EnvFactory generates 2,575 SFT and RL trajectories. Despite using 5x fewer environments than prior work, it produces +15% on BFCLv3, +8.6% on MCP-Atlas, and +6% on conversational benchmarks including tau^2-Bench and VitaBench.

## Why it matters

The agentic RL stack has been bottlenecked by environment cost. Real APIs are expensive and brittle. LLM simulators hallucinate. Static synthetic environments don't generalize. EnvFactory's two-step pipeline (autonomous environment verification, then topology-aware trajectory generation) compresses both costs into a single automated framework, and the 5x environment efficiency at +15% BFCLv3 is large enough to indicate the bottleneck has shifted. The implicit-intent observation is the substantive insight: prior synthetic trajectories read like instruction sequences, real human intents are underspecified, and the gap is what makes RL training transfer.

## Mechanism

Two pipelines. (1) **Environment synthesis:** start from authentic resources (docs, schemas, API specs); autonomous exploration generates candidate stateful environments; verification checks the environment is executable and well-formed. (2) **Trajectory generation:** topology-aware sampling traverses the environment graph in human-plausible ways; calibrated refinement removes the instruction-sequence over-specification and leaves implicit intents.

## Open questions and gaps

The "authentic resources" prerequisite is the limiting factor. EnvFactory works from existing docs and schemas; whether it can produce environments for tasks where the resource is sparse or proprietary is open. The 85 environments span 7 domains, which is wide for a paper but narrow versus the universe of real production environments. The implicit-intent calibration is the load-bearing module and the paper presumably gives details that are not in the abstract.

## Industrial implication

Production agentic RL is gated by environment construction. A pipeline that turns docs into verified stateful environments with realistic trajectories is exactly what frontier labs and serious agentic startups need. If EnvFactory's verification is robust across domains beyond the 7 tested, it becomes a default substrate for agentic RL within 90 days.

## Connections

- **OpenComputer (today, 2605.19769)** builds verifier-grounded software worlds for computer-use agents. The two papers attack the same problem (verifiable environments for agent training) from different scales: EnvFactory builds many small environments from docs, OpenComputer builds a deep desktop-application substrate with hard-coded verifiers.
- **AgentKernelArena (2026-05-19)** measures the seen-versus-unseen-shape generalization gap in GPU-kernel agents. EnvFactory's topology-aware sampling is one possible answer to whether broader environment coverage closes that gap.
