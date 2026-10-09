---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.309855+05:30
arxiv_id: 2610.10164
url: https://huggingface.co/papers/2610.10164
arxiv_url: https://arxiv.org/abs/2610.10164
date: 2026-10-08
---

# UniSkill: Learning Actor-Aligned Skill Proposals for an Evolving Policy

Large language model agents can improve across tasks by retaining reusable skills distilled from prior interactions. Recent work jointly optimizes task execution and skill extraction, enabling the policy and skillbank to co-evolve. However, as the actor continues learning, rewarding skill proposals through their reuse in subsequent training steps may conflate skill benefits with actor improvement, while directly testing each proposed skill requires costly additional actor rollouts. In this paper, we introduce UniSkill, which uses a shared policy to interact with the environment and propose skillbank edits (Add, Update, or No Edit) from the resulting trajectories. Specifically, the actor learns from environment rewards, while contrastive action feedback guides skill proposal learning. This feedback provides an actor-alignment signal by measuring how replacing the retrieved skill with a proposed skill changes the current actor's action log-likelihood gap between previously collected successful and failed trajectories from the same task, thereby avoiding new rollouts for each proposal. Since proposal-level feedback may suppress an otherwise appropriate edit operation when the proposed skill content scores poorly, we further apply skill-edit support regularization to preserve exploration. Empirically, UniSkill achieves strong performance, reaching 98.4% success on ALFWorld and 84.7% on WebShop while maintaining stable joint training. Further ALFWorld experiments show that UniSkill remains effective when the shared policy uses a smaller backbone. Our implementation is available at https://github.com/LimOkii/UniSKill.
