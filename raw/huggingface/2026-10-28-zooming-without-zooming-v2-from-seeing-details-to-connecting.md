---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.994314+05:30
arxiv_id: 2610.37037
url: https://huggingface.co/papers/2610.37037
arxiv_url: https://arxiv.org/abs/2610.37037
date: 2026-10-28
---

# Zooming without Zooming v2: From Seeing Details to Connecting Evidence for Generalizable Multimodal Perception

Multimodal perception forms the foundation of multimodal intelligence. In particular, spatial perception and multimodal long-context understanding are two pivotal tasks that underpin embodied AI and multimodal agents. However, synthesizing targeted, high-quality training data for these tasks remains difficult and costly. Our key insight is that these tasks share an underlying capability, which we call connecting evidence: identifying relevant visual facts, binding them to the correct entities, recovering their relations, and composing them into an answer. Crucially, targeted training data are far easier to synthesize for this capability than for these tasks themselves. To strengthen this capability, we propose EvidenceConnect, an easy-to-implement data synthesis framework that uses zoomed views of related regions within a single image to generate questions requiring comparison, aggregation, or chaining of visual evidence. To ensure quality, a reference answer is retained only when independent VLMs agree on it, and region-ablation tests discard questions whose answer survives the removal of selected regions. We then train base VLMs on the resulting data with RLVR, obtaining Zooming without Zooming v2 (ZwZ2). Although the synthesized data are not tailored to any downstream benchmark, ZwZ2 improves fine-grained and spatial perception, with further gains on embodied spatial reasoning, multimodal long-context understanding, multimodal agent tasks, and general visual reasoning. These results establish EvidenceConnect as an effective framework for supervising evidence connection and suggest that strengthening this shared capability leads to more generalizable multimodal perception.
