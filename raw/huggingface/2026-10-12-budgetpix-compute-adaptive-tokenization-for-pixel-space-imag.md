---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.225055+05:30
arxiv_id: 2610.12307
url: https://huggingface.co/papers/2610.12307
arxiv_url: https://arxiv.org/abs/2610.12307
date: 2026-10-12
---

# BudgetPix: Compute-Adaptive Tokenization for Pixel-Space Image Diffusion

Most image generation models rely on uniform tokenization, allocating the exact same computational budget to equally-sized image patches. This static paradigm cannot adapt to different resource constraints at inference time, and yields suboptimal quality-cost tradeoff by devoting the same effort to both plain backgrounds and intricate details. We propose BudgetPix, an adaptive tokenization framework that dynamically allocates compute based on visual complexity and spatial layout, enabling flexible computational budgeting at inference time. BudgetPix comprises three key components: (1) an adaptive encoder that maps a fixed-size image to a variable-length token sequence using an entropy-guided quadtree alongside a multi-scale patch embedder; (2) a scale-aware decoder reconstructs fixed-resolution images from multi-scale token sets; and (3) a flexible training and sampling schedule that enables pixel-space denoisers to operate across variable token counts. BudgetPix seamlessly integrates with existing pixel-space diffusion architectures, enabling a single checkpoint to be operated at a wide range of compute budgets. Evaluated on text-to-image generation, BudgetPix matches the fidelity of MiniT2I-L at 512^2 and PixelDiT at 1024^2 using just 25% of the original compute budget. In class-conditional generation using a MeanFlow backbone, BudgetPix requires merely 60% of the full compute budget to produce images with near-zero quality degradation, observing a marginal 0.8-point increase in FID. Comprehensive assessments by human and VLM judges confirm that BudgetPix establishes a significantly improved quality-efficiency tradeoff over prior budget-adaptive baselines. More details are available at our project page: https://karaozgur.com/BudgetPix
