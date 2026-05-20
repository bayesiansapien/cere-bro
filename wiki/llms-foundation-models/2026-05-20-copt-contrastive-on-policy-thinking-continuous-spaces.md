# CopT: Contrastive On-Policy Thinking with Continuous Spaces

**Source:** HuggingFace Daily Papers 2026-05-20 · [arXiv 2605.20075](https://arxiv.org/abs/2605.20075) · [raw](../../raw/huggingface/2026-05-20-copt-contrastive-on-policy-thinking-with-continuous-spaces-f.md)

## TL;DR

Standard chain-of-thought treats thinking as a prerequisite for answering: think first, then answer. That delays access to plausible answers and pays token cost even when the model could have identified the answer immediately, a behavior known as performative reasoning. CopT reverses the order. The model first emits a draft answer, then invokes on-policy thinking conditioned on its own draft for reflection and correction. To decide whether the draft is trustworthy, CopT recasts continuous embeddings as inference-time contrastive verifiers: it contrasts the model's support for the same generated tokens under discrete-token versus continuous-embedding inputs, yielding a sequence-level reverse-KL estimator for answer reliability. Under stated assumptions, the expected estimate equals the mutual information between the unresolved latent state and the emitted answer token, which is why it captures answer-relevant uncertainty rather than arbitrary latent-state uncertainty. When the draft is judged unreliable, CopT performs further on-policy thinking with a second KL estimator dynamically controlling draft-answer visibility, preserving useful partial information while reducing the risk of being misled. Across math, code, and agentic reasoning, CopT lifts peak accuracy by up to 23% and cuts token usage by up to 57% at comparable or higher accuracy, with no additional training.

## Why it matters

Test-time compute is the third leg of frontier-model economics, and the standard CoT-then-answer order pays for thinking even when answers are obvious. PUMA (2026-05-19, the semantic-redundancy early-exit method that hit 26.2% token reduction at preserved accuracy) reads reasoning-level redundancy to stop. CopT inverts the problem: it never starts the long thinking unless the draft fails a reliability test. The two compose into a stack: CopT decides whether to think at all, PUMA decides when to stop once thinking is underway.

## Mechanism

Three pieces. (1) **Reverse order:** draft answer first, thinking conditioned on it second. (2) **Continuous-embedding contrastive verifier:** the model evaluates how its own token-level support changes when the input is the discrete token stream versus the continuous embedding stream. The gap is a sequence-level reverse-KL estimator. The paper shows this estimate equals an information-theoretic quantity (the MI between latent state and answer token), giving it semantics rather than empirical heuristic value. (3) **Conditional thinking with controlled visibility:** when the verifier flags the draft as unreliable, the model thinks further; a second KL estimator dynamically masks parts of the draft so the thinking can correct without being anchored.

## Open questions and gaps

The continuous-vs-discrete contrast is computed by reading the model's own representations, which is cheap but model-specific. Whether the MI semantics survive at frontier scale, and whether the verifier degrades under instruction-tuned vs base models, is open. The 23% accuracy lift and 57% token cut are upper-bound across tasks, not means; the per-task variance is the deployment-relevant number.

## Connections

- **PUMA (2026-05-19)** stops thinking once redundancy is detected. CopT decides whether thinking is needed in the first place. Compositional.
- **AntiSD (today)** and **CEPO (today)** work inside RLVR training to sharpen credit at decisive tokens. CopT works at inference time without retraining. Three orthogonal axes on reasoning efficiency landed in one week.
- **NudgeRL (2026-05-18)** and **CIPO (2026-05-18)** changed what gets generated during training. PUMA and CopT change inference-time behavior. The composition stack is now five papers deep: training-time generation (NudgeRL), training-time failure recycling (CIPO), inference-time order (CopT), inference-time stopping (PUMA), inference-time credit shaping (CEPO / AntiSD).
