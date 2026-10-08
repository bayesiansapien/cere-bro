---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.05140
url: https://huggingface.co/papers/2610.05140
arxiv_url: https://arxiv.org/abs/2610.05140
date: 2026-10-07
---

# AutoSciBench: Autonomous Benchmark Generation for Evaluating Scientific Agents

As agents rapidly evolve, existing benchmarks can become saturated, limiting their ability to distinguish capabilities and reveal remaining failure modes. Particularly in scientific domains, constructing and updating benchmarks requires substantial time, labor, and domain expertise, making it difficult to keep evaluation aligned with advances in agent capabilities. We address this challenge by investigating whether scientific-agent benchmarks can be automatically generated and iteratively adapted as agent capabilities evolve. We introduce AutoSciBench, a framework that represents each task as a high-level concept specifying the scientific domain, data modality, and required reasoning approach, together with a low-level recipe specifying how the question, environment, and ground-truth answer are constructed and verified. Agents attempt to solve each task, producing solver trajectories and corresponding judge feedback which AutoSciBench uses to revise the recipe or concept, closing observed shortcuts and shifting tasks toward raw-data re-examination, interpretation of intermediate results, and evidence integration. Experience distilled from completed refinement trajectories further guides new concept generation, allowing lessons from earlier task refinement to inform subsequent benchmark construction. Starting from existing benchmarks, we evaluate AutoSciBench across computational biology, materials science, and clinical imaging. Generated benchmarks reduce average solver accuracy by 22.4 and 25.5 percentage points relative to the human-curated benchmarks in computational biology and materials science, respectively, while generated tasks receive higher average quality ratings across all three domains, suggesting that scientific-agent evaluation can adapt as agent capabilities advance.
