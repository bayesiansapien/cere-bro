---
source: farmer/huggingface
farmed: 2026-09-25T22:51:58.846051
arxiv_id: 2609.30077
url: https://huggingface.co/papers/2609.30077
arxiv_url: https://arxiv.org/abs/2609.30077
date: 2026-09-25
upvotes: 1
---

# Rate-distortion optimization for full-reference image quality metrics via stochastic Hessian estimates

Block-based video codecs select coding parameters based on the input by optimizing a rate-distortion trade-off. The conventional distortion choice, the sum of squared errors (SSE), simplifies parameter selection: the SSE is the sum of block-wise SSEs, so rate-distortion optimization (RDO) can treat blocks independently. Alternatively, full-reference image quality assessment (FR-IQA) metrics such as MS-SSIM or LPIPS often align better with the human visual system than SSE, but they cannot be used in-loop: they do not decompose block-wise and typically require the fully decoded image as input. Building on existing results in metric quadratization, we approximate a broad class of FR-IQA metrics by an input-dependent quadratic distortion (IDQD), whose quadratic form matrix is derived from the Hessian of the metric evaluated at the source video. To make the distortion computable block-wise, we propose two approximations of the Hessian matrix: 1) keeping the block-diagonal, and 2) keeping only its diagonal. We propose estimators for both that require only matrix-vector products with the Hessian obtained by automatic differentiation. Across five metrics for Kodak and CLIC in VVC, IDQD-RDO achieves 14.2-36.7 % BD-rate savings under the target metric with no decoder changes and incurs 10-30 % encoding complexity overhead.
