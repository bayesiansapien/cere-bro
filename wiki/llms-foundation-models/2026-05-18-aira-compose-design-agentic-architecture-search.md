# AIRA-Compose and AIRA-Design: Agentic Discovery of Neural Architectures

**Date ingested:** 2026-05-18
**Source:** HuggingFace Daily Papers 2026-05-18
**arXiv:** [2605.15871](https://arxiv.org/abs/2605.15871)
**Tier:** 2 (architecture search, agentic systems, hybrid SSM/Transformer)
**Raw:** [raw/huggingface/2026-05-18-agentic-discovery-of-neural-architectures-...md](../../raw/huggingface/2026-05-18-agentic-discovery-of-neural-architectures-aira-compose-and-a.md)

## TL;DR

AIRA is a dual-framework approach to LLM-agent-driven neural-architecture discovery. AIRA-Compose deploys 11 agents to navigate a combinatorial design space of three primitives (Attention, MLP, Mamba) under a fixed 24-hour compute budget at million-parameter scale, then extrapolates the top designs to 350M, 1B, and 3B. AIRA-Design tasks up to 20 agents with directly writing novel attention mechanisms and training scripts. The search yields 14 novel architectures across two families, AIRAformers (Transformer-based) and AIRAhybrids (Transformer-Mamba). At 1B pre-trained under a fixed token budget, the agent-discovered top architectures outperform Llama 3.2 and Composer-found alternatives on downstream tasks (+2.4% for AIRAformer-D, +3.8% for AIRAhybrid-D). Critically, the discovered architectures sit on steeper compute-optimal scaling frontiers: AIRAformer-C scales 54% faster than Llama 3.2 and 71% faster than the best Composer Transformer; AIRAhybrid-C scales 23% faster than modified Nemotron-2 and 37% faster than the Composer baseline.

## Why it matters

The headline is not the accuracy gain. The headline is the scaling-frontier gain. A 54% faster compute-optimal scaling slope at 1B compounds across the typical 100x compute multiplier between research scale and frontier scale. If the slope generalises, a frontier-scale AIRAformer pre-train would land in the regime that today requires roughly 1.5x more compute on the Llama family.

The agentic-discovery framing is the second contribution. This is the first wiki paper where an ensemble of LLM agents writes attention mechanisms and training scripts and produces architectures that outperform hand-designed baselines at non-trivial scale. The wiki has tracked agentic data generation (FrontierSmith, 2026-05-16), agentic harness construction (Sylph AI, 2026-05-16), and agentic environment synthesis (EvoEnv, 2026-05-15). AIRA closes the loop on agentic architecture design.

## Method

**AIRA-Compose (high-level architecture search):**

- 11 agents navigate a combinatorial design space over three primitive operators: Attention, MLP, Mamba.
- The search runs under a fixed 24-hour compute budget at million-parameter scale.
- Two stages: candidate proposal at the small scale, then extrapolation of the top-performing designs to 350M, 1B, 3B.
- The output is 14 novel architectures spanning AIRAformers and AIRAhybrids.

**AIRA-Design (low-level mechanism implementation):**

- Up to 20 agents directly write attention mechanism code and training scripts.
- The mechanism is more permissive than AIRA-Compose: agents can invent operators, not just compose existing ones.

**Results at 1B pre-trained scale, fixed token budget:**

- AIRAformer-D beats Llama 3.2 by 2.4% on downstream evals.
- AIRAhybrid-D beats Llama 3.2 by 3.8% on downstream evals.
- AIRAformer-C scales 54% / 71% faster than Llama 3.2 and the best Composer-found Transformer.
- AIRAhybrid-C scales 23% / 37% faster than the modified Nemotron-2 baseline.

## Connection to prior wiki context

**Raschka's architecture survey (2026-05-17, the Gmail-starred post cataloguing four moves in the May 2026 open-model wave: Gemma 4's KV sharing plus per-layer embeddings, Laguna XS.2's layer-wise attention budgeting, ZAYA1-8B's compressed convolutional attention, DeepSeek V4's mHC multi-head compression).** Raschka catalogued what frontier labs are actually shipping. Every move in his catalog is a hand-designed efficiency play converged on by independent teams. AIRA proposes that LLM-agent search can produce similar or better architectures without the human team. If AIRAhybrid-C's 37% faster scaling slope generalises, the open-model wave's architectural diversity is empirically reachable by automated search.

**MoE-muP (2026-05-17, the first principled scaling theory for Mixture-of-Experts deriving closed-form MSSP prescriptions for initialization, learning rate, weight decay, and routing temperature across the five MoE axes).** MoE-muP gives the theoretical recipe for scaling an MoE without sweeping. AIRA-Compose does not consider MoE in the listed primitive set (Attention, MLP, Mamba), so the AIRA-MoE composition is an open extension. The natural follow-up: AIRA-Compose with MoE as a fourth primitive, scaled per MoE-muP's MSSP recipe.

**Hope architecture (2026-04-28, the nested-learning architecture paper).** Hope was the prior wiki entry for "human-designed novel architecture that beats Transformer at small scale." AIRA's hybrid family is the first wiki entry where the novel architecture beating Transformer was designed by agents, not humans.

**Multi-agent self-evolution thread (LIFE survey 2026-05-17, the 200+ paper multi-agent-systems survey organising work along Lay-Integrate-Find-Evolve stages).** AIRA-Design (20 agents writing attention code) is a Stage 4 self-evolution system applied to the substrate of architecture itself. The agents evolve the model that will eventually be them.

## Research angle

1. **Scaling-frontier slope replication.** The 54% faster scaling for AIRAformer-C is measured at 1B. Whether the slope holds at 8B and 30B is the load-bearing extrapolation question. Falsifiable in one paper: train an AIRAformer-C at 8B and 30B and check the scaling fit.
2. **AIRA + MoE primitive.** Add MoE as a fourth primitive in the AIRA-Compose design space. Compare against the wiki's existing MoE-muP scaling-frontier predictions for the same (M, Ne, K). If AIRA-discovered MoE configurations land near MSSP's prescribed (M, Ne, K), that is independent confirmation of MoE-muP. If they land far away, one of them is wrong.
3. **Agent-set ablation.** The paper uses 11 and 20 agents. Whether the same scaling-frontier slope is recoverable with 3 agents matters for cost-of-discovery economics. If yes, agentic architecture search is widely accessible. If no, only labs with significant agentic compute can run it.

## Links

- arXiv: <https://arxiv.org/abs/2605.15871>
- Related summaries: [Raschka architecture survey 2026-05-17](../inference-efficiency/2026-05-17-raschka-llm-architecture-kv-sharing-mhc-compressed-attention.md), [MoE-muP 2026-05-17](../ai-routing/2026-05-17-moe-mup-maximally-scale-stable-parameterization.md), [Hope architecture 2026-04-28](2026-04-28-hope-nested-learning-architecture.md), [LIFE survey 2026-05-17](../agentic-systems/2026-05-17-life-survey-multi-agent-collaboration-failure-self-evolution.md)
