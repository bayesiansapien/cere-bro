---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.34467
url: https://huggingface.co/papers/2610.34467
arxiv_url: https://arxiv.org/abs/2610.34467
date: 2026-10-27
---

# DynaFlow: Learning Free-Form Multi-Agent Orchestration

Multi-agent systems often rely on predefined collaboration structures, limiting their ability to adapt to diverse task requirements. We introduce DynaFlow, a framework that integrates free-form executable workflow synthesis into the action space of the main agent. The agent decides when collaboration is needed and generates task-specific programs that coordinate sub-agents through sequential or parallel execution, structured information exchange, and verification. Execution results and traces inform subsequent actions, enabling the agent to adapt collaboration as reasoning progresses. We train only the main agent through supervised fine-tuning on distilled trajectories, followed by refinement on examples filtered for unsupported premises, biased verification, and information-flow defects. All sub-agents remain fixed, separating orchestration learning from executor capability improvement. Across six benchmarks spanning mathematical reasoning, scientific question answering, and multi-hop retrieval, DynaFlow achieves 88.08% overall accuracy in Forced mode, outperforming the strongest evaluated baseline by 10.90 percentage points with the same Qwen3.5-27B backbone. Workflow analysis finds more explicit use, verification, and refinement of upstream outputs after training, highlighting cross-stage information flow as a key dimension of multi-agent orchestration.
