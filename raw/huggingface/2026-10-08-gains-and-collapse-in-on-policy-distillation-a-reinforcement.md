---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.304557+05:30
arxiv_id: 2610.03185
url: https://huggingface.co/papers/2610.03185
arxiv_url: https://arxiv.org/abs/2610.03185
date: 2026-10-08
---

# Gains and Collapse in On-Policy Distillation:A Reinforcement Learning Perspective

On-policy distillation (OPD) has become an important approach to language model post-training. However, despite its performance gains, OPD can also collapse into excessively long and repetitive generation, and the mechanism underlying these divergent outcomes remains poorly understood. We explain these outcomes through a reinforcement learning perspective: the teacher implicitly rewards student behaviors, even those it rarely exhibits itself. From this perspective, our experiments show that OPD improves performance without expanding the student's capabilities. When the implicit reward model is reliable, OPD makes correct responses easier to sample. In contrast, when the preference misaligns with quality, reward hacking happens: the implicit reward model amplifies overlong, repetitive student rollouts, even though it rarely generates such text itself. Guided by this diagnosis, we find that masking unhealthy responses during training and using SFT initialization can each effectively mitigate the collapse. Together, these findings show that OPD amplifies student behaviors favored by the teacher's implicit feedback, shifting the focus from how well the teacher generates to how reliably it evaluates student rollouts. Our code is available at https://github.com/HancCui/opd_hacking.
