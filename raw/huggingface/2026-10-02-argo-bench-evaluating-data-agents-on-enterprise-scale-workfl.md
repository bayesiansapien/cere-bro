---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.819648+00:00
arxiv_id: 2610.02122
url: https://huggingface.co/papers/2610.02122
arxiv_url: https://arxiv.org/abs/2610.02122
date: 2026-10-02
---

# Argo-Bench: Evaluating Data Agents on Enterprise-Scale Workflows

Real-world enterprise data science and analytics workflows require reasoning across dozens of tables, performing statistical analyses, and acting on the results. Established text-to-SQL benchmarks evaluate query generation alone, and audits have found their answer keys frequently wrong. Because real enterprise warehouses are too sensitive to release, these benchmarks are built on public datasets where a business event fits in a single table. We introduce Argo-Bench, an evaluation framework comprising 210 data science and analytics tasks. Drawing on public data, peer-reviewed industry literature, and regulatory filings, we simulate a food delivery platform in New York City at true scale, with 81 million orders in 2024, grounded economics, fraud patterns, and marketplace incentives. We export this world to an ERP warehouse of 235 tables and 7.5 billion rows, modeled on the Oracle E-Business Suite schema. The simulator's ground-truth state is withheld from the warehouse the agent sees, so tasks require reconstructing facts by navigating the warehouse before acting on them. Argo-Bench goes beyond text-to-SQL: the agent files actions such as banning fraudulent accounts, allocating courier incentive budgets, or issuing back pay, and the grader scores each by its consequences in the simulator. Every task has an executable reference solution that demonstrates solvability using only the warehouse. The strongest of 14 frontier and open-weight models scores 95 or higher on only 34.8% of tasks and averages 59.5 points. We hope Argo-Bench drives progress toward agents that understand, navigate, and act within real data environments.
