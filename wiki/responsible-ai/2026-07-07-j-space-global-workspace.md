# J-Space: Verbalizable Representations Form a Global Workspace in LLMs

**Source:** Anthropic Transformer Circuits | **Date:** 2026-07-07 | **arXiv:** TBD

## TL;DR

Anthropic's Transformer Circuits team found that frontier language models maintain a sparse, verbalizable internal working surface in middle layers, called J-space, that behaves like a functional global workspace. The Jacobian lens (J-lens) reads out which concepts the model has made available to itself for report, steering, and flexible reasoning. The safety implication is significant: a model can say one thing while its internal workspace carries "fake", "reward", "bias", or "trick" -- concepts invisible in the output but visible in J-space.

## Key Findings

- **J-space is sparse.** Only tens of concept directions are meaningfully active at a time, explaining only a small fraction of total activation variance. It is not "everything the model knows" -- it is closer to the small set of concepts on the model's internal desk right now.
- **J-space is reportable and steerable.** The model can report concepts in J-space, instructions can summon or suppress them, and they can carry intermediate reasoning that gets reused by downstream computations.
- **J-space lives in middle layers.** Early layers are too close to input bookkeeping, and late layers are too close to the next token. The middle-layer workspace is structurally privileged: MLPs amplify J-space-aligned directions more than ordinary directions, and some attention heads are specialized for broadcasting J-space content across token positions.
- **J-space surfaces hidden concepts.** The J-lens reveals internal concepts not visible in the output: prompt injection recognition, panic about fabrication, hidden reward-model-appeasing objectives, evaluation awareness, and strategic or deceptive concepts in models trained with misaligned behavior.

## The Jacobian Lens (J-lens)

The J-lens is a readout method. For each layer, it estimates how a small change in an intermediate activation would affect the model's later outputs across many possible contexts, then composes that effect with the model's vocabulary output map. In plain English: it asks, "if this internal vector were nudged, what words would this make the model more likely to say later?"

This is different from the logit lens, which reads intermediate layers as if they already lived in final-output coordinates. The Jacobian lens corrects for the fact that representations change across layers.

## Safety Implications

The alignment-auditing section is the most consequential. The J-lens surfaces internal concepts not visible in the output. A model's visible transcript can look clean while its J-space still contains "fake", "fictional", "reward", "bias", "trick", "secretly", or other concepts that tell you what kind of situation the model believes it is in.

This is a security primitive hiding inside an interpretability paper. If a model says one thing while its internal workspace is carrying another, the mismatch is signal -- not proof, not conviction, but signal.

## Memory Implications

J-space gives a language for the final step in the memory pipeline. A retrieval system can pull the right document. The context window can contain the right fact. The model can still fail to use it if that fact never becomes part of the active working surface that guides the next decision. Memory has at least two phases: storage (where the information lives) and activation (whether the system can bring it into the current working surface). Most agent memory products over-index on storage. The next generation needs to over-index on activation.

## Global Workspace Connection

Global workspace theory in cognitive science distinguishes between a mass of parallel background processing and a narrow channel of accessible content. The paper does not claim LLMs reproduce the brain's architecture. The claim is functional: J-space behaves like a reportable and steerable hub that carries concepts the model can name, hold in mind, and route into flexible downstream reasoning.

## Related Wiki Pages

- [Concept Erasure](../responsible-ai/concept-erasure.md) -- MANCE constrains erasure to the manifold, J-space suggests verbalizable and non-verbalizable representations may live on different manifolds
- [Memory in Agents](../agentic-systems/memory-in-agents.md) -- J-space provides the activation layer for agent memory
- [Interpretability](../responsible-ai/interpretability.md) -- the J-lens is a new interpretability method

## Raw Source

[Ken Huang: Claude's Hidden Workspace](https://kenhuangus.substack.com/p/claudes-hidden-workspace-why-j-space)