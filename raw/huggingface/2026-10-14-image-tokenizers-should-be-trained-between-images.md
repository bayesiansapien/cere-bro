---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.512262+00:00
arxiv_id: 2610.16759
url: https://huggingface.co/papers/2610.16759
arxiv_url: https://arxiv.org/abs/2610.16759
date: 2026-10-14
---

# Image Tokenizers Should Be Trained Between Images

Latent diffusion models generate images as codes of an image tokenizer, whose decoder turns them into the pixel image. Recent tokenizers improve how well these codes reconstruct an image and how easily a generator learns them. Yet a generator does not reproduce the codes of training images, and when a generated code lands outside what the decoder expects, the decoded image contains imperfections. Current methods make the decoder more robust to generated codes by adding noise during training. However, generated codes lie between the training codes and resemble their mixture more than one of them plus noise. To improve generated images, decoders should therefore be trained on codes in the space between training samples. We propose InterpTok, which fine-tunes MAETok to decode mixtures of image codes into natural images. Since no target image exists between two training samples, a discriminator judges whether each decoded mixture looks as natural as its two sources. A mixing ratio loss requires the decoded mixture to keep the mixing ratio of the two codes. Together, they prevent collapse to a trivial solution and yield a sharp and natural composition of both images. InterpTok keeps MAETok's reconstruction quality and improves interpolation quality more than threefold, the best of all tokenizers in a recent benchmark. Beyond interpolation, InterpTok improves the generation FID of a matched diffusion transformer from 11.61 to 8.48 without guidance, and even reaches 8.11 at an eighth of the sampling steps, where the generator on MAETok's codes worsens. The generator trained on our tokenizer also reaches the final result of the one trained on MAETok at half the training steps. Our findings show that the space between image codes can and should be explicitly supervised rather than ignored.
