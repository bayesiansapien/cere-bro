---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.20818
url: https://huggingface.co/papers/2610.20818
arxiv_url: https://arxiv.org/abs/2610.20818
date: 2026-10-16
---

# Intern Lumina U2: A Multi-Codebook Diffusion Large Language Model for Omni-Visual Understanding and Image Generation

Unified multimodal generation covers discrete, continuous, and hybrid paradigms. Discrete approaches with single-codebook visual tokenizers align naturally with text modeling but have limited representational capacity. Continuous and hybrid approaches retain richer visual representations, but they model text and images in heterogeneous spaces with different training objectives, potentially introducing optimization conflicts between modalities with misaligned representation spaces. These choices expose a central question: how to efficiently model high-capacity visual representations alongside textual content in a shared optimization space within a single backbone. We present Intern Lumina U2, to our knowledge the first diffusion language model to represent multi-codebook visual tokens in a fully discrete space. Each visual position is represented by a group of codes from complementary codebooks, increasing its representational capacity while preserving compatibility with discrete text modeling. At the input, the embeddings are concatenated at each position; at the output, a lightweight multi-codebook autoregressive head predicts the codes within each position sequentially, while the diffusion backbone processes all positions in parallel. Built on the unified 4D representation of AToken, Intern Lumina U2 supports image, video, and 3D inputs within a single backbone and achieves leading performance among unified models in visual understanding, image generation, and image editing. We further build a full-stack training, inference, and evaluation system on both Ascend and NVIDIA platforms to verify the cross-platform effectiveness of our model. We also improve the inference efficiency through a stability-aware sampling strategy, which combines confidence-plateau-guided unmasking approach with drift-triggered cache refreshing mechanisms, accelerating image generation by 4.45x.
