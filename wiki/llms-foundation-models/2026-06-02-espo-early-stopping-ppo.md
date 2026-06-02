# ESPO: Early-Stopping Proximal Policy Optimization

## TL;DR

When an LLM under reinforcement learning makes a wrong reasoning step early in a rollout, standard PPO (Proximal Policy Optimization, the workhorse RL algorithm for LLMs) forces it to keep generating to the maximum length, spending compute on tokens that never earn reward and polluting the advantage estimates with post-failure noise. ESPO detects a doomed trajectory mid-rollout and kills it early. At each generation step it computes a surrogate regret using only the logits already produced during sampling, so there is no extra forward pass and no separate reward model. When the smoothed cumulative regret significantly exceeds its estimated value, ESPO terminates and treats the truncated trajectory as an absorbing failure state with a terminal reward, which concentrates the negative temporal-difference error (the learning signal that says "this was bad") right at the detected failure step. On DeepSeek-R1-Distill-Qwen-7B for math, ESPO beats PPO on AIME 2024, AMC 2023, and MATH-500 while saving more than 20% of rollout tokens.

```
  each gen step ─► compute surrogate REGRET from logits already produced
                                  │
                                  ▼
                     accumulate SMOOTHED cumulative regret
                                  │
                   regret >> estimate ?  ──no──► keep generating
                                  │ yes
                                  ▼
        TERMINATE early ─► mark as absorbing FAILURE state (terminal reward)
                                  │
                                  ▼
        negative TD error concentrated near the failure step ─► PPO update
        truncated tail discarded (no wasted compute, no post-failure noise)
```

## Key points

- DeepSeek-R1-Distill-Qwen-7B: AIME 2024 46.28% vs PPO 45.25%, AMC 2023 85.83% vs 82.94%, MATH-500 87.42% vs 85.43%.
- Saves more than 20% of rollout tokens cumulatively by not generating past a detected failure.
- The failure detector is free: surrogate regret is computed only from logits already produced during sampling, with no extra reward model and no human annotation.
- Truncated trajectories become absorbing failure states with a terminal reward, which sharpens the credit signal by putting the negative TD error near the actual failure step instead of smearing it over the whole post-failure tail.

## How this relates to prior wiki pages

ESPO is the cleanest "stop wasting compute on doomed computation" entry on the RLVR-efficiency thread the wiki tracks. It is the rollout-pruning sibling of [Stop Path Pruning (2026-04-20), which cut parallel-reasoning branches that were not going to pay off](../inference-efficiency/2026-04-20-stop-path-pruning-parallel-reasoning.md): both kill unproductive generation early, but ESPO does it inside the RL training loop using a regret signal derived from logits rather than at inference. It also pairs with today's [temporal scheduling for RLVR (2026-06-02), which argues when you allocate credit over training matters as much as where across tokens](2026-06-02-temporal-scheduling-rlvr.md): both attack PPO's blunt, uniform treatment of a trajectory, ESPO by truncating the failed tail and temporal scheduling by reweighting which tokens carry the signal. The "concentrate the negative signal at the failure step" idea echoes the credit-localization line in [DELTA discriminative token credit (2026-05-23), which assigned RLVR credit to the discriminative tokens rather than uniformly](2026-05-23-delta-discriminative-token-credit-rlvr.md). See [rl-for-llms.md](rl-for-llms.md).

## Gaps

Results are on a single 7B distilled model on math benchmarks, so it is unclear whether the surrogate-regret detector generalizes to other model sizes, base (non-distilled) models, or non-math domains where a "failure step" is harder to localize. The detector could in principle terminate a recoverable trajectory that would have self-corrected, and the abstract does not report false-positive rates or how the regret threshold is tuned. Whether the 20%+ token savings translate into proportional wall-clock or cost savings under real batched rollout infrastructure is not shown.

**Source:** [arXiv 2605.29860](https://arxiv.org/abs/2605.29860) · [raw file](../../raw/huggingface/2026-06-02-espo-early-stopping-proximal-policy-optimization.md)
