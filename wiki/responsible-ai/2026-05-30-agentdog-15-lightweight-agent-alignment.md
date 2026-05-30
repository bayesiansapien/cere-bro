# AgentDoG 1.5: Lightweight Agent Safety Alignment Framework

**Source:** HuggingFace Daily Papers (2026-05-30) · arxiv 2605.29801
**Raw:** [raw/huggingface/2026-05-30-agentdog-15-a-lightweight-and-scalable-alignment-framework-f.md](../../raw/huggingface/2026-05-30-agentdog-15-a-lightweight-and-scalable-alignment-framework-f.md)

## TL;DR

AgentDoG 1.5 is a lightweight, scalable safety alignment framework for open-world agent execution (Codex, OpenClaw, similar harnesses). The authors update the agent safety taxonomy to cover emergent attack surfaces, build a taxonomy-guided data engine with influence-function purification, then train small AgentDoG 1.5 variants (0.8B, 2B, 4B, 8B) on roughly 1K examples and report comparable performance to leading closed-source models (e.g., GPT-5.4). An efficient SFT + RL training environment cuts Docker-level deployment overhead by **two orders of magnitude**, and AgentDoG 1.5 is also deployed as a training-free online guardrail. All models and datasets are released.

## Why this matters

The agent safety thread on the wiki has been growing through three angles:

1. **Supply-chain attacks on the artifact** — skill.md (05-23) and the LoRA adapter backdoor paper (today, 05-30) show that the artifacts the agent loads (skills, adapters) can be weaponized at the supply layer.
2. **Trajectory-level vulnerabilities** — Trajel (05-27) and Cotrace (05-23) showed that hallucinations and attribution failures occur at the trajectory level, not just at single completions.
3. **Alignment-loop poisoning** — Alignment Tampering (05-29) showed that RLHF can amplify model bias because the LLM writes its own preference data.

AgentDoG 1.5 attacks a fourth layer: the *runtime guardrail*. Instead of trying to harden the agent itself, it adds a small classifier next to the agent that can be invoked online during execution, with the cost low enough that it can sit in front of every agent action.

## Key claims

- Variants at 0.8B, 2B, 4B, 8B parameters, trained on roughly **1K samples** with influence-function-purified data.
- Comparable to leading closed-source safety models on agentic-scenario benchmarks (GPT-5.4 cited as the comparison point).
- **~100x reduction** in deployment overhead at the Docker-environment level for the SFT/RL training stack.
- Deployable as a training-free online guardrail for real-time safety moderation.
- Open-released models and datasets.

## Gaps and limits

- Comparable-to-GPT-5.4 is an ambiguous claim without per-task numbers in the abstract; relies on reproduction.
- 1K-sample training is striking; whether the data engine's purification can scale to harder adversarial settings (e.g., the multi-turn attacks Cisco's Q1 report says no frontier model survives) is unproven.
- Online-guardrail latency on production agent workloads not characterized.

## Research angle

The Cisco Q1 2026 report (surfaced in today's AI Breakfast Gmail item) found that no closed frontier model survives multi-turn adversarial attacks. AgentDoG 1.5's framing is that you don't need to harden the model — you wrap it. That is the same architectural bet that Anthropic's Dynamic Workflows (05-28) make at a different layer: instead of one big model that does everything, ship a harness that runs adversarial verification on smaller pieces. If the bet pays off, the locus of safety work moves from RLHF (which Alignment Tampering, 05-29, just showed is structurally compromised by self-poisoning) to lightweight runtime guardrails. The open question is whether guardrails are themselves vulnerable to the LoRA-adapter-backdoor class of supply attack.

## Related concept pages

- [Responsible AI](responsible-ai.md)
