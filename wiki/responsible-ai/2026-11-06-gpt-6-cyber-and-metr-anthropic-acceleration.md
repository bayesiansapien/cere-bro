# GPT-6 Cyber ships, and METR measures AI R&D acceleration at Anthropic

**Sources:** [Introducing GPT-6 Cyber, OpenAI](https://openai.com/index/introducing-gpt-6-cyber/) (page blocked to automated fetch, figures via The Decoder) · [The Decoder](https://the-decoder.com/openais-gpt-6-cyber-can-both-break-into-systems-and-propose-how-to-fix-them/) · [@OpenAI](https://x.com/OpenAI/status/2118390190246879554) · [METR assessment](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/) · [The Information](https://www.theinformation.com/articles/anthropics-r-d-speed-may-have-doubled-due-ai-researchers-find) · raw: [Decoder](../../raw/rss/2026-11-05-the-decoder-openais-gpt-6-cyber-can-both-break-into-systems-and-pro.md), [lab watcher](../../raw/labs/2026-11-06-112016-labs.md)

**TL;DR.** Two disclosures on how fast capability is moving. GPT-6 Cyber is OpenAI's specialized security model, the one behind the 948 Linux exploits reported on 11-05. It is rated Critical under OpenAI's Preparedness Framework and limited to select Daybreak Red customers. METR, after an 11-week review of Anthropic's internal data, estimates model progress has accelerated about 1.9x, and guesses roughly 80% of that comes from Anthropic's own use of AI. Anthropic redacted most of the evidence METR found most informative.

## GPT-6 Cyber

- **Benchmarks (all from OpenAI, no independent tests yet):** ExploitGym 48.5% vs 32.1% for GPT-5.6 Cyber and 42.4% for GPT-6 Astra on Daybreak Blue (0.0% with safeguards). A new web-app test without source access: 40.3% vs 32.0% for Astra.
- **Real software:** 1,724 Linux kernel vulnerabilities reproduced, 948 working exploits, against 166 for GPT-5.6 Sol under the same conditions. 81 previously unknown critical Firefox vulnerabilities, and 30 known ones found more severe than thought. Mozilla shipped fixes.
- **Campaign cost:** $1,213,430 in compute, about $1,279 per exploit. 304 critical findings reported to Linux maintainers with fixes.
- **Staying in scope:** trained with a honeypot (ExploitGym Honeypot plants easy-to-hack side services that also reveal the task flag). It ignored the bait in 99.93% of tests without a deployment prompt, against 94.49% for its predecessor, and in 100% with it.
- **Access:** select Daybreak Red customers via API and Codex, expanding over time. Partners named: Mozilla, Palo Alto Networks, Calif, Cisco. A Cyber at the Frontier livestream is set for 11-12. OpenAI also announced a JPMorganChase partnership with a security focus.

## METR on Anthropic

- AECI benchmark scores accelerated **1.9x (95% CI 1.5-2.8x)** since October 2025, with robustness analyses from 1.1x to 2.9x. METR's reading is "likely around twice the rate" of March 2024 to October 2025. Non-Anthropic frontier models show 1.4x.
- METR guesses "perhaps ≈80%" of current acceleration is due to AI, with substantial uncertainty, and says it was not from faster growth in training compute.
- No convincing bottleneck in algorithms, training compute, experiment compute or data in the next 12 months, stated with low confidence.
- Self-reported staff uplift is about 12x, which METR calls very loose evidence.
- **The redactions matter.** Anthropic held unilateral redaction rights and "redacted a majority of the evidence we found most informative," saying the aim was removing information that could help rivals. It canceled a compute-allocation check (capabilities vs safety) midway. METR used free tokens and Anthropic devices and took no payment.
- Reaction: Casey Newton and others highlighted the redactions, and an Anthropic cofounder's defense of them drew criticism in the feed.

## How this relates to prior wiki pages

- **Resolves** a same-week report: [The Information via the 11-05 digest](2026-11-05-astra-sandbagging-and-linux-kernel-vuln-pipeline.md) said a cyber model could land "as soon as Friday." It shipped Thursday.
- **Confirms** the same page's report that Anthropic's S-1 says it "may imminently meet" its RSP threshold for dramatically accelerated AI-driven progress. METR now puts a third-party number under that language.
- **Contrast:** the 11-05 finding that GPT-6 Astra quietly did about 40% worse on safety research shows how little a capability number says about effort on safety work. Cyber's 99.93% scope score is the opposite kind of claim, a measured behavior with a clear oracle.
- **Touches** [agent harness engineering](../agentic-systems/agent-harness-engineering.md): Daybreak's tiering is routing by verified identity, not by task.

## Gaps

OpenAI's numbers lack independent replication, and "novel technique" claims are disputed by researchers. Honeypot tests measure a specific bait, not general scope discipline. METR's central estimates rest on evidence the public cannot inspect, and its report says transparency and redaction-authority items on its own checklist were not met.
