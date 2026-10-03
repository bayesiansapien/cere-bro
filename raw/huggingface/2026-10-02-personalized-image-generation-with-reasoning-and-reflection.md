---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.821914+00:00
arxiv_id: 2610.00737
url: https://huggingface.co/papers/2610.00737
arxiv_url: https://arxiv.org/abs/2610.00737
date: 2026-10-02
---

# Personalized Image Generation with Reasoning and Reflection

Personalized image generation has remained narrowly focused on conditional synthesis from curated visual exemplars, rather than capturing who a user is. In practice, however, a user's personal context is much richer, comprising reviews, posts, images, captions, and metadata accumulated over time. A truly personalized generator should leverage this history to produce images aligned with the user's lifestyle and aesthetic preferences. To this end, we introduce the first unified benchmark for personalized image generation from user histories. The benchmark comprises two complementary tasks and a multi-axis evaluation protocol that assesses target fidelity, visual quality, user distinguishability, semantic alignment with the user's history, and task-specific utility. Grounded in real-world e-commerce and social media settings, the benchmark includes: (1) Personalized Scene Generation, which places a given object in a scene that reflects a user's preferences and lifestyle, motivated by personalized product presentation; and (2) Personalized Creative Generation, which generates a novel image on a specified topic that is faithful to a user's aesthetic and visual identity, motivated by social media content creation. We further propose PEARL, which couples a multimodal reasoner with a frozen image generator in an interleaved reason-reflect loop optimized with differential data reward. Across both tasks, PEARL outperforms strong baselines, achieving an average improvement of 15% across personalization metrics.
