---
source: farmer/huggingface
farmed: 2026-10-20T15:03:41+05:30
arxiv_id: 2610.19625
url: https://huggingface.co/papers/2610.19625
arxiv_url: https://arxiv.org/abs/2610.19625
date: 2026-10-19
---

# DAGFormer: Global Topology Prediction for Transformer Cross-Layer Connections

We propose DAGFormer, a Transformer language model whose cross-layer connections are planned by a jointly trained topology predictor. Beyond the residual connections in a standard Transformer, DAGFormer adds direct connections from earlier layers to later ones, and the predictor controls the strength of every connection based on input tokens. Unlike existing cross-layer routing architectures, which set each layer's connections separately, DAGFormer plans the routing of the whole model at once. On matched OLMo-2 pairs from 75M to 1B parameters, DAGFormer lowers WikiText-2 perplexity by 17% to 25% over the vanilla Transformer, and a 1B DAGFormer trained on 5B tokens outperforms the vanilla model trained on 10B. Against four routing baselines with the same data and budget, it reaches the lowest perplexity at 75M, 300M and 1B. The gain carries over to 13 commonsense, science, reading and math evaluation tasks (2.0 to 2.5 points higher mean accuracy at 300M and 1B) and to instruction finetuning (63% to 70% AlpacaEval win rate against the vanilla Transformer, leading every routing baseline), and under structured pruning DAGFormer degrades the least in five of six settings.
