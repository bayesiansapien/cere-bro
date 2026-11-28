---
title: "Industry roundup 2026-11-28: Trainium runs Bedrock, SAP cuts, OpenAI countersues Apple, Blackwell in Shanghai"
date: 2026-11-28
tags: [industry, hardware, export-controls, funding, enterprise-ai]
raw: ../../raw/gmail/2026-11-28-newsletters.md
---

# Industry roundup, 2026-11-28 (US day 2026-11-27, Thanksgiving Friday)

**Compute and chips**
- **Amazon's chips business is a $25B+ run-rate** (Trainium plus Graviton), and most of Bedrock's inference runs on Trainium, per Andy Jassy on Semafor ([post](https://x.com/rohanpaul_ai/status/2126526160603648204)). Pairs with SemiAnalysis's [Trainium3 inference results](../hardware/2026-11-28-semianalysis-trainium3-inference.md).
- **Banned Blackwell chips found in a Shanghai data center** linked to Alice Huang; a serial number traced them to Gigabyte (Bloomberg via [The Decoder](https://the-decoder.com/banned-nvidia-blackwell-chips-turn-up-in-a-shanghai-data-center-linked-to-alice-huang-bloomberg-reports/)).
- **Singapore is negotiating with the US** to keep advanced-chip access after the new licensing rules ([The Information](https://www.theinformation.com/briefings/singapore-talks-u-s-keep-ai-chip-access)).
- **Nebius says Blackwell NVL72 work carries to Vera Rubin** without rewrites; Rubin is pitched at ~10x tokens per megawatt vs GB200 (vendor figure).
- **AMD kernels now ship through the Hugging Face Hub** kernel distribution, pulled like models.
- **Yandex released AliceAI-Foundation-80B-A3B-Base** (80B MoE, ~3B active) under Apache 2.0: 88.7% pass@8 IMO-AnswerBench, 82.9% LiveCodeBench v5-v6 (AI Weekly).

**Enterprise and labs**
- **SAP weighs 10,000+ job cuts** (about 9% of 110,000) in an AI-first restructuring ([The Decoder](https://the-decoder.com/sap-plans-to-cut-at-least-10-000-jobs-as-it-pivots-to-ai/)).
- **OpenAI countersued Apple** for trade-secret theft and supplier coercion, as OpenAI builds its own devices ([The Decoder](https://the-decoder.com/openai-countersues-apple-over-trade-secret-theft-and-alleged-coercion-of-shared-suppliers/)).
- **OpenAI is building "Athena"**, a semantic layer of standard metric definitions for its ChatGPT Work data agent; a move toward Snowflake/Databricks turf ([The Decoder](https://the-decoder.com/openai-is-building-athena-data-platform-to-cut-down-on-ai-agent-guesswork/)). Same idea as NVIDIA's Auto Ontology (11-27).
- **Google Workspace MCP servers went GA on 11-24**; from 2027-02-01 any AI-agent-driven tool must reach Gmail, Drive and Calendar through them or face quota caps and suspension. The Gmail server cannot send email (AI Weekly).
- **Cognition**: Scott Wu says a Devin bot built and maintains Cognition's whole Android app; Citi expects ~$1.5B of 2026 savings from Devin ([post](https://x.com/rohanpaul_ai/status/2126527559022289088)).
- **Apple pulled MiniMax's Talkie** worldwide after a report on sexualized content aimed at young users ([The Information](https://www.theinformation.com/briefings/apple-pulls-minimax-chatbot-app-store-report-sexualized-content)).
- **Meta / AMI Labs**: three JEPA world-model studies (robot planning, more efficient training, error correction) back LeCun's alternative to LLMs ([The Decoder](https://the-decoder.com/three-studies-from-meta-and-ami-labs-back-yann-lecuns-bet-on-jepa-world-models-over-large-language-models/)).
- **NBER (174M consumers, 114B transactions)**: consumer AI subscriptions retain worse than Netflix, Spotify and the NYT; substitutability limits pricing power ([paper](https://www.nber.org/system/files/working_papers/w35953/w35953.pdf)).

**Finance and policy**
- **Citi and JPMorgan are selling AI data-center loan portfolios**, some via synthetic risk transfers, as AI issuance "crowds out Treasurys" (Semafor via AI Weekly).
- **Congress's frontier AI bill push stalls** on committee turf; S. 918 would create a Senate select committee on AI (NYT via AI Weekly).
- **Palantir signed ~$100M with Poland** for Maven.

**Security**
- **US Air Force Cloud One breached** ([The Decoder](https://the-decoder.com/hackers-breached-the-us-air-forces-flagship-cloud-one-platform-report-says/)).
- **Mitel MiCollab attackers called commercial AI APIs** mid-intrusion; root in 12 minutes via five zero-days (Accenture via SecurityWeek, AI Weekly).

Related: [compute-economics](../hardware/compute-economics.md)
