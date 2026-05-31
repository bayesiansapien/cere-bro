---
source: farmer/huggingface
farmed: 2026-05-31T09:25:04Z
arxiv_id: 2605.29271
url: https://huggingface.co/papers/2605.29271
arxiv_url: https://arxiv.org/abs/2605.29271
date: 2026-05-31
---

# CoHyDE: Iterative Co-Training of LLM Rewriter & Dense Encoder for Tool Retrieval

Tool retrieval over large API catalogs is a core bottleneck for LLM agents: user queries arrive in colloquial, often underspecified language, while the catalog uses technical API vocabulary that no fixed encoder can bridge on its own. The two dominant training approaches, contrastive encoder fine-tuning and HyDE-style query expansion with a frozen LLM, address this problem from opposite ends and fail in complementary directions: the fine-tuned encoder excels when the query's surface form already matches the catalog but collapses when it does not, while zero-shot HyDE is more robust to underspecified queries yet generates catalog-unaware hypothetical descriptions that degrade retrieval when queries are well-formed. We introduce CoHyDE, an iterative procedure that trains the dense encoder and the LLM rewriter as a single co-evolving system: the encoder is retrained with InfoNCE on catalog-style hypothetical descriptions produced by the rewriter, and the rewriter is preference-aligned via DPO against the encoder's retrieval scores, with both sides warm-started on the tool catalog before the loop begins. On a ~10k tool subset of the ToolBench catalog, three rounds of CoHyDE improve over the strongest single-component baseline by +2.5 pp NDCG@5 on standard queries and +6.3 pp on held-out vague queries, with gains as large as +8 pp on the hardest vague tier. Ablations confirm that co-training is the key ingredient: using either component in isolation fails to match CoHyDE on both well-formed and vague queries, with losses of up to -8 pp on vague queries.
