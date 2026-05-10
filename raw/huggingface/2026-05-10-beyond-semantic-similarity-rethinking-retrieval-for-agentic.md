---
source: farmer/huggingface
farmed: 2026-05-10T03:37:12Z
arxiv_id: 2605.05242
url: https://huggingface.co/papers/2605.05242
arxiv_url: https://arxiv.org/abs/2605.05242
date: 2026-05-10
---

# Beyond Semantic Similarity: Rethinking Retrieval for Agentic Search via Direct Corpus Interaction

Modern retrieval systems, whether lexical or semantic, expose a corpus through a fixed similarity interface that compresses access into a single top-k retrieval step before reasoning. This abstraction is efficient, but for agentic search, it becomes a bottleneck: exact lexical constraints, sparse clue conjunctions, local context checks, and multi-step hypothesis refinement are difficult to implement by calling a conventional off-the-shelf retriever, and evidence filtered out early cannot be recovered by stronger downstream reasoning. We study direct corpus interaction (DCI), where an agent searches the raw corpus directly with general-purpose terminal tools (e.g., grep, file reads, shell commands, lightweight scripts), without any embedding model, vector index, or retrieval API. Across IR benchmarks and end-to-end agentic search tasks, this simple setup substantially outperforms strong sparse, dense, and reranking baselines.
