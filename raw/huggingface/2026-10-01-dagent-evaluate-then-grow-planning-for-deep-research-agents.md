---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.352040+05:30
arxiv_id: 2609.39154
url: https://huggingface.co/papers/2609.39154
arxiv_url: https://arxiv.org/abs/2609.39154
date: 2026-10-01
---

# DAGent: Evaluate-then-Grow Planning for Deep Research Agents

Deep research tasks require agents to navigate large knowledge spaces, synthesize evidence across many sources, and adapt their plans as findings emerge. Directed acyclic graph (DAG)-based multi-agent systems suit this setting because they support parallel execution and isolate each sub-task within a focused dependency context. Yet existing DAG-based agents instantiate a task-level plan before execution and repair the graph only after failures or missing evidence are observed. This Plan-then-Patch strategy is brittle for deep research: the system commits most strongly when its evidence is weakest, and later revisions waste computation on branches that should not have been planned. We propose DAGent, a DAG-based multi-agent framework with Evaluate-then-Grow incremental planning: an Orchestrator grows the task graph one batch at a time, conditioning each expansion on confidence and uncertainty signals from completed nodes. A hierarchical context layer propagates compact QueryDocs by default while preserving full execution traces for on-demand recall. The recorded DAG topology admits structural RL signals that outcome-only recipes cannot define; DAGRPO, a GRPO adaptation, injects topology-conditioned credit on Executor rollouts and a structural compliance regularization on Orchestrator plans. Across BrowseComp-Plus, GAIA, and xbench-DeepSearch, DAGent surpasses the strongest open-source baseline by 5.3 / 5.8 / 2.0 points at the Qwen3-235B-A22B scale, and the lead replicates across four open-source backbones and extends to GPT-5 at 327K context. At the Qwen3-8B scale, DAGRPO improves over a same-budget outcome-only GRPO baseline by 3.0 average Pass@1 points. A same-architecture comparison shows that evidence-conditioned planning reaches higher accuracy at lower per-task token, tool-call, and step footprints than its Plan-then-Patch counterpart. Code: https://github.com/hanwenliu6825/DAGent
