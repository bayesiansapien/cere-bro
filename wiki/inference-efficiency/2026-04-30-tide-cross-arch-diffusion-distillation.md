# Tide: Cross-Architecture Distillation for Diffusion Large Language Models

**Date:** 2026-04-30
**Source:** [HuggingFace](https://huggingface.co/papers/2604.26951) | [Paper](https://arxiv.org/abs/2604.26951)
**Raw:** [raw/huggingface/2026-04-30-turning-the-tide-cross-architecture-distillation-diffusion-llms.md](../../raw/huggingface/2026-04-30-turning-the-tide-cross-architecture-distillation-diffusion-llms.md)
**Authors:** Zhang, Wang, Tian, Yuan (Peking U, Zhejiang U)

## TL;DR

Tide is the first distillation framework that crosses architectures for *diffusion* LLMs. Prior dLLM distillation only compressed diffusion *steps* within a single architecture. Tide handles three simultaneous mismatches between teacher and student: architecture (16B MoE → 0.6B dense), attention mechanism, and tokenizer. Three modular components — Tidal (a noise-aware schedule), CompDemo (mask-completion of teacher context), and Reverse Calm (an inverted chunk-likelihood matching loss with bounded gradients) — distill an 8B dense and a 16B MoE teacher into a 0.6B BD3LM student. +1.53 avg across 8 benchmarks; HumanEval jumps from 32.3 (AR baseline) to 48.78. 22× memory reduction, 5× inference speedup vs the teacher.

## Why this is Tier 1

Two reasons: first, dLLMs are the most credible non-autoregressive frontier — parallel decoding and bidirectional context are real wins, but they were stuck at billions of parameters for competitive performance. Cross-architecture distillation is the bridge that lets dLLM capabilities flow into smaller student architectures, which is the only way these become deployment-relevant. Second, the *mechanism* of how Tide handles the three mismatches generalizes well beyond diffusion.

## The Three Mismatches and How Tide Handles Them

```
Teacher (16B MoE, BPE tokenizer, attention pattern A)
                           │
                           ▼
              ┌────────────────────────────┐
              │  Tidal: schedule strength  │  ← noise-dependent reliability
              │  per (training_step,       │     (heavy mask = noisy teacher)
              │       diffusion_timestep)  │
              └────────────────────────────┘
                           │
                           ▼
              ┌────────────────────────────┐
              │  CompDemo: mask split      │  ← give teacher complementary
              │  → enrich teacher context  │     context windows for the
              │                            │     same masked input
              └────────────────────────────┘
                           │
                           ▼
              ┌────────────────────────────┐
              │  Reverse Calm: inverted    │  ← bounded gradients;
              │  chunk-level likelihood    │     dual-end noise filter
              │  matching                  │
              └────────────────────────────┘
                           │
                           ▼
        Student (0.6B BD3LM, different tokenizer)
```

**Tidal** is a dynamic distillation-strength schedule that varies *both* across training progress and across diffusion timesteps. Diffusion teachers are noisier at high mask rates — Tidal down-weights distillation when the teacher is unreliable, up-weights when it is.

**CompDemo** addresses the heavy-masking failure mode: when too many tokens are hidden, the teacher's prediction collapses. CompDemo splits the mask into complementary halves and lets the teacher predict each half conditioned on the other — restoring its predictive power so the student gets clean supervision.

**Reverse Calm** is the cross-tokenizer bridge. Standard chunk-level likelihood matching (the dLLM analog of token-distribution matching) is unbounded — large divergences blow up gradients. Reverse Calm inverts the matching direction, which yields *bounded* gradients and a dual-end noise filter (filtering both teacher noise and student over-confidence).

## Why It Matters

dLLMs need a compression story before they can be deployed broadly. Tide provides it, and crucially, it shows that the cross-tokenizer + cross-architecture problem can be solved without a shared interface vocabulary (the BLD trick from 04-17) — instead, by inverting the loss to produce bounded gradients. That's a different technical recipe with very different practical implications: BLD requires a byte-level decoder head; Tide requires only a loss-function change.

The HumanEval result (32.3 → 48.78) is more striking than the average +1.53 — code generation is where dLLMs had the biggest gap to AR baselines, and the gap is closed.

## Connection to Prior Wiki Knowledge

**Third paper this month routing distillation through a non-token-aligned channel.** BLD (04-17) used bytes. TESSY (04-18) used cooperative interleaving. Switch-KD (04-18) used a shared text-probability space across modalities. Tide (04-30) uses inverted chunk-likelihood matching with bounded gradients. The pattern is now firmly established: when teacher and student differ on tokenizer/architecture/modality, the field is converging on solutions that engineer a *neutral exchange representation* rather than forcing token alignment.

**Confirms TIP's information-density observation (04-16) generalizes beyond AR.** TIP showed that <10% of tokens carry meaningful supervision in AR distillation. Tide's Tidal schedule applies the same insight to diffusion: *when* (which timesteps) carries meaningful supervision varies, and you can ignore the rest. Same principle, different axis.

**Extends knowledge-distillation.md beyond AR.** Until now this concept page only covered AR-to-AR distillation. Tide is the first dLLM-to-dLLM cross-architecture entry. The concept needs explicit subsections for AR, dLLM, and cross-modal.

## Research Angle

Three open problems worth tracking:

1. **AR teacher → dLLM student.** Tide handles dLLM → dLLM. The harder regime is using a strong AR teacher (e.g., GPT-5.5, Opus 4.6) to distill into a dLLM student. The diffusion timestep axis has no AR analog — what supervision signal does the AR teacher provide for the noisy intermediate states the student must learn? This is the natural follow-up.

2. **Reverse Calm vs BLD on the same benchmark.** Both solve cross-tokenizer distillation, with very different mechanisms (inverted loss vs byte interface). A head-to-head comparison would reveal whether bounded gradients beat byte-level alignment, or whether the two compose.

3. **Tidal schedule learnability.** Tidal is hand-designed. A learned schedule (as a function of teacher noise estimate and student loss curve) should outperform — and would generalize to other diffusion-style training regimes (image diffusion distillation, audio diffusion distillation).

## Related Pages

- [Knowledge Distillation](knowledge-distillation.md)
- [BLD — Byte-Level Distillation](2026-04-17-cross-tokenizer-distillation-byte-level.md)
- [TESSY — Cooperative Synthesis](2026-04-18-tessy-teacher-student-sft.md)
- [Switch-KD — VLM Distillation](2026-04-18-switch-kd-vision-language-distillation.md)
- [TIP — Token Importance](2026-04-16-tip-token-importance-on-policy-distillation.md)
