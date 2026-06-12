---
source: farmer/huggingface
farmed: 2026-06-12T09:05:40Z
arxiv_id: 2606.09290
url: https://huggingface.co/papers/2606.09290
arxiv_url: https://arxiv.org/abs/2606.09290
date: 2026-06-12
---

# Visual Para-Thinker++: A Single-Policy Multi-Agent Framework for Visual Reasoning

Visual reasoning requires integrating evidence distributed across regions, attributes, and relations, making single-chain reasoning prone to early perceptual commitment and hallucination. We propose Visual Para-Thinker++, a single-policy multi-agent framework in which one shared MLLM policy is instantiated as role-conditioned Main, Worker, and Summary Agents. The Main Agent decomposes the task with fixed allocation patterns; Worker Agents reason in parallel under context isolation; and the Summary Agent reconciles full Worker reasoning traces rather than majority-voting on final labels. The shared policy is trained by Multi-Agent Capability Injection and Role-Decoupled Multi-Agent Optimization, which assign role-specific rewards and advantages to corresponding token segments to reduce gradient conflict among collaborative roles. A native inference engine enables efficient multi-agent rollout through shared visual prefix and KV cache reuse. Across V*, CountBench, the RefCOCO family, and HallusionBench, Visual Para-Thinker++ consistently outperforms single-trajectory and inference-time parallel baselines, with especially strong gains on hallucination-sensitive visual reasoning.
