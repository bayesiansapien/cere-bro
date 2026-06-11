---
source: farmer/huggingface
farmed: 2026-06-11T08:27:36Z
arxiv_id: 2606.12195
url: https://huggingface.co/papers/2606.12195
arxiv_url: https://arxiv.org/abs/2606.12195
date: 2026-06-11
---

# InternVideo3: Agentify Foundation Models with Multimodal Contextual Reasoning

Recent progress in foundation models has shifted toward agentic behavior involving multi-step reasoning and tool use. However, open-source efforts largely focus on text-dominant settings, leaving long-horizon multimodal tasks underexplored. This gap is evident in video tasks requiring sustained temporal understanding and iterative interaction. We present InternVideo3, a framework enhancing these capabilities via Multimodal Contextual Reasoning (MCR). MCR treats understanding as a closed-loop process over a shared, evolving context containing observations, instructions, reasoning, tool actions, and memory. This frames long-video understanding as evidence accumulation and verification. To ensure efficiency, we introduce Multimodal Multi-head Latent Attention (M^2LA), a token-preserving reparameterization compressing KV-cache states while retaining the full token stream. Our staged training includes continued pretraining, short-to-long supervised fine-tuning, rule-based reinforcement learning, and on-policy distillation. Experiments show InternVideo3 achieves strong performance on benchmarks like Video-MME, MLVU, and EgoSchema. We further instantiate the model as a video agent with retrieval tools, demonstrating robust evidence-grounded behavior. Our results suggest that efficient context handling and closed-loop reasoning are vital for adapting open multimodal models toward long-horizon visually grounded agency.
