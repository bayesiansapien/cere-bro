---
source: farmer/huggingface
farmed: 2026-04-22T00:00:00
arxiv_id: 2604.15706
url: https://huggingface.co/papers/2604.15706
arxiv_url: https://arxiv.org/abs/2604.15706
date: 2026-04-22
---

# Target-Oriented Pretraining Data Selection via Neuron-Activated Graph

Everyday tasks come with a target, and pretraining models around this target is what turns them into experts. In this paper, we study target-oriented language model (LM) pretraining by introducing Neuron-Activated Graph Ranking (NAG-based Ranking), a training-free and interpretable framework for target pretraining data selection. Rather than using black-box representations, our approach directly characterizes each target input by a sparse set of high-impact neurons in any off-the-shelf LLMs. Concretely, we quantify neuron impact and select the most influential neurons across layers into a compact Neuron-Activated Graph (NAG), and rank candidate data by NAG similarity to target examples. We conduct experiments across six benchmarks, where our NAG-based Ranking improves target-oriented pretraining by 4.9% on average over random sampling, and also outperforms state-of-the-art baselines by 5.3% accuracy on HellaSwag.
