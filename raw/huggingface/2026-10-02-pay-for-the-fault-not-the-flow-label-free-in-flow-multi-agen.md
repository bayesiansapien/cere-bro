---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.823406+00:00
arxiv_id: 2610.01017
url: https://huggingface.co/papers/2610.01017
arxiv_url: https://arxiv.org/abs/2610.01017
date: 2026-10-02
---

# Pay for the Fault, Not the Flow: Label-Free In-Flow Multi-Agent Workflow Optimization

Large language models (LLMs) increasingly construct multi-agent workflows that decompose a complex task and assign specialist agents from a pool. However, building such a workflow well remains challenging: how finely to divide the task, which agent to trust with each subtask, and when to create a new specialist are all critical decisions a workflow constructor needs to settle up front. Thus, whether each subtask succeeds remains unknown until the workflow runs. Yet, improving a workflow is costly. Locating a fault usually requires a reference answer, a graded outcome, or a trained assessor, and the fix is applied to the whole workflow through re-execution, re-search, or retraining. We propose InFlowOp, which prices every decision in one label-free cost that weighs how well an agent's competence meets what a subtask demands against how much that agent takes to run. Before execution, InFlowOp bidirectionally determines the granularity of task decomposition and agent assignment following from the cost rather than from a fixed template. During execution, InFlowOp corrects a fault with the cheapest move via the same cost that serves the workflow both as it is built and as it runs. Facing the workflow-level evaluation challenge, we introduce Braid, a benchmark whose tasks require multi-agent coordination beyond single-agent capability. Across various domains and backbones, InFlowOp outperforms single agent baselines by up to +11.97%, achieving +9.64% with in-flow optimization. Our project page: https://xhguo7.github.io/InFlowOp/.
