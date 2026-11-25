---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.927517+00:00
arxiv_id: 2611.31048
url: https://huggingface.co/papers/2611.31048
arxiv_url: https://arxiv.org/abs/2611.31048
date: 2026-11-24
---

# Distill the Correction, Not the Rewrite: Hindsight Twins for Self-Improving Text-to-Image Models

Text-to-image models can learn from their own mistakes by distilling a self-teacher conditioned on a vision-language critic's revised prompt. However, such self-teachers barely improve alignment, and both they and their hindsight-contrast variants absorb the critic's unintended additions to the scene, such as lighting or scenery. We attribute this to two factors: (1) the prompt already specifies the desired fix, so a useful revision must go beyond the failed span, often rewriting the entire scene and adding details that overshadow the fix; (2) although the critic localizes the error to a single span, self-teachers condition on the rewrite, entangling the intended fix with unintended additions. Motivated by these insights, we propose Hindsight Twins (HinT), which fills the critic's revision template once with the intended fix and once with the observed error and distills only their velocity difference, anchored at the user's prompt. Because text encoders spread the edit of a single slot to all other tokens, HinT further aligns the twins' token states outside the slot. Across Qwen-Image-2512, SD3.5-M, and FLUX.2-klein, HinT keeps the rate of critic-induced bias at the base-model level while matching or exceeding the alignment gains of prior self-distillation, and it keeps improving over twelve rounds of self-training where contrastive baselines decay.
