---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2610.35219
url: https://huggingface.co/papers/2610.35219
arxiv_url: https://arxiv.org/abs/2610.35219
date: 2026-11-03
---

# Multi-Agent Relay Thinking

Existing multi-agent collaboration (MAC) methods have primarily explored a group thinking collaboration topology, where agents independently generate solutions and aggregate their outputs. In this work, we investigate an alternative relay thinking topology, where reasoning ownership is dynamically transferred across agents, allowing subsequent agents to inherit and refine an evolving reasoning trajectory. We introduce Multi-Agent Confidence-guided Relay (MACR), a framework that enables dynamical relay collaboration among agents. The key challenge is determining when reasoning should be relayed and which agent should continue the process. method addresses this challenge through confidence-guided relay triggering and a bidding mechanism that selects the next agent based on its confidence. Experiments on four benchmarks show that method outperforms the strongest single-model strategies in accuracy, e.g., +3.3% on MathVista and +3.9% on MMStar, and remains on par with multi-agent strategies while consuming 6.0x less token overhead on HallusionBench and MMStar. Further analysis demonstrates that relay collaboration enables heterogeneous agents to progressively integrate complementary insights, combining heterogeneous capabilities across reasoning stages. Our source code is available at https://github.com/67L1/MACR.
