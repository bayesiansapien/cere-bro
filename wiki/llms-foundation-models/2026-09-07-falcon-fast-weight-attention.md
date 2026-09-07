# Falcon: fast-weight attention and the timing of the recurrent memory update

**Source:** X home feed (@burkov) · ByteDance Seed with Princeton, Tsinghua, UCLA and Hyperbolic Labs

**TL;DR.** Long-context language models sit between two bad options. Transformer attention can read the entire past but costs more as the sequence grows. Recurrent models keep a fixed-size memory, and the rule they use to update that memory is itself a form of online learning. This work makes the second observation precise and finds a bug in how the field trains it: **the memory should be trained using the representation that was actually available when a target was predicted, not the more common same-step pairing.** From that correction the authors derive the **Falcon** family, normalized memory updates with explicit, separately controllable knobs for learning speed, forgetting rate, and whether each update consumes one token or a short recent window, together with chunk-parallel implementations that map onto GPUs. Reported results are competitive language modelling and notably better extrapolation on longer arithmetic sequences.

## What makes it worth a page

**The framing is the contribution.** Recurrent memory update rules have mostly been treated as architectural choices to be searched over. Falcon treats them as an **online learning algorithm with an explicit hyperparameter surface**, so learning rate, forgetting and update granularity become things you set rather than things baked into a gate design. That is the difference between a family and a model.

**The timing correction is the kind of error that is invisible until stated.** Pairing the memory update with the same-step representation trains the memory against information the predictor did not have. Using the representation available at prediction time is what makes the update rule an honest online learner, and the extrapolation improvement on longer arithmetic sequences is the signature you would expect if the fix is real: extrapolation is exactly where a memory trained on the wrong conditioning breaks first.

## Relation to prior wiki state

**It is the day's second independent result about quantifiable structure inside recurrent state.** [When Quantization Breaks Memory (09-07)](../inference-efficiency/2026-09-07-quantization-breaks-recurrent-state.md) shows that the *storage* rule for a recurrent state changes the dynamical system, not just its precision, and that repeated sub-threshold updates get silently discarded. Falcon shows that the *timing* of the update rule changes what the memory learns. **Both say the recurrent state's interface is a first-class design object rather than an implementation detail, and neither cites the other.** The composition question is direct and unrun: Falcon's explicit forgetting and learning-speed controls are exactly the knobs you would want when tuning a state to survive quantized write-back.

**It also bears on the bounded-cache branch of the [KV cache](../inference-efficiency/kv-cache.md) page.** [Maglev (08-16)](../inference-efficiency/2026-08-16-maglev-sliding-recurrent-memory.md) removes eviction entirely by bounding the cache with a fixed-size recurrent memory, and the page's open question about that direction is whether a bounded state can hold enough. Falcon is a principled framework for asking that question rather than guessing at a gate.

## Gaps

Reached the wiki through a summary post rather than the paper, so scale, baselines and the precise definition of the same-step pairing being corrected are secondhand. "Competitive language modelling" without a stated comparison set is the weakest part of the claim, and the strong result is on arithmetic extrapolation, which is a synthetic probe rather than a downstream task. No inference-cost comparison against a transformer baseline at matched quality.

## Related

- [Attention mechanisms](attention-mechanisms.md) · [KV cache](../inference-efficiency/kv-cache.md) · [When Quantization Breaks Memory (09-07)](../inference-efficiency/2026-09-07-quantization-breaks-recurrent-state.md)
- [Daily digest 2026-09-07](../daily-digest/2026-09/2026-09-07.md)
