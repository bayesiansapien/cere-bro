# The cyber wave: scale not novelty, and the open-models argument (2026-10-31)

**Sources:** [Interconnects, "Was I wrong about open models & cyber risks?"](https://www.interconnects.ai/p/was-i-wrong-about-open-models-and) (Nathan Lambert, RSS + Gmail) · [AI Breakfast 10-30](https://aibreakfast.beehiiv.com/) summarizing [CrowdStrike on VAPOR PANDA](https://www.crowdstrike.com/en-us/blog/vapor-panda-uses-artex-to-scale-global-campaign/) and [Unit 42 on PHP2Shell + Fragnesia](https://unit42.paloaltonetworks.com/cve-2026-109618-cve-2026-109619/) · [Pragmatic Engineer, The Pulse](https://newsletter.pragmaticengineer.com/p/the-pulse-time-to-rethink-software) · [Ken Huang on Binance](https://kenhuangus.substack.com/p/how-binance-lost-63-billion-in-minutes) · The Decoder on a [malicious Claude Code extension in Cursor's marketplace](https://the-decoder.com/malicious-claude-code-extension-in-cursors-marketplace-attempted-remote-access-and-data-theft/)

## TL;DR

The incidents of "Black October" share one shape: models were used to run many intrusions at once against bugs that were already public, not to invent new exploits.

- **VAPOR PANDA (CrowdStrike).** A China-nexus group ran ARTEX, an agent framework (a main agent directing planner and worker agents over a shared graph of facts and goals), mainly on DeepSeek plus an unidentified commercial model. 200+ organizations targeted, 14 countries in 11 days from one controller, post-exploitation confirmed at nine. One intrusion's planners burned ~1.4B input tokens. Agents preferred hosts without a Falcon sensor. A human steered at decision points.
- **PHP2Shell + Fragnesia.** A second crew chained two PHP RCEs (CVSS 9.2) with a Linux XFRM privilege escalation, rooting 25 servers including PAN-OS firewalls in under 15 minutes per chain. Investigators found Claude Code, a scanner wired to DeepSeek and Kimi, and FOFA keys mapping ~19,000 exposed firewalls. The PHP bugs were found defensively with GPT-5.6 Sol (OpenAI's Patch the Planet), yet AWS saw exploitation attempts four days before disclosure.
- **Supply chain.** A tampered Claude Code extension sat on Cursor's marketplace ~11 hours, up to 5,000 users exposed. Railway customer secrets leaked; PingCAP's TiDB control plane was owned for a month (Sept 9 to Oct 7). eMudhra's intermediate CA keys were single-digit numbers.
- **Binance ($6.3B).** Largest crypto theft on record, via a compromised DevOps laptop and signing misuse (EIP-7702 delegation to a sweeper). Ken Huang's careful read: scripting and automation, no evidence of an autonomous AI agent.

**Lambert's argument.** If Claude Mythos had leaked as open weights in April, "the world would have been more or less fine": an acceleration, not a step change. GLM-5.3 already crosses Mythos-level cyber capability as open weights, and a month after release there is little public evidence of a step change. Closed models have played a heavier part in recent hacks. Open models are currently expensive to serve, so near-term misuse more likely runs through a poorly secured open-model API. He concedes "fine" undersells a forced, expensive industry rewrite of how software is secured.

## Assessment

The evidence this week supports Lambert's narrower claim (no step change attributable to open weights) and also the safety community's broader one (attack throughput is now bounded by tokens, not people: 1.4B tokens for one intrusion). Both can be true. The cost lever is the interesting part: VAPOR PANDA's token bill is the first public number on what an agentic intrusion costs to run.

## Relation to prior wiki

- **Extends** the 10-30 monitoring entry ([frontier monitoring](2026-10-30-frontier-monitoring-self-assessment-open-cyber.md)): OpenAI's four-layer monitor and Anthropic's KV-cache-riding self-check are the defender-side stacks; this is the attacker-side evidence.
- **Pairs with** [Agentic backdoors via pretraining poisoning](2026-10-31-agentic-backdoors-pretraining-poisoning.md) (supply-chain risk inside the model, not just its tools).
- Concept: [responsible-ai](responsible-ai.md).
