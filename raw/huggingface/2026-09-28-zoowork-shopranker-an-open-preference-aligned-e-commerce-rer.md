---
source: farmer/huggingface
farmed: 2026-09-29T05:05:53.600862+00:00
arxiv_id: 2609.31002
url: https://huggingface.co/papers/2609.31002
arxiv_url: https://arxiv.org/abs/2609.31002
date: 2026-09-28
---

# ZooWork-ShopRanker: An Open, Preference-Aligned E-Commerce Reranker

Open rerankers trained for general web retrieval transfer imperfectly to e-commerce, where ranking decisions depend not only on topical relevance but also on user preferences, product constraints, and comparative product fit. These preference signals are difficult to supervise at scale: real search traffic provides authentic queries and candidates but no clean pairwise labels. We present ZooWork-ShopRanker, a family of e-commerce rerankers (0.6B, 4B, and 8B) aligned to judge-labeled shopping preference. Training pairs are labeled by a panel of reasoning large language models (LLMs) from different families acting as a preference oracle, with position-debiased judgments and agreement tiers, and the rerankers are trained on these labels. The aligned 8B flagship then serves as a distillation teacher for the efficient 4B and 0.6B models, which are fit to its scores and sharpened on judged pairs. To measure progress, we introduce ShopRank-Bench, a contamination-limited benchmark of ~10,000 private-traffic preference pairs in both text formats, tiered by how many judge families committed to each label. ZooWork-ShopRanker-8B and -4B significantly outperform the strongest open reranker baseline, every model significantly beats its own un-aligned base, and ZooWork-ShopRanker-0.6B beats its size peer; the gains hold in both formats and extend to common MTEB benchmarks. We release the models and the dual-format ShopRank-Bench to facilitate further research.
