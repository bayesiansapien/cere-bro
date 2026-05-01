# Speculative Decoding

A class of lossless acceleration techniques: a cheap "draft" produces candidate tokens (or blocks), an expensive "target" verifies them via exact rejection sampling, and the verified prefix is committed. The target's output distribution is preserved — quality is unchanged.

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
