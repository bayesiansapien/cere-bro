---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.147532+00:00
arxiv_id: 2611.22033
url: https://huggingface.co/papers/2611.22033
arxiv_url: https://arxiv.org/abs/2611.22033
date: 2026-11-19
---

# Thinking Harder Doesn't Lead to Better Choices: Reasoning Effort Increases the Confidence but Not the Correctness of LLM Shopping Agents

Large language models (LLMs) are increasingly deployed as autonomous shopping agents that process multimodal product listings (consisting of visual and text data) and recommend purchases on behalf of consumers. Naturally, one might assume that models with more thinking power would make higher-quality purchasing decisions. To test this belief, we ask two questions about such agents: does asking a model to think harder make it choose better products, and does the confidence it reports tell us the likelihood it may be wrong? We benchmark ten frontier models on three product-choice benchmarks built from WebShop, Amazon's SQID and Wayfair's WANDS platforms to see if LLMs with more thinking power actually make better-quality product purchase decisions. Across all three benchmarks, we found that increasing the thinking effort does not increase decision quality in a statistically meaningful way. The same change in thinking effort raises stated confidence at a statistically significant level, so extra thinking buys confidence rather than correctness. We also measure the calibration of these models (how well their reported confidence percentage matches their true correctness percentage) in these tasks and show that most models are not well-calibrated at every effort level. We also find that errors are strongly shared: when one model errs in a task, several others tend to err on that same task. Furthermore, on tasks where several models all err, a large number of them pick the same wrong product.
