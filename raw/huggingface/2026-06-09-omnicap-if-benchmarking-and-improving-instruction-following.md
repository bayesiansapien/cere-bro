---
source: farmer/huggingface
farmed: 2026-06-09T16:28:21
arxiv_id: 2606.08572
url: https://huggingface.co/papers/2606.08572
arxiv_url: https://arxiv.org/abs/2606.08572
date: 2026-06-09
---

# OmniCap-IF: Benchmarking and Improving Instruction Following Abilities for Omni-Video Captioning

While Omni-modal Large Language Models (OLLMs) have demonstrated impressive capabilities in jointly processing audio and visual streams, their ability to strictly adhere to complex, multi-faceted user instructions remains largely unexplored. Existing benchmarks primarily focus on holistic video understanding or text-only instruction following, failing to capture the intricate interplay between modalities and user constraints. To bridge this gap, we introduce OmniCap-IF, the first comprehensive benchmark specifically designed to evaluate instruction-following capabilities in omni-modal captioning. OmniCap-IF incorporates a systematic framework that assesses captions on two dimensions: format correctness and content correctness. Our benchmark encompasses 50 distinct constraint types across pure visual, pure audio, and audio-visual modalities, while integrating Temporal Grounding to assess spatio-temporal precision. Extensive evaluations of prominent models on 1,920 high-quality samples reveal significant performance disparities. Furthermore, our analysis uncovers a critical "format-content tradeoff", demonstrating that increasing formatting complexity directly degrades models' omni-modal reasoning abilities. Finally, to advance the field, we curate a 54K instruction-tuning dataset, OmniCap-IF-54K and present OmniCaptioner-IF, which achieves notable improvements in both complex instruction adherence and general omni-modal captioning performance.
