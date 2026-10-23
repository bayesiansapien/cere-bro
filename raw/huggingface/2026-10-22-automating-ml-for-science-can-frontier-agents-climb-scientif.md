---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.192363+00:00
arxiv_id: 2610.28763
url: https://huggingface.co/papers/2610.28763
arxiv_url: https://arxiv.org/abs/2610.28763
date: 2026-10-22
---

# Automating ML for Science: Can Frontier Agents Climb Scientific Hills in the Wild?

Frontier coding agents are increasingly framed as end-to-end automated researchers, and ML for science offers a demanding test of that promise: improving a scientific model often requires domain insight beyond routine ML engineering. We introduce Agent4Sci, a long-horizon testbed for measuring how far today's agents can improve the published best models on scientific ML benchmarks, spanning 20 benchmarks across 11 domains. Rather than ranking agents on a leaderboard, Agent4Sci asks what kinds of progress agents can make on these tasks under in-the-wild conditions, and where they fall short. Empirically, today's frontier agents advance the published best on every benchmark, with Claude Opus reaching 10.4% mean relative improvement and no run flagged for academic misconduct. These gains, however, come almost entirely from a bag of ML-engineering tricks rather than research-level insight. Trajectory analysis surfaces three recurring limitations in this setting: novelty miscalibration, resource under-utilization, and rapid collapse into local engineering sweeps. Lightweight plug-in skills for research ideation, experiment management, and scheduled checklists raise Claude Opus from 10.4% to 20.1% and Codex from 4.4% to 8.1%, while yielding more diverse, domain-relevant interventions. Agent4Sci gives the community a way to track and push frontier agents from ML engineering toward domain insight on real-world ML-for-science problems. Code and data are available on GitHub (https://github.com/maszhongming/agent4sci) and Hugging Face (https://huggingface.co/datasets/MingZhong/agent4sci).
