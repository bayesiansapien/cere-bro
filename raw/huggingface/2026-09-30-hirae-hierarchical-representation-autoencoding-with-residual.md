---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.37775
url: https://huggingface.co/papers/2609.37775
arxiv_url: https://arxiv.org/abs/2609.37775
date: 2026-09-30
---

# HiRAE: Hierarchical Representation Autoencoding with Residual Budgets

Pretrained visual representations support image generation, but may not fully preserve the fine-grained details needed for faithful reconstruction. Meanwhile, intermediate encoder layers contain complementary visual details, but learning to fuse them for reconstruction can produce a latent distribution that is difficult to model. Existing fusion methods require empirical tuning of layer selection or staged optimization of fusion and decoding, increasing configuration effort or training complexity. We introduce HiRAE (Hierarchical Representation Autoencoder), which learns a hierarchical fusion framework over the full encoder hierarchy to improve reconstruction fidelity while maintaining compatibility with generative modeling. HiRAE groups encoder layers by depth and learns residual corrections to the deepest representation. Group-wise norm caps bound these corrections relative to the deep anchor, with tighter budgets for shallower groups. Our HiRAE-24 preserves the latent token count and channel dimension. On ImageNet-256, HiRAE-24 reduces reconstruction FID from 0.299 to 0.209 relative to RAEv2 while maintaining competitive guided generation quality. For text-to-image generation, HiRAE-24 improves alignment over RAEv2 on GenEval, DPG-Bench, and GenAI-Bench both before and after supervised fine-tuning. Under the same generator-training and evaluation protocol, post-fine-tuning GenEval increases from 84.86 to 87.70.
