# TESSY: Teacher-Student Cooperation Framework for SFT Data Synthesis

**Date:** 2026-04-18  
**Tier:** 1 — Distillation  
**arXiv:** [2604.14164](https://arxiv.org/abs/2604.14164)  
**Raw:** [source](../../raw/huggingface/2026-04-18-how-to-fine-tune-a-reasoning-model-a-teacher-student-coopera.md)

## TL;DR

Using a stronger teacher model to generate SFT data often degrades student performance on reasoning tasks — not because the teacher is wrong, but because the student's generation style is different enough that the data looks like a foreign language to the student's optimizer. TESSY interleaves teacher and student to generate hybrid sequences that inherit the teacher's reasoning while matching the student's stylistic distribution. On code generation, TESSY turns a 10% drop into a 6.7% gain.

## Key Findings

- **Problem identified:** Stylistic divergence between teacher-generated data and the student's distribution. Qwen3-8B fine-tuned on GPT-OSS-120B data drops 3.25% on LiveCodeBench-Pro and 10.02% on OJBench.
- **Mechanism:** TESSY interleaves teacher and student: the teacher generates "non-style" reasoning tokens (the hard thinking), the student generates "style" tokens (the formatting, transitions, intermediate summaries). The resulting sequence is stylistically the student's but intellectually the teacher's.
- **Result:** +11.25% on LiveCodeBench-Pro and +6.68% on OJBench vs. the baseline of just using teacher data.

## Why It Works

A reasoning model has two distinct things to learn: (1) how to think through a problem and (2) how to format that thinking as text. Standard distillation mixes both signals from the teacher, so the student has to fight its own style priors while also learning new reasoning patterns. TESSY decouples this — the teacher only contributes the reasoning content while the student keeps its own output style. This is less about "the teacher knows better" and more about "the teacher knows different things better and the student should keep what it already does well."

The stylistic divergence problem is likely larger for models fine-tuned with RLHF/RLVR because their output styles have been deliberately shaped by reward signals that differ across labs. A GPT-family teacher and a Qwen-family student have learned to present reasoning in recognizably different ways.

## Connection to Prior Work

- **TIP (2026-04-16)**: TIP is about which tokens carry learning signal in distillation. TESSY is about whose tokens (teacher vs student) should appear in training data. Complementary: TESSY generates higher-quality synthetic data, TIP would select the most informative tokens from that data.
- **Cross-Tokenizer Distillation / BLD (2026-04-17)**: BLD handles tokenizer mismatch at inference; TESSY handles distribution mismatch at the sequence level. Both are solving teacher-student friction but at different layers.

## Research Angle

- Does the style/content decomposition generalize to tasks other than code (math, long-form reasoning)?
- Can TESSY be applied iteratively — use the improved student as the next "style" contributor in a subsequent round?
- How sensitive is performance to where the teacher/student boundary is placed within a sequence?

## Related Pages

- [Knowledge Distillation](knowledge-distillation.md)
- [TIP: Token Importance in On-Policy Distillation](2026-04-16-tip-token-importance-on-policy-distillation.md)
- [Cross-Tokenizer Distillation](2026-04-17-cross-tokenizer-distillation-byte-level.md)
