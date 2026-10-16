---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.224141+05:30
arxiv_id: 2610.18072
url: https://huggingface.co/papers/2610.18072
arxiv_url: https://arxiv.org/abs/2610.18072
date: 2026-10-15
---

# LensErase: A Foundation Model for Erase Anything

We introduce LensErase, a general-purpose mask-based Erase Anything foundation model designed to cover a broad spectrum of real-world erase scenarios. LensErase supports diverse objects, visual text, watermarks, associated visual effects, multiple-object removal, and a wide range of object scales, aspect ratios, and image resolutions. First, to enable such broad coverage, we construct LensErase-100M, a large-scale dataset containing 101.07 million paired source-mask-target examples spanning diverse erase scenarios. Second, we pretrain LensErase from the text-to-image model Lens, adapting its strong generative prior to mask-based erasing. To efficiently incorporate the source image and erase mask, we propose Mask-Aware RoPE, a 3D rotary positional encoding that directly injects mask information into the source-image tokens without introducing a separate mask token sequence. Finally, we refine the model through supervised fine-tuning and reinforcement learning with contract-guided, region-aware rewards, and apply TraceFusion at inference to preserve high-fidelity content outside the effective edit region. Across six public benchmarks and the proposed LensErase-Bench, LensErase achieves substantial improvements under both reference-based objective metrics and reference-free VLM evaluation. We hope LensErase can serve as a foundational model for erase-related applications and systems.
