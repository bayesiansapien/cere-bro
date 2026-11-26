---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.32067
url: https://huggingface.co/papers/2611.32067
arxiv_url: https://arxiv.org/abs/2611.32067
date: 2026-11-25
---

# LoopDVR: Looped Transformer for Efficient Dense Visual Recognition

We propose LoopDVR, a framework for converting pretrained Transformer-based dense visual recognition models into parameter-efficient looped networks. Rather than reducing the network width or depth directly, LoopDVR reuses Transformer blocks across layers in both the ViT backbone and Transformer decoder, reducing the number of parameters while retaining the original computational structure. However, naively sharing parameters can disrupt the distinct transformations learned at different depths. To address this challenge, we identify suitable sharing groups based on inter-layer representation dissimilarity and keep the final backbone block independent for multi-scale feature construction. We then initialize each shared backbone block with the pretrained weights of its group's terminal layer to better preserve the learned representations. An independent Loop Adapter at each layer further helps retain depth-specific transformations within shared blocks. Subsequently, we distill visual representations into the looped backbone and integrate it with a looped decoder for task-specific training. Experiments demonstrate that LoopDVR achieves the best accuracy--parameter trade-offs across dense recognition tasks. Compared with the reference models, it reduces parameters by approximately 28% while maintaining competitive accuracy. Notably, LoopDet-S achieves 50.9 box AP with only 7.0M parameters, highlighting its effectiveness in compact models.
