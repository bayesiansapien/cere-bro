---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.08299
url: https://huggingface.co/papers/2605.08299
arxiv_url: https://arxiv.org/abs/2605.08299
date: 2026-05-13
---

# Do not copy and paste! Rewriting strategies for code retrieval

Embedding-based code retrieval often suffers when encoders overfit to surface syntax. Prior work mitigates this by using LLMs to rephrase queries and corpora into a normalized style, but leaves two questions open: how much representational shift helps, and when is the per-query LLM call justified? We study a hierarchy of three rewriting strategies: stylistic rephrasing, NL-enriched PseudoCode, and full Natural-Language transcription, under joint query-corpus (QC, online) and corpus-only (C, offline) augmentation, across six CoIR benchmarks, five encoders, and three rewriters spanning independent model families (Qwen, DeepSeek, Mistral). We are the first to evaluate NL-enriched PseudoCode and snippet-level Natural Language as direct retrieval representations, rather than as transient intermediates. Full NL rewriting with QC yields the largest gains (+0.51 absolute NDCG@10 on CT-Contest for MoSE-18), while corpus-only rewriting degrades retrieval in 56 of 90 configurations, about 62%. We introduce two diagnostics, Delta H, token entropy, and Delta s, embedding cosine, and show that Delta H predicts retrieval gain under QC across all three rewriter families: pooled Spearman rho = +0.436, p < 0.001 on DeepSeek+Codestral; rho = +0.593 on Codestral alone; rho = +0.356 on Qwen. This establishes Delta H as a cheap, rewriter-agnostic proxy for deciding when rewriting pays off before running retrieval. Our analysis reframes LLM rewriting as a cost-benefit decision: it is most effective as a remediation layer for lightweight encoders on code-dominant queries, with diminishing returns for strong encoders or NL-heavy queries.
