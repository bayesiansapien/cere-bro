---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.23036
url: https://huggingface.co/papers/2610.23036
arxiv_url: https://arxiv.org/abs/2610.23036
date: 2026-10-19
---

# Towards Looped Models Done Right, Part I: Topology, Input Injection, Recurrent-State Design

Looped language models reuse physical Transformer blocks across logical depth, but established architectures entangle recurrence placement, input injection, and recurrent state organization. We isolate these axes in models trained from scratch at matched parameter scale, logical depth, and token budgets, and then test whether the resulting design principles transfer to resident- and active-parameter-matched Mixture-of-Experts (MoE) models. The prelude-recurrent block-coda sandwich architecture consistently improves performance on context extraction and reasoning-intensive tasks. Input injection primarily enhances knowledge retrieval and context utilization, whereas random initialization and separate H/L recurrent states provide mixed or negative returns. Taken together, these results favor the Huginn-style design: at the 730M-parameter and 336B-token scale, the complete Huginn architecture outperforms Ouro across all ten benchmarks. The advantages of Huginn over Ouro transfer to MoE models. At the 8BA0.8B (32BA3B when unrolled) scale trained on 500B tokens, Huginn outperforms Ouro on nearly all benchmarks spanning knowledge, reasoning, and coding, while also exhibiting more balanced expert routing. Under matched training and inference FLOPs, the Huginn-style model uses 75% fewer resident parameters than a 112-layer feedforward MoE baseline. Despite its smaller physical parameters, it outperforms the feedforward baseline on DROP and GSM8K, matches it on MATH500, and remains competitive on the other benchmarks.
