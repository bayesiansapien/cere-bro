# Tencent Hy-MT2: 1.8B / 7B / 30B-A3B translation family with 1.25-bit AngelSlim quant to 440 MB

**Source:** r/LocalLLaMA post by u/jacek2023 carrying Tencent's release notes, 2026-05-21.
**Reddit:** [Hy-MT2 thread](https://www.reddit.com/r/LocalLLaMA/comments/1tjien7/tencent_hy_30b7b18b/)
**Hugging Face:** [Hy-MT2-1.8B-FP8 (and family)](https://huggingface.co/tencent/Hy-MT2-1.8B-FP8)
**Benchmark:** [IFMTBench](https://huggingface.co/tencent/Hy-MT2-1.8B-FP8/blob/main/IFMTBench/README.md)

## TL;DR

Tencent released a three-model "fast-thinking" multilingual translation family: 1.8B, 7B, and 30B-A3B (a Mixture-of-Experts model where each forward pass uses approximately 3B active parameters out of 30B total). All three support translation among 33 languages. Tencent's claimed headline: the 7B and 30B-A3B models outperform DeepSeek-V4-Pro and Kimi K2.6 in fast-thinking mode, and the 1.8B model beats mainstream commercial APIs from Microsoft Translator and Doubao. Along with the weights, Tencent shipped IFMTBench (a translation-instruction-following benchmark) and an AngelSlim quantization stack that compresses the 1.8B model to 440 MB at 1.25 bits per weight, with claimed 1.5x inference-speed improvement.

## Why this matters for Tier 1 efficiency

The 1.25-bit quantization to 440 MB for a 1.8B model is a genuine new data point in the inference-efficiency story. Putting that in context:

- BitNet (2024) established 1.58-bit (ternary {-1, 0, +1}) as a viable quantization floor for full models.
- AngelSlim 1.25-bit is below that floor. The claim is plausible if Tencent uses a mixed-precision scheme where some weights remain higher-precision (the 1.25 bits is an average, not a uniform rate). Tencent's release does not specify the exact bit-allocation; the "1.25-bit" framing reads as marketing-friendly compression of a more complex scheme.
- 440 MB at 1.8B parameters means the on-device deployment story is now sub-512MB for a competent multilingual translation model. This is iPhone-resident.

Two follow-up things to check when more documentation is available:
1. Whether AngelSlim is uniform-1.25 or mixed-precision. The wiki cares about whether 1.25-bit uniform is achievable, which would be a real algorithmic advance.
2. The actual translation BLEU/chrF/COMET deltas at 1.25-bit vs FP8. The release claims 1.5x speed improvement; quality delta isn't stated in the Reddit summary.

## The MoE side

The 30B-A3B configuration follows the design lineage from DeepSeek-V3 / V4 and Qwen3.6-A3B that has been crystallizing as the dominant "frontier-but-deployable" MoE shape this quarter. Roughly 10% activation ratio (3B active / 30B total) is now standard. Worth tracking whether the [Kurate cs.LG #14 "How to Scale MoE: From muP to Maximally Scale-Stable Parameterization" paper](2026-05-21-moe-mup-scale-stable-parameterization.md) gives a principled reason for that ratio, or whether it remains an empirical choice.

## Industrial implication

The translation use case has been under-treated in the wiki to date, most attention has gone to coding, reasoning, and agentic agents. But translation is a useful efficiency-testbed because:
- The reward function is well-defined (BLEU, chrF, COMET) and runs at training-time without expensive eval.
- The 33-language coverage stress-tests cross-lingual representation, not just English-task fitting.
- Sub-512MB on-device deployment is a deployment story that doesn't require GPU at all.

If AngelSlim 1.25-bit generalizes from MT to reasoning models, sub-1GB on-device frontier reasoning is in reach.

## Gaps

- No public eval numbers in the release summary on translation-quality regression from 1.25-bit quantization.
- The IFMTBench is Tencent-authored, so leaderboard credibility depends on independent reproduction.
- "Fast-thinking" framing is ambiguous: it may mean smaller-than-CoT inference, or it may mean Tencent's own short-CoT regime.
- No comparison to NLLB-200 or M2M-100 baselines for the 33-language MT story.

## Cross-references

- [TIP: token-importance on-policy distillation (2026-04-16)](2026-04-16-tip-token-importance-on-policy-distillation.md)
- [MoE muP scale-stable parameterization](2026-05-21-moe-mup-scale-stable-parameterization.md) (Kurate cs.LG #14)
- [Heretic project recants Llama derivatives (2026-05-21)](../ai-industry/2026-05-21-heretic-llama-derivative-recant.md)

## Source

Raw: `raw/reddit/2026-05-22-r-localllama.md`.
