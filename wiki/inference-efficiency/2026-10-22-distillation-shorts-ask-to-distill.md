# Distillation shorts: Ask-to-Distill, privileged information for self-distillation, ProD, Projected Distillation

**Sources:** HuggingFace daily papers 2026-10-20/21: [Ask to Distill, 2610.27450](https://arxiv.org/abs/2610.27450); [Predicting Privileged Information Effectiveness for On-Policy Self-Distillation, 2610.22512](https://arxiv.org/abs/2610.22512); [Progress-Aware Distillation (ProD), 2610.19439](https://arxiv.org/abs/2610.19439). Kurate this week: [Projected Distillation, 2610.27467](https://arxiv.org/abs/2610.27467) (cs.LG #3); [Not Every Rollout Needs Distillation, 2610.25842](https://arxiv.org/abs/2610.25842) (cs.AI #7). Raw: `raw/huggingface/2026-10-2[01]-*`, `raw/kurate/2026-10-22-cs-*.md`.

## TL;DR

- **Ask to Distill**: on-policy distillation (OPD, the student generates and the teacher grades each token) works with surprisingly few questions, so questions are carriers of the teacher's distribution. A student-initialized question synthesizer is trained on a surrogate value: teacher-student disagreement plus teacher probability mass on the student's candidates, with length and diversity controls. No reference answers needed. The synthetic prompt bank matches or beats a real-question bank for OPD on math, code and agentic tasks, and elicits denser signal from shorter student responses.
- **Privileged information (PI) for self-distillation**: 16 PI configurations across three multi-turn agent benchmarks. Dense trajectories and PI from stronger generators help most; thinking models benefit less. A KL-based pre-training metric (error-step KL contrast) predicts post-training gains better than PI "utility", which is distorted by leakage, and picking PI by it beats random.
- **ProD**: SFT-distilled small agents (0.6B-8B) get stuck in loops on long trajectories ("progress stagnation"). ProD detects stagnation and penalizes it with an adaptive margin set by the student-teacher stagnation gap. Gains in- and out-of-domain across 8 SLMs.
- **Kurate picks:** Projected Distillation (learn hard problems from close, correct targets) and correctness-filtered on-policy self-distillation (skip rollouts that are already wrong).

## How this relates to prior wiki pages

- **Continues the "where is the signal" thread on [knowledge-distillation](knowledge-distillation.md)** that started with TIP (04-16: most teacher tokens carry no signal, train on 10%). Ask-to-Distill moves the selection to the question; correctness-filtered self-distillation moves it to the rollout. Three levels now: token (TIP), rollout (Kurate #7), prompt (Ask-to-Distill).
- **ProD connects to the agent-memory pattern today**: loops and repeated failed strategies are the same failure whether they come from bad stored abstractions (Anti-Persistence) or weak distillation.

## Gaps

- None of the abstracts report wall-clock or token cost of the distillation itself, which matters for Ask-to-Distill's synthesizer training.
