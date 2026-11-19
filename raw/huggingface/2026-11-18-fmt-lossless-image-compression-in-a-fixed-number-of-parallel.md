---
source: farmer/huggingface
farmed: 2026-11-19T11:13:13+05:30
arxiv_id: 2611.23108
url: https://huggingface.co/papers/2611.23108
arxiv_url: https://arxiv.org/abs/2611.23108
date: 2026-11-18
---

# FMT: Lossless Image Compression in a Fixed Number of Parallel Steps

Learned lossless codecs make smaller files than common classical codecs, yet the images we archive and train on still use classical codecs. A main reason is time: a learned codec takes seconds to decode a photo that a classical codec opens in milliseconds, and their faster variants give up most of their gain in size. We argue that much of this time is spent waiting, not computing: the network waits for the values it conditions on, and the arithmetic decoder reads them one at a time. We introduce FMT (Fixed-step Multiscale Tree), a lossless image format whose decoding order and entropy coder are designed together so that neither wait grows with the image. FMT stores an image as a coarse-to-fine tree whose steps hold independent values: a GPU predicts each step at once and decodes it in parallel rANS lanes that carry their states from step to step, so an image of any size decodes in a fixed number of sequential steps. On this tree we build a family of bit-exact codecs, from a rule with no network to large networks, and no codec we ran on the same GPU beats any of them on both size and speed. Without a network, FMT beats NVIDIA's HTJ2K on size and speed; with a large one, it decodes Kodak photos 9 to 61X faster than learned codecs we ran on the same A100, at the same size or smaller.
