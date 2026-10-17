---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.22192
url: https://huggingface.co/papers/2610.22192
arxiv_url: https://arxiv.org/abs/2610.22192
date: 2026-10-16
---

# Terminal-RSI: Recursive Self-Improving Terminal Agents via Recursive Self-Rewrite and Policy-Refine

Converting verifier outcomes into useful policy updates and partial progress into complete task resolution is crucial for terminal agents. We present Terminal-RSI, which alternates Recursive Self-Rewrite (RSR) of verified trajectories with critic-inheriting Recursive Policy-Refine (RPR). We formulate Turn-Boundary Skip-Observation GAE (TB-GAE) to retain token-specific baselines while applying decay across interaction turns. Family Dense Reward (FDR) calibrates semantic progress across task families; Success-Prioritized Reward (SPR) separates strict success from bounded partial credit. A Warm-up Critic Model, recursive critic handoff, and stage-specific learning rates coordinate the two refinement phases. The five-stage sequence from Qwen3.8-27B base model through RSR-1, RPR-1, RSR-2, and RPR-2 yields Terminal-RSI-27B: 19.84% on Terminal-Bench 4.0, 86.52% on Terminal-Bench 2.1, 16.95% on Terminal-Bench 3.0, and 79.00% on Terminal-Bench Hard. On LHTB, process reward rises from 0.21 to 0.37 and strict completion from 0/46 to 5/46; SWR100 success doubles from 3.00% to 6.00%. By recursively coupling verified trajectory rewriting with critic-inheriting policy refinement, each retained stage consolidates discovered behaviors and progressively advances the agent from partial local repairs to strict terminal verification.
