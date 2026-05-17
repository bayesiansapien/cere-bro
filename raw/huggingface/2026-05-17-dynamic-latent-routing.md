---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.14323"
url: "https://huggingface.co/papers/2605.14323"
arxiv_url: "https://arxiv.org/abs/2605.14323"
date: 2026-05-17
---

# Dynamic Latent Routing

We investigate the temporal concatenation of sub-policies in Markov Decision Processes (MDP) with time-varying reward functions. We introduce General Dijkstra Search (GDS), and prove that globally optimal goal-reaching policies can be recovered through temporal composition of intermediate optimal sub-policies. Motivated by the 'search, select, update' principle underlying GDS, we propose Dynamic Latent Routing (DLR), a language-model post-training method that jointly learns discrete latent codes, routing policies, and model parameters through dynamic search in a single training stage. In low-data fine-tuning settings, DLR matches or outperforms supervised fine-tuning across four datasets and six models, achieving a mean gain of +6.6 percentage points, while prior discrete-latent baselines consistently underperform SFT. Mechanistic analyses and targeted code ablations show that DLR learns structured routing behaviors with distinct causal roles.
