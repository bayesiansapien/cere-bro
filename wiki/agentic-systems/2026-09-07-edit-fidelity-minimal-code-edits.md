# When Models Edit Too Much: on the fidelity of minimal code edits

**Source:** HuggingFace Daily Papers, 2026-09-07 · [arXiv 2609.04061](https://arxiv.org/abs/2609.04061) · [raw](../../raw/huggingface/2026-09-07-when-models-edit-too-much-on-the-fidelity-of-minimal-code-ed.md)

**TL;DR.** A correct patch is not automatically a good patch. This paper defines **over-editing**, the tendency of a model to rewrite code beyond what the fix required, and builds a way to measure it: take 400 BigCodeBench problems, inject controlled corruptions at the abstract-syntax-tree level into the reference solutions, and you have a repair task with a **known minimal patch** to compare against. Over-editing turns out to be widespread even in strong models including GPT-5.5, and **high Pass@1 coexists comfortably with unnecessarily large edits and added cognitive complexity**. A simple preservation instruction helps a lot: average excess Levenshtein distance falls from **0.195 to 0.131**, added cognitive complexity drops **26.6%**, and Pass@1 goes **up 2.3 points**. Those gains do not come from a bigger reasoning budget or a bigger model. On learning it directly, supervised fine-tuning overfits to the corruption patterns it saw, while reinforcement learning gives the best out-of-domain trade-off between edit fidelity and retained performance.

## Why it matters beyond code review

**It names a quality axis that agent benchmarks do not score, and the correlation with the axis they do score is weak.** Pass@1 and edit minimality come apart, which means a leaderboard climb can be paid for entirely in review burden. For anyone running coding agents at volume, the review cost of a patch is a real operating cost that no benchmark currently prices.

**The preservation-instruction result is a cheap and immediately usable finding.** One sentence in the prompt buys a 33% reduction in excess edit distance, a 26.6% cut in added complexity, **and a small accuracy gain**. A change that improves two quality axes and the accuracy metric at once is rare enough to act on without waiting for a follow-up.

**The SFT-versus-RL split is the third instance of a pattern.** Supervised fine-tuning memorizes the specific corruption families in the training set and fails out of domain; RL generalizes. This wiki has recorded the same shape in the RLVR literature, where outcome-grounded training generalizes past the distribution of the demonstrations. Here the "outcome" is a behavioural constraint rather than a correctness signal, which is a slightly different use of RL and suggests **behavioural properties of code edits are learnable the same way correctness is**.

## Gaps

Injected AST-level corruptions give a clean ground-truth minimal patch, which is exactly what makes the measurement possible and also what limits it: **real bugs do not come with a known minimal repair, and real minimal repairs sometimes require refactoring**. Excess Levenshtein distance treats all extra characters alike, so a model that renames a variable for clarity is scored like one that rewrites a function unnecessarily. And the study measures single-shot repair, not the multi-turn agentic loop where over-editing compounds across iterations, which is the deployment shape that actually generates the review burden.

## Related

- [Agent benchmarks](agent-benchmarks.md) · [Agent harness engineering](agent-harness-engineering.md) · [RL for LLMs](../llms-foundation-models/rl-for-llms.md)
- [Daily digest 2026-09-07](../daily-digest/2026-09/2026-09-07.md)
