---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.307318+05:30
arxiv_id: 2610.09684
url: https://huggingface.co/papers/2610.09684
arxiv_url: https://arxiv.org/abs/2610.09684
date: 2026-10-08
---

# From Pareto to Preference: Personalized Test-Time Scaling via Amortized Agentic Policy Discovery

Test-time scaling (TTS) improves the reasoning capabilities of large language models by allocating additional inference computation. Existing approaches to improving TTS efficiency largely optimize accuracy against one resource dimension at a time, advancing either the accuracy--cost or accuracy--latency Pareto frontier. Yet user requirements are multidimensional: users may specify accuracy, latency, and inference-cost requirements jointly, and different requirements can favor different controllers. We formulate Personalized Test-Time Scaling as discovering executable controllers that maximize the joint satisfaction rate of user-specific requirements. To reduce the overhead of repeated policy discovery for new user profiles, we propose PersonTTS, an amortized agentic policy-discovery framework that reuses prior search experience through requirement-matched controller initialization and source-distilled procedural guidance, while retaining target-profile evaluation for every candidate. Experiments on AIME and HMMT show that PersonTTS substantially outperforms strong TTS baselines in joint requirement satisfaction on unseen user profiles and held-out problems. Under the same candidate-evaluation budget, cross-user experience reuse further improves policy quality while substantially reducing discovery-agent time and cost.
