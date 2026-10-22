---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.639017
arxiv_id: 2610.25078
url: https://huggingface.co/papers/2610.25078
arxiv_url: https://arxiv.org/abs/2610.25078
date: 2026-10-21
---

# CoEvo-RSI: When Harnesses Evolve, Which Models Should Follow?

Model--harness co-evolution has emerged as a prominent paradigm for recursive self-improving (RSI) agents, jointly evolving their execution scaffolds and intrinsic capabilities. We study the persistent yet often overlooked brain--body mismatch problem in this paradigm, where an evolving harness (body) demands behaviors its model (brain) has not learned or restricts capabilities it already possesses. We introduce CoEvo-RSI, a RSI framework that advances model--harness co-evolution through agent-driven, bidirectional historical inheritance. Drawing on a shared evolutionary archive and execution feedback, a meta-agent coordinates harness development from historical designs with model checkpoint selection or merging and subsequent adaptation under the selected harness, aligning inherited capabilities with evolving execution requirements to reduce brain--body mismatch. Using only supervised fine-tuning (SFT) on its own rejection-sampled trajectories, CoEvo-RSI makes Qwen3.5-9B competitive with larger models across diverse vertical applications, including multi-agent failure attribution, role-aware text-to-SQL, and smart-home instruction following. It surpasses DeepSeek-V4-Pro on TraceElephant (+14.16 agent accuracy) and GLM-5.3 on HomeBench VM (+4.90 success rate), underscoring the need for brain--body alignment and the potential of bidirectional historical inheritance to advance agent co-evolution.
