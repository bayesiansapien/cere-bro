---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.07557
url: https://huggingface.co/papers/2610.07557
arxiv_url: https://arxiv.org/abs/2610.07557
date: 2026-10-07
---

# CheckerBench: Can Long-Horizon Agents Synthesize Static-Analysis Checkers?

Static-analysis checker synthesis requires agents to interpret a defect specification, inspect a repository, implement analyzer-specific logic, and refine the checker through repeated compilation and analysis feedback. Existing coding-agent benchmarks focus on tasks such as patch generation or vulnerability detection and rarely assess whether an agent can develop a working checker in a repository from start to finish. We introduce CheckerBench, an executable benchmark of 300 tasks derived from 297 CVEs across 167 repositories, 85 CWEs, and five language ecosystems. Each task includes vulnerable and fixed revisions, a pinned analysis environment, and a checker scaffold. We further introduce CheckerLab, a common evaluation framework that independently rebuilds submitted checkers and measures vulnerable-fixed diagnostic contrast, patch localization, false positives, and tool use. Across 21 model-harness configurations and three independent repeats per configuration, mean Pass@1 is 32.30%, while the best reaches 45.33%. These results show that reliable, reusable checker development remains challenging for current coding agents.
