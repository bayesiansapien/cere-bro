---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.21910
url: https://huggingface.co/papers/2610.21910
arxiv_url: https://arxiv.org/abs/2610.21910
date: 2026-10-16
---

# CoWorld Reasoner: Agentic Multimodal Reasoning with the Evolving Video World Model-Driven Harness

As Vision-Language Models (VLMs) advance, they are increasingly expected to perform spatiotemporal reasoning over motion, actions, and view changes beyond what the input images show. Video World Models (VWMs) provide a natural unified engine for visual imagination by generating task-relevant visual content as additional evidence. However, existing approaches typically invoke a VWM through fixed pipelines centered on a predefined form of visual imagination, such as novel-view synthesis. To support flexible visual imagination for diverse reasoning tasks, we introduce CoWorld Reasoner, an agentic framework that uses a VWM as a unified visual reasoning engine. Its Video World Model-Driven Harness exposes multiple visual operations through tools and uses skills to guide the VLM in deciding whether to imagine, selecting an operation, constructing a generation request, and interpreting the resulting visual evidence. We further introduce VLM-VWM Harness Co-Evolution, which jointly revises tools, skills, and execution code based on execution feedback while keeping both model weights fixed. Across seven benchmarks spanning spatial intelligence, temporal and causal reasoning, and perceptual reasoning, CoWorld Reasoner outperforms direct reasoning with the same VLM. The strongest variant improves on all seven benchmarks, including relative accuracy gains of 11.8% on MMSI and 13.0% on ERQA, and outperforms all five evolving baselines using the same backbone across five benchmarks.
