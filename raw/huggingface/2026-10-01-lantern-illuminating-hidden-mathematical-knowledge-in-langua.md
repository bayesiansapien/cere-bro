---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.346164+05:30
arxiv_id: 2609.32264
url: https://huggingface.co/papers/2609.32264
arxiv_url: https://arxiv.org/abs/2609.32264
date: 2026-10-01
---

# LANTERN: Illuminating Hidden Mathematical Knowledge in Language Models

Language models can now prove theorems, but people still decide which problems to pursue. We ask whether a model's internal representations can help identify promising mathematical connections. We develop LANTERN, a fast, cost-efficient pipeline that uses a classifier over pretrained-model activations to rank candidate relations, followed by staged filtering, hypothesis generation, executable verification, and analytical checking. Applied to the On-Line Encyclopedia of Integer Sequences (OEIS), LANTERN ranked 50 million pairs among 10,000 frequently referenced sequences and produced 62 verified relations between pairs without an existing OEIS cross-reference. A content screen retained 13 relations worth presenting; nine of these are informative or insightful, including four which are entirely novel to the best of our knowledge: none appears in the OEIS or in our targeted literature search. The entire end-to-end process including classifier training, candidate ranking, filtering and verification took under 8 hours.
