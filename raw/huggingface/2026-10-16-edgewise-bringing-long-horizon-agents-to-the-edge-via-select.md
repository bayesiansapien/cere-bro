---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.17560
url: https://huggingface.co/papers/2610.17560
arxiv_url: https://arxiv.org/abs/2610.17560
date: 2026-10-16
---

# EdgeWise: Bringing Long-Horizon Agents to the Edge via Selective Cloud Delegation

Complex and long-horizon agent tasks often rely on frontier models deployed in the cloud to achieve strong performance. However, using these models for every step of a long-horizon trajectory incurs substantial inference cost, even though not all steps may require the same level of model capability. In this paper, we find that allocating the LLM to only a small subset of key steps can achieve performance comparable to full LLM execution while significantly reducing inference cost. Motivated by this observation, we propose EdgeWise, an edge-cloud collaboration framework that deploys an SLM on the local device as the primary solver and selectively delegates critical steps to a cloud LLM when stronger model capacity is needed. To enable autonomous delegation without additional models at inference time, we introduce a step-level RL method that jointly optimizes task solving and delegation, with fine-grained credit assignment for individual delegation decisions. We also introduce an external judge-based delegation strategy and use it to systematically investigate key design choices in edge-cloud collaboration, including when to delegate, how delegation decisions should be made, what context should be shared, and how frequently the cloud LLM should be invoked. Experiments show that EdgeWise matches or outperforms pure-LLM execution while reducing inference cost up to 62% on SWE-Rebench and 34% on Terminal-Bench 2.1. We further deploy EdgeWise on a local workstation, demonstrating comparable cost savings in a practical edge-cloud setting.
