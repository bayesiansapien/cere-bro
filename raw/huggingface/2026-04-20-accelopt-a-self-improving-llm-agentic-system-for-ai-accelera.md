---
source: farmer/huggingface
farmed: 2026-04-20T00:00:00
arxiv_id: 2511.15915
url: https://huggingface.co/papers/2511.15915
arxiv_url: https://arxiv.org/abs/2511.15915
date: 2026-04-20
---

# AccelOpt: A Self-Improving LLM Agentic System for AI Accelerator Kernel Optimization

We present AccelOpt, a self-improving large language model (LLM) agentic system that autonomously optimizes kernels for emerging AI accelerators, eliminating the need for expert-provided hardware-specific optimization knowledge. AccelOpt explores the kernel optimization space through iterative generation, informed by an optimization memory that curates experiences and insights from previously encountered slow-fast kernel pairs. We build NKIBench, a new benchmark suite of AWS Trainium accelerator kernels with varying complexity extracted from real-world LLM workloads to evaluate the effectiveness of AccelOpt. Our evaluation confirms that AccelOpt's capability improves over iterations, boosting the average percentage of peak throughput from 49% to 61% on Trainium 1 and from 45% to 59% on Trainium 2 for NKIBench kernels. Moreover, AccelOpt is highly cost-effective: using open-source models, it matches the kernel improvements of Claude Sonnet 4 while being 26x cheaper. The code is open-sourced at https://github.com/zhang677/AccelOpt.
