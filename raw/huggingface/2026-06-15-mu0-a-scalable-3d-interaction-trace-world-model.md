---
source: farmer/huggingface
farmed: 2026-06-15T06:21:28Z
arxiv_id: 2606.13769
url: https://huggingface.co/papers/2606.13769
arxiv_url: https://arxiv.org/abs/2606.13769
date: 2026-06-15
---

# mu_0: A Scalable 3D Interaction-Trace World Model

World models that capture how actions induce physical change enable scalable robot learning without reliance on embodiment-specific action labels. Pixel-space video models provide broad visual priors but expend model capacity on dense appearance reconstruction, while direct action models require embodiment-specific labels that hinder scalability. We present mu_0, a scalable world model based on 3D traces. Rather than predicting dense pixels or directly modeling actions, mu_0 forecasts smooth 3D trajectories for salient interaction points such as objects, tools, hands, and contact regions, yielding a compact, embodiment-agnostic motion interface. To enable training from diverse video sources, our TraceExtract system automatically extracts 3D supervision by selecting keypoints, constructing globally aligned traces, and associating motion segments with hierarchical language captions. This TraceExtract supervision pretrains mu_0 by combining a pretrained vision-language backbone with a modular trace expert, which represents each query via B-spline control points and predicts future traces. Experiments show that mu_0 outperforms baselines in both 2D and 3D trace prediction, including trace prediction models and tokenized VLM methods. Because mu_0 is frozen and reusable, it can be paired with action experts for downstream robot embodiments. Despite action-free pretraining, the resulting trace-conditioned policies achieve performance competitive with VLA models pretrained with action supervision, such as pi_0. These results establish 3D traces as a scalable and transferable representation for cross-embodiment manipulation.
