# Chain-of-Thought Degrades Visual Spatial Reasoning

**Date:** 2026-04-22  
**Source:** [HuggingFace](https://huggingface.co/papers/2604.16060) | [Paper](https://arxiv.org/abs/2604.16060)  
**Raw:** [raw/huggingface/2026-04-22-chain-of-thought-degrades-visual-spatial-reasoning-capabilit.md](../../raw/huggingface/2026-04-22-chain-of-thought-degrades-visual-spatial-reasoning-capabilit.md)

## TL;DR

Comprehensive evaluation across 17 models and 13 spatial benchmarks shows that CoT prompting *consistently degrades* performance on visual spatial reasoning tasks. A No-Image++ ablation reveals that Multimodal Reasoning Models (MRMs) suffer severe shortcut learning — they hallucinate visual details from textual priors even when the image is absent. Text-only CoT is not a universal reasoning enhancer; it actively interferes with vision-centric tasks.

## Key Findings

- CoT prompting consistently degrades spatial reasoning across **17 models and 13 benchmarks** — not an isolated finding
- **No-Image++ ablation**: models hallucinate spatial details from text context even with the image removed, showing they're relying on language priors not visual parsing
- Models with stronger language CoT (reasoning models) often perform *worse* on spatial tasks than vanilla MLMs
- Suggests spatial reasoning requires fundamentally different representations than language reasoning — text CoT actively crowds out visual processing

## Relation to Prior Wiki Knowledge

This paper has a direct and significant connection to **OneVL (parallel digest, 04-22)**, which proposed latent CoT to replace explicit text CoT in embodied AI. OneVL's claim: train with dual decoder supervision (language + visual world model), then discard both at inference. The latent tokens retain the intelligence of the CoT process without the text verbosity. Today's paper is the empirical validation of why this matters: explicit text CoT *hurts* spatial performance even for reasoning-capable models.

Two papers in the same week:
1. *Why text CoT fails at spatial tasks* (this paper, 04-22)
2. *How to get CoT-level intelligence without text CoT* (OneVL, 04-22 parallel digest)

This resolves what was previously just an open architectural question ("do we need explicit CoT for spatial tasks?") with a clear empirical and mechanistic answer.

**Connection to Geometric Canary (04-21)**: that paper found that models can have high benchmark accuracy while their geometric representations show signs of shortcut learning. The No-Image++ result here is the same phenomenon in a different modality — the model "passes" spatial benchmarks by pattern-matching on language cues, not by actually parsing the image.

**Connection to the benchmark Goodhart crisis (PDB 04-21, GTA-2 04-20, DR3-Eval 04-18, AIMO 3 04-17)**: This is now the fifth paper in the wiki documenting models satisfying benchmark surface metrics without solving the underlying cognitive operation. Spatial reasoning here; debugging there; research synthesis elsewhere. The pattern: models find a linguistic shortcut to any task that has linguistic signals.

## Open Questions

- Can vision-centric CoT (reasoning in the image domain rather than text) solve this? OneVL's latent approach is one answer, but may not generalize to non-action-oriented tasks.
- What is the precise mechanism? Does text CoT produce activations that interfere with the visual pathways, or does it just consume attention capacity that spatial processing needs?
- Does this apply to models with explicit visual reasoning tokens (not just text CoT)? The paper tests text CoT — not learned latent spatial representations.

## Related Pages

- [RL for LLMs](rl-for-llms.md)
- [Geometric Canary](2026-04-21-geometric-canary.md)
