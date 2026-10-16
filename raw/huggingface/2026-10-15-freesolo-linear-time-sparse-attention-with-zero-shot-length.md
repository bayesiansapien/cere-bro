---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.230769+05:30
arxiv_id: 2610.17191
url: https://huggingface.co/papers/2610.17191
arxiv_url: https://arxiv.org/abs/2610.17191
date: 2026-10-15
---

# FreeSolo: Linear-time Sparse Attention with Zero-Shot Length Extrapolation

Linear-time sequence models typically store long-context information in a recurrent state. A fixed-size state limits how much information can be stored, while hybrid architectures that add full attention for better recall incur quadratic sequence cost. Alternatively, sparse attention with continued pretraining (CPT) can extend the effective context length. Generalization beyond the trained length remains challenging, however, and CPT can be costly. We introduce FreeSolo, a native sparse attention mechanism with a short-range sliding window branch and a long-range branch that selects keypoint cells for direct token attention. Its linear-time variant, FS-L, learns to prune the prefix before query-dependent selection through short CPT. FS-B searches balanced trees with O(Nlog^2 N) algorithmic cost including radix-sort construction. FreeSolo demonstrates better zero-shot length extrapolation than the baselines without long-context fine-tuning.
