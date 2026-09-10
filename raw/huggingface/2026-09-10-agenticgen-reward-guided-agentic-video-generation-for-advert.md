---
source: farmer/huggingface
farmed: 2026-09-10T08:36:11.637058+00:00
arxiv_id: 2609.09187
url: https://huggingface.co/papers/2609.09187
arxiv_url: https://arxiv.org/abs/2609.09187
upvotes: 2
date: 2026-09-10
---

# AgenticGen: Reward-Guided Agentic Video Generation for Advertising

Advertising video generation is not only a video synthesis task, but also a product-conditioned reasoning problem whose success is measured by online business metrics. Recent video foundation models can generate realistic clips from multimodal conditions, yet they do not optimize how a product should be transformed into an effective advertisement or how future generation should be improved from online business feedback. To close this loop, we propose AgenticGen, a reward-guided agentic framework that decomposes advertising video generation into two trainable reasoning stages, strategy selection and draft generation, thereby exposing optimization targets that online business feedback can supervise. AgenticGen learns a performance-based reward from accumulated online feedback and a complementary rubric-based reward aligned with human quality standards, then uses them to supervise policy optimization. DPO first moves the agentic policies toward online preferences, and GRPO further refines both stages with process and outcome rewards. Offline experiments validate the reward models and successive policy optimization. Online A/B experiments in the TikTok advertising system show that AgenticGen after DPO and GRPO improves CTR by 2.72%, CVR by 2.63%, and Advv by 9.61% over the SFT baseline.
