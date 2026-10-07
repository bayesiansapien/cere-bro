---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.04128
url: https://huggingface.co/papers/2610.04128
arxiv_url: https://arxiv.org/abs/2610.04128
date: 2026-10-06
---

# What Gradients Add to Text Leakage in Split Language Models, Counted per Token and per Document

Split learning lets a client train a language model on a server without sending its text. The client runs the first layers itself and sends the server only their output, a vector of numbers for each token. During training, the server sends gradients back. We show that an observer at the split can rebuild most of the client's text from this traffic, and we measure how much the gradients help. On GPT-2, an attacker who holds only the publicly released weights of the client's layers recovers 94.20% of tokens from the activations alone and 97.38% when it also sees the gradients, 3.17 percentage points more 95% interval [2.72, 3.64]. Counted by document, the difference is much larger. The attacker rebuilds 13.71% of 32-token documents exactly without the gradients and 37.77% with them, because a document only counts when every token is right. How we count also changes how good a defence looks. Secret mixup, which blends each outgoing vector with a decoy, stops the attacker from rebuilding almost any document exactly, yet the attacker still recovers 83-91% of tokens. In a second experiment on GPT-2 and Qwen3-0.6B, where the server trains only a run of consecutive layers, the layer at which the run starts changes both model quality and leakage, even when the run's length is fixed. We recommend reporting leakage both per token and per document, and treating what a split model sends as being as sensitive as the text itself.
