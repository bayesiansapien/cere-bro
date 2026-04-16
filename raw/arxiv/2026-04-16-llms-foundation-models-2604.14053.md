---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.14053
category: cs.CL
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.14053
published: 2026-04-16
authors: Pavel Chizhov, Egor Bogomolov, Ivan P. Yamshchikov
---

# From Where Words Come: Efficient Regularization of Code Tokenizers Through Source Attribution

**arXiv:** https://arxiv.org/abs/2604.14053
**Authors:** Pavel Chizhov, Egor Bogomolov, Ivan P. Yamshchikov

## Abstract

arXiv:2604.14053v1 Announce Type: new  Abstract: Efficiency and safety of Large Language Models (LLMs), among other factors, rely on the quality of tokenization. A good tokenizer not only improves inference speed and language understanding but also provides extra defense against jailbreak attacks and lowers the risk of hallucinations. In this work, we investigate the efficiency of code tokenization, in particular from the perspective of data source diversity. We demonstrate that code tokenizers are prone to producing unused, and thus under-trained, tokens due to the imbalance in repository and language diversity in the training data, as well as the dominance of source-specific, repetitive tokens that are often unusable in future inference. By modifying the BPE objective and introducing merge skipping, we implement different techniques under the name Source-Attributed BPE (SA-BPE) to regularize BPE training and minimize overfitting, thereby substantially reducing the number of under-trained tokens while maintaining the same inference procedure as with regular BPE. This provides an effective tool suitable for production use.
