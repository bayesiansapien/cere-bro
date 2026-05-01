# PhyCo: Controllable Physical Priors for Generative Motion

**arXiv:** 2604.28169 · [paper](https://arxiv.org/abs/2604.28169) · [HF](https://huggingface.co/papers/2604.28169)
**Tier:** 3 — video generation / physics
**Raw:** [../../raw/huggingface/2026-05-01-phyco-learning-controllable-physical-priors-generative-motion.md](../../raw/huggingface/2026-05-01-phyco-learning-controllable-physical-priors-generative-motion.md)

## TL;DR

Video diffusion models excel at appearance but fail on physical consistency: drift, missing rebounds, wrong material responses. **PhyCo** adds physical control via three components: (1) a 100K-video photorealistic simulation dataset varying friction, restitution, deformation, force; (2) physics-supervised fine-tuning with a ControlNet conditioned on pixel-aligned physical-property maps; (3) VLM-guided reward optimization where a fine-tuned VLM evaluates videos with targeted physics queries and provides differentiable feedback. Improves Physics-IQ benchmark over strong baselines; no simulator or geometry reconstruction at inference.

## Connection to prior wiki

- **X-WAM (04-30)** unified 4D world action modeling with asynchronous denoising. PhyCo is complementary — X-WAM works at the action-level, PhyCo at the physical-property level.
- **Edit-R1 (05-01)** uses VLM-as-reasoning-verifier reward. PhyCo uses VLM-as-physics-evaluator reward. Same pattern (VLM reward provider), different domain.
- **Visual Generation Taxonomy (05-01)** — PhyCo lands at Conditional Generation with physical conditioning, a step toward higher levels in the taxonomy.

## Research angle

The interesting open question: *does physics-supervised fine-tuning generalize beyond the training scenarios?* The dataset varies friction/restitution/deformation/force; whether the model learns a generic physics prior or just memorizes per-scenario behavior is what determines whether this scales.
