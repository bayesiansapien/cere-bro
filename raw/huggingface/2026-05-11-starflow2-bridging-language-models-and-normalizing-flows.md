---
source: farmer/huggingface
farmed: 2026-05-11T00:00:00
arxiv_id: 2605.08029
url: https://huggingface.co/papers/2605.08029
arxiv_url: https://arxiv.org/abs/2605.08029
date: 2026-05-11
---

# STARFlow2: Bridging Language Models and Normalizing Flows for Unified Multimodal Generation

Unified multimodal models that understand, reason over, and generate interleaved text-image sequences remain structurally fragmented: existing approaches either sacrifice visual fidelity through discrete tokenization, impose structural asymmetry by combining causal text generation with iterative diffusion-based denoising, or degrade pretrained understanding when adapting vision-language models for generation. We observe that autoregressive normalizing flows are autoregressive Transformers - sharing the same causal mask, KV-cache mechanism, and left-to-right structure as LLMs - making them the most natural paradigm for truly unified multimodal generation that is continuous, single-pass, and purely causal. We present STARFlow2, built on the Pretzel architecture that vertically interleaves a frozen pretrained VLM stream with a TARFlow stream via residual skip connections, both operating under the same causal mask. This design simultaneously preserves pretrained multimodal understanding, enables high-fidelity continuous image generation, and achieves structural unification under a single causal mechanism. Combined with a deep-shallow flow design and a unified FAE latent space, STARFlow2 supports cache-friendly interleaved generation where both text and visual outputs directly enter the KV-cache without re-encoding. Experiments demonstrate strong performance across image generation and multimodal understanding benchmarks, validating autoregressive flows as a viable foundation for unified multimodal modeling.
