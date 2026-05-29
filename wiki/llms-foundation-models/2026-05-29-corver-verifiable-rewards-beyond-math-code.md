---
title: "CorVer: Verifiable Rewards Beyond Math and Code via Corpus-Grounded Process Supervision"
date: 2026-05-29
arxiv: https://arxiv.org/abs/2605.29648
source: huggingface
tier: 2
topic: llms-foundation-models
---

# CorVer: Verifiable Rewards Beyond Math and Code (Lightweight Corpus-Grounded Process Supervision for Factual QA)

> RLVR works for math and code because correctness is mechanically verifiable. Open-domain factual QA has had no such hook. CorVer replaces the expensive neural verifier with a Wikipedia-cooccurrence lookup and a 0.5B extractor, beating neural verifiers in 18 of 20 cells while training 4.8x–8.4x faster.

```
Reward-design dilemma in factual QA RL:

  Response-level ► coarse: can't tell which sentence in the trace is wrong
  Sentence-level ► fine-grained
       │
       └─► requires VERIFIER: NLI / LLM-judge / KB-verification pipeline
            ► expensive at RL scale
            ► UNRELIABLE for rare-entity facts (where it matters most)

CorVer (this paper):

  reasoning trace      ► extracted into sentences (0.5B extractor)
                                 │
                                 ▼
                          Wikipedia corpus
                                 │
                                 ▼
              co-occurrence statistics  (PMI-style signal: do the named entities show up together?)
                                 │
                                 ▼
                  sentence-level credit ► token-level advantage
                                 │
                                 ▼
                          GRPO update

No NLI model. No LLM judge. No knowledge-verification graph traversal.
Just a lookup. Robust on rare-entity facts because Wikipedia DOES cover rare entities.
```

## TL;DR

RL-with-verifiable-rewards (RLVR) has dominated math and code because every step has a mechanical verifier. Knowledge-intensive QA has been stuck because response-level rewards (correct/incorrect) are too coarse to distinguish good and bad steps inside a chain-of-thought, while sentence-level alternatives have required neural verifiers (NLI models, LLM-judges, knowledge-verification pipelines) that are expensive and unreliable on rare-entity facts. CorVer replaces the neural verifier entirely with a corpus-grounded signal derived from Wikipedia co-occurrence statistics. A small 0.5B extractor parses the reasoning trace into sentences; the signal at the sentence level is then mapped to token-level advantages via simple alignment, and dropped into the standard RL training loop. Across 30 (model, benchmark) cells spanning six instruction-tuned models (3B to 14B) and five QA benchmarks, CorVer improves over the raw baseline for every cell, with an average TriviaQA gain of +4.1 percentage points. It outperforms four neural-verifier baselines in 18 of 20 feasible cells while training 4.8x–8.4x faster.

## Why this matters

The "math and code only" ceiling on RLVR has been an open problem for over a year. Several recent attempts (rubric-based rewards, **C2** from 2026-04-18 — the rubric-reward-modeling paper that decomposed evaluation into criteria, today's **RUBRIC-ARROW** — the alternating rubric framework) have pushed at it from the rubric side, but rubrics still need a strong rubric-following judge to score them. CorVer takes a different cut: replace the *verifier* with a *retrieval-grounded look-up*. This is the same architectural move as RAG (retrieval beats generation when grounding matters), applied to the verifier in an RL loop.

The most consequential claim is the rare-entity reliability. Neural verifiers fail exactly where accurate signal matters most (rare facts about real entities the LLM hasn't memorized). Wikipedia covers the long tail. A simple lookup beats a learned judge on the rare-entity regime by being grounded, not smart. This is a clean second confirmation of the **"Generative Augmented Inference"** (Kurate cs.LG #18, the paper that argued inference should be retrieval-grounded) cluster of results from earlier this month.

## Connections to prior wiki

- **VGF value gradient flow RL** (2026-04-19): distribution-transport view of RL training. CorVer's per-sentence credit assignment is a concrete implementation of moving probability mass.
- **C2 rubric reward modeling** (2026-04-18) and **RUBRIC-ARROW** (2026-05-29, today): rubric-side approaches to non-verifiable rewards. CorVer is the corpus-grounded sibling.
- **W-RAC retrieval-aware chunking** (2026-04-20): retrieval-side improvements. CorVer reuses the retrieval-grounding idea but for *verifier* construction rather than *generator* construction.

## Research angle

Why does this work? The Wikipedia co-occurrence signal is a noisy proxy for "is this sentence consistent with verified knowledge." That noise is the right kind of noise: it's biased toward conservative credit (sentence with rare-entity-but-real co-occurrence gets credit). Neural verifiers' noise is biased the other way (confident on what was in training, fragile outside).

The natural follow-up is to swap Wikipedia for a domain-specific corpus (PubMed for medical QA, Lean libraries for math, Stack Overflow for code-style QA) and see if the pattern holds. If it does, CorVer is a general recipe and the math/code RLVR moat is gone: anywhere a sufficiently dense corpus exists, you can build a cheap process reward.

Industrial implication: training cost matters a lot. 4.8x–8.4x faster than neural-verifier baselines, at higher accuracy, is the kind of unit-economics shift that retrains the production decision matrix for any team running RL on factual QA models.
