---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.114110+00:00
arxiv_id: 2611.18668
url: https://huggingface.co/papers/2611.18668
arxiv_url: https://arxiv.org/abs/2611.18668
date: 2026-11-17
---

# UMM-JEPA: Generative Pretraining via Masked Next-Scale Representation Prediction for Unified Multimodal Models

Unified multimodal models can support both visual understanding and generation, yet generative training does not necessarily improve understanding. We argue that this limitation may arise from a mismatch between the representation targeted by generation and the perceptual representation used for understanding. Conventional generation objectives primarily optimize synthesis-oriented spaces such as discrete visual codes or generative latents. We therefore introduce UMM-JEPA, which reformulates generation as progressive prediction of continuous visual-understanding representations. The model constructs a multi-scale representation hierarchy from coarse to fine, while pixel rendering is decoupled from representation pretraining and attached only afterward. Controlled comparisons show that the representation-prediction objective accounts for most of the understanding improvement, while a data-matched control leaves the group means nearly unchanged. UMM-JEPA reaches a 16-benchmark visual mean of 51.71, against 46.36 for the understanding-only Qwen-VL baseline, and the text mean also rises. Compared with discrete-code and latent-flow generation objectives, perceptual representation prediction yields stronger and more consistent transfer to understanding. Linear probes and visual-evidence interventions further reveal richer object and spatial structure and stronger use of image-specific information. These results suggest that generation can benefit understanding when it directly supervises the perceptual representations that understanding consumes.
