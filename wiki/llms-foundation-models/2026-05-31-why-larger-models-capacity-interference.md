# Why Larger Models Learn More: Capacity, Interference, and Rare-Task Retention

**arXiv:** [2605.29548](https://arxiv.org/abs/2605.29548) · **HF Daily Papers:** [page](https://huggingface.co/papers/2605.29548) · **Date:** 2026-05-31
**Raw:** [farmer file](../../raw/huggingface/2026-05-31-why-larger-models-learn-more-effects-of-capacity-interferenc.md)

## TL;DR

"Larger models are better" is an empirical truism; this paper gives it a data-centric mechanism. The claim is that power-law scaling already implies a larger model will learn part of the data distribution that a smaller model cannot, *even with infinite training data*. The cause is competition over a finite resource (neurons). Small models spend their neurons on high-frequency or low-complexity tasks and therefore learn solutions that fail on rare and complex tasks, even when a solution that expresses the rare task exists in their hypothesis space. Larger models escape this by *reduced interference*: once they allocate enough neurons to common tasks, the gradient updates for those tasks become weak, so they stop overwriting the slowly-accumulating features of rare tasks. The authors validate this first in a synthetic mixture-of-tasks setup with monotonic scaling curves, then by pretraining OLMo models from 4M to 4B parameters on novel tasks of varying frequency and complexity: only the larger OLMo models learn the infrequent, complex tasks, and they embed more task features in their representations while showing measurably less gradient interference between tasks.

## The mechanism

```
Finite neurons, tasks compete for them:

  SMALL model
    common task A (high freq) ─► grabs neurons ─► strong gradient keeps
    rare task B  (low freq)   ─► few neurons    ─► overwritten each step ─► NOT learned
                                                   (even if expressible)

  LARGE model
    common task A ─► enough neurons ─► gradient goes WEAK once learned
    rare task B   ─► residual capacity ─► features accumulate WITHOUT being
                                          overwritten by A's updates ─► learned

  Key quantity: gradient interference between tasks
    larger model ⇒ lower interference ⇒ rare/complex tasks survive
```

## What problem it solves

Scaling laws describe *that* loss falls as a power of size, but they are agnostic about *what* the extra capacity buys. Practitioners need that "what" to make sizing and data-mixture decisions: if a capability only appears above some size, no amount of data at a smaller size will recover it, and a data mixture that over-weights common tasks actively starves the rare ones. The paper reframes the scaling question from "how much does loss improve" to "which parts of the distribution become learnable", and ties the answer to a concrete, measurable cause (gradient interference) rather than an abstract appeal to capacity.

## Core novelty

A phenomenological argument that connects power-law scaling to a per-task learnability threshold, plus the identification of *reduced gradient interference* (not raw representational capacity) as the operative mechanism. The synthetic setup is constructed so that every task is individually expressible at small scale, which isolates interference as the cause: the small model fails not because it cannot represent the rare task but because common-task gradients keep overwriting it. The OLMo 4M-to-4B sweep on controlled novel tasks then confirms the synthetic story in a real pretraining run, with direct measurement of feature embedding and inter-task gradient interference.

## Key takeaways

- Power-law scaling implies a larger model learns distribution slices a smaller one cannot, **even at infinite data**, so the gap is not a data-quantity problem.
- Small models allocate neurons to high-frequency / low-complexity tasks and learn solutions that fail on rare-and-complex tasks **even when those tasks are expressible** in their capacity.
- The escape mechanism is **reduced interference**: in large models, common-task gradients weaken once the task is learned, so they stop overwriting slowly-accumulating rare-task features.
- Validated on OLMo 4M→4B: only larger models learn infrequent/complex tasks, embed more task features, and show less gradient interference.

## Gaps in the study

The synthetic mixture is hand-constructed with explicitly monotonic scaling curves; real pretraining distributions are not cleanly decomposable into frequency × complexity cells, so the mapping from "rare-and-complex synthetic task" to a real capability (a reasoning skill, a low-resource language) is asserted rather than demonstrated. The OLMo runs top out at 4B, far below the frontier where the most interesting emergent capabilities live. The mechanism explains retention of rare features but does not predict *which* real-world capabilities sit above which size threshold, which is the question a practitioner actually wants answered.

## Relation to prior wiki state

This is the data-centric complement to the mechanistic superposition account. MIT's "Superposition explains scaling laws" (05-03) argued features are encoded along approximately non-interfering directions, which is *why* scaling works and why operational variables tend to be linear and steerable. Today's paper supplies the training-dynamics half of that story: superposition describes the geometry that lets many features coexist; interference describes the gradient process that decides which features actually get written during training. The "rare features are fragile and slowly-accumulating" framing is also the same shape as the sparseness-and-locatability thread the RL pages have been building (TIP 04-16, only ~10% of distillation tokens carry signal; LongAct 04-18, long-context gradient signal concentrated in high-magnitude activations): in all three, the useful signal is sparse and easily swamped by the dominant bulk. It further dovetails with the 05-23 optimizer-spectral-scaling result, which found Muon scales rare-token representation rank where AdamW stalls (β=1.02 vs 0.44): if rare-task learning is interference-limited, an optimizer that conditions updates to reduce interference would directly raise the rare-token scaling exponent, linking architecture (this paper's neuron competition), optimizer (Muon), and data mixture into one frame. Kurate cs.LG this week independently surfaces two adjacent theory papers, "A Theory of Generalization in Deep Learning" (#3) and Nexus, "Same Pretraining Loss, Better Downstream Generalization via Common Minima" (#11), the latter making the matched-loss-different-generalization point that this paper's "same expressivity, different learnability" claim presupposes.

## Research angle

The falsifiable lever is the data mixture. If rare-task learning is interference-limited rather than capacity-limited, then a curriculum or re-weighting that *reduces common-task gradient dominance* (down-weighting saturated common tasks late in training, or an optimizer that decorrelates per-task gradients) should let a smaller model learn rare tasks it otherwise misses, partially substituting for raw size. That is a concrete, measurable prediction: take the OLMo setup, freeze size, manipulate interference directly, and check whether rare-task accuracy moves. If it does, "just make it bigger" is revealed as the lazy solution to an interference problem that has cheaper fixes, which would matter enormously for the cost of acquiring tail capabilities.

## Links

- [arXiv 2605.29548](https://arxiv.org/abs/2605.29548)
- [MIT superposition scaling laws (05-03)](2026-05-03-mit-superposition-scaling-laws.md)
- [Optimizer-induced spectral scaling laws (05-23)](2026-05-23-same-architecture-optimizer-induced-spectral-scaling.md)
- [RL for LLMs concept page](rl-for-llms.md)
