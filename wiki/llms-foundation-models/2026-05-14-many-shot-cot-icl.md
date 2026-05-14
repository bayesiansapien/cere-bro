# Many-Shot CoT-ICL: long context as structured curriculum, not retrieval buffer

**Source:** HuggingFace Daily Papers · 2026-05-14
**Paper:** [arXiv 2605.13511](https://arxiv.org/abs/2605.13511)
**Raw:** [raw](../../raw/huggingface/2026-05-14-many-shot-cot-icl-making-in-context-learning-truly-learn.md)
**Tier:** 2. In-context learning, reasoning, long context

## TL;DR

Many-shot in-context learning with chain-of-thought demonstrations does not behave like many-shot ICL on non-reasoning tasks. The paper finds three things: scaling is setting-dependent and unstable for non-reasoning LLMs; similarity-based demonstration retrieval helps on non-reasoning tasks but *fails* on reasoning because semantic similarity poorly predicts procedural compatibility; performance variance grows with more CoT demonstrations. The proposal: many-shot CoT-ICL is in-context test-time learning, not scaled pattern matching. Demonstrations should be (a) easy for the target model to understand and (b) ordered to support a smooth conceptual progression. The Curvilinear Demonstration Selection (CDS) method gives up to 5.42 percentage-point gain on geometry with 64 demonstrations.

## Why it matters

The wiki has been tracking long-context capability since [MMProLong](../inference-efficiency/2026-05-14-mmprolong-long-context-vlm.md) (same day, balanced data mix wins) and [Make Each Token Count](../inference-efficiency/2026-05-12-make-each-token-count-kv-eviction.md) (05-12, full cache is dilutive). Many-Shot CoT-ICL is the third paper in two weeks saying long context is not a uniform substrate. The reframe — long context as *structured curriculum* rather than *retrieval buffer* — is the cleanest version of the argument yet. It connects directly to the Make-Each-Token-Count claim: irrelevant or badly-ordered tokens dilute the useful signal.

## Mechanism

Three findings:

1. **Setting-dependent scaling.** Adding CoT demonstrations is unstable on non-reasoning LLMs and helps reasoning-oriented LLMs. The implication: many-shot CoT works only when the base model can already do test-time learning. It is not a substitute for capability; it is an amplifier.
2. **Semantic similarity fails for procedural transfer.** The standard retrieval move — pick demonstrations most similar to the query — backfires on reasoning. The paper's interpretation: procedural compatibility (does this demonstration's reasoning *pattern* match what the query needs) is orthogonal to semantic similarity (do the words match).
3. **Order-scaling effect.** Performance variance increases with more demonstrations, because demonstration *order* matters. CDS — Curvilinear Demonstration Selection — orders demonstrations to form a smooth conceptual progression. Gain: 5.42 percentage points on geometry with 64 demonstrations.

The framing shift: many-shot CoT-ICL is in-context test-time learning. The model isn't pattern-matching; it's learning. That changes what good demonstration design looks like. The two principles: easy demonstrations for the model + smooth conceptual progression.

## Connections

- **Make Each Token Count** ([2026-05-12](../inference-efficiency/2026-05-12-make-each-token-count-kv-eviction.md)) said the full cache is dilutive. Many-Shot CoT-ICL says the unordered set of demonstrations is dilutive. Both papers reach the same architectural conclusion at different layers: signal needs to be selected and ordered, not aggregated.
- **MMProLong** ([2026-05-14](../inference-efficiency/2026-05-14-mmprolong-long-context-vlm.md)) showed that balanced-length training data beats target-length data for long-context VLMs. Many-Shot CoT-ICL is the in-context analogue: balanced and ordered demonstrations beat similarity-retrieved ones. Two papers in the same week saying the long-context regime rewards balance and structure over volume.
- **AutoTTS** ([2026-05-11](../agentic-systems/2026-05-11-autotts-agentic-discovery-test-time-scaling.md)) discovers test-time scaling controllers. Many-Shot CoT-ICL is the in-context-learning end of the same test-time scaling spectrum. The two papers bracket the design space: AutoTTS designs controllers, CDS orders demonstrations.

## Research angle

1. **CDS as a learned policy.** CDS is described as a "simple ordering method" in the abstract. Whether the ordering rule is learned or hand-designed is unclear. If learned, it is an additional in-context-learning policy that can be trained end-to-end on reasoning tasks. If hand-designed, the natural follow-up is the learned version.
2. **Reasoning-model-specific curriculum.** The setting-dependent finding implies that demonstration design should be conditional on the model's reasoning capability. A 1.7B Qwen3 needs different demonstrations than GPT-5.5. The paper doesn't quantify how the optimal demonstrations vary across models; that variance is the next axis.
3. **Composes with selective KV eviction.** If demonstrations are a curriculum, retaining them under cache pressure should be policy-conditional. Make-Each-Token-Count's learned eviction could keep the demonstrations the model actually used. Untested composition.

## Where it lives

Update [rl-for-llms.md](rl-for-llms.md) — many-shot CoT-ICL as in-context test-time learning is a different framing of the test-time scaling thread; deserves a cross-reference. New material for a future `in-context-learning.md` concept page once a third paper in this thread arrives.
