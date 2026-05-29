---
source: farmer/huggingface
farmed: 2026-05-29T09:54:41Z
arxiv_id: 2605.30349
url: https://huggingface.co/papers/2605.30349
arxiv_url: https://arxiv.org/abs/2605.30349
date: 2026-05-29
---

# AdaState: Self-Evolving Anchors for Streaming Video Generation

Autoregressive video diffusion models generate streaming video by producing frames sequentially, conditioning each chunk on previously generated content. These models are structurally anchored to the first frame: its key-value representation occupies a privileged position in the attention cache and serves as the primary scene reference throughout generation. As the cleanest and most error-free position in the cache, this anchor draws disproportionate attention, suppressing video dynamics, and locking scene composition to the initial viewpoint even as the scene naturally evolves. The result is a temporally shallow video in which motion, camera movement, and scene progression are dampened in favor of static consistency. To address this, we replace the static anchor with an adaptive state, a hidden latent that the model denoises alongside content at every chunk but never renders. Rather than referencing a frozen first frame, the model generates its own scene anchor at each step by attending to both the previous state and the current content, producing a reference that evolves with the generated content. Unlike standard video generation, which encodes an absolute notion of time, our formulation treats time as relative: every generation step sees the same positional structure regardless of how far generation has progressed, and the state transition is identical at every chunk. Together, these properties introduce a recurrence into the generation process, where denoising serves as the transition function, and the KV cache serves as the carrier, requiring no external module. Experiments demonstrate that the adaptive state substantially improves video dynamics, enabling richer motion and natural scene progression within generated videos.
