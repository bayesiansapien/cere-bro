---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.157973+00:00
arxiv_id: 2610.40599
url: https://huggingface.co/papers/2610.40599
arxiv_url: https://arxiv.org/abs/2610.40599
date: 2026-10-30
---

# HairDeck: Animation-Ready Stylized Hair Cards from a Single Image

The hair of stylized characters in games and avatars is built from hair cards: artist-placed ribbons whose geometry is the visible hair, animated by spring bones. Existing image-based methods produce realistic hair or a single fused mesh, while CHARM, the only generator of stylized hair cards, decodes a hairstyle autoregressively as a long sequence of control points. Observing that a card hairstyle is an unordered set of artist-defined primitives, we propose HairDeck, which generates it as one: each card is a single token, and a set diffusion transformer denoises all cards together. From a single image, HairDeck generates the cards and the spring-bone chains that drive them, yielding an animatable asset that exports to ready-to-use downstream formats. On CHARM's own test set, it lowers Chamfer distance by 44% and card-orientation error by more than half while running 33 times faster, and from single images it outperforms CHARM, image-to-3D pipelines and strand-based methods. Project page: https://hyzcluster.github.io/HairDeck
