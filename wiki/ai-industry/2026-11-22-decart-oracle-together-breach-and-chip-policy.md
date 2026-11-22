# Industry, US day 2026-11-21: Amazon's Decart deal, Oracle's OpenAI funding, a Together AI prompt leak, and chip policy

**TL;DR.** A weekend-quiet window with a few large moves. Amazon is nearing a roughly $7.5B purchase of Decart, the Israeli real-time video-model startup, almost twice its last $4B valuation; the reported logic is efficiency, since Decart's optimization gets more tokens per kilowatt from Amazon's Trainium chips (Amazon has claimed Trainium3 ran Decart's real-time video model 4x faster than GPUs at half the cost). Oracle says it has secured all the funding it needs for its OpenAI contract, implying the roughly $20B of extra equity and debt it flagged last month. Together AI disclosed that an AI coding agent committed a credential to its public `xorl` repo; an attacker used it to download stored prompt samples (MiniMax M3, GLM-5.2 and Kimi K2.6 requests from June and July) and searched them for further credentials. Together made zero data retention the default for new accounts. On policy, Trump threatened a "tremendous tax" on US companies building data centers abroad, TSMC paused some shipments as the new US export rules reached mobile and consumer parts, Cursor told House committees it may phase out Chinese open-weight models (its Composer 2 is built on Kimi K2.5), and Trump said Nvidia should rehire Jensen Huang while the board holds firm.

## Key items

- **Decart / Amazon:** ~$7.5B (FT via The Information). Efficiency as acquisition thesis. Prior context: [Decart, Trainium and agent CPU demand (10-12)](../hardware/2026-10-12-decart-trainium-and-agent-cpu-demand.md).
- **Oracle / OpenAI:** funding for the OpenAI contract complete (The Information).
- **Together AI incident:** agent-committed credential, prompt samples exfiltrated, five Dragos canary credentials tested by the attacker. Changes: scoped/short-lived credentials, PR secret scanning, ZDR default, new rules for AI coding agents.
- **Cairn zero-day:** Amazon says a suspected China-linked actor used the open-source Cairn agent framework to find and exploit a MONAI medical-imaging zero-day in 11 minutes from the instruction "obtain shell access" (AI Weekly Espresso).
- **Policy:** overseas data-center tax threat; TSMC shipment pauses (Nikkei); Cursor and PRC models (CNBC).
- **Jensen Huang:** Trump publicly backed his return; Nvidia's board says no (The Information).

## How it relates to prior wiki pages

- **Agent security** now has a lab-side incident caused by an agent's commit, joining the Prime Intellect breach and OpenAI's DNS-escape pause from the 11-21 digest. See [responsible-ai](../responsible-ai/responsible-ai.md).
- **Compute economics:** an acquisition priced on tokens per kilowatt is the market version of the "bytes, not FLOPs" efficiency thread. See [compute-economics](../hardware/compute-economics.md) and [Nvidia without Jensen (11-13)](../hardware/2026-11-13-nvidia-without-jensen.md).

**Sources:** [The Information: Decart](https://www.theinformation.com/briefings/amazon-nearing-7-5-billion-purchase-decart) · [@rohanpaul_ai](https://x.com/rohanpaul_ai/status/2124294348712092061) · [The Information: Oracle](https://www.theinformation.com/briefings/oracle-says-completed-funding-fulfil-openai-deal) · [Together AI incident](https://www.together.ai/blog/security-event-prompt-leakage-for-requests-in-june-and-july-of-2026) · [The Information: Jensen](https://www.theinformation.com/articles/can-jensen-return) · AI Weekly Espresso (Gmail). Raw: `raw/rss/2026-11-21-the-information-*`, `raw/labs/2026-11-22-103314-labs.md`.
