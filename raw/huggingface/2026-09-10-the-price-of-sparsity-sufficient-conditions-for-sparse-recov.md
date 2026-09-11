---
source: farmer/huggingface
farmed: 2026-09-11T00:57:36.854415+00:00
arxiv_id: 2509.01809
url: https://huggingface.co/papers/2509.01809
arxiv_url: https://arxiv.org/abs/2509.01809
date: 2026-09-10
---

# The Price of Sparsity: Sufficient Conditions for Sparse Recovery using Sparse and Sparsified Measurements

We consider the problem of support recovery for sparse binary signals from noisy linear measurements. For sparse Gaussian measurement matrices we identify sufficient conditions on the minimal sample size for maximum-likelihood recovery in the high-SNR regime ds/p to infty, where p denotes the signal dimension, s the number of non-zero components of the signal, and d the expected number of non-zero components per row of measurement. Combined with known lower bounds, this yields an information-theoretic threshold of order slog(p/s) / log(ds/p), making explicit the price of measurement sparsity. In particular, we highlight a regime where the sample-complexity loss from measurement sparsity is logarithmic while the computational gain is nearly linear.
  Second, we study recovery after sparsifying an originally dense Gaussian design: the observations are generated from the dense design, while estimation uses an independently sparsified design and a rescaled response. In the proportional regime s=αp, d=ψp, we prove that, for every fixed target error level δ and every slack varepsilon>0, a sample size of order p/ψ^2 is sufficient for support recovery for arbitrarily small ψ.
