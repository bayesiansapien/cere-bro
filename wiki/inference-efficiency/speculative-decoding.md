# Speculative Decoding

A class of lossless acceleration techniques: a cheap "draft" produces candidate tokens (or blocks), an expensive "target" verifies them via exact rejection sampling, and the verified prefix is committed. The target's output distribution is preserved — quality is unchanged.

## Current State (as of 2026-06-11)

**The MTP-acceptance collapse during RL now has a mechanism, and it is an entropy bound.** [Bebop](2026-06-11-bebop-mtp-rejection-sampling-rl.md) (arxiv 2606.12370) studies why multi-token-prediction drafting — the embedded-drafter idea Nemotron 3 Super introduced (04-21) — loses its speedup when used to accelerate RL rollouts, the application opened by [Speculative Decoding for RL Rollouts](2026-04-30-speculative-decoding-rl-rollouts.md) (04-30). The answer: MTP acceptance is negatively, near-linearly bounded by model entropy, and RL deliberately raises entropy to explore, so acceptance falls exactly when the rollout stage is most expensive. Three fixes: (1) probabilistic rejection sampling of draft tokens absorbs the entropy disturbance far better than greedy draft sampling; (2) a new end-to-end total-variation (TV) loss directly optimizes the multi-step rejection-sampling acceptance rate, where cross-entropy/KL are suboptimal, lifting acceptance to up to 95% (~10% gain); (3) train the MTP head *once before RL* — pre-RL TV-loss training holds acceptance steady across the whole run, so no costly online MTP updating. Up to 25% extra throughput and up to 1.8x end-to-end async-RL speedup on Qwen3.5/3.6/3.7. The deeper implication: rollout speed and policy-stability tuning are coupled — anything that holds entropy down (e.g. a tighter trust region like [DRPO](../llms-foundation-models/2026-06-10-drpo-divergence-regularized-policy-optimization.md), 06-10) should *raise* MTP acceptance for free.

## Current State (as of 2026-06-02)

Two same-day papers move speculative decoding past the "build a better draft architecture" era (EAGLE3, DFlash) into **better training objectives** and **better system scheduling**.

**Training axis: on-policy distillation for the drafter.** [Draft-OPD](2026-06-02-draft-opd-speculative-draft-distillation.md) (arxiv 2605.29343) diagnoses that SFT-built draft models plateau because of an offline-to-inference mismatch: the drafter trains on fixed target trajectories but is judged on the blocks it proposes under its own policy. Naive on-policy distillation fails because draft models cannot roll out reliably alone, and target-assisted rollout destroys the on-policy signal. Draft-OPD's fix: target-assisted rollout for stable continuations, but replay drafting from the verification-exposed error positions, so the drafter learns from target feedback on both accepted and rejected proposals. Over 5x lossless acceleration for thinking models, +23% over EAGLE-3, +13% over DFlash. This is the same covariate-shift lesson the wiki logs in TA-OPD (06-01), DRIFT (06-01), and DAgger-for-LLM-agents (05-14), now applied to the drafter — see [knowledge-distillation.md](knowledge-distillation.md).

**System axis: pipeline-parallel, zero-bubble speculation.** [SPD](2026-06-02-spd-speculative-pipeline-decoding.md) (arxiv 2605.30852) replaces multi-token prediction (whose difficulty escalates with depth and adds serial drafting latency) with pipeline parallelism: partition the target into n stages, process n tokens in parallel, and aggregate intermediate features across pipeline depths to predict the next token in parallel with the target's pipeline step. Result: bounded prediction difficulty, higher acceptance, and zero latency bubbles (no idle stages) in single-sequence decode. Draft-OPD improves draft *quality*; SPD removes draft *latency*. Together they show the field's gains are migrating from architecture to objective and scheduling.

## Current State (as of 2026-04-30)

Speculative decoding has crossed three axes of generalization in April 2026:

| Axis crossed | Paper | What it added |
|---|---|---|
| Inference → Training | NVIDIA / NeMo-RL (04-30) | RL post-training rollouts, lossless under policy drift |
| Text → Video | SDVG (04-22) | Token-level rejection replaced by image-quality routing |
| External draft → Embedded MTP head | Nemotron 3 Super (04-21) | The target *is* its own drafter via MTP heads |

The pattern is now: **wherever a generator has a slow target and a credible cheap proposer plus a verification signal that preserves target behavior, speculation applies**. The draft does not need to be exactly compatible with the target's architecture or even produce the same kind of output (e.g., SDVG's drafter produces video blocks, not tokens) — it only needs to produce candidates that the verification signal can accept or reject.

## Key Papers

**Nemotron 3 Super (2026-04-21)** — Embedded Multi-Token Prediction heads as the speculative drafter. The target model is its own drafter: an MTP head proposes future tokens during the same forward pass that produces the next token, eliminating the external draft model. → [summary](2026-04-21-nemotron3-super-hybrid-moe.md)

**SDVG (2026-04-22)** — Speculative decoding for autoregressive *video* generation. Token-level rejection replaced by ImageReward-based quality routing. 1.3B drafter proposes blocks; accepted blocks enter the 14B target's KV cache directly. 1.59–2.09× speedup at 95.7–98.1% quality. → [summary](2026-04-22-sdvg-speculative-decoding-video.md)

**Speculative Decoding for RL Rollouts (2026-04-30, NVIDIA)** — Lossless integration of speculative decoding into NeMo-RL + vLLM for RL post-training. Target policy is the verifier; log-probs and policy gradients are computed against target. Draft alignment to rollout distribution is the dominant variable; sweet spot at k=3. 1.77× generation, 1.41× per-step at 8B; 2.5× end-to-end projection at 235B on 2048 GB200s. → [summary](2026-04-30-speculative-decoding-rl-rollouts.md)

## Key Concepts

- **Lossless acceleration**: target's output distribution is preserved; no quality regression.
- **Draft alignment**: the draft must approximate the target's distribution well; misaligned drafts (e.g., chat draft for a math rollout) lose most of the speedup. The draft *initialization* matters more than online adaptation once aligned.
- **k = speculation depth**: number of tokens the draft proposes per round. Higher k = higher upside per accept, but also more wasted draft work on rejection. Empirically k=3 is the sweet spot at 8B reasoning workloads; k=5–7 can be net-negative.
- **Verification signal**: exact rejection sampling (text), quality router with worst-frame aggregation (video), policy-target log-probs (RL rollouts). The signal must be cheap relative to the target generation cost.
- **MTP head as embedded drafter**: a small head on the target model that produces multi-token proposals. Eliminates the external draft model and stays automatically aligned because it is part of the target.
- **Speculation under policy drift**: in RL training, the target policy moves with each gradient step. Weight synchronization between target and draft is required to keep alignment.

## Open Questions

- **Content-adaptive k**: empirically the optimal k varies with rollout phase (predictable math rollouts vs branchy reasoning). A learned k-schedule would beat the fixed-k regime.
- **Biased speculation**: current methods preserve losslessness. A drafter that deliberately proposes near *high-reward* regions (rather than approximating the current policy) could trade losslessness for sample efficiency in RL training.
- **Cross-modal speculation**: SDVG showed the verification signal does not have to be probability matching. The next test is whether speculation works for audio diffusion (worst-window quality routing?) or 3D synthesis.
- **Composition with consumer-GPU pipeline parallelism (RoundPipe, 05-01)**: NeMo-RL spec dec is a generation-during-training optimization; RoundPipe is a training-loop optimization for consumer hardware. Combining them on a consumer cluster could shrink small-lab post-training cost dramatically.
- **Composition with token-level value modeling (LenVM, 05-01)**: LenVM tells the model when to stop generating; speculative decoding makes each step cheaper. They should multiply — but no paper has measured the combined effect.

## Related Pages

- [KV Cache](kv-cache.md) — speculation populates the target's KV cache cheaply
- [Knowledge Distillation](knowledge-distillation.md) — drafts can be distilled, MTP heads can be co-trained
- [RL for LLMs](../llms-foundation-models/rl-for-llms.md) — rollout cost dominates, speculation is the answer
