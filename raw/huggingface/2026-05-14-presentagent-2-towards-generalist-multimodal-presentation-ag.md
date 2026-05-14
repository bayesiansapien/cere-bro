---
source: farmer/huggingface
farmed: 2026-05-14T00:00:00
arxiv_id: 2605.11363
url: https://huggingface.co/papers/2605.11363
arxiv_url: https://arxiv.org/abs/2605.11363
date: 2026-05-14
---

# PresentAgent-2: Towards Generalist Multimodal Presentation Agents

Presentation generation is moving beyond static slide creation toward end-to-end presentation video generation with research grounding, multimodal media, and interactive delivery. We introduce PresentAgent-2, an agentic framework for generating presentation videos from user queries. Given an open-ended user query and a selected presentation mode, PresentAgent-2 first summarizes the query into a focused topic and performs deep research over presentation-friendly sources to collect multimodal resources, including relevant text, images, GIFs, and videos. It then constructs presentation slides, generates mode-specific scripts, and composes slides, audio, and dynamic media into a complete presentation video. PresentAgent-2 supports three independent presentation modes within a unified framework: Single Presentation, which generates a single-speaker narrated presentation video; Discussion, which creates a multi-speaker presentation with structured speaker roles, such as for asking guiding questions, explaining concepts, clarifying details, and summarizing key points; and Interaction, which independently supports answering audience questions grounded in the generated slides, scripts, retrieved evidence, and presentation context. To evaluate these capabilities, we build a multimodal presentation benchmark covering single presentation, discussion, and interaction scenarios, with task-specific evaluation criteria for content quality, media relevance, dynamic media use, dialogue naturalness, and interaction grounding. Overall, PresentAgent-2 extends presentation generation from document-dependent slide creation to query-driven, research-grounded multimodal video generation.
