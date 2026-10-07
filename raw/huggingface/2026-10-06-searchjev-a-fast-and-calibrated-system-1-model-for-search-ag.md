---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.05107
url: https://huggingface.co/papers/2610.05107
arxiv_url: https://arxiv.org/abs/2610.05107
date: 2026-10-06
---

# SearchJev: A Fast and Calibrated System-1 Model for Search Agents

Search agents repeatedly make short decisions about relevance, evidence sufficiency, and search actions. Using generative language models for these decisions introduces latency and unreliable confidence. We present SearchJev, a fast and calibrated System-1 model that separates search decisions from System-2 reasoning and generation. Given a search state and a decision schema, SearchJev directly scores legal options without autoregressive output generation. We propose Soft-Label Learning for Calibrated Decisions (SLCD) to learn decision probabilities from uncertain supervision and calibrate their confidence. In a dual-system search agent, SearchJev handles short decisions and delegates uncertain judgments to System 2, which retains planning, query generation, and answer composition. We also introduce SearchDecision-Bench, a benchmark unifying six types of search decisions for training and evaluation. On SearchDecision-Bench, SEARCHJEV improves decision quality over same-size Qwen3.5 autoregressive models, achieves 5.2-5.3 times faster decisions, and reduces average expected calibration error by 41-74%. On BrowseComp-Plus, the dual-system agents achieve a 3.7-4.7 times speedup in active search time while improving answer accuracy from 45% to up to 54%.
