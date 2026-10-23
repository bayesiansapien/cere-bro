---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.191508+00:00
arxiv_id: 2610.19376
url: https://huggingface.co/papers/2610.19376
arxiv_url: https://arxiv.org/abs/2610.19376
date: 2026-10-22
---

# DeLoop: Repeated Actions as Self-Supervision for Long-Horizon Agents

Language-model agents that run long tasks often redo work they have already done: they re-issue a tool call they made earlier and get back exactly the same observation, a step that adds no new information. We identify this failure as a loop. Loops appear natively in Qwen, Llama, and Gemini agents and become far more common once the agent's history is compressed to fit its context window. To reduce these loops, we propose DeLoop, a self-supervised training method. DeLoop builds on a simple observation: the agent's own rollout can provide the supervision needed to learn from its loops. We use a looping action as a negative example and the first later non-looping action in the same rollout as a positive example. DeLoop learns from these pairs through direct preference optimization and does not require task rewards, gold answers, or LLM judges. On CodeGym under compression, DeLoop reduces the share of Qwen3-8B tasks containing loops from 57.3% to 6.1%. It also uses about one third as many steps per task, with similar task success. On Qwen3-32B, DeLoop reduces loops and steps while raising task success from 37.7% to 44.8%.
