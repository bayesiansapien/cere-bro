---
source: farmer/huggingface
farmed: 2026-06-03T06:14:02Z
arxiv_id: 2605.27346
url: https://huggingface.co/papers/2605.27346
arxiv_url: https://arxiv.org/abs/2605.27346
date: 2026-06-03
---

# MERIT: Learning Disentangled Music Representations for Audio Similarity

Current music similarity models typically compute a single, monolithic score, entangling distinct musical dimensions like melody, rhythm, and timbre. This limits user control and interpretability, making it impossible to execute nuanced queries. We introduce MERIT, a framework for learning disentangled, factor-specific music representations tailored to these three core dimensions. To overcome the lack of isolated musical variations in real-world audio, we use a novel training strategy that uses conditional audio generation and source-separated stems to strongly encourage single-factor variation in training data. Our evaluations demonstrate strong factor-wise disentanglement. Each head responds strongly to its intended perceptual dimension while remaining near chance on the others, a representational property that holds across both the synthetic training domain and independent real-world audio.
