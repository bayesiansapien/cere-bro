# NGM: A Plug-and-Play Training-Free Memory Module for LLMs

**arXiv:** [2605.16893](https://arxiv.org/abs/2605.16893) · **HF:** [paper page](https://huggingface.co/papers/2605.16893) · **Tier:** 2 (memory module, plug-and-play augmentation)

## TL;DR

Recent conditional memory modules decouple knowledge storage from neural computation, enabling more direct knowledge access than MoE's dynamic-computation route. But existing memory-module approaches depend on learned memory embeddings, requiring extra training and limiting flexibility. NGM (N-gram Memory) is a training-free, plug-and-play module composed of a Causal N-Gram Encoder and a Cosine-Gated Memory Injector. The Causal N-Gram Encoder directly averages the pretrained token embeddings of the backbone model to construct N-gram representations, eliminating the need to train separate N-gram embeddings. No additional memory table, no retrieval pipeline. The Cosine-Gated Memory Injector uses a non-parametric cosine gate with ReLU to modulate retrieved embeddings into contextual representations. On Qwen3 from 0.6B to 14B across 8 benchmarks, NGM lifts averages by 0.5 to 1.2 points, with notable gains on code generation and knowledge-intensive tasks (+3.0 LiveCodeBench, +3.03 GPQA for Qwen3-14B). Also improves multimodal performance (+1.53 MMStar for Qwen3-VL-2B).

## Key findings

- Conditional memory modules are a deployment-friendly alternative to MoE: explicit lookup instead of dynamic computation paths. But prior memory-module approaches need separately trained memory embeddings.
- NGM constructs N-gram representations by averaging the pretrained token embeddings of the backbone. No new parameters, no separate training step.
- The Cosine-Gated Memory Injector uses a non-parametric cosine gate followed by ReLU. The gate decides how strongly to inject the N-gram representation into the contextual representation; no learned gating parameters.
- Across Qwen3 scales (0.6B to 14B) and 8 benchmarks, NGM lifts average performance by 0.5 to 1.2 points. The largest gains are on knowledge-intensive and code-generation tasks (+3.0 LiveCodeBench, +3.03 GPQA on Qwen3-14B).
- The improvement extends to multimodal: Qwen3-VL-2B gets +1.53 on MMStar.

## Relationship to prior wiki entries

NGM extends the wiki's running memory thread. δ-mem (2026-05-13, the frozen-backbone associative-memory paper with an 8x8 online state that lifts the backbone by 1.10x average and 1.31x on MemoryAgentBench) was the wiki's prior cleanest plug-and-play memory module. NGM is the training-free version: no online state, no learned embeddings, just N-gram averages plus cosine gating.

The MoE-vs-memory framing in the abstract is the same comparison the wiki's [llm-routing concept page](../ai-routing/llm-routing.md) has been making. MoE adds capacity via routing through expert sub-networks; memory modules add capacity via lookup. NGM is the cleanest argument in the wiki to date that the memory-module route can deliver multi-point gains without any training cost, which makes it competitive with the considerable training cost of MoE-muP-style scaling.

It also overlaps with the knowledge-injection thread the wiki tracked yesterday and today. MixSD (2026-05-19 today, the mixed-conditional self-distillation for knowledge injection) injects knowledge into weights without catastrophic forgetting. NGM adds knowledge as an external lookup. The two are complementary: MixSD for the knowledge you want to internalise, NGM for the knowledge you want to look up at runtime.

## Why it matters

Training-free augmentations are the highest-leverage deployment pattern: no fine-tune, no retrain, just plug in. A 0.5-1.2 point average gain across 8 benchmarks at zero training cost on every Qwen3 scale from 0.6B to 14B is operationally significant. The +3 points on LiveCodeBench and GPQA for 14B is the most useful range (where evaluation noise is around 0.5-1 point), so the gain is real.

The N-gram averaging is a surprisingly simple construction. It works because the pretrained token embeddings already encode the model's notion of token similarity, and N-gram averages are a useful representation of local context. The cosine-gated injection lets the model use the N-gram representation when it is locally relevant and ignore it otherwise.

## Research angle

- **Scale to 30B and frontier MoE.** Qwen3-14B is the largest tested. Whether NGM helps Qwen3-30B-A3B (the MoE version) or whether the MoE expert mixture already captures the same signal is the natural follow-up.
- **Compose with MixSD.** Use MixSD for knowledge injection of corpora you want internalised; NGM for runtime context. Whether the two interact constructively or interfere is testable.
- **Beyond N-grams.** The Causal N-Gram Encoder is the simplest possible representation. Whether learned but training-free representations (e.g. running mean of attention outputs at a small context window) give larger gains is the natural extension.

## Source

`raw/huggingface/2026-05-19-ngm-a-plug-and-play-training-free-memory-module-for-llms.md`
