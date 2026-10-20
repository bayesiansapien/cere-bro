---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.22428
url: https://huggingface.co/papers/2610.22428
arxiv_url: https://arxiv.org/abs/2610.22428
date: 2026-10-19
---

# Embeddings Are Overpriced? A Frozen 16 MB Vocabulary for Small and Ternary Language Models

In a small language model the vocabulary is the single largest part. In Gemma 3 270M the embedding table holds 168M of 268M parameters, and because quantisation methods leave the embedding in 16-bit, it is also most of the file once the rest of the model is compressed. We ask what that table actually buys. We replace it with one frozen table of 512-bit codes, 16 MB, with no trainable parameters, derived once from a pretrained embedding by principal-component projection and sign binarisation, and we train the same Gemma-shaped body from scratch on the same 2.05B tokens with and without it. The learned table buys 0.20 nats of validation loss for 2.6 times the trainable parameters, but on LAMBADA, HellaSwag and PIQA the frozen-table model is better or tied; only ARC-Easy favours the learned table. With a ternary BitNet b1.58 body the whole model is a 46 MB file, still ties the float model on LAMBADA and PIQA, and on a laptop CPU generates 615 to 740 tokens per second in 62 MB of memory, five to six times the speed of the float model's 8-bit GGUF in llama.cpp at a seventh of the memory. The frozen table wins by 1.7 to 2.3 nats on rare words, accepts 10,000 new words after training with a 3% cost where the learned table collapses by 43%, and all of it is released with the weights, the data and every evaluation answer.
