---
source: farmer/huggingface
farmed: 2026-09-22T11:38:12.626404+05:30
arxiv_id: 2609.10706
url: https://huggingface.co/papers/2609.10706
arxiv_url: https://arxiv.org/abs/2609.10706
date: 2026-09-22
---

# HuRo: Robotizing Human Videos for Scalable VLA Pretraining

Human video datasets offer an abundant and diverse source of interaction data that can complement expensive real-robot data. To bridge the human-to-robot embodiment gap, existing approaches either robotize videos in task-matched settings or address observation and action alignment separately at scale. In this work, we systematically examine whether robotized human videos can serve as an effective and scalable source of supervision for VLA pretraining. To this end, we develop a robotization pipeline that converts heterogeneous human videos into robot-aligned observations and action trajectories while inferring missing intermediate signals across annotation levels. Using this pipeline, we construct the HuRo dataset, comprising about 630K robotized episodes and 142M processed frames from five human-video sources. Across four real-world manipulation tasks, increasing the amount of robotized pretraining data improves overall completion from 51.5% to 80.3% and OOD completion under spatial and visual shifts from 34.9% to 72.2%. Ablations further show that visual robotization improves OOD robustness and that end-to-end pretraining with retargeted actions outperforms visual-only transfer. Project website: https://3587jjh.github.io/HuRo.
