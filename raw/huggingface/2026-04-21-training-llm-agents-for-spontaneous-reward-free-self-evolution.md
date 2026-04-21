---
source: farmer/huggingface
farmed: 2026-04-21T00:00:00Z
arxiv_id: "2604.18131"
url: https://huggingface.co/papers/2604.18131
arxiv_url: https://arxiv.org/abs/2604.18131
date: 2026-04-21
---

# Training LLM Agents for Spontaneous, Reward-Free Self-Evolution via World Knowledge Exploration

Most agents today "self-evolve" by following rewards and rules defined by humans. However, this process remains fundamentally dependent on external supervision; without human guidance, the evolution stops. In this work, we train agents to possess an intrinsic meta-evolution capability to spontaneously learn about unseen environments prior to task execution. To instill this ability, we design an outcome-based reward mechanism that measures how much an agent's self-generated world knowledge improves its success rate on downstream tasks. This reward signal is used exclusively during the training phase to teach the model how to explore and summarize effectively. At inference time, the agent requires no external rewards or human instructions. It spontaneously performs native self-evolution to adapt to unknown environments using its internal parameters. When applied to Qwen3-30B and Seed-OSS-36B, this shift to native evolution yields a 20% performance increase on WebVoyager and WebWalker. Most strikingly, the generated world knowledge even enables a compact 14B Qwen3 model to outperform the unassisted Gemini-2.5-Flash, establishing a new paradigm for truly evolving agents.

**Authors:** Tencent; The Hong Kong University of Science and Technology (Guangzhou) (equal contribution, project lead noted)
