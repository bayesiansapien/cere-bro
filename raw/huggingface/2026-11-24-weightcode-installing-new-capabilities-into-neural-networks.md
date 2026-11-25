---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.923915+00:00
arxiv_id: 2611.25476
url: https://huggingface.co/papers/2611.25476
arxiv_url: https://arxiv.org/abs/2611.25476
date: 2026-11-24
---

# WeightCode: Installing New Capabilities into Neural Networks via Weight-Space Programming

Neural networks encode learned capabilities in their weights, yet extending those capabilities with explicit task knowledge remains a fundamental challenge. Here we show that Weight-Space Programming (WSP), in which executable programs read, construct or modify a network's weights directly, can install new capabilities within trained neural networks. WeightCode, a WSP framework, uses a frozen language model to write executable weight programs that install new computations into trained neural networks using task knowledge and their existing weights, without gradient-based training. Once installed, the new capabilities run independently of the language model. Given a grammar or eight demonstrations, weight programs enable previously unseen command compositions (0% to 99.8% exact match) and a new pickup action (0% to 98.4% success), while preserving the original command and navigation capabilities. On ImageNet, four weight programs achieve net gains of 8.84-17.62 points while preserving clean accuracy, outperforming the best of eight fine-tuning methods under matched examples, checks, and retention constraints. In a Vision Transformer, causal interventions show that installed noise-correction gates drive robustness gains, while their selective activation preserves clean accuracy. Rerun on five independently trained Vision Transformers without further language model calls, ten weight programs retain 83-110% of their source-network gains on average, whereas copying their fixed weight edits yields negligible gains. Six programs written for an already edited network add 5.23-14.50 points of contrast robustness while retaining the previously installed noise gain. Together, these results establish WSP as a new route to acquiring and accumulating capabilities in trained neural networks through reusable weight programs.
