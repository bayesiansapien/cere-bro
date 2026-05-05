---
source: farmer/huggingface
farmed: 2026-05-05T00:00:00
arxiv_id: 2605.02661
url: https://huggingface.co/papers/2605.02661
arxiv_url: https://arxiv.org/abs/2605.02661
date: 2026-05-05
---

# AcademiClaw: When Students Set Challenges for AI Agents

Benchmarks within the OpenClaw ecosystem have thus far evaluated exclusively assistant-level tasks, leaving the academic-level capabilities of OpenClaw largely unexamined.

The paper introduces AcademiClaw, a bilingual benchmark comprising 80 intricate, multi-step tasks curated from real university student assignments including homework, research projects, and competitions. These 80 tasks were selected from 230 student submissions through expert review and span over 25 professional domains, encompassing olympiad-level mathematics, linguistics, GPU-intensive reinforcement learning, and full-stack system debugging.

Each task executes in an isolated Docker sandbox and is scored on task completion by multi-dimensional rubrics combining six complementary techniques, with an independent five-category safety audit providing additional behavioral analysis.

Testing on six advanced models revealed even the strongest achieved only 55% success rate. The research identifies significant capability variations across different task domains, distinct behavioral patterns among models, and surprisingly, a gap between computational resource consumption and output caliber. The authors have made their data and code publicly available to benefit the broader research community pursuing more capable and adaptable AI agents.
