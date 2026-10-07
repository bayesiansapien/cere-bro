---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2609.36099
url: https://huggingface.co/papers/2609.36099
arxiv_url: https://arxiv.org/abs/2609.36099
date: 2026-10-06
---

# Data Unlearning via Inverse Distillation

Multi-step matching models, including flow and diffusion models, produce high-quality outputs but incur substantial inference costs and may reproduce unwanted components of their training datasets. We introduce Inverse Distillation Unlearning (IDU), a unified framework that simultaneously distills a teacher multi-step matching model into an efficient one-step student generator and suppresses outputs corresponding to a designated training subset. We first formulate distillation as a min-max objective over a data distribution and then represent this distribution as a mixture of the forget-set and the generated distributions. This allows us to compare this mixture with the teacher's training distribution and recover only the retained data at the optimum. Our method requires only a pretrained full-data teacher and data from the forget set, without access to retained training examples, extra feature extractors or classifiers. Extensive experiments on MNIST and CIFAR-10 datasets under flow-matching and score-based diffusion settings demonstrate that IDU substantially reduces the generation frequency of forgotten classes while preserving generation quality on the retained classes. To the best of our knowledge, IDU is the first unified framework for simultaneous unlearning and distillation in unconditional flow-matching and score-based models.
