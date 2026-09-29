---
source: farmer/huggingface
farmed: 2026-09-29T05:05:53.595783+00:00
arxiv_id: 2609.24385
url: https://huggingface.co/papers/2609.24385
arxiv_url: https://arxiv.org/abs/2609.24385
date: 2026-09-28
---

# Tactile-JEPA: Topology-Aware Self-Supervised Representation Learning for Distributed Tactile Sensors

Tactile sensing is an essential modality for robots performing contact-rich, dexterous manipulation, particularly under visual occlusion. While pre-trained image encoders are standard in robot learning pipelines, tactile encoders are still commonly trained from scratch from raw, noisy signals, which might limit their expressivity. Existing self-supervised learning (SSL) approaches focus predominantly on vision-based tactile sensors, leaving distributed electronic skins largely unaddressed. These sensors, however, have a distinctive property: their sensing elements are sparse and irregularly arranged over the surface they cover, which makes direct reuse of visual SSL methods suboptimal. We present Tactile-JEPA, an efficient self-supervised pre-training method that uses the spatial arrangement of tactile sensors to learn topology-aware representations. Specifically, it is trained to predict the embeddings of masked sensing elements from the unmasked remainder, using the sensor connectivity graph to guide spatial masking. Our analysis shows that effective tactile representations require capturing both local contact details and the global state of the tactile surface, which we achieve through dual-scale masking. Across three diverse datasets spanning magnetic and piezoresistive sensors, different robot embodiments, and single- and paired-sensor configurations, Tactile-JEPA reduces force estimation error by 6.3% and in-hand orientation error by 20.8% over the prior state-of-the-art, with consistent gains in other downstream applications, including policy learning. Overall, our results demonstrate that the benefit of tactile sensing depends critically on the quality of encoder pre-training, a problem which Tactile-JEPA addresses directly. Code is available at https://github.com/E-Kovtun/tactile.
