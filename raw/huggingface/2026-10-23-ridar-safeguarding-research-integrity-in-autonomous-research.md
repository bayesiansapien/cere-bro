---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.885144+00:00
arxiv_id: 2610.31372
url: https://huggingface.co/papers/2610.31372
arxiv_url: https://arxiv.org/abs/2610.31372
date: 2026-10-23
---

# RIDAR: Safeguarding Research Integrity in Autonomous Research Agents via Automated Detection and Runtime Intervention

Autonomous research agents are increasingly used to automate large portions of scientific research, yet they are prone to research integrity violations (RIVs): behaviors that compromise the validity, reproducibility, or faithfulness of the research process. We present RIDAR, a framework for automated RIV detection and runtime intervention. First, we introduce RIVT, a comprehensive taxonomy of 14 RIV types spanning the full research lifecycle. Building on RIVT, we present RIDAR-post-hoc, a framework to detect RIVs within agent trajectories. RIDAR-post-hoc achieves 85.2% F1 performance on RIV-Gold, a benchmark for RIV detection with 60 expert-annotated trajectories. Applying RIDAR-post-hoc to RIV-Wild, a dataset of 300 agent trajectories across 50 distinct research tasks, we detect 3,964 RIV instances in 99.7% of trajectories, revealing the prevalence of RIVs in current agents. Finally, we present RIDAR-runtime, a framework for dynamically detecting and correcting RIVs during agent runtime. RIDAR-runtime effectively reduces agent RIVs remaining at task completion by 36.8%. We will release our code and data to facilitate future research.
