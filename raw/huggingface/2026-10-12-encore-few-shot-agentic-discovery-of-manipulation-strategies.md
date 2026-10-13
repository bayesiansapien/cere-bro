---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.225799+05:30
arxiv_id: 2609.37359
url: https://huggingface.co/papers/2609.37359
arxiv_url: https://arxiv.org/abs/2609.37359
date: 2026-10-12
---

# Encore: Few-Shot Agentic Discovery of Manipulation Strategies

Coding agents can now write, run, and debug programs with little human help. Robot tasks, however, are usually specified by a sentence that leaves out how to grasp, in what order to make contact, and what the result should look like, and an agent given only the sentence must find these details by trial and error. We introduce ENCORE, which gives the agent a few demonstrations as evidence to read rather than as training data. A deterministic builder distills each demonstration into a pack of multi-view keyframes, gripper events, frame strips, and the full trajectory. A coding agent studies the pack, writes a policy program against a fixed perception and action API, refines it iteratively over a few development rollouts, and freezes it before a sealed evaluation that never reveals the success signal. On LIBERO-PRO, the agent's first program already succeeds in half of the perturbed tasks with demonstrations and in one task without them, and the frozen programs outperform the strongest prior agentic system run with the same language model (96.3% against 89.3%). On RoboDojo tasks whose instructions leave the goal unstated, no program succeeds without demonstrations. ENCORE also runs on a real bimanual robot, learning cube handover and cup inversion from five demonstrations each.
