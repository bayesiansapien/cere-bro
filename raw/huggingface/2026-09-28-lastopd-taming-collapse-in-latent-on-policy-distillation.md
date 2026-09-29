---
source: farmer/huggingface
farmed: 2026-09-29T05:05:53.595351+00:00
arxiv_id: 2609.28845
url: https://huggingface.co/papers/2609.28845
arxiv_url: https://arxiv.org/abs/2609.28845
date: 2026-09-28
---

# LastOPD: Taming Collapse in Latent On-Policy Distillation

On-policy distillation (OPD) corrects a student on the responses it writes, but its signal is the teacher's next-token distribution: it tells the student what the teacher says but misses how it thinks. Latent supervision promises the missing part by aligning the student's latent states to the teacher's. Recent methods such as OPRD bring this signal into on-policy distillation. However, we observe two failures of this recipe when distilling Qwen3-4B and Qwen3-8B into Qwen3-1.7B-Base. Early gain, late collapse: latent supervision alone lifts MATH-500 accuracy from 25 to 46 in 10 steps, but subsequent training degrades performance down to 11 with no recovery. Better alignment, worse behavior: although the alignment metric steadily improves throughout this collapse, the most aligned model turns out to be the worst performing. Further analysis suggests a mismatch in how the latent signal is applied: layers paired by depth play different roles in the two models, so continued alignment may pull the student toward teacher states it cannot understand. To address this, we propose LastOPD, which applies the latent signal only at the last-layer state, the common interface both LM heads read, and only during a 10-step crossfade into token-level OPD. This keeps the useful part of the latent signal and hands the student to token-level supervision before the collapse sets in. Extensive experiments show that LastOPD improves MATH-500 over token-only OPD by 5.55 and 4.02 points with the 4B and 8B teachers, leads on most held-out datasets, and reaches the final score of token-only OPD in about half the steps. Code is available at https://github.com/Muyiiiii/LastOPD.
