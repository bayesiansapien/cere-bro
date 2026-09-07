---
source: farmer/huggingface
farmed: 2026-09-07T09:18:04.961411
arxiv_id: 2609.04523
url: https://huggingface.co/papers/2609.04523
arxiv_url: https://arxiv.org/abs/2609.04523
date: 2026-09-07
---

# MaxKernel: Agentic Kernel Generation for TPUs

Designing and authoring high-performance custom kernels for accelerators is a complex task that requires deep hardware-level expertise. Large Language Models (LLM) can be leveraged together with real-time compiler feedback to build agentic systems for kernel generation. In this work, we present MaxKernel, a multi-agent system that implements three distinct paradigms for TPU kernel development: (1) a Human-in-the-Loop (HITL) agent for collaborative, step-by-step design; (2) an Autonomous (Auto) agent that executes a fully automated, metric/trace-driven optimization loop; and (3) a Graph-Based Autonomous Search that scales the Auto agent for global exploration of the design space. All three paradigms leverage a shared pool of specialized sub-agents to handle planning, implementation, self-debugging, testing, and hardware profiling. We evaluate MaxKernel on JaxBench, a comprehensive suite of 50 diverse kernel tasks for TPUs, alongside complex, real-world workloads from state-of-the-art open-source models. We demonstrate that MaxKernel consistently generates highly optimized implementations, matching expert hand-tuned baselines and delivering significant performance across the benchmark. Our agent is open-sourced and available https://github.com/AI-Hypercomputer/accelerator-agents/tree/main/MaxKernel.
