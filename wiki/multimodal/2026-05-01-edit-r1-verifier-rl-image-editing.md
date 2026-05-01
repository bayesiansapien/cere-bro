# Edit-R1: Verifier-Based RL for Image Editing

**arXiv:** 2604.27505 · [paper](https://arxiv.org/abs/2604.27505) · [HF](https://huggingface.co/papers/2604.27505)
**Tier:** 3 — multimodal / image editing
**Raw:** [../../raw/huggingface/2026-05-01-leveraging-verifier-based-reinforcement-learning-image-editing.md](../../raw/huggingface/2026-05-01-leveraging-verifier-based-reinforcement-learning-image-editing.md)

## TL;DR

RLHF works for text-to-image generation but applying it to *image editing* has been blocked by the lack of a robust general reward model. Existing edit reward models give one overall score and miss instruction-specific principles. **Edit-R1** introduces a CoT *reasoning verifier* reward model: it breaks the instruction into principles, evaluates the image against each, and aggregates an interpretable fine-grained reward. Built via SFT cold-start on CoT reward trajectories + Group Contrastive Preference Optimization (GCPO) on pairwise human preferences. The RRM (reward reasoning model) outperforms Seed-1.5-VL and Seed-1.6-VL as an editing reward; performance scales 3B → 7B; downstream Edit-R1 improves FLUX.1-kontext.

## Why this is interesting (despite being Tier 3 for Amit)

The mechanism — **scorer to reasoning verifier** — generalizes far beyond image editing. The same shift is happening in:
- LLM judges (judge → reasoning judge with structured rubrics)
- Process reward models for math (single answer reward → step-level CoT reward)
- Code-generation evaluation (final pass/fail → step-level lint/spec/runtime checks)

Edit-R1 is part of the **"reasoning verifiers replacing scalar rewards"** thread that connects to RLHF / RLVR work in Tier 1. Worth a one-line mention in the RL-for-LLMs concept page even though the application is multimodal.

## Connection to prior wiki

- **C2 / Rubric Reward Modeling (04-18)** — first paper to formalize rubric-based reward in this way for text. Edit-R1 is the multimodal analog. Two papers in two weeks reaching for "decompose the instruction into principles, score each, aggregate" suggests this is the convergent reward-modeling pattern.
- **RationalRewards (04-16)** — also argued for critique-before-score reward modeling for visual generation. Edit-R1 is a deeper, RL-trained version of the same idea applied specifically to editing.

## Research angle

GCPO (Group Contrastive Preference Optimization) is the RL piece — it leverages pairwise preferences to refine the pointwise RRM. The mechanism (group-contrastive instead of pairwise-DPO) is worth tracking as a generic preference-RL recipe that may transfer to text reasoning.
