# Target-Oriented Pretraining via Neuron-Activated Graph (NAG)

**Date:** 2026-04-22  
**Source:** [HuggingFace](https://huggingface.co/papers/2604.15706) | [Paper](https://arxiv.org/abs/2604.15706)  
**Raw:** [raw/huggingface/2026-04-22-target-oriented-pretraining-data-selection-via-neuron-activa.md](../../raw/huggingface/2026-04-22-target-oriented-pretraining-data-selection-via-neuron-activa.md)

## TL;DR

Training-free framework for selecting pretraining data that's relevant to a target task. Rather than using black-box embedding similarity, it characterizes each target input by which neurons activate at high magnitude across layers, builds a Neuron-Activated Graph (NAG) from the most influential neurons, then ranks candidate training data by NAG similarity. Average 4.9% improvement over random sampling; 5.3% over SOTA baselines on HellaSwag.

## Key Findings

- **Training-free**: no auxiliary model needed — uses existing LLM activations as the signal
- Characterizes target inputs by sparse high-impact neuron activation patterns (not dense embeddings)
- Builds Neuron-Activated Graph (NAG) linking neurons across layers based on co-activation
- Ranks pretraining candidates by similarity to the target's NAG
- +4.9% avg over random; +5.3% over SOTA on HellaSwag

## Relation to Prior Wiki Knowledge

The neuron-activation approach to data selection has a direct connection to **LongAct (04-18)**: LongAct found that high-magnitude activations in Q/K vectors during long-context processing identify positions where attention is "doing real work." NAG-Ranking uses a similar principle at the neuron level for data selection — high-impact neurons define what the model finds important about an input. Both papers use activation magnitude as a mechanistic signal for something that was previously treated empirically.

**Connection to TIP (04-16)**: TIP identified high-signal tokens for distillation using entropy + divergence. NAG uses neuron activation for pretraining data selection. The common thread: identify the parts of the model that carry the signal, then concentrate training resources there.

## Related Pages

- [RL for LLMs](rl-for-llms.md)
- [Knowledge Distillation](../inference-efficiency/knowledge-distillation.md)
