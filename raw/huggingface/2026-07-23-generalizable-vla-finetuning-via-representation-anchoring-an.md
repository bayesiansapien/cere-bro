---
source: farmer/huggingface
farmed: 2026-07-24T23:47:01.610703+05:30
arxiv_id: 2607.13429
url: https://huggingface.co/papers/2607.13429
arxiv_url: https://arxiv.org/abs/2607.13429
date: 2026-07-23
---

# Generalizable VLA Finetuning via Representation Anchoring and Language-Action Alignment

Finetuning a pretrained vision-language model (VLM) on robot demonstrations via behavior cloning (BC) has become the standard recipe for vision-language-action (VLA) policies. However, BC finetuning progressively overwrites the pretrained representations that support visual and semantic generalization. Co-training on web image-text data, a common remedy, does not prevent this; it applies language and action losses to separate observations, leaving VLAs with language-action misalignment that standard manipulation benchmarks do not expose. We propose Anchor-Align, which augments BC with two objectives: Vision-Language Anchoring distills layer-wise representations from a frozen VLM copy to prevent this drift, while Language-Action Alignment converts each action target into a discrete motion-direction label and jointly trains language and action prediction on the same robot observation. On a physical xArm7 robot, across two widely used VLA architectures, Anchor-Align improves real-robot success on both (28% to 54% and 37% to 60%). At scale in simulation, we demonstrate consistent improvements on OOD perturbations, perceptual robustness, and long-horizon control across LIBERO-PRO, LIBERO-Plus, and CALVIN, respectively, suggesting that preserving pretrained representations and effective action learning are not fundamentally at odds. Project page: anchoralignvla.github.io
