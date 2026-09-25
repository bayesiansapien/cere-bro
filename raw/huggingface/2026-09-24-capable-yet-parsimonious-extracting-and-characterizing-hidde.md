---
source: farmer/huggingface
farmed: 2026-09-25T17:06:04.306887+00:00
arxiv_id: 2609.26637
url: https://huggingface.co/papers/2609.26637
arxiv_url: https://arxiv.org/abs/2609.26637
date: 2026-09-24
upvotes: 13
authors: ["Xiaoyu Luo", "Tao Ren", "Wenrui Yu", "Xiao Li", "Qiongxiu Li", "Johannes Bjerva"]
---

# Capable yet Parsimonious: Extracting and Characterizing Hidden Chain-of-Thought in Frontier Models

**Authors:** Xiaoyu Luo, Tao Ren, Wenrui Yu, Xiao Li, Qiongxiu Li, Johannes Bjerva

**Upvotes:** 13

**Links:** [HuggingFace](https://huggingface.co/papers/2609.26637) · [arXiv](https://arxiv.org/abs/2609.26637)

The rapid capability gains of frontier language models are widely attributed to improved reasoning abilities, yet this cannot be verified as raw CoT traces in closed-source systems are hidden. By registering a simple custom tool through a standard API feature, we induce frontier models to externalize intermediate reasoning. Because these traces may reflect post-hoc rationalization rather than genuine reasoning, we first evaluate against native CoT on open-source models and extend to closed-source frontier models including GPT-6 Astra. We find that the extracted reasoning matches native reasoning performance and substantially outperforms no-reasoning baselines, across competition mathematics, science, and code generation. We then characterize how frontier models structure their intermediate reasoning. Across token efficiency, reasoning-step types, and induced reasoning trees, we identify systematic differences in how models externalize, compress, and organize reasoning. We find that Astra exhibits token-efficient directed reasoning, selecting a correct trajectory earlier, while resolving elementary steps internally and externalizing only crucial reasoning. These findings provide a behavioral lens on frontier-model reasoning beyond benchmark scores.
