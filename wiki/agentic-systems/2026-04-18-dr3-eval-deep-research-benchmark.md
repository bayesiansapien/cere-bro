# DR3-Eval: Realistic Benchmark for Deep Research Agents

**Date:** 2026-04-18  
**Tier:** 2 — Agents / Benchmarks  
**arXiv:** [2604.14683](https://arxiv.org/abs/2604.14683)  
**Raw:** [source](../../raw/huggingface/2026-04-18-dr3-eval-towards-realistic-and-reproducible-deep-research-ev.md)

## TL;DR

Deep Research Agents (those that plan, retrieve iteratively, and synthesize multi-source reports) have been hard to benchmark reliably: live web access gives realism but isn't reproducible; sandbox approaches lose multimodal complexity. DR3-Eval threads the needle with static, curated per-task research sandboxes built from real user files, with reverse-constructed questions (derived from verified evidential documents) so every task has a well-defined answer.

## Design Choices

- **Reverse construction:** Instead of asking open-ended questions with unknown answerability, DR3-Eval starts from evidential documents, then derives the question. Every task is answerable by exactly one well-defined evidence path.
- **Static sandbox corpus:** Each task has its own mini-corpus with evidential sources, confounding documents, and ambient noise. This lets researchers systematically test retrieval strategy and noise robustness — not possible with live web access.
- **Multi-dimensional evaluation:** Information Recall, Factual Accuracy, Citation Coverage, Instruction Following, and Depth Quality — capturing both retrieval and synthesis quality.
- **DR3-Agent:** A companion multi-agent system adapted to the closed-world benchmark setting.

## Why It Matters

Current deep research benchmarks either test live web search (irreproducible, changes monthly) or toy corpora (clean text, no multimodal noise). DR3-Eval is the first benchmark that is simultaneously realistic (sourced from actual user tasks), reproducible (static sandboxes), and multimodal (includes images and mixed document types). State-of-the-art LLMs still struggle on it.

## Related Pages

- [Agent Benchmarks](agent-benchmarks.md)
- [Corpus2Skill: Knowledge Navigation](2026-04-18-corpus2skill-knowledge-navigation.md)
- [VAKRA: Agent Reasoning Failure Modes](2026-04-16-vakra-agent-reasoning-failure-modes.md)
