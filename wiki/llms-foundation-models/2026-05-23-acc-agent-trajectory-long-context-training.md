# ACC: Compiling Agent Trajectories for Long-Context Training

**Source:** HuggingFace daily papers, 2026-05-23.
**arxiv:** [2605.21850](https://arxiv.org/abs/2605.21850)

## TL;DR

Standard agent SFT (supervised fine-tuning) masks tool responses and only trains on turn-level tool selection. ACC (Agent Context Compilation) flips this: it converts long agent trajectories (search, software engineering, database querying) into long-context QA pairs where the original question is paired with all the gathered tool responses and environment observations, training the model to answer directly without invoking tools. This makes the dependency between question and scattered evidence explicit, providing direct supervision of long-context reasoning. Training Qwen3-30B-A3B with ACC achieves 68.3 on MRCR (+18.1 over baseline) and 77.5 on GraphWalks (+7.6), comparable to Qwen3-235B-A22B while preserving general capabilities on GPQA, MMLU-Pro, AIME, and IFEval.

## What this paper does that prior agent SFT did not

Two insights compose:

1. **Agents already produce long-context training data.** Every multi-turn agent trajectory is a sequence where evidence for the original question is scattered across distant tool responses. That is exactly the input distribution that long-context models need to learn on. But standard agent SFT throws it away by masking tool outputs.

2. **Direct-answer training is the right supervision signal.** Rather than learn to call the next tool, the model learns to integrate all retrieved evidence and answer in one shot. This converts a tool-using trajectory into a long-context QA pair, no additional annotation needed.

Mechanism analysis reveals that ACC-trained models show task-adaptive attention restructuring and expert specialization (this is an MoE model). The trained 30B-A3B model matches the 235B-A22B model on the targeted long-context benchmarks while keeping general capabilities intact.

## Connections to prior wiki state

This is the most direct answer yet to a question that [LongAct (04-18, the paper that showed long-context training signal is concentrated in the first 5% of tokens)](../inference-efficiency/2026-04-18-longact-saliency-sparse-rl.md) raised: where do you get high-quality long-context training data without manual curation? LongAct attacked the question on the gradient side (where in the long context does signal concentrate). ACC attacks it on the data side (where do you get long-context examples in the first place). Agents are the answer — they generate trajectories where the dependency between input and answer is naturally long-range.

There is also a clean alignment with [TIP (04-16, on-policy distillation showing 10% of teacher tokens carry signal)](../inference-efficiency/2026-04-16-tip-token-importance-on-policy-distillation.md). Both argue against blanket masking and for selective use of available signal. ACC unmasks agent trajectories; TIP selectively keeps high-signal tokens during distillation. The pattern: agent-era SFT pipelines waste a lot of supervision through reflexive masking conventions inherited from pre-agent SFT.

For Tier 1 efficiency: a 30B-A3B model matching a 235B-A22B model is a 7x parameter compression at equal accuracy. If ACC composes with existing long-context inference tricks (KVServe-style adaptive compression, RTPurbo sparsification, Gated DeltaNet-2 recurrent state), the unit economics for long-context Qwen-style models improve sharply.

## Gaps

The "comparable to Qwen3-235B-A22B" claim is on the targeted benchmarks (MRCR, GraphWalks). Whether the smaller ACC-trained model matches the larger model on broader long-context evaluations (RULER full suite, LongBench v2) is not reported in the abstract. The general-capability preservation on GPQA / MMLU-Pro / AIME / IFEval is reassuring but says nothing about whether the model retains tool-use capability (since ACC explicitly trains for direct answering).

## Research angle

The obvious follow-up: does an ACC-trained model lose tool-use capability? If yes, ACC is best used as a curriculum step (long-context SFT first, then agent SFT on top). If no, the field has been training agents wrong for a year — direct-answer supervision on agent trajectories is a strict generalization of tool-call supervision.

A deeper open question: agent trajectories are heterogeneous in the kind of long-range dependency they exercise (search trajectories are retrieval-heavy, SWE trajectories are tool-execution heavy). Whether one ACC training mix transfers across trajectory types, or whether per-domain ACC datasets are required, is unaddressed.

## Raw source

[raw/huggingface/2026-05-23-acc-compiling-agent-trajectories-for-long-context-training.md](../../raw/huggingface/2026-05-23-acc-compiling-agent-trajectories-for-long-context-training.md)
