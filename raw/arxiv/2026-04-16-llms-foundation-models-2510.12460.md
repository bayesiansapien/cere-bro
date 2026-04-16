---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2510.12460
category: cs.CL
concept: llms-foundation-models
url: https://arxiv.org/abs/2510.12460
published: 2026-04-16
authors: Linfeng Gao, Qinggang Zhang, Baolong Bi
---

# Beyond Black-Box Interventions: Latent Probing for Faithful Retrieval-Augmented Generation

**arXiv:** https://arxiv.org/abs/2510.12460
**Authors:** Linfeng Gao, Qinggang Zhang, Baolong Bi

## Abstract

arXiv:2510.12460v3 Announce Type: replace  Abstract: Retrieval-Augmented Generation (RAG) systems often fail to maintain contextual faithfulness, generating responses that conflict with the provided context or fail to fully leverage the provided evidence. Existing methods attempt to improve faithfulness through external interventions, such as specialized prompting, decoding-based calibration, or preference optimization. However, since these approaches treat the LLM as a black box, they lack a reliable mechanism to assess when and why knowledge conflicts occur. Consequently, they tend to be brittle, data-intensive, and agnostic to the model's internal reasoning process. In this paper, we move beyond black-box interventions to analyze the model's internal reasoning process. We discover that conflicting and aligned knowledge states are linearly separable in the model's latent space, and contextual noise systematically increases the entropy of these representations. Based on these findings, we propose ProbeRAG, a novel framework for faithful RAG that operates in three stages: (i) fine-grained knowledge pruning to filter irrelevant context, (ii) latent conflict probing to identify hard conflicts in the model's latent space, and (iii) conflict-aware attention to modulate attention heads toward faithful context integration. Extensive experiments demonstrate that ProbeRAG substantially improves both accuracy and contextual faithfulness. The related resources are available at https://github.com/LinfengGao/ProbeRAG.
