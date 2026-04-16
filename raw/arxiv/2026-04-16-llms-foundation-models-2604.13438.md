---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13438
category: cs.LG
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13438
published: 2026-04-16
authors: Xingjian Zhao, Mohammad Mohammadi Amiri, Malik Magdon-Ismail
---

# WIN-U: Woodbury-Informed Newton-Unlearning as a retain-free Machine Unlearning Framework

**arXiv:** https://arxiv.org/abs/2604.13438
**Authors:** Xingjian Zhao, Mohammad Mohammadi Amiri, Malik Magdon-Ismail

## Abstract

arXiv:2604.13438v1 Announce Type: new  Abstract: Privacy concerns in LLMs have led to the rapidly growing need to enforce a data's "right to be forgotten". Machine unlearning addresses precisely this task, namely the removal of the influence of some specific data, i.e., the forget set, from a trained model. The gold standard for unlearning is to produce the model that would have been learned on only the rest of the training data, i.e., the retain set. Most existing unlearning methods rely on direct access to the retained data, which may not be practical due to privacy or cost constraints. We propose WIN-U, a retained-data free unlearning framework that requires only second order information for the originally trained model on the full data. The unlearning is performed using a single Newton-style step. Using the Woodbury matrix identity and a generalized Gauss-Newton approximation for the forget set curvature, the WIN-U update recovers the closed-form linear solution and serves as a local second-order approximation to the gold-standard retraining optimum. Extensive experiments on various vision and language benchmarks demonstrate that WIN-U achieves SOTA performance in terms of unlearning efficacy and utility preservation, while being more robust against relearning attacks compared to existing methods. Importantly, WIN-U does not require access to the retained data.
