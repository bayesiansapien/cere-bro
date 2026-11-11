---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.327364+00:00
arxiv_id: 2610.37570
url: https://huggingface.co/papers/2610.37570
arxiv_url: https://arxiv.org/abs/2610.37570
date: 2026-11-10
---

# LCM-Promo: An LLM-Based Uplift Model for Promotion Allocation

We present LCM-Promo, an LLM-based uplift model for promotion allocation. LCM-Promo is a task-specific Large Commerce Model (LCM): a finetuned LLM trained on transactional commerce data to predict user intent and promotion response. It learns monotonic promotion-response curves from production logs by interpreting single-token outputs as conversion-threshold probabilities, while conditioning on session context such as day and delivery shift. In a production A/B test on churn reactivation, LCM-Promo increased conversion by 1% and reduced promotion cost by 6% relative to the Segment-EMA production baseline.
