---
source: farmer/huggingface
farmed: 2026-05-10T03:37:12Z
arxiv_id: 2605.06200
url: https://huggingface.co/papers/2605.06200
arxiv_url: https://arxiv.org/abs/2605.06200
date: 2026-05-10
---

# A^2TGPO: Agentic Turn-Group Policy Optimization with Adaptive Turn-level Clipping

Reinforcement learning for agentic large language models (LLMs) typically relies on a sparse, trajectory-level outcome reward, making it difficult to evaluate the contribution of individual tool-calls within multi-turn interactions. We propose A^2TGPO (Agentic Turn-Group Policy Optimization with Adaptive Turn-level Clipping), which retains Information Gain (IG) as the intrinsic signal but re-designs how it is normalized, accumulated, and consumed: (i) turn-group normalization; (ii) variance-rescaled discounted accumulation; and (iii) adaptive turn-level clipping that modulates each turn's clipping range based on its normalized IG, widening the update region for informative turns and narrowing it for uninformative ones.
