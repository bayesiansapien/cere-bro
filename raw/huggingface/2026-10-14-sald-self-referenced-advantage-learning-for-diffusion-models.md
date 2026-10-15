---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.503239+00:00
arxiv_id: 2610.01496
url: https://huggingface.co/papers/2610.01496
arxiv_url: https://arxiv.org/abs/2610.01496
date: 2026-10-14
---

# SALD: Self-Referenced Advantage Learning for Diffusion Models

Recent work on language-model adaptation has shown that single models can obtain informative training signals by evaluating their behavior in demonstrationor feedback-augmented contexts, with the help of a teacher network, which is driven by the student's learned parameters. Inspired by this internal-reference principle, we investigate how diffusion models can identify self-referenced training signals without external demonstrations or teacher networks. We introduce SALD, a self-referenced training framework that evaluates each image-caption pair at two noise levels using the same model. The easier, lower-noise path is evaluated without gradient tracking to provide a reference, while the harder, higher-noise path provides the training gradient. Rather than directly distilling the easy-path prediction, SALD uses the difference between two path errors to adapt the hardpath objective. The proposed Advantage-Guided Diffusion (AGD) converts this relative error into a differentiable sample-level weight. Temporal Advantage Memory (TAM) accumulates relative difficulty across training and adapts the future gap between the two noise levels. Spectral Advantage Decomposition (SAD) further compares the residual power spectra of the two paths and constructs a differentiable, frequency-derived latent-element weight. All components share a single set of model parameters, requiring neither an external teacher network nor additional trainable parameters during training or inference, and no modification to the inference procedure. Experiments across multiple architectures and datasets demonstrate consistent improvements in generation quality, while component-wise ablations quantify the contributions of the proposed components.
