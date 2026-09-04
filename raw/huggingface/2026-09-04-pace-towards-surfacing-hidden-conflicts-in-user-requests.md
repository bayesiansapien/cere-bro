---
source: farmer/huggingface
farmed: 2026-09-04T08:38:35.484326+00:00
arxiv_id: 2609.03293
url: https://huggingface.co/papers/2609.03293
arxiv_url: https://arxiv.org/abs/2609.03293
date: 2026-09-04
---

# PACE: Towards Surfacing Hidden Conflicts in User Requests

Personalized assistants should not only comply with user requests but also assess whether those requests are appropriate given the user's current circumstances. However, prior work has primarily focused on accurately executing requests, overlooking the need for assistants to account for context and engage in conflict-based refusal. Furthermore, while existing work on conflict or safety detection relies on explicitly provided factors, real-world scenarios often involve implicit factors that must be retrieved from a knowledge base (KB). To this end, we introduce Personalized Assistants for Conflict Evaluation (PACE), a dataset for evaluating whether models can identify latent constraints, expressed as egocentric knowledge or events, that render seemingly reasonable user requests inappropriate. PACE pairs user requests grounded in well-defined personas with egocentric KB facts, requiring models to integrate contextual evidence to determine whether a request is conflicting. This implicit retrieval setting hinders the direct association between user requests and conflict-inducing knowledge, making it difficult for existing models to identify relevant user-specific facts. To address this challenge, we further propose PaceMaker, a multi-agent framework in which specialized agents coordinate across query reformulation, multi-hop graph traversal, and conflict-aware filtering to retrieve contextually decisive evidence. Experiments on PACE evaluate both evidence retrieval quality and conflict decision accuracy, showing that PaceMaker consistently outperforms existing approaches.
