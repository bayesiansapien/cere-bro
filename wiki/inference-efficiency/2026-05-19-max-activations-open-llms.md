# Measuring Maximum Activations in Open Large Language Models

**arXiv:** [2605.15572](https://arxiv.org/abs/2605.15572) · **HF:** [paper page](https://huggingface.co/papers/2605.15572) · **Tier:** 2 (quantization, activation outliers, deployment)

## TL;DR

Maximum activation magnitude is a first-order constraint on low-bit quantization, activation scaling, and stable LLM inference. Prior characterisations of outlier features and massive activations were on pre-2024 LLaMA-style models, and the downstream activation-quantization stack has inherited that picture without revisiting it for post-LLaMA open models. Under a unified pipeline (5,000-sample multi-domain corpus, family-specific tokenization, identical hooks across embeddings, hidden states, attention, MLP/MoE, SwiGLU gates, final norm) the authors measure global and layerwise maxima on 27 checkpoints from 8 open families. Global maxima span almost four orders of magnitude at comparable parameter counts. Qwen3.5 and MoE checkpoints sit in 10^2 to 10^3; Gemma3-27B-it reaches ~7x10^5. Cross-family and cross-generation comparisons break simple monotonic scaling. MoE checkpoints exhibit 14.0 to 23.4x lower peaks than matched-scale dense counterparts. The residual stream carries the global maximum in 22 of 24 checkpoints. INT-8 sanity check confirms measured maxima co-vary with low-bit reconstruction error.

## Key findings

- The activation-quantization community has been operating on an outdated census of activation magnitudes. The post-LLaMA open-model boom (Gemma 3, Qwen 3.5, Kimi, DeepSeek V4, GLM, MiMo, Laguna XS.2, ZAYA1) introduced families with very different activation distributions.
- Under a unified measurement pipeline, global maxima span four orders of magnitude at the same parameter count. Gemma3-27B-it reaches ~7x10^5; Qwen3.5 and MoE checkpoints sit in 10^2 to 10^3. The variation is a model property tied to family, architecture, and training stage, not a function of size.
- MoE checkpoints have 14.0 to 23.4x lower activation peaks than matched-scale dense counterparts. This is large enough that activation-quantization headroom for MoE is materially different from dense at the same parameter count.
- The residual stream is the dominant carrier of the global maximum in 22 of 24 checkpoints, confirming that residual-stream quantization remains the hardest target.
- A lightweight INT-8 sanity check shows measured maxima co-vary with low-bit reconstruction error. Operators that select activation scales without measuring family-specific maxima will systematically misallocate quantization headroom.

## Relationship to prior wiki entries

This paper is the practical companion to [Massive Activations & ME-Layer (2026-05-13)](../responsible-ai/2026-05-13-massive-activations-me-layer.md), which identified the structural cause of outlier activations. The May 13 paper said the same activation that troubles quantization is doing real work for the model. Today's paper takes the next step: catalog those activations across the full open-model wave and quantify how variable they are.

It also directly informs the wiki's running quantization thread. TurboQuant (2026-04-22, the Google ICLR 2026 KV cache quantizer) and LongLive-2.0's NVFP4 stack (2026-05-19 today) both assume an activation-magnitude regime. The 4-order-of-magnitude spread across families means that any "quantizer that works on LLaMA" claim needs to be re-measured on Gemma 3, Qwen 3.5, and MoE checkpoints before being trusted. The 14-23x lower peaks on MoE means MoE-native quantization can afford more aggressive precision than the dense literature predicts.

The recommendation in the abstract is operational: maximum activation magnitude should be measured and reported alongside any open-weight release before low-bit deployment. This is a community-norm-shaping claim. The closest precedent in the wiki is the post-MoE-muP recommendation that scaling-stable hyperparameters should be reported.

## Why it matters

Low-bit deployment is the dominant cost-saving lever for open-model inference. The four-order-of-magnitude spread in activation magnitudes means that quantization recipes calibrated on one family will systematically over-allocate or under-allocate precision on another. The MoE-vs-dense gap (14-23x lower peaks for MoE) is the most actionable finding: it gives MoE serving stacks headroom that dense serving stacks do not have, and quantization research that ignores this asymmetry is leaving a 1-bit-per-channel-class win on the table.

## Research angle

- **Per-family activation calibration.** A practical recipe: measure family maxima before deployment, choose per-family activation scales, never reuse scales across families. The paper provides the measurement protocol but does not publish the per-family recommended scales. The natural follow-up is the calibration table.
- **MoE-headroom-aware quantization.** Given 14-23x lower MoE peaks, an MoE-native quantizer should run at 3 bits where the dense baseline needs 4. The empirical demonstration is one experiment away.
- **Per-residual-stream attention.** The residual stream carries the global maximum in 22 of 24 checkpoints. A residual-stream-specific quantizer (different precision than other tensors) is the natural deployment recipe.

## Source

`raw/huggingface/2026-05-19-measuring-maximum-activations-in-open-large-language-models.md`
