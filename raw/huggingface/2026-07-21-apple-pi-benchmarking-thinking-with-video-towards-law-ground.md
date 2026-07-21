---
source: farmer/huggingface
farmed: 2026-07-21T07:20:44Z
arxiv_id: 2607.16401
url: https://huggingface.co/papers/2607.16401
arxiv_url: https://arxiv.org/abs/2607.16401
date: 2026-07-21
---

# Apple-π: Benchmarking Thinking with Video Towards Law-Grounded Physical Intelligence

Modern video generation models are increasingly hailed as emerging world models with an internalized grasp of physical law. Yet existing benchmarks largely evaluate physical plausibility only at the output level, without verifying whether the model arrives there through a faithful, law-grounded reasoning process. We introduce Apple-PI, the first benchmark that anchors video-model evaluation explicitly in physical laws. Apple-PI comprises three components. 1) Orchard: a dataset of 400 videos covering ten canonical tasks in classical mechanics. It separates single-law tasks for confounder-free diagnosis from multi-law tasks for probing generalization. 2) Benchmark Protocol: a three-stage protocol based on scientific reasoning, including Perception, Formulation, and Deduction. It uses chain-of-frames prompting on infographic-annotated first frames, treating the generated video as the model's visible reasoning trace. 3) Evaluation Suite: a hybrid evaluation suite that combines MLLM-based subjective scoring with physics-law-grounded objective measures. This enables stage-resolved diagnosis of not only whether a model fails, but where it fails. Benchmarking 11 models shows that current video models remain far from reliable law-grounded world simulators, with the best video model scoring only 0.473. Our stage-, pillar-, and source-resolved analyses further expose a Perception-to-Formulation-to-Deduction bottleneck, weak multi-law state transfer, and a persistent Sim-to-Real gap. These findings position Apple-PI as a diagnostic foundation for guiding future video models toward world models with law-grounded physical intelligence.
