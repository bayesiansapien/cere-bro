---
source: farmer/huggingface
farmed: 2026-07-31T19:58:50.731985
arxiv_id: 2607.28611
url: https://huggingface.co/papers/2607.28611
arxiv_url: https://arxiv.org/abs/2607.28611
date: 2026-07-31
---

# Chimera: Designing and Chinchilla-Scaling Hybrid Visual Diffusion Transformers

Visual generation increasingly requires high-resolution images, long videos, and multimodal context, making the quadratic cost of full attention prohibitive. We introduce Chimera, a hybrid visual diffusion backbone with a principled scaling recipe. Chimera processes text, image, and video tokens in one raster-ordered stream without positional embeddings. It combines Kimi Delta Attention (KDA) for long-context state tracking with O(N) complexity, interleaved Multi-head Latent Attention (MLA) for direct global interaction, and modality-aware short convolutions for local spatiotemporal context. Sparse Mixture-of-Experts (MoE) layers expand capacity while controlling activated compute. To scale this heterogeneous architecture, we introduce HeteroP, a module-wise scheme that transfers hyperparameters across width and depth according to each tensor's functional fan-in and model depth. HeteroP yields a consistently tuned family used to fit Chinchilla-style compute-optimal laws for activated model size, training-token count, and image-video data ratio. Guided by these laws, we train an 11B-parameter Chimera with 2B activated parameters. Experiments show three results. First, measured by pretraining diffusion loss, the dense backbone is 1.7x as compute-efficient as a matched full-attention Wan-2.1 2B baseline, while the complete system reaches 7.3x. Second, without length-specific fine-tuning, Chimera extrapolates zero-shot from 5-second training clips to 30-second videos, with only 6.5% FID degradation in the last five seconds. Third, the fitted laws show that compute-optimal image pretraining divides compute nearly evenly between activated model size and training-token count, whereas video pretraining modestly favors model size at higher budgets. These results establish a foundation for designing and scaling efficient long-context diffusion architectures.
