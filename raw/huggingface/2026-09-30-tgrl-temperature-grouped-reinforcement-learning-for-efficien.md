---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.33589
url: https://huggingface.co/papers/2609.33589
arxiv_url: https://arxiv.org/abs/2609.33589
date: 2026-09-30
---

# TGRL: Temperature-Grouped Reinforcement Learning for Efficient Exploration in LLMs

Efficient exploration often remains a central bottleneck in reinforcement learning with verifiable rewards (RLVR). Although temperature control and test-time scaling strategies can increase rollout diversity of large language models (LLMs), they either expand the sample budget at rollout time or leave the benefit of exploration unquantified. To this end, we propose Temperature-Grouped Reinforcement Learning (TGRL), which turns temperature-induced diversity into an explicit training signal. For each prompt, TGRL partitions its rollout group into low- and high-temperature subsets, estimates exploration gain through their reward contrast, and allocates this group-level signal as token-level credit using Jensen--Shannon (JS) divergence between the corresponding temperature-scaled next-token distributions induced by the same logits. Notably, TGRL reaches equivalent accuracy up to 36% faster than strong RLVR baselines without expanding the rollout budget. Across 11 benchmarks from diverse domains, TGRL broadly improves over strong RLVR baselines: it improves the six-benchmark math average by 1.6% at 32B, raises CodeForces rating by 196.7 points and LiveCodeBench Pass@16 by 4.4%, and improves ALFWorld/WebShop success rates by 6.3%/4.9%. Comprehensive ablations and wall-clock analysis confirm the efficacy of all proposed components. Code is available at https://github.com/1229095296/TGRL/tree/main.
