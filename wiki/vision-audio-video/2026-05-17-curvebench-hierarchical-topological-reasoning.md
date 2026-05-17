# CurveBench: Hierarchical Topological Reasoning from Visual Input

**arxiv:** [2605.14068](https://arxiv.org/abs/2605.14068)
**Raw:** [raw/huggingface/2026-05-17-curvebench-a-benchmark-for-exact-topological-reasoning-over.md](../../raw/huggingface/2026-05-17-curvebench-a-benchmark-for-exact-topological-reasoning-over.md)
**Tier:** 2 (visual reasoning benchmark, RLVR fine-tuning evidence)
**Date:** 2026-05-17

## TL;DR

CurveBench is a benchmark of 756 images of pairwise non-intersecting Jordan curves (closed planar curves that do not cross each other) across five configurations: easy, polygonal, topographic-inspired, maze-like, and dense counting. Each image is annotated with the rooted tree that encodes which curves contain which. The task is structured prediction: given the image, recover the full containment tree. The benchmark is visually trivial (humans solve it at a glance) but Gemini 3.1 Pro reaches only 71.1% tree-generation accuracy on Easy and 19.1% on Hard. RLVR-style fine-tuning of Qwen3-VL-8B lifts CurveBench-Easy from 2.8% (Qwen3-VL-8B-Thinking baseline) to 33.3%, exceeding GPT-5.4 and Claude Opus 4.5 under the same evaluation protocol.

## Key findings

1. **The visually-simple-but-cognitively-hard gap.** CurveBench Easy is solved by humans without conscious effort, but frontier vision-language models reach only 71% on it and only 19% on Hard. The gap is not perceptual (curves are clearly visible) but structural: the model fails at maintaining the containment relation while parsing.
2. **RLVR fine-tuning closes a large fraction of the gap on a small open model.** Qwen3-VL-8B with RLVR on this task lifts from 2.8% to 33.3% on Easy, exceeding two frontier closed models. The headline finding mirrors what SU-01 (05-15) showed for math olympiads: small open models with the right post-training can exceed frontier models on the specific task the post-training targets.
3. **It is a benchmark for the structural-failure-mode hypothesis.** The literature has been accumulating evidence that VLM failures on visually simple tasks come from structural representation gaps, not perception. WildTableBench (05-15) is the table-reading analog (only one of 21 frontier models crosses 50% accuracy). MemEye and MemLens (05-15) are the multi-session multimodal analogs (capped below 30%). CurveBench is a cleaner version of the same story because the underlying perceptual task is trivially within the model's perception module.

## Relation to prior wiki state

**Pattern crystallization (≥3 papers, threshold crossed).** Three recent VLM benchmarks have now reported the same diagnosis: WildTableBench (only one frontier model above 50% on table reading), MemEye/MemLens (multi-session multimodal capped below 30%), CurveBench (Gemini 3.1 Pro at 71% Easy / 19% Hard). All three argue the failure mode is structural representation, not perception or world knowledge. The pattern says: the VLM evaluation ceiling that has been reported every week for a month is real, and the obvious next research move is to design representational interventions that improve all three at once.

**RLVR-on-small-VLM as a measurement instrument.** Qwen3-VL-8B's 30-point jump on CurveBench-Easy via RLVR is informative twofold. First, it confirms the task is RL-learnable, so the structural gap is not fundamental to the architecture. Second, it shows the gap between Qwen3-VL-8B-Thinking (2.8% zero-shot) and Qwen3-VL-8B-RLVR (33.3%) is larger than the gap between Qwen3-VL-8B-Thinking and Gemini 3.1 Pro. The RLVR-tuning gap is now bigger than the model-capability gap for this class of task. This is the visual-reasoning analog of SU-01's 200-RL-steps recipe for math olympiads.

## Why it matters

CurveBench is one of three Tier 2 benchmarks this month (with WildTableBench and ViMU on the same day) that lower the previously-reported frontier-VLM ceiling on tasks that humans find trivial. Each new honest measurement lens lowers the ceiling. The deployment implication: any VLM-using product that depends on accurate structural parsing of visual inputs is shipping at lower reliability than benchmark numbers suggest.

## Research angle

1. **Cross-benchmark transfer of RLVR fine-tuning.** Does the Qwen3-VL-8B RLVR recipe that lifts CurveBench-Easy from 2.8% to 33.3% also lift WildTableBench or MemEye? If yes, the structural representation that RLVR is implicitly training is general; if no, each benchmark needs its own targeted post-training.
2. **CurveBench under WildClawBench-style harness control.** If the 18-point harness spread observation generalizes to VLM reasoning, the Gemini 3.1 Pro number might shift several points under preferred-harness evaluation. Falsifiable.
3. **CurveBench plus ATLAS (05-15) functional-token reasoning.** ATLAS introduced functional tokens that serve as both agentic operations and latent visual reasoning units. CurveBench is the natural eval for whether ATLAS-style latent visual reasoning generalizes to topological structure.

## Links

- [Paper](https://arxiv.org/abs/2605.14068)
- Raw: [raw/huggingface/2026-05-17-curvebench-a-benchmark-for-exact-topological-reasoning-over.md](../../raw/huggingface/2026-05-17-curvebench-a-benchmark-for-exact-topological-reasoning-over.md)
- Related: [WildTableBench 05-15 Quick Hit](../daily-digest/2026-05/2026-05-15.md), MemEye/MemLens 05-15 agent-memory cluster
