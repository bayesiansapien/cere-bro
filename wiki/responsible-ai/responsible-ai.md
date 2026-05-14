# Responsible AI

Concept page for alignment, interpretability, safety, and explainability work.

This topic covers:

- **Mechanistic interpretability** — circuits, features, sparse autoencoders, activation patching, linear probes, refusal directions, sycophancy steering.
- **Alignment** — RLHF, RLAIF, Constitutional AI, reward modeling, scalable oversight, weak-to-strong generalization.
- **Safety** — jailbreak attacks and defenses, red-teaming methodologies, adversarial robustness, evaluation harnesses for harmful capabilities.
- **Explainability** — chain-of-thought faithfulness, attribution methods, counterfactual reasoning over model outputs, post-hoc explanation tools.
- **Governance & oversight** — model cards, evaluation reporting standards, deployment governance, capability disclosure norms.

Source pages will accumulate at `wiki/responsible-ai/YYYY-MM-DD-<slug>.md` as papers, posts, and tweets in this area get ingested.

## Current State (as of 2026-05-14)

**Latest addition (2026-05-14): WriteSAE — first SAE that reaches state-space and hybrid models.** Existing SAEs read residual streams, which works on transformers but cannot reach the `d_k × d_v` matrix cache write of Mamba-2, Gated DeltaNet, and RWKV-7. WriteSAE factors each decoder atom into the native rank-1 outer-product shape and trains under matched Frobenius norm so atoms swap one cache slot at a time. Atom substitution beats matched-norm ablation on 92.4% of 4,851 firings at Qwen3.5-0.8B L9 H4; the closed-form predicts measured logit shifts at R² = 0.98. Sustained three-position installs lift mid-rank target-in-continuation from 33.3% to 100% under greedy decoding — the first behavioral install at the matrix-recurrent write site. The interpretability significance: as hybrid Mamba-DeltaNet architectures become the default for long-context small models, WriteSAE keeps mechanistic interpretability and safety tooling reachable on the new architecture class. → [summary](2026-05-14-writesae-sae-recurrent-state.md)

**Tweet-side signal (2026-05-12, via @hamid_kazemi22):** [Refusal-neurons paper](https://nitter.net/hamid_kazemi22/status/2054225065433256118#m) reports that a single MLP neuron is sufficient to bypass safety alignment across 7 models, 2 families, 1.7B–70B scales. No fine-tuning, no prompt engineering. WriteSAE is the architectural complement on the hybrid-model side — the same kind of single-feature install at the cache-write site rather than the MLP.
