# A Survey on LLM-Based Conversational User Simulation

**Date:** 2026-04-30
**Source:** [HuggingFace](https://huggingface.co/papers/2604.24977) | [Paper](https://arxiv.org/abs/2604.24977)
**Raw:** [raw/huggingface/2026-04-30-survey-llm-based-conversational-user-simulation.md](../../raw/huggingface/2026-04-30-survey-llm-based-conversational-user-simulation.md)
**Authors:** Adobe Research and collaborators (multi-institution)

## TL;DR

Survey of LLM-based conversational user simulation. Proposes a taxonomy along two axes: user granularity (individual vs group) and simulation objective (task-oriented vs open-domain vs evaluation-oriented). Catalogs core techniques and evaluation methodologies, and identifies gaps in high-fidelity synthetic user generation.

## Why It Matters

For agent training and evaluation, synthetic users are a load-bearing dependency: ClawGym's persona-driven data synthesis (04-30) and Reward-Free Self-Evolution Agents (04-21) both implicitly assume the synthetic-user pipeline works. The survey is a useful map of what is and isn't reliable in that pipeline.

The taxonomy's most useful split is **evaluation-oriented** simulation (synthetic users built specifically to stress-test deployed agents) vs **training-oriented** simulation (users built to generate trajectories). These have very different fidelity requirements, and conflating them has been a source of overclaiming in agent papers.

## Connection to Prior Wiki Knowledge

**Useful framing for ClawGym (04-30) and AgentSpex (04-22).** Both rely on persona-driven synthetic users. The survey's user-granularity axis flags a gap: most agent training data sits at individual-user granularity, but real deployment patterns (especially in enterprise) operate at group-user granularity (team workflows, role hierarchies). Worth flagging in the agents-tool-use concept page.

## Related Pages

- [ClawGym (04-30)](../agents-tool-use/2026-04-30-clawgym-agent-framework.md)
- [AgentSpex (04-22)](../agents-tool-use/2026-04-22-agentspex-workflow-language.md)
