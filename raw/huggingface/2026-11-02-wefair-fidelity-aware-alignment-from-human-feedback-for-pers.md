---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.496812+05:30
arxiv_id: 2610.16927
url: https://huggingface.co/papers/2610.16927
arxiv_url: https://arxiv.org/abs/2610.16927
date: 2026-11-02
---

# WeFair: Fidelity-Aware Alignment from Human Feedback for Personalized Query Rewriting in Short-Video Search

Short-video search needs compact query rewriters that recover users' personalized intent from ambiguous queries under strict latency constraints. Existing LLM-based methods have improved rewriting by using synthetic reasoning and subsequent consumption-behavioral feedback. However, overemphasizing subsequent consumption can favor engaging content over the user's immediate need, causing intent drift even when rewritten queries are grounded in behavioral history. We propose WeFair, Fidelity-Aware Alignment from Human Feedback for Personalized Query Rewriting in WeChat short-video search. WeFair uses human feedback according to how directly it reflects personalized intent, assigning feedback fidelity to a progression from demonstration to preference to verification. We first mine actual queries and user reformulations from search sessions, and then screen them for contextual support. In the demonstration stage, a supervised fine-tuning curriculum progresses from large-scale context-to-query learning to reasoning and direct prediction on human reformulation and preservation. In the preference stage, direct preference optimization learns relative preferences from subsequent consumption feedback. In the verification stage, group relative policy optimization rewards exact agreement with reformulation or preservation targets to constrain intent drift. Further analysis shows that broad supervision benefits the full curriculum supervised training, while strict verification achieves better performance than auxiliary rewards. In offline experiments, WeFair-2B outperforms strong rewriting baselines in overall accuracy and intent preservation. An online A/B test shows relative increases of 2.593% in effective video-view rate and a 2.350% relative reduction in query reformulation rate. WeFair-2B has been deployed in the WeChat short-video search system, which serves over 100 million queries per day.
