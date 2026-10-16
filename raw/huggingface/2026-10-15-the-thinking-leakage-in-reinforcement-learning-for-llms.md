---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.225203+05:30
arxiv_id: 2610.14270
url: https://huggingface.co/papers/2610.14270
arxiv_url: https://arxiv.org/abs/2610.14270
date: 2026-10-15
---

# The Thinking Leakage in Reinforcement Learning for LLMs

Hybrid reasoning models such as the Qwen3 series switch between a THINK mode and a NO-THINK mode through a few chat-template tokens. A popular recipe trains such models with reinforcement learning in NO-THINK mode and reports improved reasoning performance. We provide evidence that much of this gain can be explained by thinking leakage: the gain comes largely from partially reactivating the reasoning abilities of the original model's THINK mode instead of learning enhanced reasoning behavior. We train Qwen3-1.7B, 4B, and 8B with GRPO in NO-THINK mode. As accuracy improves, responses become longer and more reflective, are increasingly judged by the original model to resemble its own thinking, and the model's internal activations shift toward its THINK mode. We then investigate at the level of weights, activations, and attention heads: scaling the RL update further elicits THINK-mode behavior and approaches THINK-mode accuracy but does not exceed it; in Qwen3-8B, replacing a low-dimensional THINK-related activation subspace of the RL-trained model with its original-model value removes most of the RL gain, and the reverse exchange transfers a considerable fraction of the gain to the original model; and the RL-induced shift passes through the attention heads that read the empty think block. We further identify a possible mechanism in the GRPO training signal: responses favored by the advantage-weighted update are more THINK-like, and a gradient step computed from this signal moves the model toward its THINK state. Thus, gains in NO-THINK mode can largely reflect reactivation of reasoning abilities already present in the original model.
