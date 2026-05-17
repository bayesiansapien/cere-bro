---
source: farmer/huggingface
farmed: 2026-05-17T00:00:00Z
arxiv_id: "2605.14389"
url: "https://huggingface.co/papers/2605.14389"
arxiv_url: "https://arxiv.org/abs/2605.14389"
date: 2026-05-17
---

# Nexus: An Agentic Framework for Time Series Forecasting

Time series forecasting is not just numerical extrapolation, but often requires reasoning with unstructured contextual data such as news or events. While specialized Time Series Foundation Models (TSFMs) excel at forecasting based on numerical patterns, they remain unaware of real-world textual signals. Conversely, while LLMs are emerging as zero-shot forecasters, their performance remains uneven across domains and contextual grounding. To bridge this gap, we introduce Nexus, a multi-agent forecasting framework that decomposes prediction into specialized stages: isolating macro-level and micro-level temporal fluctuations, and integrating contextual information when available before synthesizing a final forecast. This decomposition enables Nexus to adapt from seasonal signals to volatile, event-driven information without relying on external statistical anchors or monolithic prompting. Evaluated on data strictly succeeding LLM knowledge cutoffs spanning Zillow real estate metrics and volatile stock market equities, Nexus consistently matches or outperforms state-of-the-art TSFM and strong LLM baselines.
