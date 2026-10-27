---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.801442+00:00
arxiv_id: 2606.00778
url: https://huggingface.co/papers/2606.00778
arxiv_url: https://arxiv.org/abs/2606.00778
date: 2026-10-26
---

# A path-following framework on fiber bundle for variational inequalities

Developing general-purpose algorithms with global asymptotic convergence guarantees for variational inequalities (VIs) remains a longstanding challenge. This paper proposes a path-following framework for finite-dimensional VIs with arbitrary continuous mappings and polytope domains. The approach first transforms a general VI into a smooth VI on a simplex. Its key innovation is to formulate the resulting problem on a fiber bundle, called the fixed-point bundle, whose geometric structure enables the systematic integration of initialization, path-following, and singularity avoidance. Without imposing monotonicity or similar assumptions, the framework guarantees global linear convergence for nonsingular solutions and global linear convergence up to any prescribed precision for singular solutions. In numerical experiments, the algorithm attained a precision of 10^{-5} on all 6400 randomly generated instances, with dimensions up to 1024. Code and data are available at https://github.com/shb20tsinghua/FiberBundle_VI.
