---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.362025+05:30
arxiv_id: 2610.40753
url: https://huggingface.co/papers/2610.40753
arxiv_url: https://arxiv.org/abs/2610.40753
date: 2026-11-04
---

# "Shall We Approve?" Consequence-Aware Approval for Autonomous Coding Agents

Coding agents increasingly rely on automated approvers to decide whether a proposed shell command may run. Existing approvers, from rule-based checkers to guardrail models and deployed permission classifiers, base their decisions on the text of the request and command. Yet a command's behavior depends on the code it invokes and the state of the workspace, and systems that observe file changes leave the assessment to the agent or a human after execution. We present Caper, a consequence-aware approval mechanism that pre-executes each command in a snapshotted sandbox, provides an independent approver with a bounded report of its observed effects, commits allowed commands, and rolls back blocked ones with a reason the agent can act on. Compared with six existing systems, Caper achieves the lowest harmful-outcome rate on SABER (6.7% versus at least 14.8%) and YoloFS-Ext, a benchmark we build in which harmful behavior is hidden inside invoked tools (7.8% versus at least 35.3%), while blocking 1.0% of the safe twins of the dangerous tasks in YoloFS-Ext.
