# SimpleTES: Evaluation-Driven Scaling for Scientific Discovery

**Date:** 2026-04-22  
**Source:** [HuggingFace](https://huggingface.co/papers/2604.19341) | [Paper](https://arxiv.org/abs/2604.19341)  
**Raw:** [raw/huggingface/2026-04-22-evaluation-driven-scaling-for-scientific-discovery.md](../../raw/huggingface/2026-04-22-evaluation-driven-scaling-for-scientific-discovery.md)

## TL;DR

SimpleTES is a general framework for scientific discovery that combines parallel exploration, feedback-driven refinement, and local selection. Applied to 21 scientific problems across six domains using GPT-OSS models: 2x speedup on LASSO algorithm, 24.5% reduction in quantum circuit gate overhead, new Erdős minimum overlap constructions surpassing best-known results. The key insight is that *scaling the evaluation loop* (not just generation) is the lever that produces novel discoveries.

## Key Findings

- Consistently outperforms both frontier-model baselines and sophisticated optimization pipelines across 21 scientific problems in 6 domains
- LASSO algorithm 2x speedup; quantum circuit routing 24.5% gate reduction; new Erdős minimum overlap constructions
- Framework: **parallel exploration** (diverse candidate generation) + **feedback-driven refinement** (iterate on promising candidates) + **local selection** (keep best per evaluation)
- Trajectory-level histories from the discovery process naturally supervise feedback-driven learning
- Uses GPT-OSS models — not frontier — implying the evaluation-loop structure matters more than model quality

## Architecture

```
SimpleTES:
  parallel exploration: generate N candidates from diverse starting points
           ↓
  feedback evaluation: run verifier/simulator/scorer on each
           ↓
  local selection: keep top-k per region of the search space
           ↓
  feedback-driven refinement: refine top-k based on evaluation feedback
           ↓
  (iterate until budget exhausted or target met)

Key design: the evaluation function is the bottleneck to optimize around,
not the generation function. Scale calls to the evaluator, not the generator.
```

## Relation to Prior Wiki Knowledge

SimpleTES connects to the **self-evolution agents (04-21)** theme: agents that improve by accumulating their own experience. SimpleTES produces trajectory-level histories that can supervise future runs — the same "accumulated experience as training signal" pattern.

**Connection to ml-intern (04-22 parallel digest)**: ml-intern runs a loop (read paper → generate data → train → evaluate → retrain). SimpleTES runs a similar loop (generate candidate → evaluate → refine → select). Both treat discovery as a search-and-evaluation problem rather than a generation problem. The binding constraint in both is the quality of the evaluation function.

**Connection to RLVR saturation (04-21)**: SimpleTES's "scale the evaluation loop" insight reframes the saturation problem. If you run out of useful training signal, don't keep generating — improve the evaluator. This is EM-style thinking: the E-step (evaluation) is what enables M-step (refinement) to work.

## Related Pages

- [Agent Benchmarks](agent-benchmarks.md)
- [Reward-Free Self-Evolution](2026-04-21-reward-free-self-evolution-agents.md)
