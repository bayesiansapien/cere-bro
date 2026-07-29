---
source: farmer/huggingface
farmed: 2026-07-29T08:14:21.288961+00:00
arxiv_id: 2607.24223
url: https://huggingface.co/papers/2607.24223
arxiv_url: https://arxiv.org/abs/2607.24223
date: 2026-07-29
---

# A New Role for Relevance: Guiding Corpus Interaction in Agentic Search

Relevance is a query-dependent estimate of whether a document or excerpt contains useful evidence. Existing retrieval agents use relevance to select top-k content, but document relevance alone cannot localize, compose, or verify the evidence required by complex questions. Direct Corpus Interaction (DCI) enables such fine-grained operations through grep-style exploration, but its relevance-agnostic search can expose useful clues late and delay convergence. Recent advances use relevance to narrow the corpus into a working space for interaction. Once interaction begins, however, relevance still does not directly guide which documents grep searches first or distinguish informative excerpts from a broad set of matches to let LLMs see them first. We introduce the Relevance-Aware RipGrep Search Agent (RARG), which turns relevance into an execution prior for corpus interaction. RARG provides coarse-to-fine relevance guidance: it orders documents for sequential 'ripgrep' traversal to expose globally relevant clues earlier, initializes promising entry points with query-relevant paragraphs, and reranks grep matches to surface informative excerpts that document-level ranking may otherwise obscure. Across challenging browse question answering and reasoning-intensive retrieval, RARG improves the accuracy--efficiency frontier over retrieval-based and direct-interaction agents. These results demonstrate that relevance-aware interaction enables faster and more reliable search convergence.
