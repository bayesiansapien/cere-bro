---
source: farmer/huggingface
farmed: 2026-04-21T00:00:00Z
arxiv_id: "2604.18574"
url: https://huggingface.co/papers/2604.18574
arxiv_url: https://arxiv.org/abs/2604.18574
date: 2026-04-21
---

# When Can LLMs Learn to Reason with Weak Supervision?

Large language models have achieved significant reasoning improvements through reinforcement learning with verifiable rewards (RLVR). Yet as model capabilities grow, constructing high-quality reward signals becomes increasingly difficult, making it essential to understand when RLVR can succeed under weaker forms of supervision. We conduct a systematic empirical study across diverse model families and reasoning domains under three weak supervision settings: scarce data, noisy rewards, and self-supervised proxy rewards. We find that generalization is governed by training reward saturation dynamics: models that generalize exhibit a prolonged pre-saturation phase during which training reward and downstream performance climb together, while models that saturate rapidly memorize rather than learn. We identify reasoning faithfulness, defined as the extent to which a model's intermediate steps logically support its final answer, as the pre-RL property that predicts which regime a model falls into, while output diversity alone is uninformative. Motivated by these findings, we disentangle the contributions of continual pre-training and supervised fine-tuning, finding that SFT on explicit reasoning traces is necessary for generalization under weak supervision, while continual pre-training on domain data amplifies the effect. Applied together to Llama3.2-3B-Base, these interventions enable generalization across all three settings where the base model previously failed.

**Authors:** Jingyan Shen, Anna Mordvina, Hamid Palangi, Saadia Gabriel, Pavel Izmailov
