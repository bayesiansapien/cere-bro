---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.823602+00:00
arxiv_id: 2609.22753
url: https://huggingface.co/papers/2609.22753
arxiv_url: https://arxiv.org/abs/2609.22753
date: 2026-10-02
---

# Replacing Large Language Models with Jev Decision Models for Low-Latency Edge Service Orchestration

Natural-language service requests can require a language-model decision before execution starts, consuming part of the request's latency budget. We integrate Jev's decision-oriented application programming interface (API) into edge service orchestration to reduce this overhead while retaining service completion. The integration extracts four to eight bounded intent fields and applies a shared validator, admission policy, and scheduler, accounting for decision waiting throughout the request timeline. We compare Jev, two self-hosted decision models, and three hosted large language models (LLMs) on 8,280 verified requests and on a live admission path with modeled execution and a real optical character recognition service. Across 33 test conditions, Jev reduces median decision latency by 22.7-64.5% relative to the fastest LLM. This latency barely moves with input size, contract width, or catalog size. On four-field contracts, Jev's API fees per correct decision are 59.7-80.9% lower at a cost of a few exact-match points, while wide contracts mark the limit of the substitution. Receiving the service catalog with each request, Jev names unseen services as accurately as known ones. On the live admission path, Jev keeps 0.91-0.95 of requests exact and on time at loads where the LLMs fall below 0.1. Since caching repeated descriptions gives the interpreters nearly the same latency, Jev's gain lies in fresh decisions. These results support decision-model substitution for latency-bound admission on bounded contracts.
