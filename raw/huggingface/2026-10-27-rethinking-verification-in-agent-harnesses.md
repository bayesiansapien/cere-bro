---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.34577
url: https://huggingface.co/papers/2610.34577
arxiv_url: https://arxiv.org/abs/2610.34577
date: 2026-10-27
---

# Rethinking Verification in Agent Harnesses

Agent harnesses enable large language models to act through tools, observe the results, and iteratively work toward a task goal. Verification checks and revises agents' work to improve output quality. Yet there is limited guidance on how harnesses should organize this effort. We study verification as an axis of test-time scaling by examining when to intervene, who checks the work, and how checking leads to revision. Our framework spans four layers of the agent lifecycle: initial instructions, mid-turn reminders, completion gates, and independent review. We compare 17 designs across seven frontier coding models on Terminal-Bench (TB) and SWE-bench Verified (SWE), and introduce VisualBench for expert evaluation of visual and interactive artifacts. Initial instructions and execution-time reminders yield modest, model-dependent average gains on the coding benchmarks, without substantially increasing average output token use. Completion gates can yield larger gains but may substantially increase cost. Independent review by a critic offers a more favorable accuracy-cost tradeoff, improving average accuracy by 5.9-9.5 percentage points on TB and 3.9-6.6 on SWE at 1.13-1.25 and 1.00-1.04 times baseline cost, respectively. On VisualBench, independent review achieves net preferences of 13.2-23.8 points over the baseline across its four designs, exceeding the evaluated L0-L2 designs. Additional review rounds or independent critics further improve average TB accuracy by up to 3.5 percentage points. Together, these results provide empirical guidance for verification design in agent harnesses and support independent review as a practical axis of test-time scaling.
