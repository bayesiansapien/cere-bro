---
source: farmer/huggingface
farmed: 2026-10-27T05:06:31.799175+00:00
arxiv_id: 2610.31931
url: https://huggingface.co/papers/2610.31931
arxiv_url: https://arxiv.org/abs/2610.31931
date: 2026-10-26
---

# Every Weight Is a Path of Shared Discrete Decisions

We introduce TWIG (Tree-structured Weights with Inherited Gates), a representation in which every weight of a neural network is the end of a path of small discrete decisions: a sign, a shift by a power of two, a zero gate, an index into a shared table. Weights that belong together share the upper part of their paths, and each decision is inherited by every weight below it, so it is stored once and applied once. This simple change has three consequences. Any trained network can be written as a TWIG, and when the decisions are powers of two its weight layers become circuits made almost entirely of wires and adders, suited to chips whose weights are fixed at fabrication. Pruning, quantization, low-rank factorization, codebooks and weight sharing become edits of one object, so a single optimizer can choose among all of them for a whole network. And choosing the decisions is the ground-state problem of a higher-order Boltzmann machine whose interactions follow the paths of the tree, the problem class that annealers and quantum optimizers are built to solve. Today these questions are handled apart: each compression method brings its own format and solver, a circuit with fixed weights needs a dedicated constant multiplier for every weight, and discrete solvers reach only narrow subproblems such as rounding. Weight formats have long been moving toward shared decisions, through group scales, shared exponents, microexponents and sparse weights; TWIG takes this trend to its end, and every common format is a shallow TWIG at no extra cost. On five weight matrices of a large language model, a flat tree whose signed power-of-two terms are chosen per weight for circuit cost, with no group scales, needs 9--15\% fewer additions than GPTQ at equal layer error at 3- and 4-bit accuracy on typical matrices, and 20--55\% fewer on matrices with strong outliers.
