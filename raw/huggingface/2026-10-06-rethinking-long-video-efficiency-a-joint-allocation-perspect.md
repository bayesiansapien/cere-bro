---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.04318
url: https://huggingface.co/papers/2610.04318
arxiv_url: https://arxiv.org/abs/2610.04318
date: 2026-10-06
---

# Rethinking Long-Video Efficiency: A Joint Allocation Perspective on Frames, Pixels, and Front-End Latency

Efficient long-video understanding with vision-language models (VLMs) is often framed as selecting informative frames or visual tokens at a fixed native resolution. We show that per-frame resolution can instead be traded for denser temporal coverage, while front-end decoding latency depends on the size of the candidate pool rather than the final token budget. An empirical study across multiple VLMs and long-video benchmarks yields three findings: dense low-resolution sampling outperforms sparse native-resolution sampling at matched token budgets; resolution-sensitive tasks benefit from selected high-resolution frames; and front-end decoding dominates wall time for hour-long videos. Motivated by these findings, we introduce LoHi, a training-free, single-pass framework that combines a dense low-resolution video stream with sparse high-resolution image frames through the VLM's native video and image pathways. LoHi-Anchor selects high-resolution frames using codec I-frame metadata, while LoHi-SemDiv uses query relevance and visual diversity over CLIP features. Across three long-video benchmarks, LoHi improves average accuracy by 10.6 percentage points over the native-resolution baseline at a matched token budget and by 5.2 percentage points over the strongest prior efficiency method. It also reduces front-end decoding latency by up to 7x on hour-long videos. Project page: https://sixundong.com/projects/lohi
