---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.934441+00:00
arxiv_id: 2609.33645
url: https://huggingface.co/papers/2609.33645
arxiv_url: https://arxiv.org/abs/2609.33645
date: 2026-09-29
---

# Pruned CTC for Memory-Efficient Large-Vocabulary ASR Training

Connectionist temporal classification (CTC) naturally supports offline and streaming speech recognition with utterance-level supervision, but conventional implementations materialize frame-by-vocabulary activations in memory, making CTC training with native LLM vocabularies prohibitively memory-intensive. A key observation is that every valid CTC alignment uses only target tokens and blank, and their union across a batch typically forms a small subset of the full vocabulary. We introduce Pruned CTC, which restricts alignment computation to this subset while retaining full-vocabulary normalization. We prove that this vocabulary reduction is exactly equivalent to full-vocabulary CTC in loss and gradients. Head-and-loss activation memory no longer scales linearly with vocabulary size. We further apply finite-beam alignment pruning. Building on Pruned CTC, we develop LLM-CTC, which adapts pretrained LLMs for non-autoregressive ASR while retaining causal attention and native vocabularies, and extend it to bounded-history streaming, avoiding chunk-level speech--text alignments. Experiments show that, with Zipformer-M encoder and 180K vocabulary, Pruned CTC reduces full-step memory by 5.1times with only 17% step-time overhead. Across three corpora, it matches standard CTC accuracy. On GigaSpeech, across six Qwen3 model sizes from 0.6B to 32B, LLM-CTC remains within 7% relative WER of LLM-CE with 7 to 10times faster recognition; when fine-tuning Qwen3-ASR for bounded-history streaming, LLM-CTC remains within 3% relative WER of matched offline models on the test set. Together, these results establish Pruned CTC as a scalable sequence objective for native-vocabulary LLM ASR across offline and streaming settings.
