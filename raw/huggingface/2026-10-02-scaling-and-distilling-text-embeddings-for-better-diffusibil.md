---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.818882+00:00
arxiv_id: 2610.01016
url: https://huggingface.co/papers/2610.01016
arxiv_url: https://arxiv.org/abs/2610.01016
date: 2026-10-02
---

# Scaling and Distilling Text Embeddings for Better Diffusibility

Diffusion language models (DLMs) offer a promising alternative to autoregressive (AR) language generation. Recent advances in continuous DLMs, which apply latent diffusion to continuous text embeddings, raise a practical question: which embedding makes the best latent space, i.e., the most diffusible? To answer this, we search through different embeddings and find that scaling the embedding model to stronger ones within the same family (T5 to T5Gemma-1 to T5Gemma-2) greatly improves generative performance. But the raw T5Gemma-2 embeddings are still not optimal. They are so discriminative that even the embeddings of plausible alternative words are separated, which makes the generation vulnerable to imperfect sampling. Consequently, continuous diffusion often fails to reach any of them and ends up at an invalid embedding instead. To address this, we distill T5Gemma-2 into a student encoder that learns the teacher's decoded probabilities as soft labels. Learning from such soft labels makes the student pull the alternative embeddings closer while maintaining the encoding-decoding mechanism. The distilled embeddings form a more connected and diffusible latent space, improving over the vanilla T5Gemma-2 embeddings. As a result, our medium-sized DLM achieves Gen. PPL 17.8 (against real-text PPL 15.4) at real-text entropy on OpenWebText, outperforming GPT-2-M on Gen. PPL.
