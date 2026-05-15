# SU-01: Gold-Medal Olympiad Reasoning at 30B via Simple and Unified Scaling

**Source:** [HuggingFace Daily Papers](https://huggingface.co/papers/2605.13301) · [arXiv 2605.13301](https://arxiv.org/abs/2605.13301)
**Date ingested:** 2026-05-15
**Tier:** 2. Reasoning models, post-training recipes, math/physics olympiad
**Raw:** [farmer file](../../raw/huggingface/2026-05-15-achieving-gold-medal-level-olympiad-reasoning-via-simple-and-u.md)

## TL;DR

A 30B-A3B backbone (Shanghai AI Lab) trained with a three-stage recipe and only **200 RL steps** reaches gold-medal-level performance on IMO 2025 (35 points), USAMO 2026 (35 points, exceeding gold line by 10 points), and IPhO 2024/2025. The pipeline: (1) Rigorous SFT on ~340K sub-8K-token trajectories using a reverse-perplexity curriculum to instill proof-search and self-checking behaviors; (2) Two-Stage RL: Coarse RL with verifiable rewards, then Refined RL with generative rewards, self-refinement, experience replay; (3) Test-time scaling via self-verification and refinement loops. 57.6% on IMO-ProofBench with direct generation; 70.2% with test-time scaling. The model supports trajectories exceeding 100K tokens.

## What's new

The headline is the **"specializable-generalist" framing**: with the right recipe, a broadly capable compact backbone can specialize toward expert-level proof reasoning while retaining scientific transfer (IPhO 2024/2025 gold). Prior gold-medal IMO results from AlphaProof / Gemini Deep Think used domain-specific search and verification (geometry via AlphaGeometry, lean-style proof search). SU-01 does it with a single 30B reasoning model and a unified three-stage recipe.

Three components in the recipe.

**Reverse-perplexity curriculum SFT.** 340K sub-8K-token trajectories ordered by reverse perplexity (hardest first under the current backbone). This is unusual; standard SFT curriculum scheduling tends to ramp from easy to hard. The reverse ordering forces proof-search and self-checking behaviors early.

**Two-stage RL: Coarse → Refined.** Coarse RL with verifiable rewards (binary correct/incorrect on proof outcome). Refined RL adds generative rewards (model-judged proof quality), self-refinement loops, and experience replay. **200 RL steps total.** This is one to two orders of magnitude fewer than typical RLVR pipelines for reasoning models.

**Test-time scaling.** Self-verification and refinement at inference. Lifts IMO-ProofBench from 57.6% (direct) to 70.2% (TTS). The 100K+ token trajectory length is the practical ceiling for the TTS regime.

## Why this matters

Gold-medal IMO on a 30B-A3B model with 200 RL steps reframes what "scale" means in reasoning. The wiki has tracked test-time scaling, RL post-training, and compact-reasoning models as three threads; SU-01 composes them into a unified recipe and shows the result is gold-medal on the hardest standardized math/physics benchmarks. The "specializable-generalist" framing also generalizes: with the right recipe, model-class is the wrong unit of analysis.

The IPhO transfer is the secondary headline. Same recipe, different domain, still gold-medal-level. This is structural evidence for the claim that the recipe (not the data) is what's load-bearing.

## Connections to prior wiki pages

- [The Extrapolation Cliff](../inference-efficiency/2026-05-14-extrapolation-cliff-on-policy-distillation.md) — yesterday. Closed-form clip-safety for OPD with structured outputs. SU-01's Refined RL with structured proofs is the natural test case for cliff-conditioned training. Whether SU-01's 200 RL steps stay below λ-star throughout is open.
- [G-Zero](2026-05-12-g-zero-verifier-free-self-play.md) — formal bound for verifier-free self-play. SU-01 uses *verifiable* rewards (proof correctness), so it sits in the verifier-bound regime where the Cliff and OPSD apply.
- **AIMO 3** (04-17) — argued prompt diversity is a dead end for inference-time scaling. SU-01's TTS uses self-verification and refinement loops, not prompt diversity, and lifts IMO-ProofBench by 13 points. This is the first concrete refutation of the "all TTS is a dead end" framing.
- [Soohak refusal subset](2026-05-12-soohak-research-math-benchmark.md) — said frontier models confidently answer ill-posed problems. SU-01 is the inverse signal: a 30B model that wins gold by *proving rigorously*. The next eval question is whether SU-01 also passes Soohak's refusal subset.

## Research angle

1. **Reverse-perplexity curriculum elsewhere.** This is a curriculum design choice that has not been studied at this scale. Whether it transfers to coding, scientific reasoning, or agentic post-training is open.
2. **200-step RL plateau.** The paper claims gold-medal performance with only 200 RL steps. Whether more steps would help, plateau, or degrade (Cliff-style format collapse) is the obvious ablation.
3. **SU-01 vs AlphaProof economics.** AlphaProof used domain-specific search + lean verification. SU-01 uses one model + recipe. The cost comparison would tell the field whether "domain-specific tooling" is now strictly worse than "well-trained generalist."

## Why it matters

The most impressive single-model reasoning result in the wiki at this scale (30B-A3B) and this RL budget (200 steps). If the recipe is reproducible (the paper claims simplicity and unified scaling), the post-training playbook for reasoning models has a new default.

## Links

- [Paper](https://arxiv.org/abs/2605.13301)
- [HuggingFace](https://huggingface.co/papers/2605.13301)
- [Raw farmer file](../../raw/huggingface/2026-05-15-achieving-gold-medal-level-olympiad-reasoning-via-simple-and-u.md)
- Related: [The Extrapolation Cliff](../inference-efficiency/2026-05-14-extrapolation-cliff-on-policy-distillation.md), [G-Zero](2026-05-12-g-zero-verifier-free-self-play.md), [AIMO 3](2026-04-17-aimo-3-inference-time-scaling-dead-end.md), [rl-for-llms.md](rl-for-llms.md)
