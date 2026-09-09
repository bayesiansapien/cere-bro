---
source: farmer/huggingface
farmed: 2026-09-09T05:28:24.738031+00:00
arxiv_id: 2609.06373
url: https://huggingface.co/papers/2609.06373
arxiv_url: https://arxiv.org/abs/2609.06373
date: 2026-09-09
---

# Multi-Grid Post-Training for Long-Form Multi-Shot Video Generation

Generating long-form multi-shot videos requires coherent within-shot motion and visually consistent narratives across shots. Existing video generators favor continuous motion and struggle to present complete shot sets when an entire narrative is packed along one temporal axis. We propose MovieGrid, a Multi-Grid Post-Training paradigm that decomposes a long video into shorter, temporally ordered chunks and arranges them on a spatial grid for joint modeling. This design reduces the number of shots handled by each temporal axis while enabling global information exchange across chunks. We construct the Multi-Grid Long Video (MGLV) dataset from 1,000 long-form videos using source video collection, hierarchical segmentation, grid video construction, and character-aware story annotation, producing 54K grid videos paired with story prompts. Our Noise-Free Random-Grid Training retains a random subset of chunks as clean visual context for denoising the remaining chunks. Grid Embedding encodes grid structure, character-aware Story Prompts link recurring entities, and Grid Boundary Loss stabilizes layouts. Under the same token budget, MovieGrid generates 6.05 times more shots than Temporal Packing in a 1,616-frame video. On a benchmark spanning five real-world categories, it achieves state-of-the-art intra-shot consistency (0.9131 versus 0.8086 for HoloCine) and inter-shot consistency (0.5914 versus 0.5384 for StoryMem). MovieGrid can further scale video length with minimal compromise through single or multiple generations.
