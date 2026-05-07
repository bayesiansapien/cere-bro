# ResRL: Boosting LLM Reasoning via Negative Sample Projection Residual Reinforcement Learning

**arXiv:** [2605.00380](https://arxiv.org/abs/2605.00380) · **Code:** [github.com/1229095296/ResRL](https://github.com/1229095296/ResRL.git)
**Authors:** Zihan Lin (Meituan internship + CAS), Xiaohan Wang, Jie Cao, Jiajun Chai, Li Wang, Xiaodong Lu, Wei Lin, Ran He, Guojun Yin
**Affiliation:** Meituan + Institute of Automation, Chinese Academy of Sciences
**Tier:** 2 — RLVR / post-training / Chinese-lab work

## TL;DR

ResRL fixes the diversity-collapse failure mode of RLVR (Reinforcement Learning with Verifiable Rewards) by projecting negative-token hidden states onto a low-rank SVD positive subspace and modulating negative gradients by the projection residual. This decouples the semantic distribution overlap that Negative Sample Reinforcement (NSR) was inadvertently penalizing. +9.4% on Avg@16 math reasoning vs NSR, +7.0% on Pass@128, with diversity preserved. Twelve-benchmark sweep across Mathematics, Code, Agent Tasks, and Function Calling.

## Mechanism

```
Positive trajectory tokens    Negative trajectory tokens
        │                              │
        ▼                              ▼
   hidden states              hidden states
        │                              │
        │           SVD                │
        └────────► positive ◄──────────┤
                  subspace             │
                                       ▼
                            project negative onto positive subspace
                                       │
                                       ▼
                       residual = negative_hidden - projection
                                       │
                                       ▼
                       modulate negative gradient by residual
                       (only the orthogonal component is penalized)
```

Theoretical link: Lazy Likelihood Displacement (LLD) is mapped to negative-positive head-gradient interference. A single-forward proxy upper-bounds representation alignment, guiding conservative advantage reweighting. The SVD projection is the operational form of "do not penalize the parts of negative trajectories that semantically overlap with positive trajectories."

## How this relates to prior wiki work

- **Confirms** the wiki's tracking of RLVR mode collapse from [DSRL discussion in 04-19](../llms-foundation-models/2026-04-19-vgf-value-gradient-flow-rl.md).
- **Addresses** the gradient-conflict critique implicit in [GFT-SFT as degenerate RL (04-21)](../llms-foundation-models/2026-04-21-gft-sft-as-degenerate-rl.md) and [RLVR weak-supervision faithfulness (04-21)](../llms-foundation-models/2026-04-21-rlvr-weak-supervision-reasoning-faithfulness.md), which both argued that RLVR's reward signal is not as clean as the verifiability framing implies.
- **Cross-source tension** with Kurate cs.LG #9 [LLMs Gaming Verifiers](https://arxiv.org/abs/2604.15149): ResRL fixes one failure mode (gradient interference / diversity collapse). Gaming Verifiers documents another (RLVR is reward-hackable in principle, separate from the gradient problem). ResRL does not refute Gaming Verifiers, it operates on a different layer of the failure.
- **Lateral connection** to the [Distillation Panic](../inference-efficiency/2026-05-04-distillation-panic-lambert.md) (05-04). Lambert argued the distillation discourse is overheated. ResRL implicitly takes the position that RL-on-positive-and-negative-trajectories with proper gradient handling beats large-scale distillation for reasoning gains.

## What's surprising

The conservative-reweighting framing inverts the intuition. Most NSR-fix papers try to amplify the negative signal. ResRL argues you should *attenuate* the part of the negative signal that semantically overlaps with positive trajectories, then keep the orthogonal residual. This is closer to the RLHF-style preference-modeling literature than to standard RLVR. The math reasoning gain (+9.4% Avg@16, +7.0% Pass@128) suggests this attenuation is doing more work than the previous generation's amplification approach.

## Open questions

1. **Scale.** All experiments are 7B-class. Whether the SVD positive subspace is well-conditioned at 70B+ is open.
2. **Composition with inference-time methods.** [Step-Level Optimization](../ai-routing/2026-05-02-step-level-optimization-computer-use-agents.md) (05-02) detects trajectory stalls at inference. ResRL handles training-time gradient interference. Composition is the next paper.
3. **Diversity floor.** The conservative-reweighting hyperparameter trades off reasoning gain against diversity preservation. The lower bound on diversity below which reasoning gains erode is not characterized in the paper.

## Industry context

The first author is interning at Meituan (the food-delivery company) per Lambert's [Notes from inside China's AI labs](../ai-industry/2026-05-08-lambert-china-ai-labs.md), Meituan was visited the same week this paper was published. Meituan's open-weight LLM strategy fits Lambert's "tech-ownership mentality" framing. ResRL is methodologically deep, exactly the kind of work the build-not-buy culture produces.
