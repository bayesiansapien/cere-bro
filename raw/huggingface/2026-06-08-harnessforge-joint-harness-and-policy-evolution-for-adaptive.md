---
source: farmer/huggingface
farmed: 2026-06-08T09:23:13Z
arxiv_id: 2606.01779
url: https://huggingface.co/papers/2606.01779
arxiv_url: https://arxiv.org/abs/2606.01779
date: 2026-06-08
---

# HarnessForge: Joint Harness and Policy Evolution for Adaptive Agent Systems

LLM agents are increasingly expected to operate across heterogeneous task regimes that require distinct execution paradigms. This challenges fixed agent systems and motivates system-level meta-adaptation beyond isolated component updates. While existing works have adapted external harness or trained underlying reasoning policies, full-system adaptation remains insufficiently characterized. The adaptation space between structure and execution is rarely made explicit, and the compatibility between the external harness and the internal reasoner is not optimized jointly. We propose HarnessForge, a meta-adaptive framework for evolving LLM agent systems. HarnessForge formulates an agent system as a harness--policy pair, defining a stable adaptation space that separates harness-level execution structure from policy-level reasoning behavior. It then performs harness--policy co-evolution through fault-guided harness tailoring and harness-conditioned policy alignment. Experiments across five benchmarks from diverse domains show that HarnessForge consistently improves both Qwen3-4B and Qwen3-8B backbones, outperforming harness-only and policy-only baselines with gains of up to 12.0\% over the strongest baseline and achieving favorable rollout-efficiency tradeoffs, demonstrating that harness--policy co-evolution is effective, and that executable compatibility between the harness and reasoning policy is essential for agent-system adaptation. The code is available at https://github.com/mingju-c/HarnessForge.
