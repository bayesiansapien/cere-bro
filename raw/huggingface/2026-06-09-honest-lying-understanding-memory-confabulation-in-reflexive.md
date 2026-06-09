---
source: farmer/huggingface
farmed: 2026-06-09T16:28:21
arxiv_id: 2605.29463
url: https://huggingface.co/papers/2605.29463
arxiv_url: https://arxiv.org/abs/2605.29463
date: 2026-06-09
---

# Honest Lying: Understanding Memory Confabulation in Reflexive Agents

Reflexion-style agents rely on self-generated reflections as memory, implicitly assuming that agents can accurately diagnose their own failures. We show that this assumption can fail systematically: across ALFWorld and HumanEval, agents store confident but incorrect interpretations of the task and continue acting on them across trials, even though the environment resets to the correct task each time. We call this failure mode memory confabulation and introduce the Reflection Repetition Rate (RRR), a log-based metric that detects repeated reliance on incorrect reflective content. Using RRR, we identify 16 frozen environments in ALFWorld, where 0 of 121 reflections mention the correct target object, and 4 analogous cases in HumanEval. Our mitigation replaces open-ended self-diagnosis with programmatic extraction of trajectory-level failure signals, increasing correct object mention from 0% to 86%, reducing RRR from 0.64 to 0.10, and solving 3 of 16 frozen ALFWorld environments, suggesting that reflective memory can reinforce false beliefs rather than correct them.
