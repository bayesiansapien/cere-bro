---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.933264+00:00
arxiv_id: 2609.34848
url: https://huggingface.co/papers/2609.34848
arxiv_url: https://arxiv.org/abs/2609.34848
date: 2026-09-29
---

# Can We Trust the Teacher? Decoupled Credit Direction-Magnitude for Self-Distillation

RLVR provides reliable trajectory-level credit, while OPSD offers dense supervision for token-level credit. This exposes a fundamental coupling when updating step-level credit direction and magnitude with teacher supervision, preventing steps from receiving reliable credit directions and contribution magnitudes, while making both vulnerable to teacher judgment errors and preference variance, as supported by our theoretical analysis. To separate credit direction from its contribution magnitude, we introduce Decoupled Credit Self-Distillation (DCSD), which theoretically decouples credit direction and magnitude into two reliable signals and uses them to calibrate privileged teacher supervision. Specifically, we design belief-margin probing to determine credit direction and marginal information gain to quantify credit magnitude, enabling step-to-token credit assignment for policy optimization. Across 11 benchmarks, DCSD achieves the best overall scores against GRPO, OPSD, RLSD, and RLCSD. Compared with base models, DCSD improves the overall score by 8.45 points on mathematical reasoning and 7.01 points on multimodal reasoning, while correcting the credit direction for 6\% of tokens and yielding a 1.5times reduction in token credit magnitude.
