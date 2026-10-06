---
source: farmer/huggingface
farmed: 2026-10-06T11:30:06.338949+05:30
arxiv_id: 2609.32046
url: https://huggingface.co/papers/2609.32046
arxiv_url: https://arxiv.org/abs/2609.32046
date: 2026-10-05
---

# Receiver-Conditioned Latent Communication gives 94% CacheBack

Multi-agent systems distribute large contexts across agents that communicate to solve a task. Text messages are compact but require decoding and may omit evidence the receiving agent needs. Recent latent communication instead transfers KV caches. This avoids text generation and can improve accuracy and latency. However, a full KV cache grows linearly with both the context an individual agent processes, and the number of agents that coordinate together. This raises memory and context costs, often far exceeding available GPU resources and context window sizes. Our key observation is that agents need only send what the receiving agent requires for its local task -- which we call receiver-conditioned communication. The receiver agent passes the sender a small description of its information needs, which serves to filter and compress the sender agent's KV cache. CacheBack is a simple, robust, training-free instance of receiver conditioning based on the sender's attention weights. On FanOutQA, CacheBack with Qwen 3 removes 75% of the state the agent would otherwise receive, improving accuracy by 14.7 percentage points and reducing median task-completion latency by 3.2x relative to text communication. We show comparable improvements across model families that span dense Transformers, Mamba-attention hybrids, and sliding-window attention.
