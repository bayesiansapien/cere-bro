---
source: farmer/huggingface
farmed: 2026-08-12T03:35:42Z
arxiv_id: 2608.07645
url: https://huggingface.co/papers/2608.07645
arxiv_url: https://arxiv.org/abs/2608.07645
date: 2026-08-12
---

# Mendel Gödel Machine: Recursive Self-Improving Coding Agents via Comparative Evolution

Self-improving coding agents that iteratively rewrite their own source code have demonstrated impressive performance on coding tasks. However, existing solutions generally derive self-modification from a single failure trajectory at a time, overlooking rich comparative signals available in the agent's expanding archive of past attempts. According to Mendelian principles of controlled inheritance, we introduce Mendel Gödel Machine (MGM). In addition to the general single-trajectory clonal mutation, MGM includes two new types of self-modification that better utilizes evidences accumulated: the reaction-norm mutation edits an agent based on its trajectories on multiple tasks simultaneously, and the cross-lineage hybridization edits an agent using the trajectory of a reference agent from another lineage on the same task. Under an additive fitness landscape model, we prove theoretically and demonstrate via controlled surrogate simulation that the new strategies facilitate a faster and better convergence over single-trajectory baselines. Experiments on SWE-bench and Polyglot confirm MGM's consistent improvement in performance, efficiency, and generalizability.
