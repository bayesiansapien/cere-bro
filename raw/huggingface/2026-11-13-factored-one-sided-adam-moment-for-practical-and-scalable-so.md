---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.529617+00:00
arxiv_id: 2611.16905
url: https://huggingface.co/papers/2611.16905
arxiv_url: https://arxiv.org/abs/2611.16905
date: 2026-11-13
---

# Factored One-sided Adam-Moment for Practical and Scalable SOAP

Second-order optimizers (e.g., Shampoo, SOAP) have emerged as compelling alternatives to Adam/AdamW and promise faster per-step convergence than AdamW in transformer training. However, they still remain costly in practice, and even SOAP still pays substantial optimizer-state memory and eigendecomposition overhead. We ask whether the benefits of SOAP can be retained at nearly the efficiency of AdamW. In this paper, we answer yes with a lightweight SOAP variant, Factored One-sided Adam-Moment (FOAM). The path to practical impact is twofold: first, FOAM employs input-only preconditioning, dropping the output-side Kronecker factor to reduce memory and remove one eigendecomposition. The Kronecker structure of the Hessian shows that this is exact for a diagonal output-side curvature and nearly lossless for a near-diagonal one, as we observe empirically. Second, FOAM replaces SOAP's dense rotated second moment with a factored Adam-moment estimator based on row-by-column statistics. Under the K-FAC Fisher assumption with a diagonal output curvature, this estimator exactly recovers SOAP's dense second moment, and we measure only a 15-20% K-FAC violation, with negligible effect on the update. Our empirical results support the claim that FOAM matches strong SOAP and Muon baselines in validation loss across scales of large language model (LLM) pre-training, uses half of SOAP's optimizer state, runs at Muon-class wall-clock time, and retains robustness across a three-fold learning-rate range. The results hold from 124M to 760M parameters, demonstrating that SOAP's gains need not require SOAP's cost. Code: https://github.com/naver-ai/foam
