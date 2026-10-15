---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.506464+00:00
arxiv_id: 2610.16118
url: https://huggingface.co/papers/2610.16118
arxiv_url: https://arxiv.org/abs/2610.16118
date: 2026-10-14
---

# Elephant in the Fridge: Constant-Memory Frame Packing for Long Video Understanding

Hour-long videos, streaming feeds, and movie-length content are pushing vision-language models (VLMs) past their breaking point -- the standard recipe of encoding each frame into visual tokens yields sequences that grow linearly with video length, causing prohibitive memory consumption and inference latency. Existing approaches, such as token reduction and keyframe selection, shorten the token sequence but leave the O(n) scaling intact, failing to resolve the fundamental bottleneck. We propose FramePack-U, a strikingly simple, training-free frame packing framework that compresses arbitrarily long videos into a fixed size visual representation at constant memory cost. FramePack-U requires no fine-tuning or architectural modification -- it plugs directly into off-the-shelf VLMs at inference time. Inspired by FramePack from the generation literature, we propose a content-aware compression strategy for visual understanding under a fixed token budget. Specifically, FramePack-U (1) scores each frame by its semantic similarity to the text prompt and ranks frames in a diversity-driven manner, and (2) packs the selected frames at varying resolutions into a fixed-length context window. This concentrates the memory budget on frames that are both instruction-relevant and visually diverse. While FramePack-U can in theory pack arbitrarily many frames into the fixed budget, we identify an empirical instantiation that generalizes robustly across settings. Extensive experiments on LongVideoBench, MLVU, and Video-MME show that FramePack-U consistently outperforms full-resolution baselines and prior token reduction and keyframe selection methods across diverse model families, parameter scales, and frame budgets. Notably, on Qwen3.5-35B-A3B with a 128-frame budget, FramePack-U yields gains of +12.9\%, +10.6\%, and +9.7\% over the official model on the three benchmarks, respectively.
