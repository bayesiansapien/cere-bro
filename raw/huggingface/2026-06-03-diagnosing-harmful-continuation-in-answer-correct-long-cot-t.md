---
source: farmer/huggingface
farmed: 2026-06-03T06:14:02Z
arxiv_id: 2605.29288
url: https://huggingface.co/papers/2605.29288
arxiv_url: https://arxiv.org/abs/2605.29288
date: 2026-06-03
---

# Diagnosing Harmful Continuation in Answer-Correct Long-CoT Training Traces

Long chain-of-thought (CoT) traces are widely used as supervision for reasoning-oriented LLM SFT, yet answer-correct traces can still lead to markedly different fine-tuning outcomes. We study post-conclusion continuation in answer-correct long-CoT data: a continuation where the answer appears sufficiently supported, but the trace continues with additional reasoning that remains in the supervised target. To test its training effect, we use a delete-only editor to construct answer-preserving suffix removal and compare CoT-based SFT on the original and processed traces. We observe improved SFT outcomes after removing the editor-identified post-conclusion continuation, suggesting that this continuation is harmful to training in our setting. We therefore refer to this empirically supported phenomenon as harmful continuation. Beyond this intervention, we further characterize the removed post-conclusion continuation through uncertainty and hidden-state progress. We observe persistent local uncertainty together with weakened terminal-directional progress, forming an uncertainty--geometry mismatch. Finally, we instantiate Harmful Continuation Cut (HCC), a lightweight boundary proxy that approximates the editor-identified post-conclusion continuation boundary.
