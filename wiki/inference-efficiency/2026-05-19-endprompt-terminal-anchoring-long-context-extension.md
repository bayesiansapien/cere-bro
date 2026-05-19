# EndPrompt: Efficient Long-Context Extension via Terminal Anchoring

**arXiv:** [2605.14589](https://arxiv.org/abs/2605.14589) · **HF:** [paper page](https://huggingface.co/papers/2605.14589) · **Tier:** 1 (long-context, training efficiency)

## TL;DR

EndPrompt extends an LLM's context window using only short training sequences. It preserves the original short context as an intact first segment and appends a brief terminal prompt as a second segment with positional indices placed near the target context length. The two-segment construction injects both local and long-range relative distances inside a short physical sequence while keeping semantic continuity intact, which chunk-based simulation approaches do not. On LLaMA models extending 8K to 64K, EndPrompt averages 76.03 on RULER and posts the highest LongBench average, beating LCEG (72.24), LongLoRA (72.95), and full-length fine-tuning (69.23) at substantially lower compute.

## Key findings

- The standard recipe for context extension is training on sequences at the target length, which incurs quadratic memory and compute. This is what makes 64K and 128K extension expensive enough to be a research bottleneck.
- The core insight is that exposing the model to long-range relative positional distances does not require constructing full-length inputs. What matters is that the relative-distance distribution the model sees during training covers the target length, not that the physical sequence does.
- Two-segment construction: keep the original short context as segment 1, append a brief terminal prompt as segment 2, assign segment 2 positional indices near the target context length. Local distances live within each segment; long-range relative distances live across the two-segment boundary.
- This preserves the semantic continuity of the underlying training text because segment 2 is a natural terminal of segment 1, unlike chunk-based simulation approaches that split contiguous context.
- A Rotary Position Embedding (RoPE) and Bernstein-inequality analysis shows position interpolation imposes a rigorous smoothness constraint over the attention function, and shared Transformer parameters further suppress unstable extrapolation to unobserved intermediate distances.
- Empirically dominates baselines on RULER (76.03 avg) and LongBench while requiring substantially less compute than full-length fine-tuning.

## Relationship to prior wiki entries

EndPrompt is the training-side complement to several inference-side long-context threads the wiki has been mapping. Lighthouse Attention (2026-05-16, the pre-training wrapper that pools queries, keys, and values into a multi-resolution pyramid and uses a gradient-free top-k cascade to hierarchically pick a dense sub-sequence under a removable wrapper) attacked the same bottleneck (cost of long-context training) at the attention substrate level. EndPrompt attacks it at the positional supervision level. They are compatible: a Lighthouse-trained model could be context-extended via EndPrompt.

EndPrompt also contradicts a prevailing assumption baked into the long-context literature: that dense long-sequence training is necessary for reliable context-window extension. The wiki has flagged earlier sparse-position-supervision approaches as fragile. The 76.03 RULER number is the cleanest evidence to date that sparse positional supervision is sufficient for principled extension.

## Why it matters

Context extension is one of the two ways frontier labs deliver long context (the other is architectural, e.g. Lighthouse Attention or sliding-window hybrids). The cost of full-length fine-tuning at 64K-plus is the practical bottleneck. EndPrompt reduces the training-time cost to the cost of short-sequence fine-tuning while delivering better RULER than the full-length baseline. If this replicates at 128K and 256K, it is the recipe most open-model context extensions will adopt by default.

## Research angle

- **Does EndPrompt extend to 128K and 256K with the same compute discount?** The paper reports 8K to 64K. Whether the discount holds or grows at longer targets is the deployment-relevant question.
- **Compose with Lighthouse Attention.** Lighthouse is a training-time attention modification; EndPrompt is a training-time supervision modification. The compose should reduce training cost multiplicatively. Diagnostic: train a model with Lighthouse, extend via EndPrompt, measure compute relative to dense full-length fine-tuning.
- **Does the smoothness constraint hold under linear-attention substrates (Mamba2, GDN, Momentum DeltaNet)?** The theoretical analysis is RoPE-specific. Whether a similar argument applies to position-aware linear-attention recurrences is open.

## Source

`raw/huggingface/2026-05-19-endprompt-efficient-long-context-extension-via-terminal-anch.md`
