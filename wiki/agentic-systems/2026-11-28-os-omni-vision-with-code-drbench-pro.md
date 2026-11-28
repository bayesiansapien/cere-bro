---
title: "OS-Omni, Solve Vision with Code, and DRBench Pro"
date: 2026-11-28
arxiv: [2611.34232, 2611.34813, 2611.34852]
tags: [agent-benchmarks, computer-use, program-synthesis, deep-research]
raw: ../../raw/huggingface/2026-11-27-os-omni-benchmarking-generalist-computer-using-agents-on-lon.md
---

# OS-Omni, Solve Vision with Code, and DRBench Pro

**TL;DR.** Three Hugging Face benchmark papers from the 11-27 list.

- **OS-Omni** ([2611.34232](https://arxiv.org/abs/2611.34232), 104 upvotes). A live cross-platform computer-use benchmark: Windows, Ubuntu, macOS, iOS, Android, Web, released in waves of 300 tasks (v1: 48 per platform plus 12 desktop-plus-phone workflows). Tasks need 67.5 human steps vs 15.0 for OSWorld, and are scored by executable final-state checks on service-backed apps (cart, budget, calendar). Claude Opus 5.5 leads at 68.5% vs 77.3% human. Frontier models beat humans on Linux (Gemini 4 Argon 95.8% vs 74.6%) but trail by 25+ points on iOS and macOS (Argon falls to 18.8% on iOS, per AI Weekly).
- **Solve Vision with Code** ([2611.34813](https://arxiv.org/abs/2611.34813)). Same first frame, prompt and rule-based evaluator for video models and for coding agents that write a program to render the answer video. On the 500-item VBVR-Pro-Bench, Codex with gpt-6-astra scores 0.923, Claude Code with Fable 5.1 0.894, Gemini CLI 0.893, each 0.22+ above the best video model. Best open-weight agent (GLM-5) 0.572.
- **DRBench Pro** ([2611.34852](https://arxiv.org/abs/2611.34852)). Knowledge-tree rubrics (44,102 rubrics, 144 cases, 24 domains) measure breadth and depth of a deep-research report. Best of 16 agents reaches 57.04% coverage.

## How this relates to prior wiki pages

- OS-Omni's platform gap extends [gui-agents](gui-agents.md) and the 11-26 [where-evals-break](2026-11-26-where-evals-break-yan-gdpx-owe-bench.md) theme: a single average hides a 77-point spread across platforms. The likely driver is training-data mix (Linux shells are abundant, iOS traces are not).
- Solve Vision with Code is a cost result in disguise: a program that renders the answer is far cheaper to run and verify than denoising pixels. Same direction as the 11-25 "plain records plus code search" memory result on [agent-memory](agent-memory.md): code as the reasoning medium keeps winning.

Related: [agent-benchmarks](agent-benchmarks.md)
