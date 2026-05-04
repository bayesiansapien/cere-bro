# Ken Huang — World Models, Architectures, and the Next Phase of AI

**Source:** Ken Huang / Agentic AI Substack
**Raw:** [raw/rss/2026-05-03-agentic-ai-world-models-architectures-and-the-next-phase-of-ai.md](../../raw/rss/2026-05-03-agentic-ai-world-models-architectures-and-the-next-phase-of-ai.md)
**URL:** https://kenhuangus.substack.com/p/world-models-architectures-and-the
**Date:** 2026-05-03
**Tier:** 1/2 — architecture survey with routing/efficiency intersections

## TL;DR

A long-form survey framed around the LeCun (JEPA) vs Xing (PAN/GLP) March-2026 debate at the Spring School AI For Impact. JEPA: prediction in latent space without a decoder; the encoder must learn to discard what cannot be predicted. PAN/GLP: latent prediction *with* a generative decoder as a guardrail against representation collapse. The essay maps five "schools" of world modeling — agent-centric (Dreamer line), foundation-world-model (Genie/Cosmos), spatial-intelligence (World Labs/Marble), video-as-simulation (Sora), and abstraction-with-validation (JEPA + GLP) — and walks through transformers, diffusion, state-space, and recurrent architectures as competing substrates.

## Key claims

- **The debate is rationalism vs empiricism.** LeCun's bet: prediction must throw away the unpredictable. Xing's bet: discarded information turns out to matter on downstream tasks; reconstruction is a guardrail.
- **PAN's key technical claim:** their generative loss is a *strict upper bound* on latent loss — minimizing the generative loss minimizes the latent loss, but not vice versa. Reconstruction prevents the encoder/predictor from quietly degenerating.
- **V-JEPA 2 (2025) is the strongest empirical case for JEPA:** ~1M hours of internet video at 8B scale; SOTA on Something-Something v2 (77.3), Epic-Kitchens-100 (39.7 R@5), PerceptionTest (84.0). V-JEPA 2-AC post-trained from <62 hours of unlabeled robot videos and deployed zero-shot on Franka arms.
- **Mamba/SSM is quietly excellent for world models.** DRAMA (Mamba-2-based) achieved 105% normalized human performance on Atari100k with 7M parameters vs DreamerV3's 200M. S4WM beat transformers and RNNs on long-term memory tasks at lower training cost.
- **Hybrids are the empirical default.** Jamba (Mamba+attention 1:7), Nemotron-H (92% Mamba2 layers, 3× LLaMA-3.1 throughput at parity accuracy). For world models specifically: autoregressive temporal + diffusion spatial (Genie 2/3, Astra).
- **The LeCun-Xing dispute may be less load-bearing than it appears.** A weak-decoder GLP approximates JEPA; a strong-regularizer JEPA approximates a generative model. PAN authors: "GLP strictly subsumes JEPA — turn off the generative function, and you have a JEPA."

## Why this matters for cere-bro

This is a Tier 1/2 reference because it gives the architectural map under which routing, KV cache, and compression decisions live. Three intersections:

1. **TransDreamer's KV-cache constraint is the routing-relevant bottleneck.** A transformer state-space model could only imagine from 3 states per replay sample because KV cache makes longer rollouts infeasible. This is the same long-context bottleneck that FlashRT (05-02) attacks for red-teaming and that NeMo-RL speculative decoding (04-30) attacks for RL rollouts. *World-model rollouts are another long-context iterative-gradient workload.*
2. **Mamba/SSM as the world-model substrate.** If DRAMA-style results (105% human at 1/30 the parameters) generalize, the next world models are not transformers. Composability with the ViPO/Semi-DPO (05-02) preference-data lessons and CoPD (05-01) policy-distillation lessons is uncharted.
3. **Spatial intelligence vs simulation.** World Labs' Marble (Tier 4 normally) is a billion-dollar bet that 3D reconstruction is the foundation, with physics on top. Xing's critique: static 3D ≠ world model. The wiki should track whether World Labs ships physics integration in 2026.

## Connections to prior wiki pages

- **HOPE Nested Learning (04-28)** — biological hippocampal architecture; world-model substrates with multi-time-scale memory parallel HOPE's nested-cycle inspiration. The architectural-bet space is converging from two directions.
- **PRL-Bench physics benchmark (04-20)** — physics evaluation for agents. World-model evaluation needs the same kind of structured benchmark; pure video-fidelity metrics (FID/FVD) miss the physical-causality dimension Sora fails on.
- **AVR Adaptive Visual Reasoning (04-20)** — visual reasoning under uncertainty. World models that handle multimodal uncertainty (diffusion family) vs those that compress it away (JEPA) face the same tradeoff this paper raises.
- **CoT degrades spatial reasoning (04-22)** — text-trained CoT hurts spatial tasks. World-model arguments from Fei-Fei Li / World Labs cite exactly this evidence: language-only training cannot build true 3D understanding.

## Research angles

- **State-space world models for trajectory routing.** DRAMA gets 105% normalized human at 7M params. If composed with Step-level Optimization (05-02), the small policy could itself be a Mamba world-model — making "imagined rollouts" available to the Stuck/Milestone monitors. No paper has tried this.
- **Long-context world-model rollouts.** The TransDreamer KV-cache wall is the same wall as long-context RL rollouts. FlashRT-style efficiency primitives should transfer directly.
- **PAN-style decoder-as-guardrail in language modeling.** Reasoning-mode steering (Compliance vs Sensibility, 05-02) is a kind of latent-prediction problem. Adding a "generative validator" — train the model to also reconstruct the conventional output as a check — is structurally analogous to GLP. Worth testing.
