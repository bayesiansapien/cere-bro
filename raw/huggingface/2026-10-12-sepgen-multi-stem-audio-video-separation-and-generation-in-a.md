---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.217329+05:30
arxiv_id: 2610.11361
url: https://huggingface.co/papers/2610.11361
arxiv_url: https://arxiv.org/abs/2610.11361
date: 2026-10-12
---

# SepGen: Multi-Stem Audio-Video Separation and Generation in a Single Model

A 4D audio-visual scene comprises a video, the dynamic geometry it depicts, and the sound sources that populate it, each with its own position and trajectory. Rendering such a scene from a novel viewpoint requires that every source be available as an individual waveform, so that it can be localized in the scene and propagated to the observer before the signals are mixed. Joint audio-video generators can synthesize the video and its soundtrack, but the soundtrack is emitted as a single audio-mix in which the sources are not individually accessible. We present SepGen, which extends a pretrained audio-video generator to emit the video, the mixed soundtrack, and one waveform per captioned source in one joint sampling run. SepGen supports two complementary modes: generation and separation. In generation mode, each source caption specifies what its stem contains. A two-speaker dialogue, for example, comes out as one stem per speaker in the original turn order. In separation mode, the input audio-mix remains clean while the captions specify what to extract, so the model can decompose a recording from a free-text description. We evaluate generation on scenes synthesized from text, and separation on scenes rendered by other generators and on real recordings of speech, music, and sound effects. Given an audio-mix and captions that carry the spoken lines, SepGen outperforms language-conditioned separators, most clearly on speech, and it keeps the lead when the lines are removed from the captions. Code, checkpoints, and datasets are available at https://sepgen.github.io/
