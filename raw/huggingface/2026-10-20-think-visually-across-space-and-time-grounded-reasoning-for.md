---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.25090
url: https://huggingface.co/papers/2610.25090
arxiv_url: https://arxiv.org/abs/2610.25090
date: 2026-10-20
---

# Think Visually Across Space and Time: Grounded Reasoning for Video Segmentation

Video Reasoning Segmentation (VRS) requires a model to identify an implicitly described target and predict its pixel-level mask trajectory, while resolving the spatial relations and temporal events that determine the answer. Text-only Chain-of-Thought (CoT) can explain a target choice without making the underlying visual references explicit, leaving a video reference gap between linguistic inference and the evidence distributed across frames. We introduce Temporal Chain of Video Primitives (TCoVP), a spatiotemporally grounded form of Video CoT that organizes query-relevant observations into a chronological reasoning chain. Each primitive associates an entity reference with temporal support and timestamped spatial evidence, and the chain interleaves these references with language to guide reasoning about which entity is relevant, when the queried event holds, and where its evidence appears. The selected target primitives then provide box prompts and temporal support for video mask prediction. We construct TCoVP-SFT-15k and TCoVP-RL-13k to learn this representation through supervised fine-tuning and chain-aligned reinforcement learning. Extensive experiments across five VRS benchmarks and three model backbones demonstrate the strong performance of TCoVP, highlighting the effectiveness of organizing spatial and temporal evidence within the reasoning process. All models and code will be publicly released. Project page: https://victor-wjw.github.io/TCoVP/
