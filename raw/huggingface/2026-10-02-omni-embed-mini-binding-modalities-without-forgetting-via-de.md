---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.820015+00:00
arxiv_id: 2610.02148
url: https://huggingface.co/papers/2610.02148
arxiv_url: https://arxiv.org/abs/2610.02148
date: 2026-10-02
---

# Omni-Embed-Mini: Binding Modalities Without Forgetting via Dense Distillation

Extending a text embedding model to new modalities typically degrades text retrieval quality, and existing omni-modal embedders compensate with multi-billion parameters. We present Omni-Embed-Mini, a 0.9B-parameter model that maps text, speech, audio, images, video, and visually-rich documents into a single shared cosine space without updating any text-side parameter. Our key insight is that the teacher signal requires no separate embedding model: each media sample is paired with a dense cascaded caption, and the teacher target is simply the frozen backbone's own embedding of that caption. Because teacher and student share the same backbone weights, they inhabit byte-identical geometry, and lightweight projectors plus phased LoRA adapters on the modality encoders suffice for alignment. Training combines a Matryoshka SigLIP contrastive loss with an online hybrid hard-negative miner whose negatives sharpen as the encoder improves. The recipe carries over to a 2.3B variant by swapping in a native vision-language backbone. Omni-Embed-Mini-0.9B keeps its text weights bit-identical to the backbone, so training cannot regress text retrieval (49.57 nDCG@10 on MTEB-v2 BEIR-8), while extending it to five additional modalities, and is ~2.7x to 9.5x smaller than every open omni embedder we compare against. The 2.3B variant is competitive with the closed gemini-embedding-2, edging ahead of it on the overall-modality average. Models, code, data and evaluation harness are on our project page: https://omniembed.cvmbzuai.com
