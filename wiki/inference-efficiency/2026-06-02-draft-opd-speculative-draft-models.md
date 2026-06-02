# Draft-OPD: On-Policy Distillation for Speculative Draft Models

## TL;DR

Speculative decoding speeds up large language model inference by pairing a big "target" model with a small "draft" model. The draft proposes a block of tokens, the target verifies them all in parallel, and any prefix the target agrees with is committed for free, so quality is unchanged. The usual way to build a drafter is supervised fine-tuning (SFT) on trajectories the target generated. Draft-OPD shows that this plateaus. The drafter trains on the target's own sequences but is judged on the blocks it proposes under its own policy, an offline-to-inference mismatch that caps how long its proposals get accepted. The fix is on-policy distillation (OPD), where the target supervises the drafter on states the drafter actually produces. Naive OPD fails here because draft models cannot roll out a full sequence reliably on their own, and letting the target assist the rollout erases the on-policy signal. Draft-OPD uses target-assisted rollout for stable continuations, then replays drafting from the exact positions where verification exposed an error, so the drafter learns from target feedback on the draft-induced mistakes that actually limit acceptance. It reaches over 5x lossless acceleration for reasoning ("thinking") models, beating EAGLE-3 by 23% and DFlash by 13%.

```
┌──────────┐ block  ┌──────────┐ accept/reject  ┌───────────────────┐
│  Draft   │ ─────► │  Target  │ ─────────────► │ verification finds │
│  model   │        │ verifies │   (parallel)   │  error positions   │
└──────────┘        └──────────┘                └─────────┬─────────┘
     ▲                   │ target-assisted rollout         │ replay drafting
     │ OPD loss          ▼ (stable continuation)           │ from EACH error pos
     └───────────── target supervises drafter ◄────────────┘
                    on draft-induced errors  ──► loop
```

## Key points

- **Diagnosis: SFT drafters plateau from covariate shift.** The drafter's acceptance length on test data stops improving under SFT because it trains on fixed target-generated trajectories yet is evaluated on blocks proposed under its own (drifted) policy.
- **The naive-OPD trap.** Draft models cannot reliably roll out complete sequences alone, but if the target assists the rollout the collected sequence follows the target distribution and the on-policy signal disappears. Draft-OPD threads this needle: target-assisted rollout for stable continuations, replayed drafting from verification-exposed error positions.
- **Learns from both accepted and rejected proposals.** Training concentrates on the draft-induced errors that limit speculative acceptance, rather than spreading signal uniformly over every token.
- **Results:** over 5x lossless acceleration for thinking models across diverse tasks; +23% over EAGLE-3 and +13% over DFlash. Acceleration is lossless because the target still verifies every token by exact rejection sampling.

## How this relates to prior wiki pages

Draft-OPD is the same instinct as [TA-OPD](2026-06-01-ta-opd-token-teachability.md) (2026-06-01, which showed you should train only on the roughly 5% of tokens whose teacher correction the student can actually reach, formalized as "token teachability"), applied one level out: instead of selecting the teachable tokens inside a student's vocabulary distribution, Draft-OPD selects the load-bearing positions inside a draft block, namely the verification-exposed error positions. Both papers reject uniform supervision and concentrate training where the signal lives. It also extends the on-policy-distillation covariate-shift thread documented in [knowledge-distillation.md](knowledge-distillation.md): the offline training distribution does not equal the on-policy test distribution, and Draft-OPD carries that lesson cleanly to the speculative-decoding drafter. On the decoding side it is the training-axis counterpart to the system-axis work catalogued in [speculative-decoding.md](speculative-decoding.md): Draft-OPD improves draft quality, whereas pipeline-parallel scheduling removes draft latency.

## Gaps

The headline 5x is reported for reasoning/"thinking" models; whether the same offline-to-inference gap is large enough to matter for short, non-reasoning generations is not shown. The paper measures gains relative to EAGLE-3 and DFlash, but does not report how much of the drafter's remaining acceptance ceiling is structural (block-size limits, target entropy) versus still addressable by better training. The cost of the extra target-assisted rollout and replay passes during training, and how that scales with model size, is not quantified here.

**Source:** [arXiv 2605.29343](https://arxiv.org/abs/2605.29343) · raw: [raw/huggingface/2026-06-02-draft-opd-on-policy-distillation-for-speculative-draft-model.md](../../raw/huggingface/2026-06-02-draft-opd-on-policy-distillation-for-speculative-draft-model.md)
