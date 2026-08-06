---
source: farmer/huggingface
farmed: 2026-08-06T10:35:34.247620Z
arxiv_id: 2608.05102
url: https://huggingface.co/papers/2608.05102
arxiv_url: https://arxiv.org/abs/2608.05102
date: 2026-08-06
---

# ABSeeker: Training Long-Horizon Search Agents via Answer-Backtracked Credit Assignment

Long-horizon search agents must make multiple sequential actions (steps) to search, retrieve, verify, and integrate evidence to reach a final answer. However, existing methods for training these agents typically treat all steps within a trajectory uniformly during both supervised fine-tuning (SFT) and reinforcement learning (RL), failing to distinguish useful actions from erroneous or redundant ones. In this paper, we propose Answer-Backtracked Credit Assignment (ABC), a fine-grained credit assignment framework for training long-horizon search agents by converting sparse trajectory-level outcomes into dense step-level supervision that rewards useful actions (even in failed trajectories) while suppressing erroneous or redundant actions. Specifically, given a potentially obscure query and its corresponding ground-truth answer, ABC first performs Answer-Backtracked Clue Recovery, which traces back from the answer to recover intermediate clues required to solve the question. It then applies Clue-Anchored Step Scoring to evaluate each search step against these clues, converting sparse binary outcome supervision into dense step-level rewards. Based on these rewards, we develop ABC-SFT, which reweights the loss of each turn, and ABC-GRPO, which uses the step-level scores as rewards in GRPO. Building on this framework, we train ABSeeker based on Qwen3.5-4B with only 8.5k examples. ABSeeker achieves 37.3% on BrowseComp and 39.1% on BrowseComp-ZH. With context management, the scores further improve to 55.3% and 52.9%, respectively, significantly outperforming same-scale (4B) agents and even matching the performance of larger ones (approximately 30B). These results demonstrate the effectiveness of answer-backtracked step-level credit assignment for training long-horizon search agents.
