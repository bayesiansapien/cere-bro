# Shannon Scaling Law: LLMs as noisy channels with U-shaped degradation

**arxiv:** [2605.23901](https://arxiv.org/abs/2605.23901) · **HF:** [papers/2605.23901](https://huggingface.co/papers/2605.23901) · **Raw:** [farmed](../../raw/huggingface/2026-05-25-llms-as-noisy-channels-a-shannon-perspective-on-model-capaci.md)

## TL;DR

The existing scaling laws for LLMs are monotonic power laws fit on clean pretraining. They fail to explain non-monotonic phenomena: catastrophic overtraining (loss going up with more data), quantization-induced degradation (performance dropping below the unquantized baseline despite more compute), and the U-shaped curves that appear under perturbation. The Shannon Scaling Law treats LLM training as transmission over a noisy channel grounded in the Shannon-Hartley theorem. Model parameters map to channel bandwidth, training tokens to signal power, and intrinsic learning noise to the channel noise floor. The framework predicts that scaling without preserving signal-to-noise ratio inevitably triggers a transition from monotonic improvement to U-shaped degradation. Fitted on Pythia <=6.9B with <=180B tokens, the law extrapolates to the unseen 12B model at 307B tokens with pooled R^2 = 0.847; monotonic baselines collapse on the same extrapolation.

## Why this matters

This is the first published scaling law that includes catastrophic overtraining and quantization degradation in one framework. The Distillation Panic from 2026-05-04 ([2026-05-04-distillation-panic-lambert.md](2026-05-04-distillation-panic-lambert.md), Nathan Lambert's piece on the field's overreliance on distillation as a substitute for understanding) was the rhetorical version of the same recognition. The Extrapolation Cliff from 2026-05-14 ([2026-05-14-extrapolation-cliff-on-policy-distillation.md](../inference-efficiency/2026-05-14-extrapolation-cliff-on-policy-distillation.md), which found a closed-form threshold above which on-policy distillation collapses) was the first paper to predict a phase transition in training behavior. The Shannon Scaling Law generalizes: every regime where scaling makes performance worse is a noise-amplification regime, predictable from the channel model. The mathematical apparatus is the Shannon-Hartley theorem, which is unusual in scaling-law literature and is the contribution.

The R^2 = 0.847 on the 12B / 307B extrapolation is the load-bearing empirical result. Monotonic power laws have R^2 near zero on the same extrapolation because they cannot represent the U-shape that the perturbation regime produces. The framework recovers the loss basin (the depth and location of the U) from a fit on smaller perturbed runs. That is the first quantitative prediction of a perturbation basin from a small-scale fit.

## Where this fits

The wiki has tracked four related findings about scaling law breakdowns in the past six weeks:

1. **TIP (2026-04-16)** — most teacher tokens carry no signal; uniform supervision wastes 90% of the budget. (signal density)
2. **Same Architecture Different Capacity (2026-05-23)** — optimizer choice changes effective spectral capacity; matched loss does not imply matched representation. (optimizer-spectral capacity)
3. **Extrapolation Cliff (2026-05-14)** — closed-form threshold above which on-policy distillation collapses. (phase transition)
4. **Shannon Scaling Law (today)** — SNR-preserving scaling avoids U-shape degradation; the noisy-channel model explains all four phenomena.

The pattern: the monotonic power-law era of scaling-law research is closing. The next era is non-monotonic, perturbation-aware, signal-shaped. This paper provides the unifying theory.

## Open research angles

- The Shannon model maps parameters to bandwidth and tokens to signal power. Whether the optimizer (Muon vs AdamW vs Pion) and the architecture (linear vs full attention) are separate channel parameters or recoverable from the existing bandwidth-and-power formulation is open.
- The framework predicts loss basins. Whether it predicts the *location* of the basin (which dataset compositions trigger collapse at which compute level) precisely enough to drive curriculum design is the next test.
- Quantization-induced U-shape is explained by SNR loss in the parameter representation. Whether the same model predicts KV-cache-quantization breakdown (relevant to Octopus, OSCAR, KVServe from 2026-05-21 / 2026-05-24) is the inference-side test.

## Industrial implication

Pretraining teams have been operating on monotonic scaling laws for token-count selection. The Shannon law predicts that crossing the SNR threshold makes more data actively harmful, not just unhelpful. The practical recipe is: estimate the SNR floor of the training corpus before deciding how many tokens to train on. Corpus-quality work (data filtering, deduplication, perplexity-based pruning) gets a more rigorous justification: it is SNR engineering.

## Related wiki pages

- [2026-05-23-same-architecture-optimizer-induced-spectral-scaling.md](2026-05-23-same-architecture-optimizer-induced-spectral-scaling.md) — optimizer-induced capacity
- [2026-05-14-extrapolation-cliff-on-policy-distillation.md](../inference-efficiency/2026-05-14-extrapolation-cliff-on-policy-distillation.md) — closed-form distillation phase transition
- [2026-04-16-tip-token-importance-on-policy-distillation.md](../inference-efficiency/2026-04-16-tip-token-importance-on-policy-distillation.md) — token-level signal density
