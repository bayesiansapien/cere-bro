---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.22362
url: https://huggingface.co/papers/2610.22362
arxiv_url: https://arxiv.org/abs/2610.22362
date: 2026-10-16
---

# CoDA: Co-Evolution of Data Engines and Action Policies

Generative simulation can automate robot environment construction, but physically valid environments are not necessarily useful for training. The challenge is to identify environments that address a policy's failures and supervision that helps it overcome them. We introduce CoDA, a framework in which a simulation data engine and an action policy co-evolve through a shared heterogeneous memory of environment construction, policy failures, and learning progress. The memory compiles validated diagnoses from a vision-language critic into generation programs that recreate difficulties and training programs that help the policy overcome them. We further propose Text2potential to convert these diagnoses into staged potentials for action-chunk value learning, providing dense supervision for policy updates while preserving the task's optimal policy under standard shaping assumptions. Measured learning progress guides further generation and program refinement. Across four manipulation task families, CoDA improves out-of-distribution success from 5.3% after supervised fine-tuning to 27.6%, exceeding the strongest closed-loop baseline by 9.5 percentage points with the same generation budget. On LIBERO-Pro, 15 rounds of generation and training raise success from 25% to 84% under position perturbations and from 1% to 76% under instruction perturbations.
