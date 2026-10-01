---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.32722
url: https://huggingface.co/papers/2609.32722
arxiv_url: https://arxiv.org/abs/2609.32722
date: 2026-09-30
---

# Scaling Properties of Same-Family On-Policy Distillation

*Reinforcement learning (RL)* can induce substantial reasoning capabilities in large language models (LLMs), but how much of this capability transfers across model scales, and how quickly, remains unclear. We study the scaling properties of *on-policy distillation (OPD)* across *weak-to-strong*, *same-base*, and *strong-to-weak* teacher--student setups. We find that early OPD training dynamics uniformly exhibit a regular *useful-transfer* regime, in which held-out accuracy (the *gold score*, G) rises approximately linearly in d=mathrm{KL(π_θVert π_{ref})}, the square root of token-level reverse KL divergence from the student initialization. In every observed weak-to-strong pair, the student's peak gold score exceeds its teacher's own, so a compact RL expert can transfer capability to a much larger student via OPD. To estimate OPD outcomes, we fit *power laws* for how G_{peak} and the slope of the useful-transfer regime scale with student and teacher parameter counts and with teacher gold score. These laws show that peak gold score improves with teacher scale only up to roughly the student's scale, and that at a matched gold score smaller teachers transfer better, so a teacher's score alone does not define its supervision value. We also study the scaling effects of two OPD variants, bootstrapping weak-to-strong OPD, and the degree of on-policy supervision.
