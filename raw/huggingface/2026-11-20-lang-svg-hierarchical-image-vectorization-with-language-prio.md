---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.393158+00:00
arxiv_id: 2611.15941
url: https://huggingface.co/papers/2611.15941
arxiv_url: https://arxiv.org/abs/2611.15941
date: 2026-11-20
---

# Lang-SVG: Hierarchical Image Vectorization with Language Priors

Image vectorization reconstructs raster images as compact scalable vector graph- ics (SVG), providing a structured and editable code representation of images. However, most existing vectorization methods optimize for pixel-level render- ing fidelity, often producing SVGs that lack alignment with human-perceived object-part hierarchies, making them difficult to manipulate. To address this, we propose Lang-SVG, which introduces an explicit tree structure to organize SVG primitives with semantic labels and parent-child relationships. Lang-SVG incorporates granularity-controllable and open-vocabulary segmentation priors to initialize object-part hierarchies and leverages multimodal large language models (MLLMs) with SVG tree context to assign semantic labels to unlabeled nodes. To reduce redundancy, we introduce depth-adaptive simplification to reduce shape complexity and Tree-Guided Pruning and Merging to eliminate redundant SVG nodes. L1-SAM-Prompting further recovers missing regions to improve recon- struction fidelity and structural completeness. Beyond reconstruction fidelity, we introduce a new evaluation protocol that measures structural quality and semantic part alignment. Experiments demonstrate that Lang-SVG achieves state-of-the-art performance in both rendering fidelity and structural quality. Project website: https://xiliu8006.github.io/Lang-SVG/.
