---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.994394+05:30
arxiv_id: 2610.33624
url: https://huggingface.co/papers/2610.33624
arxiv_url: https://arxiv.org/abs/2610.33624
date: 2026-10-28
---

# RSI Arena: Towards Recursive Self-Improvement with Human Feedback

Can AI agents autonomously train useful language models and improve them using feedback from users? We introduce RSI Arena, a two-stage study of autonomous post-training as a step toward recursive self-improvement. Ten frontier models act as training agents, each starting from NVIDIA Nemotron 3.5 Lightning 30B-A3B Base. During a six-day first stage, each agent has 1,000 GPU-hours and $300 in API credit on a shared 64-GPU cluster, independently selecting data, implementing training procedures, and choosing checkpoints. We evaluate their models on 20 benchmarks and through blind human evaluations. All ten agents produce working assistants, with the strongest model, trained by GPT-6 Astra, closing a median of 76% of the base-to-Instruct gap across 12 capability benchmarks. Its human-preference rating is also close to NVIDIA Instruct after statistical adjustment for answer length and formatting. In Stage 2, each agent receives the comparison records and votes involving its Stage 1 model and is given three additional days for further training. Using NVIDIA Instruct as a common reference across the two evaluation rounds, we observe an improvement from Stage 1 to Stage 2 in the style-adjusted relative rating of eight of the ten models. We show that benchmark gains were modest, with no clear link to preference gains, while some agents encouraged longer responses and one model showed increased harmful compliance on StrongREJECT. RSI Arena provides an auditable setting for studying how human feedback can guide autonomous model development. It takes a step toward recursive self-improvement with human feedback (RSIHF), in which people help define what improvement means for the AI systems they use.
