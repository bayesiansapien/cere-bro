---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.511693+00:00
arxiv_id: 2610.15124
url: https://huggingface.co/papers/2610.15124
arxiv_url: https://arxiv.org/abs/2610.15124
date: 2026-10-14
---

# ShellElastic: Scalable Elastic Pretraining with Simultaneous Maximal Updates and Hyperparameter Transfer

Foundation models need to support diverse inference budgets, yet training a separate model for each budget duplicates pretraining effort. Elastic models train several nested sub-networks inside one weight-shared supernet, but existing recipes face three obstacles: variable per-step workloads that hinder distributed scaling, limited hyperparameter (HP) transfer across model sizes, and no guarantee that all sub-networks are maximally updated at once. We present \Ours, an elastic transformer that organizes hidden dimensions into a dense core and successive shells, so that every hidden matrix is block lower triangular. One full-width forward pass contains every sub-network's exact hidden states as prefixes, so joint training keeps a fixed computation graph and costs about as much per step as training the widest sub-network alone. We further introduce \muE, an extension of maximal update parameterization (\mup) to \Ours and other elastic architectures. Its scaling rules provably keep all sub-networks of a supernet maximally updated simultaneously (\muI), and keep doing so when the supernet is widened or given more shells; sweeps confirm that HPs tuned on a small non-elastic proxy stay near-optimal for elastic families and larger supernets (\muT). A single \Ours run produces sub-networks that outperform MatFormer and fully elastic baselines at matched parameter counts, and approach separately trained models that together take several times the steps.
