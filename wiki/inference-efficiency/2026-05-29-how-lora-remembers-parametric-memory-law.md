---
title: "How LoRA Remembers? A Parametric Memory Law for LLM Finetuning"
date: 2026-05-29
arxiv: https://arxiv.org/abs/2605.30260
source: huggingface
tier: 1
topic: inference-efficiency
---

# How LoRA Remembers? A Parametric Memory Law for LLM Finetuning

> LoRA's effective-parameter count and sequence length predict exact-recall loss reduction by a power law. At the token level, a sharp phase transition appears: any token with predicted greedy probability above 0.5 is verbatim-recallable. MemFT, a threshold-guided budget reallocator, beats vanilla LoRA on memory fidelity.

```
LoRA as a memory-capacity probe:

       loss reduction (ΔL)
          on memorized text
              │
              │             ───  Power law: ΔL = α · (effective params · seq length)^β
              │           ──
              │         ──
              │       ──
              │     ──
              │   ──
              │ ──
              └─────────────────────────────►  (effective_params × sequence_length)

Token-level phase transition:

  Greedy-decoding probability of token t:
     p(t) < 0.5  ►  verbatim recall FAILS
     p(t) > 0.5  ►  verbatim recall SUCCEEDS  ◄── sharp threshold, not gradual
  
MemFT (this paper):
   while training:
     for token t in batch:
       if p(t) < 0.5:  ► up-weight gradient  (push past threshold)
       else:           ► down-weight        (already recalled; budget elsewhere)
```

## TL;DR

Most studies of LoRA-as-memory rely on qualitative downstream metrics. This paper treats LoRA as a controlled memory-capacity probe in latent space and derives the **Parametric Memory Law**: a robust power law linking exact-recall loss reduction to the product of effective parameters and sequence length. Fine-grained token-level analysis then reveals a deterministic phase transition: **a predicted greedy probability above 0.5 is a sufficient condition for verbatim recall**. Below it, the token does not memorize; above it, it does. The authors turn this observation into MemFT, a threshold-guided optimizer that dynamically reallocates training budget toward sub-threshold tokens. Empirically MemFT improves memory fidelity and efficiency. Code at github.com/zjunlp/ParametricMemoryLaw.

## Why this matters for Tier 1

This is the LoRA-side companion to the **token-importance** thread that ran through April. **TIP** (2026-04-16, the paper that argued 10 percent of teacher-generated tokens carry the actual learning signal under on-policy distillation) and **LongAct** (2026-04-18, the paper that found long-context gradient signal concentrates in the first 5 percent of tokens) both argued, for *training*, that uniform per-token treatment wastes compute. **The Parametric Memory Law extends the same observation to *finetuning recall***: most tokens are already above the 0.5 threshold; only the sub-threshold tokens need additional gradient. Three papers across two months now agree that compute should follow signal density at the token level. This is a pattern.

The phase-transition observation is also important on its own. It says memorization is **not** a smooth function of training; it is binary at the token level. Either the token is past the 0.5 probability cliff or it is not. If you stop training early you get a partially-memorized sequence with sharp drops at sub-threshold positions, not a uniformly weak copy.

## Connections to prior wiki

- **TIP** (2026-04-16): selective gradient on the 10 percent of tokens that carry signal during distillation. Same logic, training side.
- **LongAct** (2026-04-18): saliency-driven gradient sparsity for long-context training. Same logic, length axis.
- **Why Larger Models Learn More** (2026-05-29, same day): argues larger models avoid the rare-task interference that hurts small models. This paper's token-level phase transition is the recall-side companion: capacity allows you to push more tokens past the 0.5 cliff before you run out of gradient.
- **ShadowPEFT centralized layer space** (2026-04-22): on the parameter side; how to organize LoRA updates spatially. MemFT is orthogonal, on the gradient-allocation side.

## Research angle

The 0.5 threshold is suspiciously clean. Either it is a discretization artifact of greedy decoding or there is a real phase transition in the underlying log-probability landscape. The next experiment is to vary the decoding strategy: under nucleus sampling does the threshold shift, smooth, or disappear? If it smooths, the phase transition is decoding-artifact-bound; if it stays sharp, there is a real cliff in the loss landscape worth understanding.

Open: does the power law transfer to *full fine-tuning* (not LoRA)? If so, the effective-parameter dimension can be replaced by full parameter count and we have a memorization-scaling law that complements the Chinchilla pretraining laws on the recall axis.
