---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.16409
url: https://huggingface.co/papers/2609.16409
arxiv_url: https://arxiv.org/abs/2609.16409
date: 2026-09-30
---

# Reasoning with Image Generation

Chain-of-thought reasoning has revolutionized natural language processing by enabling large language models (LLMs) to decompose problems into intermediate steps before answering. Yet confining reasoning to the textual domain presents limitations for tasks requiring direct manipulation of visual representations. Recent efforts augment multimodal LLMs with external visual expert tools such as depth estimation or object detection modules, but these remain fundamentally limited by their reliance on narrow, rigid operations that cannot flexibly generate or transform visual content. We propose ReImaGin, which leverages image generation models as a flexible visual reasoning mechanism for multimodal LLMs: unlike fixed-function tools, they accept natural language commands and can perform open-ended visual operations, like removing an occlusion or generating a floorplan from multiple disjoint views of a room. Across six diverse visual reasoning tasks including multi-view spatial reasoning and collision prediction, ReImaGin consistently outperforms both text-only reasoning and specialist vision-tool baselines, with gains of up to 25\%, demonstrating the advantage of flexible, generative visual reasoning.
