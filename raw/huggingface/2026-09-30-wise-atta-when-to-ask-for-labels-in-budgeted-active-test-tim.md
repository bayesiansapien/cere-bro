---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.37687
url: https://huggingface.co/papers/2609.37687
arxiv_url: https://arxiv.org/abs/2609.37687
date: 2026-09-30
---

# WISE-ATTA: When to Ask for Labels in Budgeted Active Test-Time Adaptation

Active test-time adaptation (ATTA) improves robustness under distribution shift by updating a deployed model during inference while selectively querying supervision. However, most existing ATTA methods implicitly assume that supervision can be requested for every incoming test batch, which can incur substantial annotation cost over long test streams. In this work, we introduce budgeted ATTA in which labels are available for only a fraction of test batches. This formulation shifts the central challenge from deciding what to label within a batch to deciding when supervision should be applied over time. To address this challenge, we propose a budget-aware approach WISE-ATTA that allocates supervision over the test stream based on lightweight signals computed online, prioritizing periods where supervision is likely to be most useful. When a batch is selected for supervision, we further employ a drift-based sample selection criterion that targets samples exhibiting ongoing, unconverged adaptation dynamics, enabling effective updates from a single labeled example. We evaluate this approach on synthetic corruptions (ImageNet-C) and natural distribution shifts (ImageNet-R/K/A). Across settings, WISE-ATTA achieves competitive or improved performance compared to recent ATTA methods while requiring substantially fewer labels. Overall, we find that the timing of supervision is a key, yet underexplored, aspect of active test-time adaptation. Code: https://github.com/Muhammad-Huzaifaa/WISE-ATTA
