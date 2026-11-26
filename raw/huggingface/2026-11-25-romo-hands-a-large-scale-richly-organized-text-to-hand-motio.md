---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.31766
url: https://huggingface.co/papers/2611.31766
arxiv_url: https://arxiv.org/abs/2611.31766
date: 2026-11-25
---

# RoMo Hands: A Large Scale Richly Organized Text to Hand Motion Dataset

While text-driven body motion generation has matured, pure-hand synthesis remains bottlenecked by data. Existing datasets often treat hands as rigid end-effectors, lack fine-grained captions, or are too limited in scale to support robust generalization. We introduce RoMo Hands, an in-the-wild, text-paired dataset of ~542K sequences (884 hours, 95.5M frames at 30 fps) which is an order of magnitude larger than prior work. To ensure high-quality supervision, a stringent dexterity filter discards low-articulation sequences, focusing the distribution on complex bimanual movement. Each clip is paired with five captions at increasing granularities from global semantic tags to atomic finger states, organized under a hierarchical taxonomy. To bridge the gap between body and hand architectures, we propose a novel 393-D bimanual representation that adapts redundant body-motion paradigms to the high-DoF kinematics of hands. Systematic benchmarking of diffusion, masked-token, and autoregressive generators reveals distinct trade-offs under these hand-specific adaptations, including a sharp divergence between semantic alignment and kinematic plausibility. Our dataset, representation, and benchmark establish a rigorous foundation for the next generation of dexterous motion synthesis. Project page: https://romodataset.github.io/romo-hands/.
