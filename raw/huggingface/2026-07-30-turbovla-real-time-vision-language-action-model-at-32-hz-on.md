---
source: farmer/huggingface
farmed: 2026-07-30T12:41:02.128718+05:30
arxiv_id: 2607.27205
url: https://huggingface.co/papers/2607.27205
arxiv_url: https://arxiv.org/abs/2607.27205
date: 2026-07-30
---

# TurboVLA: Real-Time Vision-Language-Action Model at 32 Hz on an RTX 4090 with <1 GB VRAM

Vision-language-action (VLA) models commonly adopt an LLM-centric V to L to A pathway, where visual observations are projected into the representation space of a large language model before being decoded into robot actions. Although effective, this design incurs substantial computation and memory overhead at every policy invocation. In this work, we introduce TurboVLA, a new VLA paradigm that reformulates the conventional V to L to A pathway as a direct V + L to A mapping. Instead of using a large language model as the central interface between perception and action, TurboVLA independently encodes visual observations and language instructions, directly exchanges information between them through lightweight bidirectional vision-language interaction, and predicts continuous action chunks with a compact decoder. This simple design constructs task-conditioned representations directly from visual and linguistic features, significantly reducing the computational and memory costs of VLA inference. On LIBERO, TurboVLA achieves 97.7% average success with only 0.2B parameters, 31.2 ms inference latency, and 0.9 GB inference VRAM on a consumer-grade RTX 4090, matching or outperforming substantially larger VLA policies. These results establish TurboVLA as a simple and effective alternative to the prevailing LLM-centric VLA paradigm, offering a new perspective on how vision, language, and action can be connected for efficient robotic manipulation. Code is available at https://github.com/H-EmbodVis/TurboVLA.
