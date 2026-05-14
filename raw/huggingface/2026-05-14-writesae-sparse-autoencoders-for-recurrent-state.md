---
source: farmer/huggingface
farmed: 2026-05-14T00:00:00
arxiv_id: 2605.12770
url: https://huggingface.co/papers/2605.12770
arxiv_url: https://arxiv.org/abs/2605.12770
date: 2026-05-14
---

# WriteSAE: Sparse Autoencoders for Recurrent State

We introduce WriteSAE, the first sparse autoencoder that decomposes and edits the matrix cache write of state-space and hybrid recurrent language models, where residual SAEs cannot reach. Existing SAEs read residual streams, but Gated DeltaNet, Mamba-2, and RWKV-7 write to a d_k x d_v cache through rank-1 updates k_t v_t^T that no vector atom can replace. WriteSAE factors each decoder atom into the native write shape, exposes a closed form for the per-token logit shift, and trains under matched Frobenius norm so atoms swap one cache slot at a time. Atom substitution beats matched-norm ablation on 92.4% of n=4,851 firings at Qwen3.5-0.8B L9 H4, the 87-atom population test holds at 89.8%, the closed form predicts measured effects at R^2=0.98, and Mamba-2-370M substitutes at 88.1% over 2,500 firings. Sustained three-position installs at 3x lift midrank target-in-continuation from 33.3% to 100% under greedy decoding, the first behavioral install at the matrix-recurrent write site.
