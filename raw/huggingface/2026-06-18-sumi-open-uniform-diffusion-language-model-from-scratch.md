---
source: farmer/huggingface
farmed: 2026-06-18T00:00:00Z
arxiv_id: 2606.19005
url: https://huggingface.co/papers/2606.19005
arxiv_url: https://arxiv.org/abs/2606.19005
date: 2026-06-18
---

# Sumi: Open Uniform Diffusion Language Model from Scratch

Diffusion models have become a promising alternative to autoregressive models. Among these, uniform diffusion language models (UDLMs) permit any token to be updated at any step, in principle enabling more flexible generation. However, no UDLM has yet been pretrained from scratch at both large parameter scale and large token budget. Both autoregressive modeling and masked diffusion modeling already have capable models at scale that the community can study and build on; uniform diffusion has none. A scratch-pretrained UDLM at scale would provide a clean reference point for studying scaling behavior, generation dynamics, controllability, and trade-offs against established autoregressive and masked diffusion models. To this end, we introduce Sumi ("ink" in Japanese), a fully open 7B uniform diffusion language model pretrained from scratch on 1.5T tokens. Sumi performs competitively with autoregressive models trained at comparable token budgets on knowledge, reasoning, and coding benchmarks, while under-performing on commonsense benchmarks, where our education-heavy data mixture is a likely contributor. We release our model weights, checkpoints, and full training recipe, including a complete specification of the data mixture over publicly available corpora. We hope this release enables the community to study native uniform diffusion at scale and catalyzes work on its as-yet poorly understood aspects.
