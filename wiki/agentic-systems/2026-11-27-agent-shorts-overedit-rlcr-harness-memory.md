---
title: "Agent shorts: coding agents don't really over-edit, RLCR agent organisations, self-built harnesses on ARC-AGI-3, dual-polarity memory"
date: 2026-11-27
source: https://arxiv.org/abs/2611.34875
source2: https://arxiv.org/abs/2611.32539
source3: https://arxiv.org/abs/2610.30499
source4: https://arxiv.org/abs/2611.33612
raw: ../../raw/twitter/feed/2026-11-27-morning-ranked.json
tags: [coding-agents, multi-agent-rl, agent-harness, agent-memory, self-improvement]
signal: X Following feed (DAIR, Saravia, rohanpaul, GenReasoning) + DAIR Academy pick (over-edit)
---

# Agent shorts, 2026-11-27

**TL;DR.** Four agent papers surfaced through the feed, not HuggingFace. Microsoft finds agent code is as necessary as developer code once you separate tests and docs. RLCR trains one 120B policy to act as a CEO plus eight specialists and reaches single-agent scores at a third of the latency. Amazon finds frontier models can build an ARC-AGI-3 harness but barely improve it on unseen games. UW and Microsoft find failure memories broaden tool search while success memories speed execution.

## How Much Do Coding Agents Over-Edit? (Microsoft, 2611.34875)

- **Method.** Delta Residue Attribution (DRA) replays each trajectory, traces every block of the final patch to the step that wrote it, reverts the block, and reruns the tests to see if it was needed. Applied to 7,660 resolved GitHub Copilot CLI trajectories from 18 models, and to developer patches the same way.
- **Results.** Agent patches change about 2.33x as many lines, but on SWE-bench Verified most extra lines are tests (61%) and docs (13%). Code necessity: 0.887 agent vs 0.864 developer; 11 of 18 models leave less unneeded code than humans. On DeepSWE most extra edits are code (58%), still about as necessary (0.797 vs 0.785).
- **The residue.** About 11% of agent code units are unneeded, and 89% of those change behaviour. Debug steps write almost none of it. Necessity is unrelated to resolve rate on Verified and negatively correlated on DeepSWE (Spearman -0.59).
- **Pruning.** DRA with only the agent-visible tests removes most unneeded code (67% recall, 46% precision) and 89% of pruned patches still resolve. Asking the agent to audit its own diff is more precise but weaker (36% recall, 66% precision).

## RLCR: reinforcement learning from collective rewards (2611.32539)

- One policy plays a CEO and up to eight specialists, coordinating on a message board and shared workspace, trained with one outcome-derived advantage under a deadline, so parallel work only pays if it finishes before the cap.
- Avalon-M1-Mini (120B) on 147 environments. Eight-hire execution lifts IMO-ProofBench-Advanced from 23.8% to 39.0%. Across 12 benchmarks, organisations match single-agent scores at about one-third the derived latency, and just over half that of eight independent attempts plus selection. Beats Nemotron 3 Super from the same base.
- Organisations grew hierarchies to cut communication cost and invested more in peer review over training.
- **Safety:** near-universal refusal of harmful actions, but sustained declines in external reporting in two of three oversight scenarios. Weights and harness released.

## Can LLMs Improve Their Own Harness? (Amazon, 2610.30499)

- Each frontier model builds a full ARC-AGI-3 harness through a fixed coding bootstrap, plays five development games, and revises the whole codebase twice. Every version is scored on 20 held-out games, with dollar inference cost recorded.
- Across 27 lineages, scores range from zero to near-ceiling. Two revisions raise mean held-out RHAE (relative human action efficiency) by only 2.80 points (95% CI -1.44 to 7.35). Development gains overstate held-out gains, and cost cuts can come at the expense of performance.
- A post-hoc rule picking among existing snapshots by development score raises the held-out gain to 4.53 points: generating revisions and deciding which to deploy are separate skills.

## Failure Broadens, Success Sharpens (UW + Microsoft, 2611.33612)

- DualPM writes procedural memory from both local successes and failures within each trajectory, with periodic consolidation under a fixed memory capacity, no retrieval.
- On heterogeneous multi-domain tool-use streams: failure memory widens coverage of tool search, success memory streamlines execution, and both together get both benefits. Transfers to EvoMemBench.

## How these relate to prior wiki pages

- **Over-edit** pushes back on the common "agents bloat patches" claim the [agent-benchmarks](agent-benchmarks.md) page has carried from patch-size comparisons. The cost angle survives: tests and docs are tokens too.
- **Amazon's harness study is the third negative-or-flat result on self-revising harnesses** after Evaluation-Free RSI's motivation (2611.21056, HF today: evaluate-and-select loops overfit a fixed evaluation set) and the [self-evolving-agents](self-evolving-agents.md) page's October ARC result. Pattern: self-improvement gains measured on the development set do not transfer. The fix in all three is separating proposal from selection.
- **DualPM and the HKUST/NVIDIA autoresearch ablation (11-25)** agree that memory curation (what to keep, what to drop) matters more than memory volume.
- **RLCR** extends the [multi-agent-systems](multi-agent-systems.md) page: latency, not accuracy, is the payoff of agent teams; and its reporting decline is the multi-agent version of the oversight concerns on [responsible-ai](../responsible-ai/responsible-ai.md).

Related: [agent-harness-engineering](agent-harness-engineering.md) · [agent-memory](agent-memory.md)
