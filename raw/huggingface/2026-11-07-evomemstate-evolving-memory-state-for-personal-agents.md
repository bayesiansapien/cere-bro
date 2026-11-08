---
source: farmer/huggingface
farmed: 2026-11-08T17:18:50.591093+00:00
arxiv_id: 2611.03743
url: https://huggingface.co/papers/2611.03743
arxiv_url: https://arxiv.org/abs/2611.03743
date: 2026-11-07
---

# EvoMemState: Evolving Memory State for Personal Agents

Long-term memory enables large language model (LLM) agents to provide continuous personalized assistance by retaining user information across interactions. Existing systems support this process through fact extraction, organization, updating, and retrieval, but largely maintain memories as independent facts. This fact-centric paradigm may overlook how new facts update, constrain, or conflict with earlier ones, while leaving their applicability, role, and priority for the current request implicit. In this paper, we introduce EvoMemState, a state-centric framework that augments persistent facts with two complementary states: Relational States that capture how facts remain valid and relate to one another as memory evolves, and a Reasoning State that determines how these facts should be applied to the current request. Specifically, EvoMemState consists of three key components: (i) Ontology-Guided Memory State Induction extracts Persistent Facts and constructs Relational States that maintain their validity, scope, and evolving relations. (ii) RL-Based State Evolution internalizes memory-use experience into a policy through reinforcement learning to generate a request-specific Reasoning State. (iii) State-Aware Reasoning then combines the relevant facts with their Relational States and the generated Reasoning State to guide the personal agent. Extensive experiments on long-term dialogue and memory-use benchmarks demonstrate consistent improvements over existing memory systems in retrieval completeness and memory-grounded response accuracy. Our code and implementation details are available at https://github.com/XMUDeepLIT/EvoMemState.git.
