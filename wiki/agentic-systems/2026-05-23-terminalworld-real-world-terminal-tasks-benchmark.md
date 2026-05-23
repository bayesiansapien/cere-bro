# TerminalWorld: Benchmarking Agents on Real-World Terminal Tasks

**Source:** HuggingFace daily papers, 2026-05-23.
**arxiv:** [2605.22535](https://arxiv.org/abs/2605.22535)

## TL;DR

TerminalWorld is an automated data engine that reverse-engineers high-fidelity evaluation tasks from 80,870 in-the-wild terminal recordings. The result is a benchmark of 1,530 validated tasks across 18 real-world categories, ranging from short operations to workflows exceeding 50 steps and covering 1,280 unique commands. The Verified subset (200 representative manually-reviewed tasks) finds that across eight frontier models and six agents, the maximum pass rate is only 62.5%. TerminalWorld captures capabilities distinct from expert-curated benchmarks: only weak correlation (Pearson r=0.20) with Terminal-Bench. The automated data engine makes the benchmark scalable as developer practice evolves.

## Why this matters

The wiki has tracked the agent-benchmark thread since the 04-17 Dive-into-Claude-Code design-space paper. The pattern across recent agent benchmarks (SaaSBench 05-21, SpecBench 05-21, EnvFactory 05-20, OpenComputer 05-20, AutoResearchClaw 05-20) is the move from expert-curated test sets to scalable real-world capture. TerminalWorld extends the pattern to the terminal modality: 80K real recordings reverse-engineered into 1.5K validated tasks.

The 62.5% ceiling on the Verified subset is the load-bearing claim. Frontier models on a real terminal benchmark cap below two-thirds. The r=0.20 correlation with Terminal-Bench is the deeper claim: expert-curated benchmarks underspecify what terminal agents actually fail at in production. Two different benchmarks measure two different things.

## Connections to prior wiki state

- [SaaSBench (2026-05-21)](2026-05-21-saasbench-enterprise-saas-coding-agents.md): same pattern: real enterprise workflows reverse-engineered into agent tests.
- [SpecBench (2026-05-21)](2026-05-21-specbench-reward-hacking-coding-agents.md): testing for reward hacking and gaming.
- [OpenComputer (2026-05-20)](2026-05-20-opencomputer-verifiable-software-worlds.md): verifiable software environments.
- [EnvFactory (2026-05-20)](2026-05-20-envfactory-tool-use-agents-executable-environments.md): executable env synthesis.

Five papers in three weeks ship a real-world-derived agent benchmark. The community has converged that expert-curated test sets miss too much.

## Gaps

The Verified subset is 200 tasks. Maximum pass rate on the full 1,530 tasks is not reported in the abstract. The "weak correlation with Terminal-Bench" claim wants per-category decomposition: which task categories drive the divergence? If TerminalWorld is harder on long-step workflows (50+ steps) and Terminal-Bench is easier on those, the correlation gap may be driven by horizon, not coverage.

## Research angle

If TerminalWorld plateaus production-frontier models at 62.5%, the gap is exactly where the next year of agent engineering will concentrate. Worth checking in 90 days: which lab clears 75% first, and on which task category.

## Raw source

[raw/huggingface/2026-05-23-terminalworld-benchmarking-agents-on-real-world-terminal-tas.md](../../raw/huggingface/2026-05-23-terminalworld-benchmarking-agents-on-real-world-terminal-tas.md)
