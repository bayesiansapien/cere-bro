---
source: farmer/huggingface
farmed: 2026-06-12T09:05:40Z
arxiv_id: 2606.12087
url: https://huggingface.co/papers/2606.12087
arxiv_url: https://arxiv.org/abs/2606.12087
date: 2026-06-12
---

# FORT-Searcher: Synthesizing Shortcut-Resistant Search Tasks for Training Deep Search Agents

Training deep search agents requires verifiable questions whose answers remain unavailable until sufficient evidence has been acquired through search. Existing synthesis methods often increase apparent difficulty by enriching graph structures, but structural complexity alone does not guarantee realized search difficulty: the intended search process can collapse through a cheaper identifying route. We formalize this gap with a shortcut-aware difficulty framework and identify four actionable shortcut risks: evidence co-coverage, single-clue selectivity, exposed constants, and prior-knowledge binding. To diagnose their realized effects, we use trajectory signatures including solving cost, answer hit time, and prior-shortcut rate. Guided by this framework, we introduce FORT, a Framework of Shortcut-Resistant Training-Data Synthesis. FORT constructs shortcut-resistant training data by controlling shortcut risks across entity selection, evidence graph construction, question formulation, and adversarial refinement. Experiments show that FORT induces longer pre-answer search and fewer shortcut patterns than existing open-source deep search datasets. Using the resulting trajectories, we train FORT-Searcher with supervised fine-tuning (SFT) only, and it achieves the best overall performance among comparable-size open-source search agents on challenging deep search benchmarks. Relevant resources will be made available at https://github.com/RUCAIBox/FORT-Searcher.
