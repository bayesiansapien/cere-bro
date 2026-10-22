---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.647897
arxiv_id: 2610.23010
url: https://huggingface.co/papers/2610.23010
arxiv_url: https://arxiv.org/abs/2610.23010
date: 2026-10-21
---

# What Makes a Good Symbol for Hybrid Discrete-Continuous Planning?

The physical world has continuous state and action spaces, yet robot planning often benefits from hybrid discrete-continuous formulations that explicitly expose combinatorial structure, such as contact modes or discrete primitive actions. Existing methods typically rely on human-defined symbol sets or symbols derived from language supervision, without asking what makes a symbol computationally useful. In this paper, we take an inference-algorithm--centric view to define usefulness: a good symbol should expose the discrete commitments that simplify solving the original planning problem. We first introduce the concept of solver-sufficient symbolization by studying finite-horizon piecewise-affine systems, for which solver sufficiency can be precisely characterized, and develop a counterexample-guided algorithm for symbol invention. We then extend this principle to invent symbols for optimization objectives parameterized by general neural networks as energy functions, showing that solver-sufficient symbols can nevertheless be induced from their continuous optimization landscapes. Experiments on simulated and real-robot tasks show that the resulting symbols reduce solving cost while preserving solution quality, while also improving interpretability and steerability. Furthermore, our theoretical and algorithmic insights help explain why certain human-defined symbols are computationally useful.
