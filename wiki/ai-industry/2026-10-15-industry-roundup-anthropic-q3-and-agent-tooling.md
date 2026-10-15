# Industry roundup, 2026-10-15: Anthropic's Q3, Cohere buys AISLE, agent tooling ships

**Date:** 2026-10-15 · **Sources:** The Information (RSS), lab watcher (Cohere, NVIDIA, OpenAI, Anthropic, Microsoft HF), X Following feed, Gmail (Runpod, Concordia), YouTube
**Raw:** `raw/rss/2026-10-1[45]-the-information-*.md`, `raw/labs/2026-10-15-143721-labs.md`, `raw/gmail/2026-10-15-newsletters.md`, X feed captures (private)

## Funding, valuations and deals

- **Anthropic Q3 revenue $16.8B**, +45% QoQ (Q2 was >140% per The Information, ~2.4x per FT), 3.6x all of 2025; adjusted profitable for a second quarter (11% adjusted operating margin); $1.70 revenue per $1 of compute; rival-lab distillation had been 5-7% of revenue until cut back in Q3; bankers have floated an IPO raising >$100B at ~$2T ([The Information](https://www.theinformation.com/articles/anthropics-rapid-slowing-growth-weigh-ipo-valuation)).
- **Anthropic licenses Opaque Systems** (confidential computing: AI jobs inside hardware-sealed enclaves with cryptographic run attestations) and hires CEO Aaron Fulkerson and CTO Rishabh Poddar. Opaque was valued at $300M after a $24M Series B ([X](https://x.com/rohanpaul_ai/status/2110467312549810266)).
- **Cohere to acquire AISLE** (autonomous vulnerability discovery; 500+ CVEs in year one, all 12 in OpenSSL's January release, 18 of 24 in curl's latest) after Reliant AI and Aleph Alpha ([Cohere](https://cohere.com/blog/cohere-and-aisle-sign-letter-of-intent-to-advance-cyber-resilient-sovereign-ai)).
- **Anduril** employee tender at ~$90B valuation, $94.80 per share, capped ~$1.3B ([The Information](https://www.theinformation.com/briefings/anduril-talks-employee-share-sale-90-billion-valuation)).
- **Harbor** raises a $10M seed to insure companies against AI-agent failures (six named perils, from hallucination to IP infringement) ([X](https://x.com/rohanpaul_ai/status/2110050322349686887)).
- **Sovereign funds** approached Perplexity to run its agent product entirely on hardware they own (X, Bloomberg via @rohanpaul_ai).
- **Sweden** startups raised $2.8B in 1H 2026, projected $5B for the year; Nordic AI clouds plan ~1 GW by end-2027; the Sferical One consortium (Ericsson, AstraZeneca, Saab, SEB, Wallenberg) runs 1,152 GB300 GPUs ([NVIDIA](https://blogs.nvidia.com/blog/nordics-technology-ecosystem/)).
- **Morgan Stanley CEO** Ted Pick expects another decade of major AI investment with bottlenecks and overbuild periods ([The Information](https://www.theinformation.com/briefings/morgan-stanley-ceo-expects-another-decade-major-ai-investment)).
- **People:** OpenAI compute-strategy VP Sachin Katti leaves 11-15 to build something new ([The Information](https://www.theinformation.com/briefings/openais-computing-lead-sachin-katti-depart-november)).

## Products and models

- **Meta Muse Wonder (Max)** enters Agent Arena at #12 (+6.4%), $1.13 median per task (2.1x Muse Spark 1.3), within 1 pt of GPT-5.6 Sol at 25% lower cost ([Arena](https://x.com/arena/status/2110465487914295770)).
- **Claude Code**: dynamic workflows (script-held orchestration of many subagents), a session sidebar sorted by "needs you" with recap cards, and agent step tracing (latency, tokens, tool calls per step, OpenTelemetry-style export) in public beta; Max and Team plans now include monthly API credits ($100 / $200 / up to $500 pooled).
- **Microsoft UserRepGen-4B** (MIT): a Qwen3.5-4B LoRA that writes task and behavior descriptions of a user from a conversation to condition user simulators ([HF](https://huggingface.co/microsoft/UserRepGen-4B)).
- **Grok Voice 3.0** claims the top conversational voice model; **Apple Intelligence** launches in mainland China in December ([The Information](https://www.theinformation.com/briefings/apple-prepares-debut-apple-intelligence-china-december)).
- **Runpod** Global Volumes on Serverless (one weights copy served across data centers; object storage, no locking).
- **OpenAI** case studies: SentinelOne (malware analysis weeks to hours with Daybreak) and Block security; OpenAI says over half of EU enterprise AI use now involves agents, small-business users up 8x.

## Policy and people

- Jensen Huang: "If the product is not safe, just don't release it," and he would not sell GPUs to irresponsible labs. Anthropic's international chief says open-weight models carry more safety risk by definition (Bloomberg via X).

Related: [TSMC and neocloud credit](../hardware/2026-10-15-tsmc-q3-and-neocloud-credit-stress.md) · [Monitorability and governance](../responsible-ai/2026-10-15-monitorability-firings-and-safety-governance.md)
