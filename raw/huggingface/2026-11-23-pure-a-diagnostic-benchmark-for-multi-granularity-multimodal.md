---
source: farmer/huggingface
farmed: 2026-11-24T05:05:48.249135+00:00
arxiv_id: 2611.22343
url: https://huggingface.co/papers/2611.22343
arxiv_url: https://arxiv.org/abs/2611.22343
date: 2026-11-23
---

# PURE: A Diagnostic Benchmark for Multi-Granularity Multimodal Identity Matching

Identity matching asks whether two records denote the same identity, yet the answer depends on the target granularity. Two records may match at the base level but not at the variant level: they share an underlying design while differing in attributes such as color or size. Final matching accuracy does not separately characterize the capabilities involved. To study this problem, we use e-commerce as a challenging real-world domain. We introduce PURE, a diagnostic benchmark for multi-granularity multimodal identity matching covering four capability dimensions: Perception, Understanding, Reasoning, and Evidence-grounded Judgment. The benchmark comprises 1,457 multiple-choice questions across 14 tasks, derived from real-world matching pairs and verified by two domain experts. Across ten recent MLLMs, overall scores range from 47.1% to 86.0%. Understanding receives the highest mean score and Judgment the lowest, with weaknesses in visual difference localization and variant-level rule judgment. Modality ablations show that models benefit from multimodal evidence but can incorrectly identify conflicts between matching records. In direct matching, most models recognize matching pairs more reliably than non-matching pairs at the base level, whereas the reverse holds at the variant level. PURE therefore reveals what aggregate matching accuracy hides: not only whether models judge a pair correctly, but where they struggle to interpret evidence and apply matching criteria.
