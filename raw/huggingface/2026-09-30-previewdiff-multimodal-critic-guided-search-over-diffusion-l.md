---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.36199
url: https://huggingface.co/papers/2609.36199
arxiv_url: https://arxiv.org/abs/2609.36199
date: 2026-09-30
---

# PreviewDiff: Multimodal Critic-Guided Search over Diffusion Latents

Diffusion models can produce striking images and videos, but they still struggle with the compositional details that make a generation faithful to a prompt, such as object counts, attribute binding, spatial relations, and temporally grounded actions. A common way to improve prompt satisfaction is to spend more compute at test time through Best-of-N sampling, but final-sample selection is fixed. Best-of-N can only choose among completed outputs and cannot repair a promising trajectory before it fails. We introduce PreviewDiff, a training-free test-time search method that turns diffusion sampling from scalar search into a multimodal critic-guided search over intermediate latents. At selected denoising checkpoints, PreviewDiff decodes a partial preview, asks a multimodal judge to score and critique it, and uses the resulting natural-language feedback to branch over semantic prompt edits and locally re-noised latent continuations. These branches are then scored and selectively rolled forward, allowing verifier compute to guide generation while the sample is still editable. Across image and video generation benchmarks, PreviewDiff consistently improves over budget-matched Best-of-N selection and strong scalar-search baselines. Ablations show that earlier interventions and increased search width provide the largest gains, while deeper search and additional semantic variants offer complementary improvements. PreviewDiff demonstrates that multimodal feedback is most useful not only as a final verifier, but as an active controller inside the denoising process.
