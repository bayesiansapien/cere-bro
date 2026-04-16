---
source: farmer/huggingface
farmed: 2026-04-16T00:00:00Z
arxiv_id: 2604.14142
url: https://huggingface.co/papers/2604.14142
arxiv_url: https://arxiv.org/abs/2604.14142
date: 2026-04-16
authors: Yuqiao Tan, Minzheng Wang, Bo Liu
---

# From P(y|x) to P(y): Investigating Reinforcement Learning in Pre-train Space

**Authors:** Yuqiao Tan, Minzheng Wang, Bo Liu
**arXiv:** [2604.14142](https://arxiv.org/abs/2604.14142)
**HuggingFace:** [hf.co/papers/2604.14142](https://huggingface.co/papers/2604.14142)

## Abstract

While reinforcement learning with verifiable rewards (RLVR) significantly enhances LLM reasoning by optimizing the conditional distribution P(y|x), its potential is fundamentally bounded by the base model's existing output distribution. Optimizing the marginal distribution P(y) in the Pre-train Space addresses this bottleneck by encoding reasoning ability and preserving broad exploration capacity. Yet, conventional pre-training relies on static corpora for passive learning, leading to a distribution shift that hinders targeted reasoning enhancement. In this paper, we introduce PreRL (Pre-train Space RL), which applies reward-driven online updates directly to P(y). We theoretically and empirically validate the strong gradient alignment between log P(y) and log P(y|x), establishing PreRL as a viable surrogate for standard RL. Furthermore, we uncover a critical mechanism: Negative Sample Reinforcement (NSR) within PreRL serves as an exceptionally effective driver for reasoning. NSR-PreRL rapidly prunes incorrect reasoning spaces while stimulating endogenous reflective behaviors, increasing transition and reflection thoughts by 14.89x and 6.54x, respectively. Leveraging these insights, we propose Dual Space RL (DSRL), a Policy Reincarnation strategy that initializes models with NSR-PreRL to expand the reasoning horizon before transitioning to standard RL for fine-grained optimization.
