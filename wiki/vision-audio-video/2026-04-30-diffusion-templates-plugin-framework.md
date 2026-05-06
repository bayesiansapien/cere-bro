# Diffusion Templates: A Unified Plugin Framework for Controllable Diffusion

**Date:** 2026-04-30
**Source:** [HuggingFace](https://huggingface.co/papers/2604.24351) | [Paper](https://arxiv.org/abs/2604.24351)
**Raw:** [raw/huggingface/2026-04-30-diffusion-templates-unified-plugin-framework-controllable-diffusion.md](../../raw/huggingface/2026-04-30-diffusion-templates-unified-plugin-framework-controllable-diffusion.md)

## TL;DR

Alibaba ModelScope's Diffusion Templates decouples controllable-diffusion *capability injection* from the underlying base model. A standardized **Template cache** sits between Template models (which encode task-specific inputs) and the Template pipeline (which loads/merges/injects caches into a base diffusion runtime). Crucially, both KV-Cache *and* LoRA fit under the same abstraction, because the interface is defined at the systems level rather than tied to a specific control architecture. Open-source model zoo: structural control, brightness/color/sharpness adjustment, super-resolution, inpainting, age control, content reference, and more.

## Why It Matters (Tier 3)

The interesting move is treating KV-Cache and LoRA as instances of a single "capability carrier" abstraction. That's a useful framing for the inference-efficiency side of the wiki: KV-Cache and LoRA come from very different research traditions but operationally behave similarly — both are detached state that gets merged into a base runtime. A single plugin contract means efficiency improvements (KV compression, quantization, etc.) can ride the same interface.

For Amit's interests this is mostly Tier 3 — the diffusion control surface itself is not in scope — but the systems-level lesson generalizes to inference plugins for LLMs. The same shape (encoder → standardized cache → injector) is roughly what MCP does for tools and what the Template framework now proposes for diffusion control.

## Related Pages

- [KV Cache](../inference-efficiency/kv-cache.md)
