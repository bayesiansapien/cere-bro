---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.884237+00:00
arxiv_id: 2610.31494
url: https://huggingface.co/papers/2610.31494
arxiv_url: https://arxiv.org/abs/2610.31494
date: 2026-10-23
---

# AgentVQA: A Unified Benchmark for Agentic Visual Understanding

Vision-language models (VLMs) can perform a broad range of tasks across diverse settings, yet their performance in agentic contexts remains poorly understood. Although online evaluations in simulators and real-world environments are essential for measuring interactive agent performance, they are costly and challenging to scale. Complementary offline VQA benchmarks can enable faster and more reliable comparisons across agentic domains, yet existing benchmarks remain limited and fragmented. To address this gap, we introduce AgentVQA, an offline benchmark for evaluating VLMs on realistic agentic scenarios across five agent domains: Web Agents, Robotics, Egocentric Videos, Games, and Spatial Planning. We build AgentVQA by manually selecting 1000 challenging, real-world agent examples from 23 source datasets and adapting them for reliable offline evaluation. The resulting benchmark preserves realistic scenarios from interactive environments across diverse domains, and its model rankings track those from corresponding online evaluations. Across the 22 evaluated models, the best achieves only 58.5% accuracy. Our cross-domain analysis shows that errors are driven primarily by failures to ground and maintain accurate representations of the current and evolving visual state, including localizing relevant UI elements, interpreting motion, tracking state changes over time, and inferring 3D spatial relationships, rather than by task misinterpretation or downstream logical reasoning.
