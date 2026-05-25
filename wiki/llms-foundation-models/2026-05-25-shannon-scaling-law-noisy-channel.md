# Shannon Scaling Law: LLMs as noisy channels

**arXiv:** [2605.23901](https://arxiv.org/abs/2605.23901) · **HF Daily Papers:** [page](https://huggingface.co/papers/2605.23901) · **Date:** 2026-05-25
**Raw:** [farmer file](../../raw/huggingface/2026-05-25-llms-as-noisy-channels-a-shannon-perspective-on-model-capaci.md)

## TL;DR

A unified scaling law that models LLM training as information transmission over a noisy channel, grounded in the Shannon-Hartley theorem. Parameters map to channel bandwidth, training tokens to signal power. The framework predicts a fundamental Shannon capacity for an LLM above which scaling without preserving SNR amplifies noise and degrades performance. Validated on Pythia and OLMo2 under perturbation (Gaussian noise, quantization, supervised fine-tuning on math/QA/code). Extrapolates from <=6.9B Pythia with <=180B tokens to predict 12B model at 307B tokens with pooled R^2 = 0.847, where monotonic baselines collapse.

## Key claims

- Classical monotonic power-law scaling fits well within a narrow range but cannot explain catastrophic overtraining or quantization-induced degradation. Both phenomena look like sudden performance drops as compute or data grows past a threshold.
- The Shannon channel framing explains both as the same mechanism. The channel has finite capacity. Pushing more signal through (more parameters, more tokens) past the SNR ceiling injects noise faster than it injects signal, and total information falls.
- The U-shaped performance curve is the natural prediction: a regime of monotonic improvement (more data is more signal) transitions into a regime of monotonic degradation (more data is more noise) at the Shannon capacity.
- On Pythia and OLMo2, the Shannon Scaling Law fits substantially better than classical power laws and recent perturbation-aware variants, with strong R^2 and accurate capture of the U-shaped loss basins that prior laws miss.
- Extrapolation is the load-bearing claim: fitted on <=6.9B Pythia at <=180B tokens, the law predicts 12B at 307B tokens at pooled R^2 = 0.847 where monotonic baselines collapse.

## Relation to prior wiki content

This is a substantial rewrite of how the wiki should be thinking about scaling laws. The standard Chinchilla-style power-law frame is monotonic by construction; it cannot represent the catastrophic-overtraining basin that has been documented in [Distillation Panic](../inference-efficiency/2026-05-04-distillation-panic-lambert.md) (the 05-04 Lambert piece arguing that on-policy distillation has hit a wall because the signal-to-noise of teacher rollouts collapses past a certain dataset size) and similar findings. Shannon Scaling gives those a unified mechanism: distillation is an information-transmission process and has its own Shannon capacity beyond which more teacher data is destructive.

It also gives a clean account of [the Extrapolation Cliff](../inference-efficiency/2026-05-14-extrapolation-cliff-on-policy-distillation.md) (the 05-14 paper that found a closed-form threshold above which on-policy distillation collapses). The cliff is the channel capacity boundary. The closed-form threshold is the SNR-preservation constraint.

Quantization-induced degradation is the third phenomenon the law captures cleanly. Aggressive quantization is equivalent to injecting noise into the channel; below the SNR threshold the network is fine, above it the channel collapses. This connects directly to the BitCPM-CANN (the today's r/LocalLLaMA report on 1.58-bit ternary QAT) result that 1.58-bit training retains 95.7-97.2 percent performance on 1B+ models but only 90.1 percent on 0.5B: smaller models hit the Shannon capacity faster because their channel bandwidth is smaller.

## Research angle

The most consequential open question is whether Shannon capacity is a property of the architecture or the training data. The paper's experiments vary parameters and tokens but fix the architecture; the law might be quite different if you vary depth, width, or attention pattern at fixed parameter count. If the Shannon capacity scales differently with width versus depth, the law gives a principled way to choose architecture shape at fixed budget, which is the practical lever every model-design team would care about.

Second open question: does the same framework predict the failure of [Muon](../inference-efficiency/2026-05-25-pion-muon-spectral-rlvr-vla.md) on low-SNR RLVR gradients? Both findings reduce to "uniform amplification of noise destroys learning when SNR is low." If Shannon Scaling and the spectral high-pass argument are the same theorem at different layers, that would be a substantial unification.

The 0.847 extrapolation R^2 is the most testable part. The paper makes a specific quantitative prediction about an unseen 12B model run. If anyone repeats the extrapolation on a different architecture family (Qwen, Mistral, OLMo3) and the law continues to extrapolate, the framework becomes the default for scaling-law analysis.
