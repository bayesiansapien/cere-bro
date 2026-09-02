---
source: farmer/huggingface
farmed: 2026-09-02T13:31:46.243214
arxiv_id: 2608.30730
url: https://huggingface.co/papers/2608.30730
arxiv_url: https://arxiv.org/abs/2608.30730
date: 2026-09-02
---

# E-Commerce Bench: Evaluating LLM Agents on Long-Horizon Autonomous Business Operation

Long-horizon agentic tasks go beyond chaining short tasks over more interaction turns. Their evolving dynamic environments and long-range dependencies require Large Language Models (LLMs) to continually explore, learn from experience, and adapt their policies over thousands of steps. We introduce E-Commerce Bench, the first open-source benchmark that integrates multi-round counterpart negotiation and dynamic events into a year-long business operation. Over a 365-day year, an LLM agent concurrently runs multiple online stores, researching the market, negotiating with suppliers to source inventory, optimizing sales strategies, fulfilling orders, handling returns, and managing cash flow to maximize its end-of-year total assets. To construct a realistic merchant-side operating environment, the product and supplier data are derived from a real e-commerce platform, while a year-long calendar of promotions, natural disasters, and supply-chain shocks continually reshapes demand. For reproducibility, both sides of the market are deterministic: customer purchases and returns follow a fixed demand model, while a negotiation kernel determines supplier pricing, concessions, and decisions, with an LLM used only to verbalize them. We evaluate 18 frontier models across seven dimensions, including year-end assets, and find that no single model dominates. GPT-5.6 Sol earns the most, growing the 100,000 opening stake into 1,431,425, yet it ranks 16th of 18 on fraud avoidance and trails Fable5 in operational efficiency. Among open-weight models, Qwen3.8-Max-Preview leads with 416,252, 38% above GLM 5.2 (high), and achieves the strongest learning over the horizon, progressively bargaining down prices across repeated orders. Our code is available at https://github.com/QwenLM/E-CommerceBench.
