---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.149386+00:00
arxiv_id: 2611.23236
url: https://huggingface.co/papers/2611.23236
arxiv_url: https://arxiv.org/abs/2611.23236
date: 2026-11-19
---

# PGPO: Prototype-Guided Progressive Obfuscation for Privacy-Preserving LLM-Enhanced Recommendation

LLM-enhanced recommender systems encode item side information into semantic embeddings, but these embeddings may leak sensitive textual attributes through inversion attacks. Existing input-side defenses rely on trusted collection or local token perturbation, often disrupting the inter-item semantic topology needed for recommendation. To address it, we introduce relational fidelity as the key objective, requiring semantic shift for privacy while preserving relative item relations for utility. Based on this principle, we propose prototype-guided progressive obfuscation (PGPO), which learns topology-aware obfuscation anchors for high-influence prototype words and propagates them through a static semantic graph. PGPO is optimized with GRPO using individual dissimilarity, structural consistency, and semantic constraint rewards. Experiments on two benchmarks show strong inversion defense with near-upper-bound recommendation performance. The code is available at https://github.com/Shengxiang-Lin/PGPO.
