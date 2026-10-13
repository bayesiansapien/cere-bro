---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.216593+05:30
arxiv_id: 2609.38748
url: https://huggingface.co/papers/2609.38748
arxiv_url: https://arxiv.org/abs/2609.38748
date: 2026-10-12
---

# Hear the World in Stereo: Learning Dynamic Spatial Correspondence for Immersive Joint Video-Audio Generation

Recent joint video-audio generation models have achieved strong semantic correspondence and temporal synchronization. However, applications such as AR/VR and interactive gaming further require stereo audio to provide an immersive sense, which remains largely overlooked. Effective stereo audio requires the perceived sound location to evolve consistently with the motion of its corresponding visual source. We refer to this property as Dynamic Spatial Correspondence and propose StereoBind, a framework that binds visual source motion to stereo sound generation. StereoBind uses motion tracks to coordinate visual motion and stereo audio through three complementary mechanisms. Visual Motion Binding establishes source-aware audiovisual correspondence, the Spatial Track Encoder captures absolute source positions, and Residual Track RoPE models relative motion. For supervision and evaluation, we construct StereoWorld-29K, a large-scale stereo audio-video dataset with paired motion tracks, and StereoWorldBench for measuring audiovisual spatial consistency. Experiments show that StereoBind substantially improves spatial alignment in stereo audio generation over existing models while preserving overall audiovisual quality.
