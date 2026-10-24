---
source: farmer/huggingface
farmed: 2026-10-24T12:49:20.883470+00:00
arxiv_id: 2610.31305
url: https://huggingface.co/papers/2610.31305
arxiv_url: https://arxiv.org/abs/2610.31305
date: 2026-10-23
---

# Cola2: Co-Adaptive Hierarchical Language Modeling with Continuous Semantic Compression and Balanced Discrete Generation

Hierarchical language generation separates continuous semantic modeling from discrete text realization, but its effectiveness depends on what the latent space compresses and how the discrete generator uses it. We propose Cola2, a framework that jointly studies continuous semantic compression, the balance between reconstruction and generation, and continuous-discrete co-adaptation. Cola2 dynamically segments text into semantic spans, controls the compression rate through auxiliary-loss-free negative feedback, and combines reconstruction and generation supervision to learn compact, predictive latent representations. A block-causal masked diffusion decoder is trained with clean, noisy, and dropped latent conditions, while classifier-free guidance adjusts the balance between semantic reconstruction and autonomous generation. Token-prediction gradients update the encoder through the latents, whereas Flow Matching prior learning is decoupled from representation learning by stop-gradient. During inference, generated text is re-encoded under a fixed span layout to keep the latent history consistent with the actual text context. Experiments on five downstream tasks with about 210 billion training tokens validate the core designs and show competitive, unsaturated scaling. With 346.03 billion source tokens, an unconverged checkpoint reaches a 60.10 average across eight tasks and surpasses Llama-3-8B on HellaSwag and StoryCloze despite its reported pretraining budget being over 43 times larger. These results demonstrate the potential of continuous-latent hierarchical language generation.
