---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.34981
url: https://huggingface.co/papers/2609.34981
arxiv_url: https://arxiv.org/abs/2609.34981
date: 2026-09-30
---

# What Makes World Action Models Generalize? An Empirical Study of Test-Time Future Modeling

World action models (WAMs) predict the future alongside actions during training. Due to the heavy computation cost of video denoising, whether the future must still be generated during inference is disputed: Explicit WAMs denoise it into clean frames along with every action chunk, whereas Latent WAMs discard it entirely for acceleration. We find that latent WAMs, despite matching explicit ones on in-distribution tasks, fail to retain the generalization benefits that originally motivated WAMs. To demonstrate this, we evaluate generalization along three axes: environmental perturbation, data efficiency, and task generalization. Controlled comparisons with a matched backbone, training data, and budget reveal consistent degradation across all three axes when the action expert no longer conditions on future representations. Further analysis shows that the gap arises almost entirely from the first denoising step: the benefit comes from preparing the future, not generating it. We therefore propose Simple-WAM, which simplifies future modeling into a single forward pass of fully noised video tokens and adapts the training-time noise schedule to this inference behavior. Across simulation and real-world tasks, Simple-WAM achieves the best of both worlds, leading explicit WAMs in generalization performance with efficiency comparable to Latent WAMs. Project Page: https://zrporz.github.io/Simple-WAM-Web/
