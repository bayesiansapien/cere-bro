---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.819368+00:00
arxiv_id: 2609.40362
url: https://huggingface.co/papers/2609.40362
arxiv_url: https://arxiv.org/abs/2609.40362
date: 2026-10-02
---

# Multimodal Flow: Unified Flow Modeling of Language and Vision in Embedding Spaces

We present Multimodal Flow, a fully continuous generative model of language and vision. Most unified multimodal models either model both language and quantized images as discrete tokens or combine discrete language prediction with continuous image generation. The former introduces a visual quantization bottleneck. The latter requires modality-dependent objectives and sampling procedures. Fully continuous modeling avoids these trade-offs and enables a shared generative process, but remains underexplored for multimodal pretraining. Multimodal Flow introduces a unified continuous architecture that integrates multimodal continuous representations with a shared chunk-causal flow backbone. It organizes text blocks and images as ordered continuous hyperchunks, preserving textual token order and visual spatial structure. The backbone learns a single vector field over these hyperchunks through Flow Matching. Joint attention enables cross-modal interaction, while modality-specific feed-forward networks process each modality. The model predicts multiple target chunks in parallel during training and generates hyperchunks sequentially at inference. We instantiate MF-1 and pretrain it on multimodal data. Across 0.6B, 1.2B, and 1.6B scales, continued pretraining consistently improves multimodal modeling. With only 150B pretraining tokens, MF-1 achieves an average score of 82.8 across GenEval and DPG-Bench and 75.3 across VQAv2, MMBench, and POPE, remaining competitive with unified models trained on substantially more data. Under matched data, optimization, and parameter budgets, Multimodal Flow further outperforms representative hybrid and discrete models. These results establish continuous chunk-based embedding flow modeling as a new fully continuous paradigm for unified multimodal modeling. The related code and model are publicly released at https://github.com/hustvl/Multimodal-Flow.
