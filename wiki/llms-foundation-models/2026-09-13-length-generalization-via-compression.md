# Length Generalization for Transformers via Compression

**Source:** arXiv [2609.08851](http://arxiv.org/abs/2609.08851), Georg Zetzsche, Hongjian Jiang, Andy Yang, Pascal Bergsträßer, Marco Sälzer et al., published 2026-09-08. Kurate cs.LG #9, ai_rating 6.5/10. Absent from HuggingFace Daily Papers. Raw: [`raw/kurate/2026-09-13-cs-lg.md`](../../raw/kurate/2026-09-13-cs-lg.md).

**TL;DR.** There is a theory that predicts when a transformer will generalize to sequences longer than it was trained on: the C-RASP hypothesis, which says length generalization happens if and only if a solution to the task can be written in the C-RASP language (a formal language designed to express exactly what a transformer can compute). The theory had two problems. No computable bound existed on how much training data length generalization would require, and some experiments appeared to contradict it. This paper fixes both by an exponential tightening of the sample-complexity bound, from double-exponential down to **polynomial, provided you measure the strings in compressed form**, via a connection to power words. The compression is not an engineering trick applied to the model; it is the representation in which the bound becomes tractable, and choosing it is what dissolves the apparent experimental contradictions.

---

## What it claims

**The setting.** C-RASP+ and C-RASP1 are recently proposed fragments of C-RASP that do have computable length-generalization bounds, but those bounds require, in the worst case, a **double-exponential** number of samples. Whether that was tight was open.

**The result.** It is not tight. The paper gives an exponentially tighter bound, and shows a **polynomial** length-generalization bound for transformers when strings are represented in compressed form. The route is a connection to **power words**, strings written as products of repeated blocks (think `(ab)^n` rather than `ababab...`). A length-n string with structure has a compressed description far shorter than n, and the sample complexity tracks the compressed length rather than the raw one.

**The application, which is the part that matters empirically.** With the tighter bound in hand, the authors give a fine-grained analysis of the C-RASP conjecture that resolves the contradicting experimental evidence against it. The apparent counterexamples were tasks where the raw length and the compressed length diverge sharply, so measuring sample complexity against raw length made the theory look wrong.

---

## How this relates to prior wiki pages

**It is a compression result that is not an efficiency result, and that distinction is worth keeping.** This wiki's [quantization](../inference-efficiency/quantization.md), [pruning](../inference-efficiency/model-pruning-sparsity.md) and [KV cache](../inference-efficiency/kv-cache.md) pages all use "compression" to mean *spend fewer bytes for the same behaviour*. Here compression is the **coordinate system in which a learning-theoretic quantity becomes small**. The two uses are not obviously related, and it would be easy to force a connection that is not there. The honest statement is narrower and more interesting: **both are claims that the naive length of an object overstates its true complexity**, and both find that the right measure of size is a compressed one. Whether a sequence whose compressed description is short is also a sequence whose KV cache is compressible is an open and, as far as this wiki records, unasked question.

**It sits on the theory side of a gap the [scaling laws page](scaling-laws.md) has been widening.** That page records a run of results arguing the received scaling law is misspecified in ways that matter (Skaling's additive form on 08-10, LLaDA's cross-objective transfer failure on 08-05, and SMELT's 09-02 argument that architecture belongs inside the law). Those are all empirical fits failing. This is a case where **theory makes a prediction precise enough to be wrong, gets tested, appears to fail, and is rescued by fixing the measurement rather than the theory.** That is a healthier epistemic position than the scaling-law literature currently occupies, and the contrast is the reason to keep this page.

**It bears on long-context claims generally.** Every "1M context" announcement this wiki has recorded is a claim about what a model can attend to, not about what it can generalize over. C-RASP-style theory is the only line of work that says anything predictive about the second, and a polynomial bound makes it, in principle, checkable for specific tasks before you train.

## Gaps

Worst-case bounds on formal-language fragments, with no experiments on real models at real scale, and the paper does not claim any. C-RASP1 and C-RASP+ are fragments, so the improvement does not automatically lift to full C-RASP. And the polynomial bound is contingent on the compressed representation, which means the practical question (is the compressed length of the sequences I care about actually small) is pushed entirely outside the theory.

## Industrial implication

Little in the short term. The medium-term value is as a **pre-training triage instrument**: if a task's target behaviour has a short C-RASP+ description and its inputs compress well, length generalization is predicted and cheap to obtain; if not, no amount of longer-context training data is the answer and the architecture has to change. Almost nobody currently runs that check before committing a long-context training budget.

## Related pages

- [Scaling laws](scaling-laws.md)
- [Attention mechanisms](attention-mechanisms.md)
- [Looped transformers](looped-transformers.md)
