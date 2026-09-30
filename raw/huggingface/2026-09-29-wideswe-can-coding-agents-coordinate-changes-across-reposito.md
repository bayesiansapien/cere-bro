---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.930920+00:00
arxiv_id: 2609.33382
url: https://huggingface.co/papers/2609.33382
arxiv_url: https://arxiv.org/abs/2609.33382
date: 2026-09-29
---

# WideSWE: Can Coding Agents Coordinate Changes Across Repositories?

Coding-agent evaluation has progressed from resolving individual issues to carrying out long-horizon development, yet task completion is still largely assessed within a single codebase. In software ecosystems, many features and bug fixes require coordinated changes across multiple repositories. We introduce WideSWE to evaluate coding agents on such cross-repository tasks. Mining and reviewing changes across 103 software ecosystems yields 120 real-world tasks, balanced between 60 bug fixes and 60 features. We derive prompts from related issues and pull requests. We systematically review and adapt hidden tests to support diverse correct implementations while preserving required behavior and regression checks. Across seven agent configurations, full task success ranges from 10.83% to 42.50%, with the configuration pairing Codex CLI with GPT-5.6-sol achieving the highest rate. Trajectories show agents failing to identify necessary changes, recognizing changes but leaving them unfinished, or modifying the required repositories without fully satisfying the request. To examine whether working on one repository at a time can alleviate these difficulties, we compare it with joint execution under identical prompts. Independent execution mainly recovers omitted work and is less effective at correcting previously attempted but unsuccessful implementations. Joint execution can use information from related repositories to guide implementation and verification. Code is available at https://github.com/ZJU-ACES-ISE/WideSWE.
