# How LoRA Remembers: A Parametric Memory Law for LLM Finetuning

**arXiv:** [2605.30260](https://arxiv.org/abs/2605.30260) · **HF Daily Papers:** [page](https://huggingface.co/papers/2605.30260) · **Date:** 2026-05-31
**Code:** https://github.com/zjunlp/ParametricMemoryLaw
**Raw:** [farmer file](../../raw/huggingface/2026-05-31-how-lora-remembers-a-parametric-memory-law-for-llm-finetunin.md)

## TL;DR

LoRA (Low-Rank Adaptation, the dominant way to cheaply fine-tune an LLM by training a small low-rank weight delta) is used everywhere for injecting new knowledge, but its memorization behavior has only been studied qualitatively through downstream task scores. This paper turns LoRA into a controlled *capacity probe* and measures exact parametric memory directly. The result is the Parametric Memory Law: a power law linking loss reduction ΔL to effective parameters and sequence length. At the token level, a sharper finding appears: a deterministic phase transition where a prediction probability of p > 0.5 is a *sufficient* condition for verbatim recall under greedy decoding. Because recall is gated at a threshold, training budget spent pushing already-above-threshold tokens is wasted. The authors turn that into MemFT, a threshold-guided strategy that dynamically redistributes the training budget toward sub-threshold tokens, improving both memory fidelity and efficiency.

## The mechanism

```
Parametric Memory Law:
  ΔL  ∝  (effective parameters)^a · (sequence length)^b      ← smooth power law

Token-level phase transition (the sharp part):
  p(token) ─────────────┬──────────────► p < 0.5 : NOT reliably recalled
                        0.5 threshold
                         └──────────────► p > 0.5 : verbatim recall (greedy)  ✓

MemFT (act on the threshold):
  per token, check p
     p already > 0.5  ─► stop spending budget here  (recall is locked in)
     p still < 0.5    ─► redistribute budget HERE   (push it over the line)
  ⇒ higher memory fidelity at lower cost
```

## What problem it solves

Teams fine-tune LoRA adapters to make a model "remember" new facts, policies, or documents, then evaluate with downstream accuracy and hope. There has been no quantitative account of *how much* a given LoRA rank and training length can memorize, or *when* a fact crosses from "approximately learned" to "reliably reproduced." Without that, budget is allocated uniformly across tokens, over-training the easy ones and under-training exactly the rare, hard tokens that fail. The paper supplies both the macroscopic capacity law and the microscopic recall condition, which together make memory budgeting a measurable engineering quantity rather than a guess.

## Core novelty

Using LoRA itself as a latent-space capacity probe to isolate *exact* parametric memory, then deriving two complementary results at two scales: a smooth power law (ΔL vs effective parameters and sequence length) at the aggregate level, and a deterministic threshold (p > 0.5 ⇒ verbatim greedy recall) at the token level. The threshold is the actionable part, because it identifies which tokens are already "done" and which still need budget. MemFT operationalizes this directly by reallocating optimization toward sub-threshold tokens.

## Key takeaways

- **Parametric Memory Law**: loss reduction ΔL follows a power law in effective parameters and sequence length, a robust quantitative capacity description for LoRA memorization.
- **Token-level phase transition**: p > 0.5 is a *sufficient* condition for verbatim recall under greedy decoding, so memorization is gated, not gradual.
- **MemFT** dynamically redistributes the training budget toward sub-threshold tokens, raising memory fidelity and efficiency over uniform training.
- LoRA is used as a clean controlled probe of exact parametric memory, not just evaluated by downstream proxies.

## Gaps in the study

Verbatim greedy recall is the cleanest possible memory target; whether the p > 0.5 threshold transfers to paraphrastic recall, sampling-based decoding, or multi-fact composition is untested, and real knowledge updates rarely demand exact regurgitation. The capacity law's "effective parameters" term bundles LoRA rank and placement, and the paper does not separate how much each contributes. Catastrophic forgetting of the base model's prior knowledge under MemFT's redistributed budget is not characterized, which matters because the whole point of LoRA memory updates is to add knowledge without destroying what was there.

## Relation to prior wiki state

This is the memorization-side instance of the wiki's strongest running pattern: *the useful training signal is sparse and locatable, so spend the budget there*. TIP (04-16) showed only ~10% of teacher-generated distillation tokens carry learning signal. LongAct (04-18) showed long-context RL gradient signal concentrates in a small set of high-magnitude activations. The Extrapolation Cliff (05-14) found a sharp closed-form threshold in on-policy distillation past which behavior collapses. MemFT adds the same shape to LoRA fine-tuning: most tokens are already above the recall threshold and waste budget, so redistribute toward the sub-threshold minority. The p > 0.5 phase transition is itself a new member of the "sharp threshold governs a training regime" family that the Extrapolation Cliff opened. It also pairs naturally with today's "Why Larger Models Learn More," which argues rare features are slowly-accumulating and easily overwritten: MemFT's threshold-guided redistribution is exactly a mechanism for protecting and pushing those fragile sub-threshold tokens, one paper diagnosing the fragility and the other prescribing where to spend.

## Research angle

The high-value open question is whether the p > 0.5 verbatim-recall threshold predicts *forgetting* as well as *learning*. If a token's recall is gated at a measurable probability threshold, then a knowledge-editing system could monitor that probability over continued training and detect the moment a previously-installed fact slips back below threshold, giving an early-warning signal for catastrophic forgetting before it shows up in downstream accuracy. Concretely: install a fact via MemFT, continue training on unrelated data, and check whether the fact's token probabilities decay smoothly (predictable) or fall off a cliff at the same 0.5 boundary (the threshold is bidirectional). A bidirectional threshold would make LoRA memory budgeting a closed-loop control problem rather than a one-shot allocation.

## Links

- [arXiv 2605.30260](https://arxiv.org/abs/2605.30260)
- [TIP: token-importance on-policy distillation (04-16)](../inference-efficiency/2026-04-16-tip-token-importance-on-policy-distillation.md)
- [Why Larger Models Learn More (05-31)](2026-05-31-why-larger-models-capacity-interference.md)
- [Knowledge distillation concept page](../inference-efficiency/knowledge-distillation.md)
