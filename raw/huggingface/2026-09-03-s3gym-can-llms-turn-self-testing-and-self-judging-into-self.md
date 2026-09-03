---
source: farmer/huggingface
farmed: 2026-09-03T17:01:45.591071
arxiv_id: 2608.31100
url: https://huggingface.co/papers/2608.31100
arxiv_url: https://arxiv.org/abs/2608.31100
date: 2026-09-03
---

# S3Gym: Can LLMs Turn Self-Testing and Self-Judging into Self-Improvement?

Large language models (LLMs) increasingly interact with external environments and accumulate substantial behavioral experience, yet existing agent benchmarks largely evaluate them as fixed policies. It therefore remains unclear whether an agent can actively test its behavior, judge the resulting experience, and use that experience to improve future decisions. We introduce S\textsuperscript{3Gym}, an interactive benchmark for evaluating LLM self-improvement through three coupled capabilities: Self-Testing, Self-Judging, and Self-Improvement. S^3Gym separates permissive exploration from strict held-out evaluation and instantiates this protocol in seven text-based games with executable environment verifiers. We evaluate three pathways for incorporating interaction experience: direct History ICL, score-conditioned Summary Memory, and parameter Training.
  Our experiments reveal that self-improvement is neither automatic nor uniform. Context-level experience improves performance for several model--game pairs, but the most effective pathway depends strongly on the task structure: summaries are beneficial when experience can be compressed into reusable strategic rules, yet often underperform raw history when success depends on precise, state-contingent information. Parameter training produces substantial gains on some tasks, but also exhibits unstable improvement and severe negative transfer on others. These findings show that recognizing successful actions is insufficient; agents must also transform feedback into executable and transferable policies. S^3Gym provides a unified framework for diagnosing this process and identifying the bottlenecks that prevent agents from translating interaction experience into reliable self-improvement.
