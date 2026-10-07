---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.05303
url: https://huggingface.co/papers/2610.05303
arxiv_url: https://arxiv.org/abs/2610.05303
date: 2026-10-06
---

# ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation of Verified Experience

A large language model (LLM) agent solves long-horizon tasks through many reasoning-action turns, with one verification signal at termination. Deployed agents face streams of related tasks, making their trajectories a natural resource for improvement. In-context adaptation agents store reflections, memories, or skills as text, so reuse depends on retrieving the right experience and on a frozen policy executing it. We study Online Agentic Test-Time Training (OaTTT), which trains the LLM's weights on its own execution trajectories during deployment. The agent executes each task once, in one pass over the stream, and the executed trajectory with its verification result is the only learning signal for weight updates that persist across tasks. Directly imitating or reinforcing the generated tokens of this single attempt destabilizes the policy. We introduce ASCENT (Agentic Self-distillation for Cross-task EvolutioN at Test-time), which instead self-distills verified experience. A stable version of the LLM, its frozen initial copy, receives the verified trajectory as privileged information and predicts next-token distributions along it with this hindsight. Distilling them into persistent LoRA fast weights updates the agent for later tasks, without an external reference solution or stronger teacher. By further removing invalid-action turns, ASCENT distills enhanced privileged experience for more efficient execution. We characterize its population target and the limits of sparse outcome selection. Across ALFWorld, WebShop, and AppWorld at varied model scales, ASCENT improves task success and interaction efficiency as experience accumulates, outperforms online adaptation methods, and transfers to held-out scenes, showing that an agent can consolidate verified experience into its weights without a separate training phase or memory retrieval. Project page: https://artificer-ai-lab.github.io/ASCENT
