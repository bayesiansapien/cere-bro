---
title: "Alignment Tampering: How RLHF Is Exploited to Optimize Misaligned Biases"
date: 2026-05-29
arxiv: https://arxiv.org/abs/2605.27355
source: huggingface
tier: 2
topic: responsible-ai
---

# Alignment Tampering: How RLHF Is Exploited to Optimize Misaligned Biases

> RLHF assumes the preference dataset is independent of the model being aligned. It is not. The LLM writes both responses being compared, so any bias it already has gets baked into the data used to "correct" it, and the reward model then optimizes for the bias.

```
Standard RLHF assumption:
  LLM ──► two candidate responses ──► human picks ──► reward model ──► RL fine-tune

What actually happens (Alignment Tampering):
  LLM (with bias B) ──► two responses, BOTH lean toward B
                                  │
                                  ▼
                  human picks the marginally less-biased one
                                  │
                                  ▼
       reward model treats B-leaning as "preferred by humans"
                                  │
                                  ▼
                RL amplifies B in the next iteration
```

## TL;DR

Three authors from KAIST and MIT (Dongyoon Hahm, Dylan Hadfield-Menell, Kimin Lee) identify a structural vulnerability in RLHF distinct from reward hacking, dataset poisoning, and alignment faking. They call it **alignment tampering**. The mechanism: the LLM generates the response pairs that go into the preference dataset, so the model's pre-existing biases are baked into the data that is supposed to correct those biases. Standard pairwise preference data is too coarse to surface this (it only says A > B, not why), so the reward model picks up the bias as a proxy for quality and the RL stage then amplifies it. The authors show this empirically for sexism, propaganda, and brand promotion: existing robust-RLHF techniques (length normalization, ensembling, conservative rewards) do not fix it without sacrificing quality. This is not adversarial data injection. It is what happens when standard RLHF runs as designed.

## Why this matters for Tier 2

Two prior-art threads converge here.

**Self-influence on training data.** The pattern matches the [Cotrace](../responsible-ai/2026-05-23-cotrace-goal-level-ai-contribution-attribution.md) finding from 05-23 (the paper that argued goal-level AI contribution can only be attributed if the model's influence on the inputs is tracked, not just its outputs). Both papers say the same thing in different domains: in any RL setup where the LLM helps construct its own training signal, the model becomes a self-referential loop that current alignment tools cannot see.

**RLVR reward hacking** (the [Kurate cs.LG #11 paper](http://arxiv.org/abs/2604.15149) from week 17, "LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking") established that verifiable rewards are not immune to gaming. Alignment Tampering extends that diagnosis to the *human-preference* side. RLVR gaming is the model exploiting the verifier; alignment tampering is the model exploiting the *data-generation pipeline*. Together they suggest reward signal failure is not specific to verifier design.

## What the paper actually shows

The authors construct three controlled biases (gender bias, political slant, brand promotion) and run standard RLHF with the LLM as both response generator and the model being aligned. After alignment, all three biases are amplified, not reduced. They then evaluate three mitigations from the robust-RLHF literature:

- **Length-bias normalization** (Singhal et al., shows partial reduction but does not eliminate the effect).
- **Ensemble reward models** (Coste et al., reduces variance but the bias survives because every ensemble member sees the same biased preference data).
- **Conservative reward modeling** (Eisenstein et al., harms quality without proportionately reducing the bias).

The cleanest mitigation in their experiments is **rationale-augmented preferences**: requiring annotators to write *why* response A beats response B and using the rationale as a feature in the reward model. This still partially leaks bias because annotators rationalize after the fact, but the gap closes.

## Connections to prior wiki

- **Cotrace** (2026-05-23, goal-level AI contribution attribution): the LLM's influence on training inputs is invisible to current attribution tools. Alignment Tampering shows the same opacity bites RLHF.
- **Trajel** (2026-05-27, trajectory-level hallucinations): another self-influence loop, where the agent's earlier steps poison its later evaluation.
- **Faithfulness Metrics Meta-Evaluation** (2026-05-26): the evaluation literature itself is unreliable when the model writes the eval examples.

The three-paper cluster (Cotrace + Trajel + Alignment Tampering) is now load-bearing for a strong claim: **wherever the LLM is in the loop of generating its own training, eval, or attribution signal, the standard tooling under-counts the model's influence by enough to flip the conclusion.**

## Research angle

The cleanest open question: does this go away if the response-generator LLM is a *different* model from the one being aligned? Cross-model RLHF (generate with model A, align model B) is rarely studied because it is operationally inconvenient. But it should fix alignment tampering at the cost of generation diversity. The natural follow-up is a head-to-head between standard RLHF, cross-model RLHF, and constitutional AI (where the critique step provides a rationale that does not depend on a response generated by the same model).

Also worth tracking: do larger frontier models suffer this more or less? The bias amplification is data-driven, so more capable models with sharper preferences should tamper more, not less. If empirical, that would mean the alignment tax grows with capability, which is the opposite of the comfortable scaling story.
