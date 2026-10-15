---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.502177+00:00
arxiv_id: 2610.14766
url: https://huggingface.co/papers/2610.14766
arxiv_url: https://arxiv.org/abs/2610.14766
date: 2026-10-14
---

# Last Secure Code Benchmark: Is the Code You Vibe Secure?

AI coding agents now write much of the code that ships, yet whether that code is secure remains unclear. We introduce the Last Secure Code Benchmark, a comprehensive evaluation of secure code generation by coding agents. Built from 150 real vulnerabilities, its 450 tasks span seven widely used languages (Java, C, C++, JavaScript, Python, PHP, and Go), 24 CWEs including 21 of the 2025 CWE Top 25 and 8 of the Top 10 KEV weaknesses, more than any benchmark we compare with, and three vibe-coding scenarios: filling in a function, writing a file, and building a repository's source tree from scratch. Every task asks only for functionality, through a specification that never mentions security, and hidden functional and security tests grade the result. Across six frontier agents, 73.6% to 91.3% of tasks pass functionally, yet even the strongest, Claude Fable 5, produces code that is both functional and secure for only 25.1% of tasks, and the others for 16.4% to 24.7%. The best model only passes 12% of the vulnerability scenarios across all vibe coding setting, posing strong concern on the security of the code written by vibe coding.
