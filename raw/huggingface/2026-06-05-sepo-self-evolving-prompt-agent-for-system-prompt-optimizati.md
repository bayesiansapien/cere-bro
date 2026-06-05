---
source: farmer/huggingface
farmed: 2026-06-05T08:18:05.247595+00:00
arxiv_id: 2606.04465
url: https://huggingface.co/papers/2606.04465
arxiv_url: https://arxiv.org/abs/2606.04465
date: 2026-06-05
upvotes: 1
---

# SePO: Self-Evolving Prompt Agent for System Prompt Optimization

System prompt optimization improves agent behavior without modifying the underlying model, yielding human-readable, model-agnostic instructions. Existing methods build a prompt agent that refines task agents' system prompts, yet leave the prompt agent's own system prompt hand-engineered and fixed. We propose Self-Evolving Prompt Optimization (SePO), which treats the prompt agent's own system prompt as an optimization target alongside task agents' system prompts. SePO adopts a self-referential design. A single prompt agent improves both task agents' system prompts and its own under an open-ended evolutionary search that maintains an archive of candidate prompts as stepping stones. Training proceeds in two stages: pre-training evolves the prompt agent on a multi-task pool, and fine-tuning then applies it to a target task. Across five benchmarks spanning math (AIME'25), abstract reasoning (ARC-AGI-1), graduate-level science (GPQA), code generation (MBPP), and logic puzzles (Sudoku), SePO consistently outperforms Manual-CoT, TextGrad, and MetaSPO, improving the average accuracy by 4.49 points compared to Manual-CoT. The prompt optimization skill from pre-training also generalizes to tasks beyond the pre-training mixture, rather than memorizing per-task prompts.
