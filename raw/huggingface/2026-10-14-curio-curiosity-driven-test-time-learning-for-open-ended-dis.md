---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.513410+00:00
arxiv_id: 2610.04851
url: https://huggingface.co/papers/2610.04851
arxiv_url: https://arxiv.org/abs/2610.04851
date: 2026-10-14
---

# CURIO: Curiosity-Driven Test-Time Learning for Open-Ended Discovery

Open-ended discovery requires learning from repeated attempts while continuing to explore directions whose value is not yet apparent. Search with a frozen large language model (LLM) can reuse previous solutions in context, but cannot update the model from its successes and failures on the test problem. Reinforcement learning (RL) enables such adaptation; however, strongly favoring high-reward trajectories may suppress low-reward yet potentially promising directions too early. We introduce CURIO, a curiosity-driven test-time learning framework that complements task feedback with an Intrinsic Curiosity World Model (ICWM). The ICWM learns transitions in the policy's hidden-state representation and supplies prediction-error bonuses at sampled tokens outside the policy's top-k choices. Epoch normalization and an annealed weight regulate their contribution to the policy update. On six mathematical discovery tasks and single-cell denoising with Qwen3 backbones from 8B to 235B, three-run means improve over a matched task-only RL control on five mathematical objectives, match the best reported performance on Circle Packing, and improve denoising Score and mean squared error (MSE) on both held-out corpora at every tested scale. Relative gains reach 18.3% on Hadamard and 10.8% on denoising Score. Code-diversity measurements show greater structural variation among generated programs, supporting curiosity as a complementary exploration signal for learning in open-ended discovery.
