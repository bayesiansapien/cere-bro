# ClawGym: A Scalable Framework for Building Effective Claw Agents

**Date:** 2026-04-30
**Source:** [HuggingFace](https://huggingface.co/papers/2604.26904) | [Paper](https://arxiv.org/abs/2604.26904)
**Raw:** [raw/huggingface/2026-04-30-clawgym-scalable-framework-claw-agents.md](../../raw/huggingface/2026-04-30-clawgym-scalable-framework-claw-agents.md)

## TL;DR

ClawGym (Renmin U / IQuest / Beihang) is a full-lifecycle framework for Claw-style personal agents — agents that operate over local files, tools, and persistent workspace state across multi-step workflows. It bundles a 13.5K-task synthetic dataset (ClawGym-SynData) generated via dual-route synthesis, a 200-instance evaluation benchmark (ClawGym-Bench) calibrated by automated filtering + human-LLM review, and a sandbox-parallel RL pipeline. Qwen3-8B fine-tuned on the data improves 38.90% on PinchBench and 43.46% on ClawGym-Bench; Qwen3-30B-A3B improves 54.68% / 25.96%.

## Key Contributions

- **Dual-route data synthesis**: persona-driven top-down (start from a user persona, generate plausible workflows) + skill-grounded bottom-up (start from concrete skills, compose workflows). Hybrid verification combines code-based checks (deterministic) with rubric-based judging (open-ended steps).
- **Per-task sandboxes for parallel RL rollouts**: each task gets its own isolated workspace; rollouts run in parallel without state contamination. This is the operational answer to the question "how do you do RL on agents that mutate persistent state?"
- **Calibrated benchmark**: 200 instances filtered by rollout difficulty + human review.
- **Black-box trajectory SFT followed by lightweight RL**: a two-stage recipe that scales without requiring access to teacher logits.

## Why It Matters

The Claw-agent space (personal agents that own a workspace) has been chronically under-served by training infrastructure — the data is hard to synthesize because workflows are personal and the verification is hard to automate because outcomes are stateful. ClawGym is the first end-to-end open framework for this class of agent. The Qwen3-8B +43.46% on ClawGym-Bench result is large enough to suggest that the bottleneck for personal agents has been data, not model capability.

## Connection to Prior Wiki Knowledge

**Sibling to Persistent Agent Infrastructure (2026-04-23).** Persistent agent infrastructure asked how to make agent state durable across long sessions. ClawGym is the *training-data* counterpart: how to generate workflows over persistent state at scale. Together they form the personal-agent stack — execution substrate (Persistent Agent Infrastructure) + training data infra (ClawGym).

**Resolves an open question from From Skills to Talent (2026-04-28).** That paper proposed organizing agents as a Talent Market with skill matching. ClawGym's *skill-grounded bottom-up* synthesis route is one concrete way to populate that market: skills become the atomic unit from which workflows are composed. The 13.5K-task dataset is, in effect, a snapshot of what the talent market would look like for a single agent type.

**Confirms a now-clear pattern across April papers.** Reward-Free Self-Evolution Agents (04-21), AgentSpex (04-22), ML-Intern (04-22), and now ClawGym all share a structural design: synthetic-data engine + verification harness + RL on per-task sandboxes. Four papers in three weeks converging on the same pipeline shape — the field has converged on the recipe for training agentic models.

## Research Angle

The dual-route synthesis split (persona-driven vs skill-grounded) is the most interesting design choice. Persona-driven synthesis covers realistic distributions but is bounded by persona diversity; skill-grounded synthesis covers compositional space but may produce unrealistic workflows. The optimal mixture is task-dependent and currently hand-tuned. A follow-up that *learns* the persona/skill ratio against a downstream benchmark would generalize the framework.

A second thread: the gap between Qwen3-8B (+43.46%) and Qwen3-30B-A3B (+25.96%) on ClawGym-Bench is the wrong way around if the task is just "harder = more capacity needed." The smaller model gains *more*. This is consistent with the TEMPO observation (04-22) that test-time training and RL fine-tuning reward smaller models proportionally more — they have more to learn from the data, while larger models already encode the relevant priors. Worth tracking whether this is a consistent regularity across agent training corpora.

## Related Pages

- [Persistent Agent Infrastructure (04-23)](2026-04-23-persistent-agent-infrastructure.md)
- [Reward-Free Self-Evolution Agents (04-21)](2026-04-21-reward-free-self-evolution-agents.md)
- [ML-Intern Agentic Posttraining (04-22)](2026-04-22-ml-intern-agentic-posttraining.md)
- [AgentSpex (04-22)](2026-04-22-agentspex-workflow-language.md)
