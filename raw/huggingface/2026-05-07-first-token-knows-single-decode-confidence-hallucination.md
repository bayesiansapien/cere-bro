---
source: farmer/huggingface
farmed: 2026-05-08T00:00:00Z
arxiv_id: "2605.05166"
url: https://huggingface.co/papers/2605.05166
arxiv_url: https://arxiv.org/abs/2605.05166
date: 2026-05-07
---

# The First Token Knows: Single-Decode Confidence for Hallucination Detection

Self-consistency detects hallucinations by generating multiple sampled answers to a question and measuring surface-form agreement, a strategy that often breaks down when answers are semantically similar but lexically different. Semantic self-consistency extends this idea by producing multiple diverse candidate answers per question and using a natural language inference (NLI) model to cluster them by meaning. This method requires repeated sampling and additional inference; a typical setup uses one greedy decode plus ten sampled generations per question, followed by NLI-based aggregation to compute semantic agreement. We show that first-token confidence (phi_first)—the normalized entropy of the top-K logits at the first content-bearing answer token of a single greedy decode—matches or modestly exceeds semantic self-consistency on closed-book short-answer factual QA at roughly 1/11 the generation cost, even before accounting for the extra NLI computation overhead. Across three 7–8B instruction-tuned models (Llama-3.1-8B, Mistral-7B-v0.3, Qwen2.5-7B) and two benchmarks (PopQA and TriviaQA, n=1000 each), phi_first achieved a mean AUROC of 0.820, compared with 0.793 for semantic agreement and 0.791 for standard surface-form self-consistency. A subsumption test shows that phi_first is moderately to strongly correlated with semantic agreement (Pearson 0.54–0.76), and a logistic ensemble of the two yields only a +0.02 AUROC improvement over phi_first alone, indicating that single-decode confidence captures most of semantic agreement's discriminative power. Partial-correlation analysis further shows that the apparent association between phi_first and answer length largely disappears after controlling for correctness. We argue that first-token confidence should be reported as a default, low-cost baseline before invoking sampling-based uncertainty estimation.
