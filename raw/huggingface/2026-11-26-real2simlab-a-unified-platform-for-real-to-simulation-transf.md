---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.901864+00:00
arxiv_id: 2611.34849
url: https://huggingface.co/papers/2611.34849
arxiv_url: https://arxiv.org/abs/2611.34849
date: 2026-11-26
---

# Real2SimLab: A Unified Platform for Real-to-Simulation Transfer

Real-to-simulation transfer, which builds simulations from real-world observations, has long been studied in research and industry. Recently, coding agents have become capable of generating simulation programs from video recordings, and several benchmarks have been proposed to evaluate them. However, each individual benchmark defines its own inputs, deliverables, and scoring pipeline. This leads to N times M integrations when evaluating N methods on M benchmarks. To this end, we present Real2SimLab, a unified platform for real-to-simulation transfer. It evaluates a method by running its written program and scoring the output simulation with the original scorer of each benchmark. Moreover, Real2SimLab provides a pipeline to create training data and reward annotations for real-to-simulation methods. Our pipeline carefully avoids data contamination by filtering out the video recordings that exist in benchmarks. For each video recording, a program is first produced, and then our pipeline computes its reward with the same code that Real2SimLab uses for evaluation. So far, it supports 47 coding agents and 5 non-agent methods on 6 benchmarks. Both the platform and Awesome-Real2Sim, our research map of nearly 300 real-to-simulation papers, are open source, and we invite the Real2SimHub community to build them together.
