---
source: farmer/huggingface
farmed: 2026-05-20T09:54:48.537969+00:00
arxiv_id: 2605.17360
url: https://huggingface.co/papers/2605.17360
arxiv_url: https://arxiv.org/abs/2605.17360
date: 2026-05-20
---

# Omni-DuplexEval: Evaluating Real-time Duplex Omni-modal Interaction

Real-time duplex interaction is essential for multimodal AI systems operating in real-world scenarios, where models must continuously process streaming inputs and respond at appropriate moments. However, most existing multimodal large language models (MLLMs) are evaluated in offline settings, where the entire video input is processed before any response is generated. While recent work has started to explore real-time duplex MLLMs, there is still no comprehensive benchmark or automatic evaluation method for this setting. To address this gap, we propose Omni-DuplexEval, a benchmark for systematically evaluating real-time duplex interaction. The benchmark consists of two complementary scenarios: (1) Real-Time Description, which evaluates the ability to generate continuous, time-aligned responses that track evolving multimodal inputs, and (2) Proactive Reminder, which evaluates the ability to identify salient events and respond at appropriate moments. Omni-DuplexEval contains 660 videos with fine-grained, human-annotated labels and precise temporal metadata, spanning 9 tasks grounded in real-world scenarios, where all questions are formulated as open-ended queries. We further introduce an automatic evaluation framework based on LLM-as-a-Judge, which enables systematic assessment by jointly evaluating response-content alignment and response timing through timestamp-aware and sequential reasoning, achieving strong alignment with human judgments. Experiments on state-of-the-art duplex MLLMs reveal substantial limitations. The best-performing model achieves only 39.6% overall, while scoring only 20.0% on Proactive Reminder. Our analysis identifies two key challenges: models struggle to balance timely responses with coherent, holistic content generation, and they often fail to determine both when to respond and what to produce. We hope our work facilitates further progress in MLLMs.
