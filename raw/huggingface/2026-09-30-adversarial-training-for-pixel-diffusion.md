---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.38170
url: https://huggingface.co/papers/2609.38170
arxiv_url: https://arxiv.org/abs/2609.38170
date: 2026-09-30
---

# Adversarial Training for Pixel Diffusion

Pixel diffusion models generate RGB images directly, avoiding the bottleneck of an autoencoder, yet their outputs still systematically underrepresent fine-scale natural-image statistics. We show that adversarial learning provides an effective post-training correction for this deficiency. Starting from a pretrained model, we retain its original diffusion or flow-matching objective and add an adversarial loss to the predicted output at non-high-noise timesteps, leaving the model architecture and sampling procedure unchanged. To our knowledge, this is the first systematic study of adversarial post-training for pixel diffusion. Across two pixel backbones, the method jointly improves distribution fidelity, coverage, prompt alignment, and perceptual quality. We further investigate why it works. Frequency-band and power-law analyses show that the original models systematically underproduce natural-image high-frequency content, while adversarial post-training restores this missing spectral power. In contrast, perceptual loss also increases high-frequency content but sacrifices distribution fidelity and prompt alignment. Nearest-neighbor, recall, and matched no-GAN SFT controls further rule out memorization, mode dropping, and additional optimization as simple explanations. Finally, we examine the boundary of this effect. Under the tested latent diffusion configurations, the same procedure does not produce comparable joint gains and adds almost no decoded high-frequency power. These results identify direct output access to the image statistics being corrected as a key factor governing when adversarial post-training succeeds.
