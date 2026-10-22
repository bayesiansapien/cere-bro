---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.644108
arxiv_id: 2610.27435
url: https://huggingface.co/papers/2610.27435
arxiv_url: https://arxiv.org/abs/2610.27435
date: 2026-10-21
---

# Harness Self-Evolution for Long-Horizon Terminal Agents

Long-horizon terminal agents may solve a task in one run yet fail across repeated runs. Stochastic errors can propagate through actions and context, creating a gap between capability and reliable execution. We present RiseHarness, a framework for iteratively improving agent harnesses with model weights fixed. It focuses on flipping tasks with both successful and failed runs under the same configuration, using successful runs as references for failure analysis. RiseHarness combines agent trajectories with internal harness traces from a runtime monitor to examine how model actions interact with command execution, feedback, context management, and completion decisions. A Harness Handbook links this evidence to harness behaviors and source code, helping identify recurring problems in mechanisms shared across tasks. RiseHarness then searches other harness frameworks for relevant implementations and adapts them as design references to the current model and execution protocol. Candidate changes undergo behavioral checks and repeated task evaluation; versions with measured gains seed the next iteration. This loop integrates suitable mechanisms from different frameworks into a single harness and uses new execution evidence to guide further changes. We evaluate task success and reliability across models, ablate harness execution evidence and external research, and test transfer to unseen benchmarks with the same model. RiseHarness treats a specific model as the unit of harness adaptation, studying how changes to shared interaction mechanisms can make existing capabilities more reliable across tasks.
