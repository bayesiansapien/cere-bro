---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.304720+05:30
arxiv_id: 2610.07591
url: https://huggingface.co/papers/2610.07591
arxiv_url: https://arxiv.org/abs/2610.07591
date: 2026-10-08
---

# Recurrent Looped Transformer

State tracking requires an update at every input, but the depth a Transformer applies to each token is fixed regardless of sequence length. We introduce the Recurrent Looped Transformer (RLT), which splits its layers between a parallel causal encoder and a recurrent decoder. At each token, the decoder merges the encoder output with the previous token's final decoder state, so the computation path grows with sequence length at a fixed per-token cost. On six algorithmic tasks, we compare five splits of eight layers with an eight-layer Transformer over three seeds. Trained on at most 40 bits, two RLT splits generalize parity to 256 bits with 100% accuracy in every seed, while the Transformer stays at chance. On swap-based S_5 permutation tracking at eight times the training length, RLT reaches 97% final-state accuracy versus under 1% for the Transformer, and accuracy increases with decoder depth. On modular arithmetic beyond the training lengths, RLT reaches up to 93% versus 33% for the Transformer. Ablations show that these gains depend on the feedback: removing it drops parity and swap-based S_5 to chance at every split. Updating the feedback once per four-token chunk lets known tokens in a chunk run in parallel and keeps 64-bit parity at 99%, while permutation tracking depends on per-token feedback: chunking lowers length-64 swap-based S_5 from 100% to 20%.
