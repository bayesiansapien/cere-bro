# Claw-SWE-Bench: A Benchmark for Evaluating OpenClaw-style Agent Harnesses on Coding Tasks

**TL;DR.** General-purpose agents like OpenClaw are increasingly used as autonomous coders, but they do not natively satisfy SWE-bench's clean Docker-workspace, patch, and prediction contract, so their coding ability is hard to measure fairly. Claw-SWE-Bench is a multilingual SWE-bench-style benchmark plus an adapter protocol that makes heterogeneous agent harnesses ("claws") comparable under fixed conditions (fixed prompt, runtime budget, workspace contract, patch extraction, evaluator). It has 350 issue-resolution instances across 8 languages and 43 repos, plus an 80-instance Lite subset. The headline: OpenClaw with a minimal direct-diff adapter scores only 19.1% Pass@1, but the *full* adapter reaches 73.4% with the same GLM 5.1 backbone — harness design moves Pass@1 by 27.4 points, and model choice by 29.4 points. Cost varies widely between systems of similar accuracy.

**Source:** HuggingFace Daily Papers · arxiv [2606.12344](https://arxiv.org/abs/2606.12344)

## Key findings

- **Harness is a first-class axis, not scaffolding.** Same model, same tasks: adapter design alone swings Pass@1 from 19.1% to 73.4%. Harness choice (27.4 pp) is nearly as large a lever as model choice (29.4 pp).
- **Fair comparison protocol.** A fixed prompt, runtime budget, workspace contract, patch-extraction procedure, and evaluator let different agent harnesses be compared without one winning on plumbing.
- **Cost as a metric.** Systems with similar accuracy can differ substantially in total API cost; Claw-SWE-Bench treats cost accounting as a first-class evaluation axis.

## How this relates to prior wiki knowledge

This is the **measurement** counterpart to the 06-11 substrate cluster. [DeNovoSWE](2026-06-11-denovoswe-whole-repo-generation.md) builds long-horizon coding *training data*; Claw-SWE-Bench measures whether a harness *uses* its model and data well. Its core finding — harness moves the score as much as the model — is the empirical confirmation of the [self-evolving agents](self-evolving-agents.md) page's load-bearing 06-08 result from [Disentangling Agent Self-Evolution](2026-06-08-disentangling-agent-self-evolution.md): harness-benefit is a real, large, separable axis. It also gives the [agent benchmarks](agent-benchmarks.md) thread a cost-aware, harness-aware evaluation standard, which the wiki's "evals don't predict deployment" worry has been asking for.

→ Raw: [`raw/huggingface/2026-06-11-claw-swe-bench-a-benchmark-for-evaluating-openclaw-style-age.md`](../../raw/huggingface/2026-06-11-claw-swe-bench-a-benchmark-for-evaluating-openclaw-style-age.md)
