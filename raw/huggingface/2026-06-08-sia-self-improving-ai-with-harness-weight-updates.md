---
source: farmer/huggingface
farmed: 2026-06-08T09:23:13Z
arxiv_id: 2605.27276
url: https://huggingface.co/papers/2605.27276
arxiv_url: https://arxiv.org/abs/2605.27276
date: 2026-06-08
---

# SIA: Self Improving AI with Harness & Weight Updates

Humans are the bottleneck in building and improving AI. Both the models and the agents that wrap them are written, tuned, and corrected by people. The long-horizon goal of an AI that can figure out how to improve itself remains open. Two largely disjoint research lines attack this bottleneck. The harness-update school has a meta-agent rewrite the scaffold of a task-specific agent (its tools, prompts, retry logic, and search procedure) while the model weights are held fixed. The test-time training school uses hand-written RL pipelines to update the model's own weights on task feedback while the harness is held fixed. These two silos operate in isolation. We propose SIA, a self-improving loop in which a language-model agent (the Feedback-Agent) updates both the harness and the weights of a task-specific agent. We evaluate across three contrasting domains: Chinese legal charge classification, low-level GPU kernel optimisation, and single-cell RNA denoising. Combining both levers outperforms scaffold iteration alone on all three benchmarks. The gains are 56.6% on LawBench, 91.9% runtime reduction on GPU kernels, and 502% on denoising over the initial baseline. Harness updates make the model agentic, shaping how it searches and acts, while weight updates build the domain intuition that no prompt or scaffold can instil.
