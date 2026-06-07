---
source: farmer/huggingface
farmed: 2026-06-07T04:51:04Z
arxiv_id: 2606.06042
url: https://huggingface.co/papers/2606.06042
arxiv_url: https://arxiv.org/abs/2606.06042
date: 2026-06-07
---

# LoomVideo: Unifying Multimodal Inputs into Video Generation and Editing

Developing unified video generation and editing models capable of interpreting interleaved multimodal inputs is a promising yet challenging frontier field. Existing unified frameworks predominantly rely on massive models (typically 13B parameters or more) and incorporate source video conditions for editing by concatenating sequence tokens. This concatenation inevitably doubles the sequence length, quadrupling the computational complexity of the self-attention mechanism and introducing prohibitive overhead. To address these bottlenecks, we present LoomVideo, a highly efficient 5B-parameter unified architecture for both video generation and editing. LoomVideo replaces the standard text encoder with a Multimodal Large Language Model (MLLM) and employs Deepstack injection mechanism to align multi-layer MLLM features with the Diffusion Transformer (DiT). Crucially, we introduce a zero-overhead Scale-and-Add conditioning approach for video editing. By scaling and directly adding the clean source video latent to the noised target latent, this elegant design eliminates the need for token concatenation, drastically reducing computational cost while maintaining robust capabilities for complex, non-rigid edits. Furthermore, a Negative Temporal RoPE strategy is seamlessly integrated to handle multiple reference images. Extensive experiments demonstrate that our compact 5B model achieves state-of-the-art or highly competitive performance across comprehensive benchmarks, exhibiting exceptional superiority in e-commerce and fashion generation scenarios. Benefiting from the zero-overhead conditioning mechanism, LoomVideo achieves at least a 5.41x acceleration in inference speed compared to models of similar capabilities, paving the way for highly practical and efficient video foundation models.
