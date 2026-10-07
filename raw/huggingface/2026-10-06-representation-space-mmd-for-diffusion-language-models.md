---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.06648
url: https://huggingface.co/papers/2610.06648
arxiv_url: https://arxiv.org/abs/2610.06648
date: 2026-10-06
---

# Representation-Space MMD for Diffusion Language Models

We introduce a post-training method for diffusion language models (DLMs) that minimizes Maximum Mean Discrepancy (MMD) between generated and reference distributions in the feature space of a frozen pretrained DLM. To estimate MMD, we retain contextual features at individual token positions, obtaining multiple observations per sequence from a single extractor pass. We optimize this objective using policy gradients for discrete models and direct differentiation through generated latents for continuous models. In both cases, computing the loss directly from these features enables efficient post-training without full sampling trajectories or jointly trained auxiliary models. Experiments show lower generative perplexity at comparable entropy on OpenWebText and better accuracy-computation trade-offs on GSM8K. On 16B DMax-LLaDA2.0 models with hybrid masked-uniform diffusion, we increase decoding parallelism with similar or higher accuracy on math and code benchmarks.
