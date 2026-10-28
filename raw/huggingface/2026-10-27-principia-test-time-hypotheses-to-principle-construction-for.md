---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.32195
url: https://huggingface.co/papers/2610.32195
arxiv_url: https://arxiv.org/abs/2610.32195
date: 2026-10-27
---

# Principia: Test-Time Hypotheses to Principle Construction for Scientific Discovery

Scientific discovery requires identifying the scientific principles underlying observed phenomena to guide further investigation. As these empirical principles are often unknown in complex discovery processes, they are constructed via a hypotheses-to-principle pipeline to obtain recurring causalities from progressively accumulated observations during test-time discovery. However, constructing this knowledge requires substantial domain expertise, time, and effort, making this translation stage a bottleneck for scientific discovery. To address this limitation, we propose Principia, an LLM-based framework that constructs and continually refines scientific principles at test time. Drawing on how human researchers develop principles, Principia forms comparative causal hypotheses from related inputs and their observed outcomes, then synthesizes recurring relationships across these hypotheses into inductive principles. By applying the constructed hypotheses and inductive principles to the task, it obtains new observations, revises the hypotheses used based on these new observations, and reconstructs principles from the updated hypotheses, allowing scientific knowledge to continuously evolve throughout test-time discovery. Across benchmarks spanning molecular optimization, protein engineering, gene perturbation, and molecular property prediction, Principia outperforms baselines relying on internal knowledge, external sources, or experience summaries, while generating principles that are plausible and consistent with the scientific literature, demonstrating its effectiveness in constructing and refining task-specific hypotheses and principles at test time for scientific discovery. Our code is available at https://github.com/DongkiKim95/Principia.
