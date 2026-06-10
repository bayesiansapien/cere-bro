---
source: farmer/huggingface
farmed: 2026-06-10T06:28:48Z
arxiv_id: 2606.09068
url: https://huggingface.co/papers/2606.09068
arxiv_url: https://arxiv.org/abs/2606.09068
date: 2026-06-10
---

# Emergent Misalignment Can Be Induced by Sycophancy and Reversed via Alignment Gating

Prior work has shown that fine-tuning large language models on malicious or incorrect outputs in narrow domains can induce broad misalignment and harmful behavior, a phenomenon known as emergent misalignment. However, efficient methods for reversing such misalignment remain limited. In this work, we make two contributions. First, we identify sycophancy fine-tuning, i.e., training models to passively agree with users' incorrect opinions, as a previously underexplored driver of emergent misalignment, and show that it induces broad and severe misaligned behavior. Second, we propose Alignment Gating, an efficient method for reversing emergent misalignment that inserts learnable and controllable gates into the model during fine-tuning. Through fine-tuning, these gates learn to identify the internal representations responsible for unsafe responses. Thus, amplifying or suppressing these representations then exacerbates or mitigates EM, respectively. We further find that alignment gating module exhibits strong generalization: gating weights obtained from narrow-domain fine-tuning substantially suppress broad-domain misaligned behavior while preserving the model's general capabilities.
