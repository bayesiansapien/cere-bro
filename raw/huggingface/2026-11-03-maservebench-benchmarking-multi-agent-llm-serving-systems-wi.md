---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2610.40293
url: https://huggingface.co/papers/2610.40293
arxiv_url: https://arxiv.org/abs/2610.40293
date: 2026-11-03
---

# MAServeBench: Benchmarking Multi-Agent LLM Serving Systems with Hierarchical Collaboration Workloads

Large language model (LLM)-based multi-agent systems (MAS) coordinate specialized agents to solve complex tasks, turning each user request into interdependent model and tool operations. Unlike independent requests, these operations become ready at different times and consume evolving context as agents coordinate and exchange results. This creates changing patterns of concurrency, computation, and memory demand that can expose different bottlenecks in LLM serving hardware. Yet benchmarking these effects requires capturing the collaboration rules that generate serving workloads, beyond the requests observed during execution. We present MAServeBench, a benchmark that treats multi-agent collaboration as a configurable dimension of serving workloads for LLM serving and hardware evaluation. Its composable stages capture how agents coordinate and exchange context in documented MAS workflows, enabling native executions to generate different workloads even when task inputs and tools remain unchanged. Hierarchical Semantic Traces preserve realized operations and dependencies for reproducible comparisons of legal release constraints at fixed work. Task-linked measurements connect these workloads to serving execution and GPU/NPU hardware behavior, revealing why serving efficiency does not always translate into timely task completion. The benchmark code is available at https://github.com/ShengxuanQiu/MAServeBench.
