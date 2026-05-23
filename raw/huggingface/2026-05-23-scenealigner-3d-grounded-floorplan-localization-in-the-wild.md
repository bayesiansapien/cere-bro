---
source: farmer/huggingface
farmed: 2026-05-23T00:00:00Z
arxiv_id: 2605.22581
url: https://huggingface.co/papers/2605.22581
arxiv_url: https://arxiv.org/abs/2605.22581
date: 2026-05-23
---

# SceneAligner: 3D-Grounded Floorplan Localization in the Wild

Many public buildings provide floorplans with a "you are here" indicator to help visitors orient themselves. Floorplan localization seeks to computationally replicate this capability by determining where visual observations were captured within a floorplan. However, existing methods typically assume controlled small-scale environments and precise vectorized floorplans, limiting their ability to operate in large-scale buildings and rasterized floorplans. In this work, we present an approach for performing floorplan localization in the wild by grounding the task in a reconstructed 3D representation of the scene. Given an unconstrained image collection, our method reconstructs a gravity-aligned 3D scene and projects it into a 2D density map that serves as a floorplan proxy. Floorplan localization is then formulated as aligning this proxy with the input floorplan via a 2D similarity transform. To bridge the appearance gap between density maps and architectural floorplans, we adapt a 2D foundation model to learn cross-modal correspondences, introducing a fine-tuning scheme that encourages semantically aligned matches while preserving structural consistency. Extensive experiments demonstrate substantial improvements over prior methods, including in extremely sparse settings with as little as a single input image. Our code and data will be publicly available.
