---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2611.02074
url: https://huggingface.co/papers/2611.02074
arxiv_url: https://arxiv.org/abs/2611.02074
date: 2026-11-03
---

# SWE-Trail: History-Guided Trajectory Collection for Coding Agent Training

Coding agents solve repository issues through long sequences of exploration, editing, and validation. These trajectories are increasingly used as post-training data, so how they are collected shapes what the trained model learns. A common approach is to sample multiple trajectories independently for each issue and then select or curate them. However, as more trajectories are sampled independently, later trajectories become increasingly redundant, even though earlier trajectories could guide where subsequent collection effort should be spent. A natural way to use this history is to expose it to the coding agent as advice. But training on such trajectories can make the model rely on advice that is unavailable at test time, creating a train-test mismatch. Instead, we argue that history should guide where collection effort is spent, while the coding agent decides what to generate. We introduce SWE-Trail, a trajectory collector that uses earlier trajectories to guide subsequent collection while keeping that history outside the coding agent's context. During a new rollout, SWE-Trail uses history to identify a state where additional collection effort may be useful. There, the coding agent proposes candidate next actions from its ordinary context, and SWE-Trail briefly executes them from the same checkpoint to decide which route continues. We evaluate collection approaches by training student models on the trajectories they produce. For a 124B student initialized from Ling-3.0-flash-base, SWE-Trail improves mean resolution over independent sampling by 2.33 and 1.60 percentage points on SWE-bench Multilingual and SWE-bench Pro, respectively. Without history, the same pipeline produces more resolved trajectories than independent sampling, but improves by only 0.11 points on Multilingual. These results show the value of using history to guide collection without exposing it to the coding agent.
