---
source: farmer/huggingface
farmed: 2026-11-28T10:45:04+05:30
arxiv_id: 2611.34232
url: https://huggingface.co/papers/2611.34232
arxiv_url: https://arxiv.org/abs/2611.34232
date: 2026-11-27
---

# OS-Omni: Benchmarking Generalist Computer-Using Agents on Long-Horizon Workflows Across Platforms

Computer-using agents are increasingly expected to complete realistic user goals rather than isolated GUI actions. However, existing benchmarks typically isolate web, mobile, or desktop environments, leaving it unclear whether a single generalist agent can execute long-horizon workflows that span multiple operating systems and persistent application states. We introduce OS-Omni, a live cross-platform benchmark and execution environment for evaluating computer-using agents across Windows, Ubuntu, macOS, iOS, Android, and Web environments. OS-Omni is released in versioned waves of 300 tasks each; this paper focuses on the first release, v1, which contains 48 tasks per platform and 12 cross-platform workflows that pair a desktop with an Android phone. OS-Omni provides reproducible initialization, platform-specific adapters, trajectory logging, and executable final-state evaluators, and includes controlled service-backed applications for workflows involving account, cart, budget, calendar, message, and other persistent state. Human studies show that OS-Omni tasks require 67.54 interaction steps, substantially exceeding OSWorld references of 15.0 steps. On v1, the strongest evaluated agent, Claude Opus 5.5, reaches 68.5% average success, trailing the 77.3% human reference by 8.8 points; the gap is uneven across platforms, with frontier models exceeding humans on Linux but trailing them by more than 25 points on iOS and macOS. These results indicate that current agents remain far from platform-robust, long-horizon computer use, especially when success requires sustained state tracking and durable final-state changes.
