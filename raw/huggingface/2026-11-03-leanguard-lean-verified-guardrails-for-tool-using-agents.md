---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2611.02332
url: https://huggingface.co/papers/2611.02332
arxiv_url: https://arxiv.org/abs/2611.02332
date: 2026-11-03
---

# LEANGUARD: Lean-Verified Guardrails for Tool-Using Agents

Tool-using language-model agents often execute actions that their domain policies forbid. We present LeanGuard, a runtime that checks every proposed tool call against a policy written in Lean4 before the call reaches the environment. Policies combine state predicates with scoped past-time temporal operators over the execution history, evaluation is fail-closed, and the decision procedure is proved equivalent to a LeanLTL semantics. A denied call can be corrected in two ways. With feedback, the agent receives the violated rule and a hint; with proof-guided repair, Lean metaprogramming searches for a nearby call that preserves the user's intent and proves that the policy admits it, without the model. On Tau-Bench with five Qwen models (0.8B-27B), unguarded agents execute at least 33 calls that the Lean policy forbids, while LeanGuard executes none; with feedback, task success does not change significantly. On DTap, LeanGuard reduces direct prompt-injection success from 57.9% to 5.9%, and in telecom, where benign tasks need no writes, benign success is unchanged. Feedback reduces repeated blocked calls and raises task success for four of five models over a bare denial. On replayed denials, repair proves an admissible edit for 88 of 252 denials caused by argument values, in a median of 2,ms.
