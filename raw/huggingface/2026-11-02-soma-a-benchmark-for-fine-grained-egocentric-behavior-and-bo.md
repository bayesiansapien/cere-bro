---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.500706+05:30
arxiv_id: 2610.36384
url: https://huggingface.co/papers/2610.36384
arxiv_url: https://arxiv.org/abs/2610.36384
date: 2026-11-02
---

# SOMA: A Benchmark for Fine-Grained Egocentric Behavior and Body-Motion Understanding

Perceiving human body motion is critical for multimodal systems that understand and assist people. Yet current evaluations of Multimodal Large Language Models (MLLMs) largely focus on objects, scenes, and coarse actions, leaving their ability to reason about the body itself poorly assessed. This is especially challenging from the egocentric perspective, in which the body is only partially visible and motion must be inferred from occluded and temporally distributed cues. We introduce SOMA, a benchmark for fine-grained body-motion understanding from egocentric video, comprising 1,632 human-verified questions across three capability axes: body configuration, motion dynamics, and temporal reasoning. We evaluate 37 leading closed-source, open-source, and specialized egocentric MLLMs, complemented by an extensive human evaluation. We find that humans also find this task difficult from video alone (68.5% accuracy), yet clearly outperform the strongest MLLM (Qwen3.6-27B), which reaches 50.0% zero-shot accuracy. Our error analysis shows that MLLMs often misread the wearer's own body, misjudge events in time, and are prone to biases such as favoring the right hand or under-counting repetitions. To narrow the gap to human performance and support further progress, we introduce a training dataset of aligned video, body motion, and language supervision, and a multimodal baseline that jointly learns from these modalities. By identifying common failure modes and missing capabilities in current MLLMs, we hope SOMA will inspire future research on body-motion understanding and multimodal reasoning. Full benchmark, training data, and code will be released at: https://cnai.epfl.ch/soma
