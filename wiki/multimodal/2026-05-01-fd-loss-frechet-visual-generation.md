# FD-loss: Representation Fréchet Loss for Visual Generation

**arXiv:** 2604.28190 · [paper](https://arxiv.org/abs/2604.28190) · [HF](https://huggingface.co/papers/2604.28190)
**Tier:** 3 — visual generation / training objective
**Raw:** [../../raw/huggingface/2026-05-01-representation-frechet-loss-visual-generation.md](../../raw/huggingface/2026-05-01-representation-frechet-loss-visual-generation.md)

## TL;DR

Fréchet Distance has been the gold-standard *evaluation* metric for visual generation but was thought impractical as a *training* objective because gradients require a population. **FD-loss** decouples the population size for FD estimation (50K) from the batch size for gradient computation (1024), making it tractable. Optimizing FD-loss in the Inception feature space yields **0.72 FID on ImageNet 256×256** for a one-step generator. The same loss repurposes multi-step generators into strong one-step generators *without teacher distillation, adversarial training, or per-sample targets*. Plus: FID can misrank visual quality — modern representations yield better samples despite worse Inception FID, motivating a multi-representation FDrk metric.

## Why interesting

Two threads:

1. **One-step generators without distillation.** The standard recipe for fast image generation is teacher-student distillation (multi-step model → one-step model). FD-loss replaces the teacher with a *distributional* objective in feature space. This bypasses the cross-architecture distillation problem entirely for visual generation.
2. **FID is not visual quality.** Modern representations rank samples better than Inception FID. This is a general lesson: *evaluation metrics atrophy as representation backbones improve.* Worth tracking whether the same effect appears in text (perplexity vs LLM judges).

## Connection to prior wiki

- **Tide (04-30)** distillation for diffusion LLMs. FD-loss is the *non-distillation* path for visual generation — distributional matching in feature space replaces token-level matching in token space. **The neutral-exchange-channel pattern (BLD, TESSY, Switch-KD, Tide)** could view FD-loss as another instance: the "channel" here is the population-level feature-space distribution.
- **Tier 1 distillation work** — the implicit comparison FD-loss invites: *when should you distill vs. minimize a feature-space distributional distance?* For text reasoning the answer is "distill" (token-level supervision is rich). For visual generation it may be "distributional."

## Research angle

The decoupling trick (population for estimation ≠ batch for gradient) is a small but generic engineering pattern. Whether it transfers to other distributional objectives (Sinkhorn, MMD, Wasserstein) for other domains (audio, text representations) is the obvious follow-up.
