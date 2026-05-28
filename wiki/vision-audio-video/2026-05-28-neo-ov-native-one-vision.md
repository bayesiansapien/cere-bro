# NEO-ov: Native One-Vision Foundation Model at Scale

**Date ingested:** 2026-05-28
**Source:** HuggingFace Daily Papers
**Links:** [arxiv 2605.28820](https://arxiv.org/abs/2605.28820) · [HuggingFace](https://huggingface.co/papers/2605.28820) · [code](https://github.com/EvolvingLMMs-Lab/NEO) · [raw](../../raw/huggingface/2026-05-28-from-pixels-to-words-towards-native-one-vision-models-at-sca.md)

## TL;DR

Most vision-language models stitch a separate vision encoder to a language decoder through multi-stage alignment. That modular design fragments pixel-level signals across frames and scatters early pixel-word interactions. NEO-ov is a native foundation model that learns cross-frame and pixel-word correspondence end-to-end with no external encoders, adapters, or post-hoc fusion. By removing module boundaries, fine-grained and unified spatiotemporal modeling emerges natively inside the model. The paper reports NEO-ov narrowing the gap to modular counterparts while excelling at fine-grained visual perception, and shows the architecture is feasible and competitive at scale, with detailed training recipes.

## Key findings

- Eliminating the encoder-decoder split lets cross-frame and pixel-word correspondences emerge natively rather than be stitched in post hoc.
- Fine-grained spatiotemporal modeling, including multi-image and video understanding, falls out of the unified architecture.
- Performance largely closes the gap to modular VLMs at scale.
- Detailed training recipes for native multimodal modeling are published with the codebase.

## How this fits prior wiki state

NEO-ov continues the "native" multimodal thread that has shown up periodically across the wiki. The trade-off is the standard one: modular VLMs are easier to train but inherit alignment artifacts at the encoder boundary; native models pay a training-cost premium but get unified representations. This paper argues the native side is now competitive at scale, which is a meaningful update.

It also pairs with today's Gamma-World ([[2026-05-28-gamma-world-multi-agent-modeling]]) at the spatiotemporal-modeling level: both papers are about pushing visual-token interaction past the current paradigm, Gamma-World via sparse hub attention for multi-agent scenes, NEO-ov via end-to-end pixel-word coupling.

## Related pages

- [[2026-05-28-gamma-world-multi-agent-modeling]] — multi-agent world modeling beyond two players
- [[vision-language-models]] — concept page

## Research angle

The interesting open question is whether the native-vs-modular gap closes from "narrows" to "wins" at the next scale jump. If yes, the encoder-stitching era of VLMs ends. If no, modular models remain the practical default and native ones become research curios. The training-recipe disclosure helps the field test this directly. A secondary angle: native cross-frame learning should improve any task with temporal continuity, including world-model rollout and long-video understanding, where the encoder boundary has been the worst offender.
