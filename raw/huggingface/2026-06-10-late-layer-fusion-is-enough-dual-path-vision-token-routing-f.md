---
source: farmer/huggingface
farmed: 2026-06-10T06:28:48Z
arxiv_id: 2606.09131
url: https://huggingface.co/papers/2606.09131
arxiv_url: https://arxiv.org/abs/2606.09131
date: 2026-06-10
---

# Late-Layer Fusion is Enough: Dual-Path Vision Token Routing for Multimodal Large Language Models under Visual Saturation

Multimodal large language models (MLLMs) commonly inherit the deep, symmetric Transformer backbone designed for unimodal text modeling, and apply the same computation uniformly to image and language tokens. This design overlooks a key modality asymmetry: image and text tokens differ substantially in information density, redundancy, and required reasoning depth. Through a layer-wise analysis of LLaVA-1.5, we observe that vision tokens tend to saturate in the middle layers. Specifically, text-to-image attention decreases from 0.68 at layer 0 to 0.07 by layer 4, and stabilizes near 0.04 after layer 18, whereas text tokens continue to benefit from deep semantic processing. These findings suggest a mismatch between architectural symmetry and depth-asynchronous modality evolution, resulting in redundant visual computation and possible drift in perceptual representations during deep task-specific adaptation. Motivated by this, we propose Dual-Path Vision Token Routing (DPVR), a modality-asymmetric routing framework for efficient MLLMs. Its core instantiation, DPVR-LF (Late-Layer Fusion), routes vision tokens at the saturation point into a one-layer trainable side branch, runs a thirteen-layer text-only forward that skips image positions in the deep stack, and re-fuses the visual and textual streams only at the final layer. With approximately 3% trainable parameters, DPVR-LF preserves competitive multimodal performance on standard benchmarks while reducing visual computation in the deep Transformer stack. The results challenge the conventional assumption that vision tokens must traverse all deep language-model layers, and indicate that a single late fusion layer can be sufficient for maintaining strong perceptual competence in LLaVA-style MLLMs.
