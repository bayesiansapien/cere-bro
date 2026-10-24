---
title: "Research shorts 2026-10-24: where 'wait' comes from, IQuest-Q1, Deep Fusion Memory, Cola2, Heartbeat Thinking, Agent Mosaic, RIDAR, OpenDS-World, PLE, EvalResearchBench"
date: 2026-10-24
sources:
  - https://arxiv.org/abs/2610.30882
  - https://arxiv.org/abs/2610.30949
  - https://arxiv.org/abs/2610.25100
  - https://arxiv.org/abs/2610.31305
  - https://arxiv.org/abs/2610.26233
  - https://arxiv.org/abs/2610.30418
  - https://arxiv.org/abs/2610.31372
  - https://arxiv.org/abs/2610.30181
  - https://arxiv.org/abs/2610.30537
  - https://arxiv.org/abs/2610.04184
raw: raw/huggingface/2026-10-23-*.md, raw/twitter/feed/2026-10-24-morning-ranked.json
tags: [reasoning, rl, moe, parametric-memory, voice-agents, safety, benchmarks]
---

# Research shorts (2026-10-24)

- **Inherited, Not Invented: where "wait" comes from (2610.30882).** RL is credited with teaching models to write "wait" before rechecking. Tracing open models' training histories, zero-RL almost never coins it: on bases without the word, RL lifts MATH-500 a lot while "wait" stays absent. The marker arrives with data (OLMo-3 mid-training, SFT on reasoning traces). RL-Zero recipes multiply it where it exists; KL-free GRPO from the same base does not, and their GRPO recipe erases a seeded marker. Marker frequency is not evidence of RL-induced reasoning, and LLM judges can reverse human-labelled trends. Relevant to every "aha moment" claim logged under [rl-for-llms](rl-for-llms.md).
- **IQuest-Q1 (2610.30949).** Open 320B-total / 15B-active MoE for agentic CLI work. Stable SplitNorm + Muon + muP pre-training with a coding-heavy second stage, progressive context extension, multi-scaffold post-training (SFT, domain RL, MOPD) and model merging across stages. Another small-active open MoE (about 4.7% active), alongside Flint (40B/2.5B) and Kimi K3.1 Pro (2.8T/104B).
- **Deep Fusion Memory (2610.25100).** A parametric memory: a causal predictor generates a chunk-level memory vector from preceding context (supervised by retrieved chunk embeddings) and fuses it into hidden states via gated cross-attention, backbone frozen, no retrieval at inference. 32x fewer retrieval queries and 2048x fewer retrieved items to build training data than token-level parametric memories; +12.71% on Mistral-7B and +11.19% on Qwen3-8B across six QA tasks. Sits next to today's Raw-RAG result: one paper says keep raw text, the other says compile it into weights; neither tests the other's setting.
- **Cola2 (2610.31305).** Hierarchical LM: dynamic semantic spans compressed into continuous latents, decoded by a block-causal masked-diffusion decoder. An unconverged checkpoint at 346B source tokens averages 60.10 on eight tasks and beats Llama-3-8B on HellaSwag and StoryCloze despite a 43x smaller reported budget. A token-efficiency claim to watch at scale.
- **Heartbeat Thinking (2610.26233).** Voice agents start reasoning and tool calls while the user is still speaking; new "thinker" invocations read the latest partial transcript without cancelling ongoing ones. +16 points tool coverage and 36.4% lower response latency on FDBench v3. Latency hidden by speculation, the same idea as speculative decoding at the agent level.
- **Agent Mosaic (2610.30418).** Agents assemble forbidden conclusions from individually allowed documents. GPT-5.6 Sol leaks composites in 7.08% of benign-query answers in simulation, worse in live harnesses; classification headers and aggregation rules still leave 32.37% unsafe across intents. Refusals can reveal the conclusion anyway.
- **RIDAR (2610.31372).** A 14-type taxonomy of research-integrity violations by autonomous research agents; a detector finds 3,964 violations in 99.7% of 300 trajectories; runtime intervention cuts remaining violations 36.8%. Pairs with the 10-23 finding that automated research wins mostly by engineering tricks.
- **OpenDS-World (2610.30181).** 200 live-web deep-search tasks with verified unique answers; the best of 12 frontier models reaches 39.0%, humans 21.1% over 1,000 attempts.
- **PLE: Physical-Engineering's Last Exam (2610.30537, Google Cloud; DAIR pick via X).** 85 billable engineering deliverables across electrical, civil, structural and mechanical work; the best agent configuration averages 50.6% at 27M tokens and 63 minutes per task under seven public harnesses.
- **EvalResearchBench (2610.04184).** Can agents design their own compact evaluators for self-improvement? The best frozen evaluators order ~75% of model pairs like the target benchmarks (ceiling 91%), and the cheapest evaluator had the highest agreement. A human-picked public sample stays a strong baseline.
- **Training Small Language Models for Transferable Tool Selection (2610.31483)** and **RouteWeaver (2610.19705)**: see [routing summary](../ai-routing/2026-10-24-routeweaver-and-small-tool-selectors.md).
