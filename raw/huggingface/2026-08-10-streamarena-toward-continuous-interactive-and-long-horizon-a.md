---
source: farmer/huggingface
farmed: 2026-08-10T09:04:01.722687
arxiv_id: 2608.05703
url: https://huggingface.co/papers/2608.05703
arxiv_url: https://arxiv.org/abs/2608.05703
date: 2026-08-10
---

# StreamArena: Toward Continuous, Interactive, and Long-Horizon Agentic Streaming Video Understanding

Deploying autonomous multimodal agents in continuous, real-world environments requires them to ingest unbounded audio-visual streams and maintain hour-scale memory. However, current evaluations predominantly rely on brief clips and multiple-choice formats. This design allows minimal baselines that process only the last four frames to match or surpass complex streaming models, while answer options also expose language shortcuts. We introduce StreamArena, a benchmark for hour-scale, interactive streaming video understanding. StreamArena contains 243 full-length videos averaging 88.8 minutes and 3,646 rigorously annotated, open-ended question-answer pairs that evaluate real-time perception, historical retrospection, proactive interaction, and multimodal tool utilization. Evaluation across diverse systems exposes a tension between continuous interaction and long-horizon multimodal comprehension. Methods that retain only recent frames cannot recover distant events, methods that convert past observations into text lose visual evidence, and methods that repeatedly compress visual memory struggle to preserve fine-grained details over time. We address this tension with StreamMind, a two-tier architecture that assigns latency-critical interaction and proactive monitoring to independently scheduled frontend workers, while backend workers asynchronously construct persistent multimodal memory and perform historical recall and external search. StreamMind outperforms existing streaming baselines across all four capabilities and reduces query-to-answer latency by reusing persistent state.
