# ATESD: Adaptive Teacher Exposure for Self-Distillation in LLM Reasoning

**Source:** HuggingFace Daily Papers · [arXiv 2605.11458](https://arxiv.org/abs/2605.11458)
**Raw:** [farmer file](../../raw/huggingface/2026-05-16-adaptive-teacher-exposure-for-self-distillation-in-llm-reaso.md)
**Tier:** 1 — on-policy self-distillation, reasoning post-training, teacher-side control

## TL;DR

Every on-policy self-distillation (OPSD) method for LLM reasoning gives the teacher the **full reference solution** when supervising the student's rollouts. ATESD argues this is a hidden bug. A controlled fixed-exposure sweep finds two facts: full exposure is not reliably the best choice, and student-teacher mismatch grows monotonically as the teacher sees more privileged reasoning. ATESD makes the **teacher exposure ratio** a learnable training-time control variable, modeled by a Beta-policy controller conditioned on compact training-state statistics. One sampled exposure holds for a short window of student updates; a discounted **learning-progress reward** scores the held decision by its effect on the student's future improvement, addressing the delayed credit assignment of OPSD. On AIME 24, AIME 25, and HMMT 25 across Qwen3-{1.7B, 4B, 8B}: consistent improvements over OPSD of +0.95, +2.05, +2.33 Average@12 points respectively.

## Why it matters

This is the third distillation paper in three days reshaping the teacher signal. **Extrapolation Cliff** (2026-05-14) gave a closed-form policy for when on-policy distillation outperforms on-policy RL based on three measurable training quantities. **SDAR** (2026-05-15) introduced a gated OPSD auxiliary controlled by a sigmoid over detached token-level signals. ATESD now controls **what the teacher sees**, not how the student listens. Three axes of teacher-signal control are now in scope: the exposure on the teacher side (ATESD), the gating on the student side (SDAR), and the choice between OPD and on-policy RL based on the Cliff. None of the three papers composes with the other two; the composition has not been written.

The deeper claim is that the assumption "the teacher should see everything" is the same kind of unexamined default that the wiki tagged as a research target on 04-18 (LongAct: uniform gradient flow is wasteful). Two months later, a structurally identical paper lands one rung up the stack: the teacher's information advantage was also uniform, also wasteful.

## Connections to prior wiki state

- **Extrapolation Cliff** ([2026-05-14](2026-05-14-extrapolation-cliff-on-policy-distillation.md)) — provided the routing rule between OPD and OPRL. ATESD takes the OPD branch as given and asks the next question: given that we are doing OPD, what should the teacher's information exposure be? The combination (Cliff selects branch, ATESD tunes exposure within OPD) is the natural composition.
- **SDAR Self-Distilled Agentic RL** ([2026-05-15](../agentic-systems/2026-05-15-sdar-self-distilled-agentic-rl.md)) — operates on the same OPSD substrate but controls the student-side gate. SDAR + ATESD compose orthogonally: SDAR decides which student tokens absorb teacher signal, ATESD decides which fraction of the reference the teacher sees in the first place.
- **TIP / LongAct / Make Each Token Count** — the "selective dense > uniform dense" thread now spans the gradient axis (LongAct), the token axis (Make Each Token Count, TIP), the cache axis (KV-cache eviction), and now the teacher exposure axis (ATESD). Same pattern at four different layers in two months.
- **DLR latent codes** ([2026-05-15](../ai-routing/2026-05-15-dlr-dynamic-latent-routing-post-training.md)) — the Beta-policy controller in ATESD is structurally similar to a learned routing policy over teacher exposures. ATESD is, in a real sense, a routing problem inside the distillation loop: route between high-exposure and low-exposure teacher signals based on training state.

## How it works

The controller observes a small set of training-state statistics (current student loss, recent improvement, reward margins) and parameterizes a Beta distribution over reveal ratios in [0, 1]. A reveal ratio of 0.3 means the teacher sees 30% of the reference solution before being asked to supervise the rollout, the rest is masked. The controller samples one ratio and holds it for a short window of student updates. Each held decision is scored by a **discounted learning-progress reward**: how much did the student improve in the future, not how much the immediate per-token loss changed. This addresses the delayed credit assignment that single-step rewards cannot solve.

The Beta-policy formulation is convenient: it gives a smooth distribution over a bounded interval, supports policy-gradient updates, and stays well-defined under sparse rewards.

## Open problems / Research angle

- **ATESD for agentic OPSD.** SDAR gated OPSD for multi-turn agents. ATESD's reveal ratio extends naturally: how much of the teacher's full multi-turn trajectory does the student get to condition on? Falsifiable: a follow-up paper that reports SDAR + ATESD jointly tuned for multi-turn benchmarks, with a measurable gain over either alone.
- **Closed-form ATESD via Cliff observables.** The Extrapolation Cliff produced a closed-form predictor for OPD effectiveness from three quantities. Whether an analogous closed-form exists for optimal teacher exposure as a function of the same three observables is the obvious theoretical follow-up. Falsifiable: a paper that derives this and matches ATESD's learned controller within 0.5 Average@12 points.
- **ATESD for cross-modal distillation.** DiffusionOPD (2026-05-15) lifted OPD into continuous-state diffusion models. The reveal-ratio concept extends naturally to image-token grouping. Falsifiable: a paper that applies ATESD-style exposure modulation to T2I distillation with reported quality gains.
- **Curriculum effect.** Does ATESD effectively reverse-engineer a reverse-perplexity curriculum (like SU-01's, 2026-05-15)? Both methods schedule difficulty, but SU-01 schedules the student's input and ATESD schedules the teacher's input. Whether the learned exposure trajectory looks curriculum-like is a one-figure ablation.

## Concept tags

`on-policy-distillation` · `teacher-side-control` · `beta-policy` · `learning-progress-reward` · `selective-dense-signal`
