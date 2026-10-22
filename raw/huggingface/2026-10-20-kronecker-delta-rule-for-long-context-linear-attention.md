---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.26834
url: https://huggingface.co/papers/2610.26834
arxiv_url: https://arxiv.org/abs/2610.26834
date: 2026-10-20
---

# Kronecker Delta Rule for Long Context Linear Attention

We propose KronLSTM, a linear attention architecture based on the Kronecker Delta Rule, a novel update rule for associative matrix memories. KronLSTM extends the xLSTM family with a memory-revision mechanism that corrects targeted associations while modifying the memory only along a single direction in matrix space. This minimally invasive memory revision reduces interference with previously stored information compared with delta-rule updates, making it particularly well suited for long-context language modeling. The resulting memory dynamics can be mathematically described as a Markov chain that converges to a steady-state distribution, while the expected norm of the memory matrix remains uniformly bounded throughout the entire input sequence. Hence, KronLSTM ensures stable memory dynamics without requiring additional normalization and stabilization mechanisms for the memory state. Experiments show that KronLSTM is competitive with, and often outperforms, existing linear attention architectures, including models of the (Gated) DeltaNet family, with particularly strong performance on long context benchmarks. These results establish the Kronecker Delta Rule as an effective and analytically tractable foundation for stable associative memory in recurrent linear attention architectures. Our code (https://github.com/NX-AI/KronLSTM) and models (https://huggingface.co/collections/NX-AI/kronlstm) are open-source.
