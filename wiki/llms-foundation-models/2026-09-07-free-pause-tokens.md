# Free Pause Tokens: extra prediction compute without extra tokens

**Source:** X home feed (@rohanpaul_ai) · [arXiv 2609.03807](https://arxiv.org/abs/2609.03807) · Microsoft with Cornell University

**TL;DR.** In a standard decoder the same hidden state has to do two jobs at once: carry the running context forward and predict the next token. This paper gives prediction its own extra computation, and does it **without adding a token, without growing the KV cache, and without adding a decode step**. The result is a model that **matches a standard model trained on 50% more tokens** for **14% more training time and roughly 1% more inference latency**. It also does not have to run for the whole training run: switching the mechanism on after **42.5%** of training retains about **94% of the full quality gain** at 1.33x the baseline wall-clock, and at equal node-hours the phased variants still beat standard training.

## Why the three "withouts" are the whole result

Pause tokens as originally proposed give the model extra computation by inserting placeholder tokens it can think through. That works and it is expensive in the three ways that matter most for serving: each pause token occupies a sequence position, each occupies KV cache, and each costs a decode step. **This version buys the same extra prediction computation while paying none of those three.** For a reader whose attention is on KV cache and serving cost, that is the sentence: a training-time quality gain that leaves the inference-time memory profile essentially unchanged, at about 1% latency.

**The phased-schedule finding is the practical one.** The recommendation that falls out is to train normally for most of the run and switch the extra prediction computation on near the end. That is a cheap change to an existing recipe rather than a new architecture, and the 94%-of-the-gain-for-part-of-the-cost curve is the kind of result that gets adopted quickly because it does not require anyone to commit up front.

## Relation to prior wiki state

**It is the day's third result arguing that the compute budget is misallocated across the run rather than insufficient.** [Don't Drop Dropout (09-07)](../inference-efficiency/2026-09-07-dont-drop-dropout-layer-sparsity.md) finds that dropping whole layers on a tuned schedule reaches lower loss at equal training FLOPs and saves up to 25% of them, and its gains also depend on the *time* schedule rather than just the drop rate. [RISE (09-07)](../inference-efficiency/2026-09-07-rise-self-extrapolating-distillation.md) manufactures a dense teacher from the model's own trajectory rather than importing more supervision. **All three say the same thing: at a fixed FLOP budget, when you spend matters as much as how much you spend.** Two of the three (Don't Drop Dropout and Free Pause Tokens) find that a *phased* schedule beats a constant one, which is a specific and testable convergence.

**It also gives the [scaling laws](scaling-laws.md) page a datapoint it should be uncomfortable with.** "Matches a model trained on 50% more tokens" is an architectural change producing a data-efficiency multiplier, which is the kind of result that makes token-count-based scaling curves architecture-dependent rather than universal.

## Gaps

This reached the wiki through a summary post rather than the paper, so the mechanism by which prediction gets its own computation without an extra position is described only in outline. No scale sweep is quoted, and a 50%-token-equivalent gain that shrinks with model size would be a materially different result. And the 1% inference latency figure is presumably at a specific batch and context; the interaction with long context, where the extra per-step computation competes with an already memory-bound decode, is not addressed.

## Related

- [Scaling laws](scaling-laws.md) · [Don't Drop Dropout (09-07)](../inference-efficiency/2026-09-07-dont-drop-dropout-layer-sparsity.md) · [KV cache](../inference-efficiency/kv-cache.md)
- [Daily digest 2026-09-07](../daily-digest/2026-09/2026-09-07.md)
