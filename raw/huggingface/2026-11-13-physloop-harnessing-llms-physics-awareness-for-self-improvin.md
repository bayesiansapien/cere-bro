---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.526657+00:00
arxiv_id: 2611.16748
url: https://huggingface.co/papers/2611.16748
arxiv_url: https://arxiv.org/abs/2611.16748
date: 2026-11-13
---

# PhysLoop: Harnessing LLMs' Physics Awareness for Self-Improving Video Generation Models

Video generation models produce visually realistic videos but still struggle with physical dynamics and causal consistency. Learning from generated videos requires fine-grained physical supervision, yet reliable quality judgments, correction pairs, and controlled variations are difficult to obtain. Large language models (LLMs) possess physical knowledge, but struggle to reliably guide video generation models in producing their training videos. We present PhysLoop, a unified harness designed to support physically grounded self-improvement in video generation models. The harness guides and constrains LLMs throughout video generation, selection, and correction, distilling their physical knowledge into physically consistent videos. The framework supports controllable training-data construction and inference-time video repair. By identifying and correcting failures, PhysLoop marks a key milestone toward recursive self-improvement (RSI) in video generation models with limited human intervention. We release 100K videos spanning diverse, realistic indoor and outdoor scenes, along with generation tools and two evaluation datasets: PhysLoop-Gen and PhysLoop-Repair. We evaluate controllable generation and localized repair on these datasets, respectively, and assess physical behavior on the external Physics-IQ Verified benchmark.
