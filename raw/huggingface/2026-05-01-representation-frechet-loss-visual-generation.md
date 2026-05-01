---
source: farmer/huggingface
farmed: 2026-05-01T00:00:00Z
arxiv_id: "2604.28190"
url: https://huggingface.co/papers/2604.28190
arxiv_url: https://arxiv.org/abs/2604.28190
date: 2026-05-01
---

# Representation Fréchet Loss for Visual Generation

We show that Fréchet Distance (FD), long considered impractical as a training objective, can in fact be effectively optimized in the representation space. Our idea is simple: decouple the population size for FD estimation (e.g., 50k) from the batch size for gradient computation (e.g., 1024). We term this approach FD-loss. Optimizing FD-loss reveals several surprising findings. First, post-training a base generator with FD-loss in different representation spaces consistently improves visual quality. Under the Inception feature space, a one-step generator achieves 0.72 FID on ImageNet 256x256. Second, the same FD-loss repurposes multi-step generators into strong one-step generators without teacher distillation, adversarial training or per-sample targets. Third, FID can misrank visual quality: modern representations can yield better samples despite worse Inception FID. This motivates FDrk, a multi-representation metric. We hope this work will encourage further exploration of distributional distances in diverse representation spaces as both training objectives and evaluation metrics for generative models.
