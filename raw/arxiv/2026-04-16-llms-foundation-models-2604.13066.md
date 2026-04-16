---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13066
category: cs.AI
concept: llms-foundation-models
url: https://arxiv.org/abs/2604.13066
published: 2026-04-16
authors: Andresa Rodrigues de Campos, David Lee, Imry Kissos
---

# Lossless Prompt Compression via Dictionary-Encoding and In-Context Learning: Enabling Cost-Effective LLM Analysis of Repetitive Data

**arXiv:** https://arxiv.org/abs/2604.13066
**Authors:** Andresa Rodrigues de Campos, David Lee, Imry Kissos

## Abstract

arXiv:2604.13066v1 Announce Type: cross  Abstract: In-context learning has established itself as an important learning paradigm for Large Language Models (LLMs). In this paper, we demonstrate that LLMs can learn encoding keys in-context and perform analysis directly on encoded representations. This finding enables lossless prompt compression via dictionary encoding without model fine-tuning: frequently occurring subsequences are replaced with compact meta-tokens, and when provided with the compression dictionary in the system prompt, LLMs correctly interpret these meta-tokens during analysis, producing outputs equivalent to those from uncompressed inputs. We present a compression algorithm that identifies repetitive patterns at multiple length scales, incorporating a token-savings optimization criterion that ensures compression reduces costs by preventing dictionary overhead from exceeding savings. The algorithm achieves compression ratios up to 80$\%$ depending on dataset characteristics. To validate that LLM analytical accuracy is preserved under compression, we use decompression as a proxy task with unambiguous ground truth. Evaluation on the LogHub 2.0 benchmark using Claude 3.7 Sonnet demonstrates exact match rates exceeding 0.99 for template-based compression and average Levenshtein similarity scores above 0.91 for algorithmic compression, even at compression ratios of 60$\%$-80$\%$. Additionally, compression ratio explains less than 2$\%$ of variance in similarity metrics, indicating that decompression quality depends on dataset characteristics rather than compression intensity. This training-free approach works with API-based LLMs, directly addressing fundamental deployment constraints -- token limits and API costs -- and enabling cost-effective analysis of large-scale repetitive datasets, even as data patterns evolve over time.
