---
source: farmer/huggingface
farmed: 2026-08-03T12:36:11.005337+05:30
arxiv_id: 2607.29679
url: https://huggingface.co/papers/2607.29679
arxiv_url: https://arxiv.org/abs/2607.29679
date: 2026-08-03
---

# Scaling Properties of Text Conditioning in Visual Generation

We study empirical scaling properties for text conditioning in visual generation. Such properties have rarely been measured because diffusion loss does not scale with the number of tokens in natural-language prompts. Surprisingly, we find that the converged diffusion loss scales with the amount of structured language in the prompt. To quantify structured language, we adapt two complementary measures: a white-box likelihood metric (GPG) and a black-box attribute metric (ED). Across controlled training runs, the converged diffusion loss decreases approximately linearly with GPG and follows a power law with ED. Guided by these scaling properties, we improve diffusability by constructing structured prompts with semantic and geometric annotations derived from images, and improve promptability by training a prompter through supervised fine-tuning, cold-start, and verifier-gated on-policy distillation. The resulting system outperforms all evaluated open-weight models on nearly every compositional, reasoning, and world-knowledge benchmark, while matching or surpassing the strongest closed-weight models on most evaluations.
