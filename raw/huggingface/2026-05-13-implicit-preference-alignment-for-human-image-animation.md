---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.07545
url: https://huggingface.co/papers/2605.07545
arxiv_url: https://arxiv.org/abs/2605.07545
date: 2026-05-13
---

# Implicit Preference Alignment for Human Image Animation

Human image animation has witnessed significant advancements, yet generating high-fidelity hand motions remains a persistent challenge due to their high degrees of freedom and motion complexity. While reinforcement learning from human feedback, particularly direct preference optimization, offers a potential solution, it necessitates the construction of strict preference pairs. However, curating such pairs for dynamic hand regions is prohibitively expensive and often impractical due to frame-wise inconsistencies. In this paper, we propose Implicit Preference Alignment (IPA), a data-efficient post-training framework that eliminates the need for paired preference data. Theoretically grounded in implicit reward maximization, IPA aligns the model by maximizing the likelihood of self-generated high-quality samples while penalizing deviations from the pretrained prior. Furthermore, we introduce a Hand-Aware Local Optimization mechanism to explicitly steer the alignment process toward hand regions. Experiments demonstrate that our method achieves effective preference optimization to enhance hand generation quality, while significantly lowering the barrier for constructing preference data. Codes are released at https://github.com/mdswyz/IPA
