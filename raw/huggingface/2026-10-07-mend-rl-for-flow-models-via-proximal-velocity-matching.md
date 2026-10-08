---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.05954
url: https://huggingface.co/papers/2610.05954
arxiv_url: https://arxiv.org/abs/2610.05954
date: 2026-10-07
---

# MEND: RL For Flow Models via Proximal Velocity Matching

Reward post-training of flow models either reweights the model's own samples under a KL penalty or a frozen reference, often for thousands of updates, or backpropagates the reward and moves every sample without checking that the move is worth its size. We introduce MEND, a reinforcement learning method built on proximal velocity matching. MEND caps rewards within each prompt group, so samples that already score well receive no move. Below the cap, it proposes moves along the reward gradient and accepts one only when its capped reward gain exceeds a quadratic displacement price. The model then regresses onto the resulting velocity targets, with no KL term, frozen reference model, or advantage weights. In 100 updates, MEND outperforms Flow-GRPO (about 4k updates) on five of six evaluators at the same distance to base-model images. Under an equal-budget protocol, it surpasses ReFL and DiffusionNFT at every evaluated update across four training rewards, reaching PickScore 24.03 versus 23.92 and 23.43, respectively. A 300-update three-reward run also surpasses the five-reward DiffusionNFT model on all three rewards it trains on. MEND is general and easy to adopt: it applies to any flow backbone with a differentiable reward.
