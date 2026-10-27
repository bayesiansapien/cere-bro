---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.801542+00:00
arxiv_id: 2609.16158
url: https://huggingface.co/papers/2609.16158
arxiv_url: https://arxiv.org/abs/2609.16158
date: 2026-10-26
---

# The fixed-point bundle method over product-of-simplex domains arising from game equilibria

Developing general-purpose algorithms with global asymptotic convergence guarantees for Nash equilibria of general-sum games remains a longstanding challenge. This paper extends the fixed-point bundle framework for finite-dimensional variational inequalities (VIs) from simplex domains to product-of-simplex domains, enabling its direct application to Nash equilibrium computation. The resulting fixed-point bundle exhibits a composite fiber bundle structure. The key innovation is to construct an equivalent VI on a simplex and establish the equivalence between the two fixed-point bundle frameworks via a fiber bundle isomorphism. Exploiting this geometric equivalence, we show that the path-following algorithm for VIs on product-of-simplex domains inherits the global linear convergence guarantees of the simplex-domain framework. In numerical experiments, the algorithm attained a precision of 10^{-5} on all 5600 randomly generated game instances, with dimension ranging from 2-player 128-action to 128-player 2-action. Code and data are available at https://github.com/shb20tsinghua/FiberBundle_VI.
