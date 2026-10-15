---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.507460+00:00
arxiv_id: 2610.14228
url: https://huggingface.co/papers/2610.14228
arxiv_url: https://arxiv.org/abs/2610.14228
date: 2026-10-14
---

# Latent World Action Model for GUI Agents

Pixel-space world models have recently emerged as a promising approach for GUI agents, predicting future screens prior to execution and subsequently re-perceiving them for action selection. However, this two-stage paradigm faces two key challenges in GUI environments: (L1) the high computational cost of pixel reconstruction and (L2) the need to reconstruct large and diverse appearance-level details beyond what is required for action selection. In practice, this screen-generation objective can induce an identity shortcut problem, where future-state prediction largely preserves the current state rather than capturing action-induced changes. In this work, we reformulate GUI world modeling by shifting the prediction target from full-screen reconstruction to action-induced future information in latent space. Concretely, we leverage a large multimodal model as the latent world model, whose shared representations support two dedicated heads for both action selection and predictive transition modeling. The action head directly translates these latent representations into action selection, while the transition head captures action-conditioned future information. To mitigate the identity shortcut, we further introduce an action-aware contrastive objective that encourages the transition representations to capture discriminative action-induced changes. Extensive experiments across offline and online GUI settings show that our method achieves up to 31.9% and 40.6% relative gains in success rate over pixel-space world models, respectively, while substantially reducing inference latency by up to 98.9%. Our code is available at https://github.com/sjyu001/latent2world.
