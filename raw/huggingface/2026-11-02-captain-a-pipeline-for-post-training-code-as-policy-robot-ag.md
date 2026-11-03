---
source: farmer/huggingface
farmed: 2026-11-03T14:58:56.498476+05:30
arxiv_id: 2610.40799
url: https://huggingface.co/papers/2610.40799
arxiv_url: https://arxiv.org/abs/2610.40799
date: 2026-11-02
---

# CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents

Across coding, web, and tool-use tasks, language-model agents are now routinely trained with the same recipe: supervised fine-tuning (SFT) to learn the interface, then multi-turn reinforcement learning (RL) to master it. Code-as-policy (CaP) casts robot manipulation in the same form, as the policy writes code against robot APIs and reads back the results, so the same recipe should apply. Yet existing CaP agents sidestep training: they either prompt closed frontier models or delegate manipulation to pre-trained vision-language-action models (VLAs) and high-level skills, while small open vision-language models (VLMs) fail outright. We present CaPtain, an open post-training pipeline that turns a small open VLM into a capable CaP agent, with no VLA, frontier model, or privileged state at test time. CaPtain trains and deploys the policy inside CaPtain-Harness, which exposes low-level perception, geometry, and guarded-motion primitives across simulation and real hardware. We first align the base model via SFT on synthetic trajectories generated with GPT-6 Astra, then apply multi-turn RL. Multi-turn RL must credit tens of agent requests, whose physical effects often surface turns later, from a single end-of-episode outcome. We therefore introduce a physical critic that reads privileged simulator state, never seen by the policy, and credits each request by how much it changes the predicted chance of success. Starting from Qwen3.5-4B (0% zero-shot), CaPtain-4B reaches 55.4% held-out LIBERO success after SFT and 73.8% after RL. On LIBERO-PRO, it reaches 78.5%, surpassing several frontier-model agents, and its RL gains persist across three perturbation suites (+17.6 to +21.2 points). Without target-domain training, it attains 83.3% on SimplerEnv WidowX, exceeds frontier models on CaP-Bench, and runs on a real robot after simulation-only adaptation. We release all code, data, and model weights.
