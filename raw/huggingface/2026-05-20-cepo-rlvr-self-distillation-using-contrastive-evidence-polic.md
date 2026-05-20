---
source: farmer/huggingface
farmed: 2026-05-20T09:54:57.890882+00:00
arxiv_id: 2605.19436
url: https://huggingface.co/papers/2605.19436
arxiv_url: https://arxiv.org/abs/2605.19436
date: 2026-05-20
---

# CEPO: RLVR Self-Distillation using Contrastive Evidence Policy Optimization

When a model produces a correct solution under reinforcement learning with verifiable rewards (RLVR), every token receives the same reward signal regardless of whether it was a decisive reasoning step or a grammatical filler. A natural fix is to condition the model on the correct answer as a teacher, identifying tokens it would have generated differently had it known the answer. Prior work shows this either corrupts training by leaking the answer into the gradient, or produces a weak signal that cannot distinguish decisive steps from filler, since both look equally surprising relative to the model&#39;s baseline. We propose Contrastive Evidence Policy Optimization (CEPO), which asks a sharper question at every token: not just &#34;does the correct answer favor this token?&#34; but &#34;does the correct answer favor it while the wrong answer disfavors it?&#34; A token satisfying both is a genuine reasoning step; one satisfying neither is filler. The wrong-answer teacher is constructed from rejected rollouts already in the training batch, incurring no additional sampling cost. We prove CEPO inherits all structural safety guarantees of the prior state of the art while strictly sharpening credit at decisive tokens, with the improvement vanishing exactly at filler positions. Empirically, CEPO achieves 43.43% and 60.56% average accuracy across five multimodal mathematical reasoning benchmarks at 2B and 4B scale, respectively, versus 41.17% and 57.43% for GRPO under identical training budgets. Distribution-matching self-distillation methods (OPSD, SDPO) fall below the untrained baseline, empirically confirming the information leakage our theory predicts. Our code is available at this https URL .
