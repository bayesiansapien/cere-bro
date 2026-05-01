---
source: farmer/huggingface
farmed: 2026-05-01T00:00:00Z
arxiv_id: "2604.28158"
url: https://huggingface.co/papers/2604.28158
arxiv_url: https://arxiv.org/abs/2604.28158
date: 2026-05-01
---

# Intern-Atlas: A Methodological Evolution Graph as Research Infrastructure for AI Scientists

Existing research infrastructure is fundamentally document-centric, providing citation links between papers but lacking explicit representations of methodological evolution. In particular, it does not capture the structured relationships that explain how and why research methods emerge, adapt, and build upon one another. With the rise of AI-driven research agents as a new class of consumers of scientific knowledge, this limitation becomes increasingly consequential, as such agents cannot reliably reconstruct method evolution topologies from unstructured text. We introduce Intern-Atlas, a methodological evolution graph that automatically identifies method-level entities, infers lineage relationships among methodologies, and captures the bottlenecks that drive transitions between successive innovations. Built from 1,030,314 papers spanning AI conferences, journals, and arXiv preprints, the resulting graph comprises 9,410,201 semantically typed edges, each grounded in verbatim source evidence, forming a queryable causal network of methodological development. To operationalize this structure, we further propose a self-guided temporal tree search algorithm for constructing evolution chains that trace the progression of methods over time. We evaluate the quality of the resulting graph against expert-curated ground-truth evolution chains and observe strong alignment. In addition, we demonstrate that Intern-Atlas enables downstream applications in idea evaluation and automated idea generation. We position methodological evolution graphs as a foundational data layer for the emerging automated scientific discovery.
