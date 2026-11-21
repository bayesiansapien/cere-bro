---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.382734+00:00
arxiv_id: 2611.26603
url: https://huggingface.co/papers/2611.26603
arxiv_url: https://arxiv.org/abs/2611.26603
date: 2026-11-20
---

# Depth Pro 2: Sharp and Temporally Consistent Metric Monocular Depth

We present Depth Pro 2, an approach to estimating dense metric depth for images and video at full resolution. By analyzing prior methods for monocular depth estimation, we find that they commonly trade off temporal consistency and boundary sharpness: multi-frame methods favor consistency, single-frame methods favor sharpness. To overcome this trade-off, we train a single, scalable network that processes both images and video and predicts depth maps at native resolution. Depth Pro 2 produces depth maps that are metrically accurate, sharp, and temporally consistent all at once, outperforming prior work in all of these dimensions. We release a family of models that define a new Pareto frontier in terms of metric accuracy, sharpness, temporal consistency, and runtime. We release code and weights at https://apple-aiml-research.github.io/ml-depth-pro-2/
