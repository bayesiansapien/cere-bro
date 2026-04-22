---
source: farmer/huggingface
farmed: 2026-04-22T00:00:00
arxiv_id: 2604.17761
url: https://huggingface.co/papers/2604.17761
arxiv_url: https://arxiv.org/abs/2604.17761
date: 2026-04-22
---

# Contrastive Attribution in the Wild: An Interpretability Analysis of LLM Failures on Realistic Benchmarks

Interpretability tools are increasingly used to analyze failures of Large Language Models (LLMs), yet prior work largely focuses on short prompts or toy settings, leaving their behavior on commonly used benchmarks underexplored. To address this gap, we study contrastive, LRP-based attribution as a practical tool for analyzing LLM failures in realistic settings. We formulate failure analysis as contrastive attribution, attributing the logit difference between an incorrect output token and a correct alternative to input tokens and internal model states, and introduce an efficient extension that enables construction of cross-layer attribution graphs for long-context inputs. Using this framework, we conduct a systematic empirical study across benchmarks, comparing attribution patterns across datasets, model sizes, and training checkpoints. Our results show that this token-level contrastive attribution can yield informative signals in some failure cases, but is not universally applicable, highlighting both its utility and its limitations for realistic LLM failure analysis.
