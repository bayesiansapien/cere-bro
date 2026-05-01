# CoPD: Co-Evolving Policy Distillation

**arXiv:** 2604.27083 · [paper](https://arxiv.org/abs/2604.27083) · [HF](https://huggingface.co/papers/2604.27083)
**Tier:** 2 — RL/distillation hybrid, post-training
**Raw:** [../../raw/huggingface/2026-05-01-co-evolving-policy-distillation.md](../../raw/huggingface/2026-05-01-co-evolving-policy-distillation.md)

## TL;DR

Standard "all-in-one" multi-capability post-training has two failure modes: **mixed RLVR** suffers inter-capability divergence (training one capability hurts another), and **train-experts-then-OPD** avoids divergence but the student fails to absorb teacher capabilities because the behavioral pattern gap is too wide. CoPD fixes both by training experts *in parallel* and inserting on-policy distillation *during* each expert's RLVR run, with experts serving as **mutual teachers** (bidirectional OPD). Result: a single model that integrates text, image, and video reasoning, beating both mixed RLVR and MOPD baselines and even surpassing domain-specific experts.

## Mechanism

```
              ┌──────── Expert A (text reasoning, RLVR) ─────────┐
              │            │                                      │
              │    ←── OPD bidirectional ──→                      │
              │            │                                      │
              ├──────── Expert B (image reasoning, RLVR) ─────────┤
              │            │                                      │
              │    ←── OPD bidirectional ──→                      │
              │            │                                      │
              └──────── Expert C (video reasoning, RLVR) ─────────┘
                          ↓
                  Co-evolved unified model
```

The key differentiation from MOPD (mixture-of-OPD): MOPD distills *after* each expert is fully trained, by which time the experts have drifted into specialist behavioral patterns. CoPD interleaves OPD with RLVR, so experts co-evolve — neither drifts too far from the others. Bidirectional OPD means each expert is both teacher and student of every other expert, which keeps behavioral patterns consistent throughout training.

## Why this matters

**Multi-capability post-training has been an open infrastructure problem.** Single-capability RLVR is well-understood (TIP 04-16, PreRL 04-16, GFT 04-21); but combining capabilities at frontier scale has been ad-hoc. CoPD is the first paper to give the parallel-training-with-mutual-distillation pattern a clean formalization.

The **"experts surpass domain-specific experts"** claim is the surprise. Standard intuition: a domain expert beats a generalist. CoPD's bidirectional OPD allows cross-capability transfer to act as regularization — the text expert benefits from being constrained by the image expert's behavioral patterns. This is the multimodal-RLVR analog of what TESSY (04-18) showed for stylistic distillation: cross-domain pressure improves both domains.

## Connection to prior wiki

- **TESSY (04-18) / Switch-KD (04-18) / Tide (04-30)** — all cross-architecture or cross-modality distillation papers that engineer a *neutral exchange channel*. CoPD's bidirectional OPD between RLVR experts is the same architectural choice applied to *parallel* training rather than student/teacher pipeline. **Five papers in three weeks** all expressing variants of "engineer the channel between mismatched models" — this is now a confirmed convergence.
- **Mixed RLVR's divergence cost** echoes the **Hope (04-28)** finding that nested learning architectures need structured cross-timescale interfaces or they collapse. Both papers are arguments against naive multi-objective training.
- **GLM-5V-Turbo MMTP (04-30)** trained perception, reasoning, and tool use jointly via MTP heads. CoPD trains modality experts in parallel via bidirectional OPD. Two different mechanisms (architectural vs procedural), same goal.

## Research angle

Three open follow-ups:

1. **Number of experts.** CoPD demonstrates 3 experts (text, image, video). Does the bidirectional-OPD pattern scale to 10? 30? The communication cost of full bidirectional OPD is O(N²) in expert count.
2. **Asymmetric capability investment.** Should text-RLVR steps and video-RLVR steps run at the same rate? The behavioral-pattern gap may be wider for some pairs than others, suggesting an adaptive interleaving schedule.
3. **Composition with KV cache primitives.** All experts presumably share a backbone. What does the KV cache look like during bidirectional OPD — are there reuse opportunities? This is where CoPD intersects Tier 1: efficient mutual distillation at frontier scale will require KV-aware scheduling.

The phrase "may inspire a novel training scaling paradigm" in the abstract is doing a lot of work. The bidirectional-OPD-during-RLVR structure is a real candidate for the next default post-training recipe — worth tracking whether anyone reproduces it at frontier scale within 90 days.
