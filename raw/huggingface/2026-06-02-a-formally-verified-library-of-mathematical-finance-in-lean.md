---
source: farmer/huggingface
farmed: 2026-06-02T11:05:30Z
arxiv_id: 2606.01356
url: https://huggingface.co/papers/2606.01356
arxiv_url: https://arxiv.org/abs/2606.01356
date: 2026-06-02
---

# A Formally Verified Library of Mathematical Finance in Lean 4

We describe a library of mathematical finance built in the Lean 4 proof assistant, on top of Mathlib and the BrownianMotion package. It is broad: more than two hundred sorry-free theorems across eleven areas, from the measure-theoretic foundations of continuous-time stochastic calculus through derivative pricing to applied risk, portfolio, and fixed-income theory, and, to our knowledge, the most comprehensive machine-checked development of mathematical finance to date. Breadth is the setting, not the point. Two things make it more than a catalogue. It reaches into the continuous theory far enough to construct the L2 Itô integral as a bounded linear isometry and to derive, rather than assume, the risk-neutral pricing measure. And it audits its own faithfulness: every result is classified by how its Lean statement relates to the mathematics it claims, and a build-enforced gate pins the axioms each proof actually uses, so a reader can see precisely what has been proved and what has only been proved under added hypotheses. We close with a candid finding: a formal base over classical financial mathematics yields certified unification of known results rather than new financial theory. The contribution is therefore methodological and infrastructural, reusable verified foundations for mathematical finance, together with the faithfulness audit.
