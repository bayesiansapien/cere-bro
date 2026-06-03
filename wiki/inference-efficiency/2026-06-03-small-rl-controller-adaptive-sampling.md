# Small RL Controller, Large Language Model: RL-Guided Adaptive Sampling for Test-Time Scaling

**Date:** 2026-06-03
**Source:** HuggingFace Daily Papers
**arXiv:** [2606.03102](https://arxiv.org/abs/2606.03102)
**Tier:** 1/2 — Test-time scaling, inference cost control, adaptive sampling

## TL;DR

Test-time scaling (sampling many candidate answers and picking the best) improves reasoning accuracy but costs a lot in total compute and latency. Existing adaptive-sampling methods decide when to stop drawing samples, but they lean on heuristic rules or distributional assumptions. This paper formalizes adaptive sampling as a Markov decision process and trains a tiny RL controller to make the stop-or-sample-more decision each round, jointly balancing answer correctness, latency, and compute cost. The controller only needs statistics of the final answers seen so far, so it is light enough to train and run on CPU alongside the large model. The authors show the resulting objective is the Lagrangian relaxation of a constrained optimization with explicit budget limits, which gives the knobs a clean interpretation. Against strong baselines (ASC and ESC), it gets better trade-offs among correctness, number of sampling rounds, and total samples.

```
   query ──► big LLM ──► sample batch ──► answer statistics
                                              │  (agreement, counts)
                                              ▼
                                   ┌────────────────────┐
                                   │ small RL controller │  (MDP, runs on CPU)
                                   │  stop?  sample more? │
                                   └─────────┬──────────┘
                              stop ◄─────────┴────────► acquire more samples
                          (return answer)            (spend budget)

   reward = correctness  −  λ_latency·latency  −  λ_cost·samples
            └─ Lagrangian relaxation of a budgeted constrained problem ─┘
```

## Key findings

1. **Adaptive sampling as an MDP.** Framing the stop/continue decision as sequential decision-making, rather than a fixed heuristic, lets a learned policy adapt to the difficulty signal that the answer statistics carry round-to-round.
2. **The controller is cheap and decoupled.** It consumes only final-answer statistics (not hidden states or logits), so it trains and deploys on CPU, sitting beside the GPU-bound LLM rather than inside it.
3. **Clean theory.** The training objective is the Lagrangian relaxation of a constrained optimization with explicit budget constraints, so the cost/latency weights map to real budget limits.
4. **Better Pareto trade-offs.** Improves the correctness-vs-rounds-vs-total-samples frontier over ASC and ESC.

## Relation to prior wiki state

This is the test-time-compute companion to the wiki's broad "spend computation where it matters" thread. The [rl-for-llms page](../llms-foundation-models/rl-for-llms.md) and the inference stack have repeatedly tracked the move from a static schedule to a learned controller: [LenVM](2026-05-01-lenvm-token-level-length-value-model.md) (05-01) put a token-level length-value model on the generation budget, [ESPO](../llms-foundation-models/2026-06-02-espo-early-stopping-ppo.md) (06-02) added early stopping inside PPO, and [Temporal Scheduling for RLVR](../llms-foundation-models/2026-06-02-temporal-scheduling-rlvr.md) (06-02) scheduled the credit-allocation criterion over training. The Small RL Controller is the same shape applied to the outermost loop — how many samples to draw — and is notable for putting the controller on CPU, which makes it free relative to the LLM's GPU cost.

It is also a structural cousin of LLM routing. The [llm-routing page](../ai-routing/llm-routing.md) tracks cheap models that decide where to send a query; here a cheap RL policy decides *how much to spend* on a query already in flight. Routing-as-policy and budgeting-as-policy are the same idea at two layers of the stack.

The "only final-answer statistics" design connects to [Conf-KV](2026-05-30-conf-kv-confidence-aware-eviction.md) (05-30) and the broader confidence-signal line: a scalar derived from the model's own outputs is enough to control a budget, without peeking inside the model.

## Research angle

1. **Difficulty-conditioned routing + budgeting.** The controller currently reacts to answer statistics. Conditioning it on a cheap upfront difficulty estimate (a router signal) before the first sample would let it allocate the initial batch size, not just the stopping point.
2. **Transfer across models.** Because the controller only sees answer statistics, it should transfer across base models without retraining. Whether a controller trained on one model's agreement dynamics works on another is a clean, falsifiable test.
3. **Compose with verifier-based scaling.** ASC/ESC are self-consistency style. Plugging a verifier or process-reward signal into the controller's state (instead of bare agreement counts) is the obvious upgrade and connects to the wiki's process-reward thread.

## Links

- [Paper (arXiv)](https://arxiv.org/abs/2606.03102)
- [HuggingFace page](https://huggingface.co/papers/2606.03102)
- Raw: [raw/huggingface/2026-06-03-small-rl-controller-large-language-model-rl-guided-adaptive.md](../../raw/huggingface/2026-06-03-small-rl-controller-large-language-model-rl-guided-adaptive.md)
- Concept page: [KV Cache](kv-cache.md) · [LLM Routing](../ai-routing/llm-routing.md)
- Related: [LenVM 05-01](2026-05-01-lenvm-token-level-length-value-model.md) · [ESPO 06-02](../llms-foundation-models/2026-06-02-espo-early-stopping-ppo.md)
