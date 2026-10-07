---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2609.39420
url: https://huggingface.co/papers/2609.39420
arxiv_url: https://arxiv.org/abs/2609.39420
date: 2026-10-06
---

# QuantCode Model: Specializing Language Models for Executable Algorithmic Trading Code

Large language models are strong general-purpose code generators, but executable algorithmic trading remains a demanding specialization target: a model must translate a natural-language strategy specification into correct program logic for a specialized trading framework, execute on historical data, produce trades, and remain semantically faithful to the request. We study two complementary mechanisms for specializing language models for this setting: continued pretraining on algorithmic-trading framework code and supervised fine-tuning (SFT) on agent-validated request-to-code pairs. Evaluation is centered on QuantCode-Bench, our 400-task benchmark for Backtrader strategy generation, together with a repository-level SWE-bench-like track. Continued pretraining improves single-turn Judge Pass from 41.5% to 47.5% for Qwen3.5-397B-A17B and from 27.8% to 33.0% for Qwen3.6-35B-A3B. SFT applied after continued pretraining yields a larger gain for Qwen3.6-35B-A3B, reaching 58.2% Judge Pass and 83.5% successful backtests; in agentic evaluation it raises first-turn success from 22.3% to 58.3% and final success after up to 10 turns from 47.5% to 79.5%. Continued pretraining alone improves first-turn agentic success but lowers final success after repair from 47.5% to 32.5%, consistent with degraded instruction following, whereas SFT improves both. We also identify a capability-retention failure: domain specialization degrades parser-conformant structured tool calling, and targeted recovery SFT restores tool-call formatting but not the base checkpoint's repository-level agent performance. The results show that framework-oriented pretraining, validated SFT, and explicit capability-retention evaluation address distinct failure modes in domain-specific executable code generation.
