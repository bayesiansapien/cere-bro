---
source: farmer/huggingface
farmed: 2026-09-03T17:01:45.591071
arxiv_id: 2609.02783
url: https://huggingface.co/papers/2609.02783
arxiv_url: https://arxiv.org/abs/2609.02783
date: 2026-09-03
---

# EarlyEval: Cheaper Agent Evaluation via Early Outcome Prediction

Evaluating LLM agents is essential for guiding their development, yet it has grown prohibitively expensive: a single pass of a frontier model over an agentic benchmark can cost hundreds to thousands of dollars, a price paid repeatedly across iterative development cycles. Prior efforts, centered on benchmark distillation, reduce the number of evaluation tasks but leave the cost of executing each retained task untouched. In this work, we introduce early outcome prediction, a complementary axis of efficiency that instead cuts cost within each task. Our key insight is that an agent's final outcome is often evident from its intermediate behavior well before execution completes. We instantiate this idea in EarlyEval, a lightweight framework that trains a pair of LightGBM success and failure classifiers over behavioral, textual, and reference-solution features, and halts an agent run the moment either classifier crosses a calibrated confidence threshold, adding negligible per-step overhead. Across three benchmarks, SWE-bench Verified, TerminalBench, and Toolathlon, EarlyEval can eliminate 13%-26% of agent steps and up to 44.1% input tokens and 29.4% output tokens at 89%-97% prediction accuracy, while perturbing per-agent resolve rates by only one to two percentage points on average.
