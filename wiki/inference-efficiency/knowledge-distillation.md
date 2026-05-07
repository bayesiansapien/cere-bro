# Knowledge Distillation

Transferring capabilities from a large teacher model to a smaller student model. On-policy distillation (OPD) trains the student on its own rollouts under token-level supervision from the teacher.

## Current State (as of 2026-05-07)

On-policy distillation has become the dominant approach for reasoning model compression. The key open question is which tokens actually carry the learning signal, naive approaches use all tokens, but most are uninformative. The distillation toolbox now ranges from token-importance methods (TIP) to neutral-channel cross-architecture transfer (BLD, TESSY, Switch-KD, Tide), parallel co-evolution (CoPD), and self-distillation under conditioning asymmetry (D-OPSD, 05-07). **Two papers on 2026-05-07 attack the heterogeneous-information-density problem in diffusion distillation specifically:** Stream-R1 reweights the DMD objective at both rollout and pixel level using a single shared reward model, and D-OPSD eliminates the external teacher entirely by making the model its own teacher under different conditioning. **Policy dimension (2026-05-05):** Nathan Lambert's "Distillation Panic" warns that the term is being conflated with API-jailbreaking attacks, and that pending U.S. legislation aimed at "distillation attacks" risks chilling the legitimate technique used by every lab. xAI's trial admission ("Generally AI companies distill other AI companies") is the most direct insider acknowledgment that the practice is industry-wide. The technical and political surfaces of distillation are now both load-bearing.

## Key Papers

**TIP: Token Importance in On-Policy Distillation (2026-04-16)** — Identifies two high-signal token regions: high-entropy (uncertain student) and low-entropy + high-divergence (overconfident but wrong). Entropy-based 50% token selection matches full training with 47% less peak memory. <10% of tokens (targeting overconfident region) nearly matches full baseline. → [summary](../inference-efficiency/2026-04-16-tip-token-importance-on-policy-distillation.md)

## Key Concepts

- **On-policy distillation**: student generates its own rollouts, then learns from teacher's token-level distribution over those rollouts
- **High entropy tokens**: student is uncertain — natural learning signal
- **Overconfident tokens** (low entropy, high divergence): student is wrong but confident — dense corrective signal often missed by entropy-only selection
- **Memory efficiency**: token selection not only improves learning quality but also reduces peak GPU memory — critical for distilling large reasoning models

**Cross-Tokenizer Distillation / BLD (2026-04-17)** — When teacher and student use different tokenizers, standard token-level distillation breaks. Byte-Level Distillation (BLD) solves this by converting both to a shared byte-level representation and distilling there. A lightweight byte-level decoder head is added to the student. Competitive with complex CTD methods despite its simplicity. → [summary](2026-04-17-cross-tokenizer-distillation-byte-level.md)

**TESSY (2026-04-18)** — Stylistic divergence between teacher and student causes SFT performance drops even when the teacher's reasoning is correct. TESSY interleaves teacher and student: teacher generates reasoning-heavy tokens, student generates style tokens. The hybrid sequence is stylistically the student's but intellectually the teacher's. Turns a 10% performance drop (Qwen3-8B on GPT-OSS-120B data) into a 6.7% gain on code generation. → [summary](2026-04-18-tessy-teacher-student-sft.md)

**Switch-KD (2026-04-18)** — Multimodal distillation for VLMs. Routes the student's visual outputs through the teacher's language pathway, forcing transfer through a shared text-probability space instead of separate modality silos. +3.6 points averaged across 10 benchmarks for a 0.5B student distilled from a 3B teacher. → [summary](2026-04-18-switch-kd-vision-language-distillation.md)

## Key Concepts

- **On-policy distillation**: student generates its own rollouts, then learns from teacher's token-level distribution over those rollouts
- **High entropy tokens**: student is uncertain — natural learning signal
- **Overconfident tokens** (low entropy, high divergence): student is wrong but confident — dense corrective signal often missed by entropy-only selection
- **Memory efficiency**: token selection not only improves learning quality but also reduces peak GPU memory — critical for distilling large reasoning models
- **Cross-tokenizer distillation (CTD)**: transferring knowledge when teacher and student use different tokenizers — the vocabulary mismatch problem
- **Byte-level interface**: using raw bytes as a universal common representation between any two tokenizers
- **Stylistic divergence**: teacher and student have different learned generation styles; a teacher's reasoning traces can be too foreign for the student's optimizer
- **Cooperative synthesis (TESSY)**: interleaving teacher/student token generation to create hybrid training data that matches student style while containing teacher reasoning

**ShadowPEFT (2026-04-22)** — Centralized PEFT via depth-shared shadow module. Shifts adaptation from distributed weight-space perturbations (LoRA) to a single shadow module that evolves a parallel state through all transformer layers. Decoupled from backbone, independently pretrainable, optionally deployable in detached mode for edge computing. Matches or outperforms LoRA and DoRA at comparable parameter budgets. → [summary](2026-04-22-shadowpeft-centralized-layer-space.md)

**Tide: Cross-Architecture Distillation for Diffusion LLMs (2026-04-30)** — First framework to handle teacher/student mismatch in *all three* of architecture, attention mechanism, and tokenizer for diffusion LLMs. Three components: Tidal (noise-aware schedule across timesteps + training progress), CompDemo (complementary-mask context enrichment), Reverse Calm (inverted chunk-likelihood matching with bounded gradients). Distills 16B MoE / 8B dense teachers into a 0.6B BD3LM student; +1.53 avg across 8 benchmarks; HumanEval 32.3 → 48.78; 22× memory reduction, 5× inference speedup vs teacher. → [summary](2026-04-30-tide-cross-arch-diffusion-distillation.md)

**CoPD: Co-Evolving Policy Distillation (2026-05-01)** — Multi-capability post-training via parallel expert RLVR + bidirectional OPD during training (not after). Mixed RLVR has divergence cost; train-experts-then-OPD has behavioral-pattern gap; CoPD avoids both by having experts mutually distill while RLVR-training in parallel. Integrates text/image/video reasoning into one model that *surpasses domain-specific experts*. Bidirectional OPD as the neutral exchange channel, applied to parallel training rather than student/teacher pipeline. Fifth paper in the cross-distillation-channel pattern (after BLD, TESSY, Switch-KD, Tide). → [summary](../llms-foundation-models/2026-05-01-copd-co-evolving-policy-distillation.md)

**The Distillation Panic — Nathan Lambert (2026-05-04)** — policy/discourse piece arguing that the "distillation attacks" framing being pushed in U.S. legislation conflates legitimate post-training distillation (used by every lab, including Nemotron and Olmo) with API jailbreaking (which should be called jailbreaking). The risk: a domestic ban on Chinese open-weight models built via API distillation, with collateral damage to Western academics and small labs. Quotes Musk's xAI trial admission as evidence the practice is industry-standard. Adds the policy dimension to the wiki's distillation tracking. → [summary](2026-05-04-distillation-panic-lambert.md)

**Stream-R1: Reliability-Perplexity Aware Reward Distillation (2026-05-07)** — DMD (Distribution Matching Distillation) for streaming video diffusion, reweighted by a single shared video reward model on two axes: inter-reliability (per-rollout, via `exp(reward_score)`) and intra-perplexity (per-pixel, via gradient saliency from the same reward). Adaptive balancing prevents any single quality axis (visual, motion, alignment) from dominating. The video-streaming analogue of TIP: heterogeneous information density across rollouts, frames, and pixels means uniform supervision wastes signal. → [summary](2026-05-07-stream-r1-reliability-perplexity-distillation.md)

**D-OPSD: On-Policy Self-Distillation for Step-Distilled Diffusion (2026-05-07)** — addresses the practical problem that standard SFT destroys the few-step capability of step-distilled diffusion models (Z-Image-Turbo, FLUX.2-klein). Novel paradigm: the same model serves as teacher and student under different conditioning. Teacher sees text plus target image (multimodal), student sees only text. Loss minimises divergence between the two over the student's own rollouts. The seventh paper in the neutral-exchange-channel pattern, but with a new neutral channel: **conditioning asymmetry on the same network**. → [summary](2026-05-07-d-opsd-self-distillation-step-distilled-diffusion.md)

## Key Concepts

- **On-policy distillation**: student generates its own rollouts, then learns from teacher's token-level distribution over those rollouts
- **Centralized PEFT (ShadowPEFT)**: single depth-shared module performs layer-space refinement, unlike LoRA's per-layer weight perturbations
- **Layer-space vs weight-space adaptation**: ShadowPEFT refinement evolves a parallel state through the network depth; LoRA adds local rank-decomposed perturbations to individual matrices
- **Cross-architecture diffusion distillation (Tide)**: distill from a diffusion teacher to a diffusion student of different size/attention/tokenizer; requires noise-aware scheduling, complementary-mask context enrichment, and bounded-gradient cross-tokenizer losses
- **Neutral exchange representation pattern**: across BLD (bytes), TESSY (cooperative interleaving), Switch-KD (shared text-probability space), Tide (inverted chunk-likelihood with bounded gradients), and CoPD (bidirectional OPD between parallel RLVR experts), the field has converged on engineering a *neutral channel* between mismatched teacher/student rather than forcing token alignment. **Five papers, five mechanisms, one principle.**
- **Co-evolution distillation (CoPD)**: parallel RLVR-trained experts serve as mutual teachers via bidirectional OPD *during training*, eliminating both the inter-capability divergence of mixed RLVR and the behavioral-pattern gap of train-then-distill

## Related Pages

- [../llms-foundation-models/rl-for-llms.md](../llms-foundation-models/rl-for-llms.md)
- [../llms-foundation-models/2026-04-16-prerl-rl-in-pretrain-space.md](../llms-foundation-models/2026-04-16-prerl-rl-in-pretrain-space.md)
- [kv-cache.md](kv-cache.md)
