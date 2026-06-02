# Speculative Pipeline Decoding (SPD): Zero-Bubble Speculation via Pipeline Parallelism

## TL;DR

Speculative decoding speeds up low-concurrency LLM inference with a draft-then-verify loop: a cheap proposer guesses the next tokens, the expensive target verifies them in parallel, and quality stays unchanged. Most methods build the proposer from multi-token prediction (predict several future tokens at once), but prediction difficulty climbs the further ahead you guess, and drafting runs serially, adding latency. Speculative Pipeline Decoding (SPD) drops the separate draft model entirely. It splits the target LLM itself into n pipeline stages (groups of layers placed across devices) so the model can process n tokens in parallel. To keep the pipeline busy during single-sequence decoding, where normally only one token flows through and most stages sit idle, SPD adds a speculation module that aggregates intermediate features from across the pipeline depths and predicts the next token. That prediction runs strictly in parallel with the target's own pipeline step, so speculation costs no extra latency. The result is bounded prediction difficulty, higher acceptance rates, and zero latency bubbles (no idle stages). The paper reports a significantly higher theoretical speedup than mainstream baselines, and the code is released.

```
┌─────────┐   ┌─────────┐   ┌─────────┐        ┌─────────┐
│ Stage 1 │ ─►│ Stage 2 │ ─►│ Stage 3 │ ─► ... ─►│ Stage n │  (target LLM, split across devices)
└────┬────┘   └────┬────┘   └────┬────┘        └────┬────┘
     │ feats       │ feats       │ feats            │ feats
     └─────────────┴──────┬──────┴──────────────────┘
                          ▼  aggregate intermediate features (across depths)
                   ┌──────────────┐ predict next token  ┌────────┐
                   │ speculation  │ ──────────────────► │ verify │ (runs IN PARALLEL
                   │   module     │   (no idle stages)  └────────┘  with pipeline step)
                   └──────────────┘
```

## Key points

- **No separate draft model.** SPD reuses the target's own layers as pipeline stages, so there is no second model to train, host, or keep aligned with the target.
- **Speculation in parallel with the pipeline step.** The speculation module aggregates intermediate features from multiple pipeline depths to predict the next token, executing strictly in parallel with the target's pipeline step. That is what gives "zero bubbles": stages that would otherwise idle in single-sequence decode now do useful speculative work.
- **Bounded difficulty, higher acceptance.** Because each speculative prediction draws on already-computed intermediate features rather than guessing many tokens ahead, prediction difficulty is bounded and acceptance rates rise relative to multi-token-prediction baselines.
- **Result:** a significantly higher theoretical speedup than mainstream baselines; presented as a scalable solution for single-sequence (low-concurrency) decode. Code: https://github.com/yuyijiong/speculative_pipeline_decoding

## How this relates to prior wiki pages

SPD and [Draft-OPD](2026-06-02-draft-opd-speculative-draft-models.md) (same day, 2026-06-02, which fixes the offline-to-inference mismatch in SFT-trained draft models with on-policy distillation for over 5x lossless speedup) attack speculative decoding from two different layers: Draft-OPD improves the *training objective* of a draft model, SPD changes the *system scheduling* and removes the draft model altogether. Together they show the field's gains are migrating off draft-architecture tweaks (EAGLE-3, DFlash) toward better objectives and better hardware scheduling. See the synthesis in [speculative-decoding.md](speculative-decoding.md). SPD also belongs to the pipeline-parallel-on-few-devices line the wiki tracks for low-concurrency serving, where filling otherwise-idle pipeline stages is the whole game.

## Gaps

The reported speedup is "theoretical" in the abstract; the gap between theoretical and measured end-to-end latency on real hardware (where stage imbalance, activation transfer between devices, and verification overhead bite) is not quantified here. The method targets single-sequence, low-concurrency decode; how it interacts with continuous batching at higher concurrency, where stages are already busy, is unaddressed. Acceptance-rate numbers versus the multi-token-prediction baselines it critiques are asserted but not broken out per task in the abstract.

**Source:** [arXiv 2605.30852](https://arxiv.org/abs/2605.30852) · raw: [raw/huggingface/2026-06-02-speculative-pipeline-decoding-higher-accruacy-and-zero-bubbl.md](../../raw/huggingface/2026-06-02-speculative-pipeline-decoding-higher-accruacy-and-zero-bubbl.md)
