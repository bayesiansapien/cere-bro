# PUMA: Semantic-Preserving Early Exit for Reasoning Models

**arXiv:** [2605.17672](https://arxiv.org/abs/2605.17672) · **HF:** [paper page](https://huggingface.co/papers/2605.17672) · **Tier:** 1 (reasoning efficiency, early exit, test-time compute)

## TL;DR

Existing inference-time early-exit methods for Large Reasoning Models (LRMs) rely on answer-level signals (confidence, trial-answer consistency) which reflect answer readiness rather than reasoning convergence. PUMA identifies reasoning-level semantic redundancy as a complementary signal: when successive steps add no novel progress and instead revisit established conclusions, the reasoning trajectory has converged. PUMA pairs a lightweight Redundancy Detector with answer-level verification: the detector flags semantically redundant candidate exits and verification confirms safety. Across five LRMs and five reasoning benchmarks it reduces tokens by 26.2% average while preserving accuracy and a coherent retained CoT.

## Key findings

- LRMs often "overthink": they keep reasoning after a solution has stabilized, wasting tokens and increasing latency. Answer-level early-exit signals trigger before the model has finished exploring or self-correcting, which causes premature exits that degrade accuracy and leave the retained CoT semantically incomplete.
- The complementary signal is reasoning-level semantic redundancy. The trajectory has converged when successive steps no longer add novel progress and start revisiting established conclusions.
- PUMA is plug-and-play: a lightweight Redundancy Detector identifies candidate exits; answer-level verification gates the actual exit. Stopping is conditioned on both reasoning saturation and answer correctness, not either alone.
- Across five LRMs and five challenging reasoning benchmarks, PUMA cuts tokens by an average 26.2% while preserving accuracy and the coherence of the retained reasoning prefix.
- Generalises beyond math: PUMA works on code generation, zero-shot vision-language reasoning, and shows that the stopping policy can be internalised (learned into the model rather than applied as an external detector).

## Relationship to prior wiki entries

PUMA is the test-time-compute companion to the wiki's running RLVR thread. CIPO (2026-05-18, the paper that mines on-policy failed trajectories and converts them into correction-oriented supervision by pairing each failed prefix with a correct continuation from the same model's adjacent success rollouts) and NudgeRL (2026-05-18, the paper that conditions each rollout on a lightweight strategy-level context and matches vanilla GRPO at 8x larger rollout budgets) attack the train-time end of reasoning efficiency. PUMA attacks the inference-time end. The three are orthogonal: NudgeRL diversifies what gets generated, CIPO recycles the failures, PUMA stops the generation when it converges.

PUMA is also the third entry in the wiki's "early exit on LRMs" thread, following the 2026-04-25 SpecExitVLM and 2026-05-13 layer-wise CoT early-exit paper. PUMA's contribution is the reasoning-level redundancy signal, which prior methods treated implicitly via answer-level proxies.

The 26.2% token reduction matches the magnitude RLVR weak-supervision (2026-04-21, the paper that argued RLVR mostly redistributes probability mass rather than expanding reasoning capacity) predicted should be available if reasoning chains carry significant redundant probability mass. PUMA quantifies that the answer is yes, the redundancy is real and detectable from CoT semantics alone.

## Why it matters

Test-time compute is the third leg of frontier model economics (the other two are parameter scaling and post-training compute). LRMs spend most of that compute on the long CoT. A 26.2% reduction at preserved accuracy is large enough that it dominates ad-hoc tricks like reducing temperature or hard-capping max tokens. Reasoning-level signals also have the advantage of being interpretable: the operator can audit which steps were flagged redundant, unlike answer-confidence which is opaque.

## Research angle

- **Compose PUMA with CIPO and NudgeRL.** PUMA stops at convergence. CIPO recycles failures. NudgeRL diversifies exploration. The full composition is one training-and-serving recipe. Diagnostic: pass@K under the composed system versus the sum of individual contributions.
- **Redundancy as a training signal.** The paper shows the policy can internalise the stopping rule. The natural extension is to use redundancy detection as a reward during RLVR, encouraging the model to avoid generating redundant continuations in the first place.
- **Cross-domain transfer.** PUMA generalises to code and vision-language. Whether the same Redundancy Detector trained on math generalises zero-shot to code is the deployment-relevant transfer question.

## Source

`raw/huggingface/2026-05-19-stop-when-reasoning-converges-semantic-preserving-early-exit.md`
