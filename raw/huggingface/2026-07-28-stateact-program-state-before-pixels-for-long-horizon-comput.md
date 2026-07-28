---
source: farmer/huggingface
farmed: 2026-07-28T03:19:32Z
arxiv_id: 2607.22798
url: https://huggingface.co/papers/2607.22798
arxiv_url: https://arxiv.org/abs/2607.22798
date: 2026-07-28
---

# StateAct: Program State, before Pixels, for Long-Horizon Computer-Use Agents

Computer-use agents are usually improved by strengthening perception: better models for reading a screenshot and choosing where to click. Yet a screenshot is only a lossy rendering of the underlying program state, e.g., the files, application backends, and DOM that hold the task data. Different states can produce the same pixels, while code can inspect and modify that state directly. StateAct is a code-first, multi-agent harness built around this distinction. Its main agent works directly with program state by using code, while a dedicated GUI subagent handles screenshot-and-click interaction on the few subgoals that need it, just 28 of 108 tasks and 1.1% of main-agent steps. The same direct access to program state also supports verification: an independent finish gate double-checks the saved result for structural failures, e.g., output that is missing, unsaved, or written to the wrong path. To stay on track over hundreds of steps, the main agent hands subgoals to fresh subagents, keeping its own context focused. On OSWorld 2.0, StateAct lifts Claude Opus 4.8 from 20.6% to 26.9% on binary success, and from 54.8% to 61.6% on partial success, at ~ 9x lower cost per task than the same model driven by screenshots alone; a code-only variant with no GUI subagent reaches only 45.9% partial, below that screenshot-based baseline's 54.8%. In general, grounding action, verification, and memory in state, what we call state-grounding, shifts the main bottleneck from perception toward reasoning: failures depend more on what the agent thinks than on what it sees.
