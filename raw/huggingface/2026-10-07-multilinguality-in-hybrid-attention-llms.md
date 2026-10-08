---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2609.35378
url: https://huggingface.co/papers/2609.35378
arxiv_url: https://arxiv.org/abs/2609.35378
date: 2026-10-07
---

# Multilinguality in Hybrid Attention LLMs

In response to the growing demand for long sequences in agentic and reasoning use cases, many state-of-the-art LLMs combine multiple variants of attention to mitigate the quadratic complexity of traditional softmax attention. These hybrid attention LLMs aim to balance the strengths and limitations of full attention and alternatives based on recurrence. This work presents a first study of how hybrid attention impacts the multilinguality of LLMs. Beyond the impact on long sequences in poorly tokenized languages, our study is motivated by the possibility that the inductive biases of the recurrent state alter linguistic processing. Our interpretability analysis confirms this, showing that cross-lingual representations in hybrid models develop in patterns tied to the ordering of recurrent and full-attention layers. Across diverse models, we notably observe a pronounced spike in cross-lingual alignment around the first full-attention layer. These findings lead us to question the conventional ordering of attention layers. In distillation experiments on multilingual data, all alternative layer orderings outperform the standard throughout training, learning up to 2.5X faster. These stark, replicable results prompt our theory that multilingual models would benefit from starting with a full-attention layer rather than recurrent layers.
