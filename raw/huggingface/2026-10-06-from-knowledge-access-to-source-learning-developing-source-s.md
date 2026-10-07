---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.02150
url: https://huggingface.co/papers/2610.02150
arxiv_url: https://arxiv.org/abs/2610.02150
date: 2026-10-06
---

# From Knowledge Access to Source Learning: Developing Source-Specific Competence

Large language model (LLM) agents increasingly rely on persistent external sources to solve sequences of knowledge-intensive tasks. Existing methods improve how source content is accessed and organized, while agent-memory systems preserve reusable knowledge from prior interactions, but repeated use of the same source is still largely treated as repeated access rather than an opportunity to progressively improve understanding of that source. We study source learning: developing reusable source-specific competence over a persistent authoritative source. We represent this competence with a persistent source model that captures reusable understanding of the source, including how its knowledge is structured, interpreted, and applied. To construct and progressively refine such models, we propose SourceLearn, which combines two complementary learning mechanisms. Self-Directed Source Learning identifies what remains incompletely understood and adaptively revisits the source, while Task-Guided Source Learning uses downstream experience to reveal local representational gaps and recurring needs in how source knowledge should be organized. In both cases, learning signals determine what should be reconsidered, while persistent updates are reconstructed from the authoritative source. Across five benchmarks and three LLM backends, SourceLearn achieves the best performance in 13 of 15 settings, with gains of up to 22.6 points over Hybrid RAG and substantial overall improvements over static source representations and experience-based memory baselines.
