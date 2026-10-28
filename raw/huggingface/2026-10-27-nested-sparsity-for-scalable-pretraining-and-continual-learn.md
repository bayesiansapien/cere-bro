---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.31818
url: https://huggingface.co/papers/2610.31818
arxiv_url: https://arxiv.org/abs/2610.31818
date: 2026-10-27
---

# Nested Sparsity for Scalable Pretraining and Continual Learning

Mixture-of-experts (MoE) transformers, the standard backbone for modern large-scale deep learning, employ conditional computation: only a sparse subset of model weights is used in each forward pass. In MoE transformers, this sparsity arises in the MoE operator, which generalizes the multi-layer perceptron in the classical transformer. In this work, we explore an alternative mechanism for conditional computation that analogously generalizes the attention operator. The sparsity induced by this mechanism naturally nests (i.e., hierarchically composes) with the sparsity induced by the MoE operator. We show that a transformer employing this nested sparsity mechanism, which we call Nestor, performs better than a conventional MoE transformer at equal compute and equal sparsity in language model pretraining. We also show that Nestor is well-suited for continual pretraining: it can be adapted to longer contexts more effectively than conventional MoEs, as well as adapt more efficiently to new domains while forgetting less on old domains. Furthermore, we demonstrate that these benefits persist as model size, dataset size, and context length grow. Our results demonstrate the potential of alternative conditional computation mechanisms for deep neural network architectures. Code and checkpoints are available on GitHub at https://github.com/Ma-Lab-Berkeley/Nestor .
