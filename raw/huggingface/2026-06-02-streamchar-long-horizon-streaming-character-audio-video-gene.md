---
source: farmer/huggingface
farmed: 2026-06-02T09:40:06Z
arxiv_id: 2605.25659
url: https://huggingface.co/papers/2605.25659
arxiv_url: https://arxiv.org/abs/2605.25659
date: 2026-06-02
---

# StreamChar: Long-Horizon Streaming Character Audio-Video Generation with Decoupled Orchestration

Real-time streaming joint audio-video generation for character animation requires a generator to speak the requested transcript, maintain visual identity across chunks, and run within a strict playback budget. These requirements are difficult to satisfy simultaneously: chunk-wise autoregressive generation can accumulate transcript-audio misalignment and visual drift, while the few-step distillation needed for low latency often degrades spatial diversity and temporal quality. We present StreamChar, a streaming framework that separates long-horizon orchestration from short-window audio-video denoising. An LLM-based orchestrator uses the transcript and historical context to produce frame-aligned audio conditions, and a joint audio-video DiT performs local bidirectional denoising with reference and motion-frame conditioning. For efficient deployment, we use a two-stage distillation pipeline that first compresses the sampler and then fine-tunes the student under online chunk rollouts. A progress-aware pointer aligns partial transcripts with generated audio during rollout training, and a sink-chunk memory provides a persistent visual anchor for reducing long-horizon drift. Experiments on short-clip and long-horizon protocols show that StreamChar runs in real time on a single H100 GPU and provides a favorable system-level trade-off among transcript fidelity, audio-visual synchronization, visual quality, and streaming stability compared with recent joint and audio-driven baselines.
