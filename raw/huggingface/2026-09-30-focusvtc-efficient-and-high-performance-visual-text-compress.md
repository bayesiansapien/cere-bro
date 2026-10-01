---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.36651
url: https://huggingface.co/papers/2609.36651
arxiv_url: https://arxiv.org/abs/2609.36651
date: 2026-09-30
---

# FocusVTC: Efficient and High-Performance Visual Text Compression with Adaptive Resolution

Long-context reasoning in large language models incurs substantial computation and memory costs. Visual text compression (VTC) reduces input length by rendering text as images, but fixed-resolution rendering creates a compression-performance trade-off: low DPI saves tokens at the expense of legibility, whereas high DPI spends tokens on irrelevant content. We introduce FocusVTC, which breaks this trade-off through adaptive resolution while preserving general multimodal capabilities. It combines compressed low-DPI global views with selective region enhancement, integrating enhanced views into ongoing reasoning. We construct 29.4K high-quality Reasoning-Evidence Localization (REL) chain-of-thought examples (REL-CoT) that link reasoning traces to page indices and bounding boxes. Multi-resolution REL supervised fine-tuning (REL-SFT) teaches the model to localize relevant regions, and Group Relative Policy Optimization learns when to enhance resolution and how to use the resulting observations, without a separate continual-pretraining stage. At 72 DPI on RULER v1, FocusVTC scores 87.4 at 2.9times input compression, including tool observations, versus 57.5 for Glyph at 3.0times input compression. It surpasses its text-input backbone on LongBench (56.40 versus 55.86), improves the MRCR macro-average by 13.91 points, and achieves a 51.19 macro-average on VTCBench. The MRCR latency evaluation also shows a 2.79times online end-to-end speedup over Text. General multimodal capabilities are preserved, with MMMU increasing from 65.12 to 66.73 and MME from 2424.02 to 2457.62.
