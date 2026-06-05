# EvoDS: Self-Evolving Autonomous Data Science Agent with Skill Learning and Context Management

**TL;DR.** EvoDS is a self-evolving data-science agent that fixes two limits of prior systems: static action sets and unprincipled long-horizon context handling. It adds **Autonomous Skill Acquisition** (synthesize, validate, and reuse executable skills) and **Adaptive Context Compression** (treat context management as a learned control problem, not passive truncation), orchestrated in a two-stage multi-agent training scheme via agentic RL. It proves the hierarchical design reduces tool-selection error and that its objective aligns with an information-bottleneck principle. Empirically it beats open-source data-science agents by 28.9% average across four benchmarks while eliminating out-of-token failures.

**Source:** HuggingFace Daily Papers (upvotes: 2)
**arxiv:** [2606.03841](https://arxiv.org/abs/2606.03841) · **Code:** https://github.com/usail-hkust/EvoDS
**Raw:** [raw/huggingface/2026-06-05-evods-self-evolving-autonomous-data-science-agent-with-skill.md](../../raw/huggingface/2026-06-05-evods-self-evolving-autonomous-data-science-agent-with-skill.md)

## Key points

- **Autonomous Skill Acquisition (ASA):** the agent synthesizes, validates, and reuses executable skills, replacing a fixed action set with a growing one.
- **Adaptive Context Compression (ACC):** context management is a *learned control problem* rather than passive truncation, the same "learn the memory instead of scheduling it" instinct as [Echo-Infinity (06-04)](../inference-efficiency/2026-06-04-echo-infinity-evolving-memory-video.md) and [MemTrain (06-04)](2026-06-04-memtrain-self-supervised-context-memory.md), here applied to a data-science agent.
- **Theory:** hierarchical design provably reduces tool-selection error; the optimization objective aligns with an information-bottleneck principle (compress context while preserving task-relevant information).
- **Results:** +28.9% average over SOTA open data-science agents across four benchmarks; eliminates out-of-token failures.

## Relation to prior wiki

Part of today's self-evolving-agents cluster ([Continual Experience Internalization](2026-06-05-continual-experience-internalization.md) is the keystone). EvoDS learns *skills* via RL; the keystone paper's finding that on-policy internalization is less stable than off-policy is the caution to read alongside EvoDS's agentic-RL skill acquisition. Its learned context compression is the agent-memory analogue of the learned-memory trend the wiki logged in video (Echo-Infinity) and self-supervised memory (MemTrain). DataCOPE (also today, unsupervised verifier-guided skill discovery for data analysis, +32.3% on reasoning-style tasks) is the sibling result on the same task family.

## Related pages
- [2026-06-05-continual-experience-internalization.md](2026-06-05-continual-experience-internalization.md)
- [tool-calling.md](tool-calling.md)
- [agent-memory.md](agent-memory.md)
