# MMProLong: training long-context vision-language models with generalization beyond 128K

**Source:** HuggingFace Daily Papers · 2026-05-14
**Paper:** [arXiv 2605.13831](https://arxiv.org/abs/2605.13831)
**Raw:** [raw](../../raw/huggingface/2026-05-14-training-long-context-vision-language-models-effectively-wit.md)
**Tier:** 2. Long-context VLMs, training recipes, generalization

## TL;DR

A systematic study of long-context continued pre-training for vision-language models, extending a 7B model from 32K to 128K context. Three findings: long-document VQA is substantially more effective than OCR transcription; balanced sequence-length distribution beats target-length-focused training (better generalization at unseen lengths); retrieval remains the primary bottleneck, favoring retrieval-heavy data mixtures. The resulting model, MMProLong, comes from Qwen2.5-VL-7B with only 5B tokens of long-context pretraining, gains 7.1% on long-document VQA, and maintains strong performance at 256K and 512K well beyond its 128K training window. It also transfers without supervision to webpage-multimodal needle retrieval, long-context vision-text compression, and long-video understanding.

## Why it matters

The wiki has been tracking long-context training and serving on two tracks: pretraining recipes (this paper, Lighthouse Attention) and inference-time selectivity ([Make Each Token Count](2026-05-12-make-each-token-count-kv-eviction.md), [MISA](2026-05-11-misa-mixture-of-indexer-sparse-attention.md), [UniPrefill](2026-05-11-uniprefill-universal-prefill-acceleration.md)). MMProLong is the cleanest long-context-VLM training recipe in the wiki and one of the more useful negative results on data mix (target-length focused is *worse* than balanced).

## Mechanism

Three ablations, each operationalized:

```
  Pre-training data mix           Headline finding
  ─────────────────────────       ───────────────────────────────────
  Long-document VQA  vs OCR  ───► VQA wins. The reasoning task pulls
                                  more long-context capability than
                                  transcription.

  128K-focused vs balanced  ───► Balanced wins. Generalization
                                  beyond train length requires
                                  diverse retrieval positions.

  Retrieval-heavy vs reasoning ──► Retrieval-heavy wins. Long-context
                                   bottleneck is finding the relevant
                                   chunk, not reasoning over it.
```

The result is a tight recipe: extend with VQA, balance the lengths, weight retrieval. Total cost: 5B tokens on a 7B base. The transfer claims (256K, 512K beyond 128K training; webpage needle retrieval; vision-text compression; long-video understanding without task-specific training) suggest the recipe is buying genuinely transferable long-context capability rather than memorizing target-length artifacts.

## Connections

- **Make Each Token Count** ([2026-05-12](2026-05-12-make-each-token-count-kv-eviction.md)) said the full cache is dilutive once context is long enough. MMProLong gives the training-side complement: training data should also be diverse-length to teach the model to find signal at any position. The two papers together say "long context needs balance at both training and inference time."
- **Lighthouse Attention** (NousResearch, [@omarsar0 retweet 2026-05-12](https://nitter.net/omarsar0/status/2054224130103554359#m), [paper 2605.06554](https://arxiv.org/abs/2605.06554)) speeds long-context training via a removable subquadratic wrapper. MMProLong is orthogonal — same training, different mix. The natural composition: train with Lighthouse Attention's wrapper *and* MMProLong's balanced retrieval-heavy mix.
- **r/LocalLLaMA Qwen 3.6 long-context practitioner reports** ([1tcc7h5: 24 tok/s on GTX 1080 with KV cache quantization](https://www.reddit.com/r/LocalLLaMA/comments/1tcc7h5/24_toks_from_30b_moe_models_on_an_old_gtx_1080_8/)) confirm long-context inference is now a tractable deployment target. MMProLong's training recipe is what gets you a long-context model worth deploying.

## Research angle

1. **Recipe transfer across base models.** MMProLong is built on Qwen2.5-VL-7B. The transfer question: does the same recipe (balanced length distribution, retrieval-heavy, VQA-driven) work on Llama-VL, InternVL, or LLaVA-OneVision at the same parameter scale? If yes, this becomes the default long-context VLM recipe.
2. **Beyond VLMs.** Long-document VQA is the VLM analogue of long-document QA in text-only models. Whether the balanced-mix finding transfers to text-only long-context training is a one-experiment check, but with large practical implications for the broader long-context training literature.
3. **Composability with diffusion-decoder approaches.** [Orthrus](2026-05-14-orthrus-dual-view-diffusion-ar.md) (same day) accelerates inference via parallel decoding. Whether an MMProLong-trained model retains its long-context behavior under Orthrus drafting is an open composition question.

## Where it lives

Update [kv-cache.md](kv-cache.md) — first long-context VLM training recipe in the wiki. Cross-reference with [knowledge-distillation.md](knowledge-distillation.md) — the retrieval-heavy mix finding implies that long-context distillation should weight retrieval-style examples too.
