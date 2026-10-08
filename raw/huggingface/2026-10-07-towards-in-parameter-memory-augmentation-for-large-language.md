---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.08630
url: https://huggingface.co/papers/2610.08630
arxiv_url: https://arxiv.org/abs/2610.08630
date: 2026-10-07
---

# Towards In-Parameter Memory Augmentation for Large Language Models

Recently Large Language Models (LLMs) and LLM-based agents increasingly need to incorporate knowledge acquired after pretraining, e.g., domain facts, user preferences, documents, and interaction experience. In-context learning (ICL) and ICL-based agent harness remain flexible, but they consume context capacity and incur repeated discretized encoding cost that grows with context length. In-parameter memory offers a complementary substrate: reusable memory information is represented in model parameters, adapters, or other parameter-like objects that are composed into the forward pass at inference time. This survey focuses on methods that augment LLMs with such parametric memory at deployment: a memory-bearing parameter object is plugged into the forward pass during inference, whether it is acquired before or during deployment. We organize the landscape with two orthogonal axes: Parameter Placement, which includes Embedding, Attention, FFN layers, or Hybrid when two or more layers are used; and Parameter Acquisition Time, which distinguishes methods whose memory object is acquired during deployment (online) from those acquired before it (offline). We clarify boundaries, conduct comparisons, and discuss open directions in interference, safety, co-design with ICL, and recursive self-improvement.
