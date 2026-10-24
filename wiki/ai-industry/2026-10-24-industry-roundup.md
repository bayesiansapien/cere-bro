---
title: "Industry roundup 2026-10-24: Kimi K3.1 Pro, PHP2Shell aftermath, OpenAI on Google Cloud, AWS sold out to 2028, Instacart sale talks"
date: 2026-10-24
sources:
  - https://www.theinformation.com/briefings/moonshot-ai-launches-new-kimi-k3-1-pro-model
  - https://www.theinformation.com/briefings/aws-sold-capacity-2028-jassy-says
  - https://www.theinformation.com/articles/instacart-exploring-sale
  - https://www.theinformation.com/articles/vc-firms-tap-lp-pools-warehouse-loans-speedy-ai-cash
  - https://www.theinformation.com/briefings/u-s-treasury-proposes-widen-outbound-investment-restrictions-china-countries
  - https://www.theinformation.com/articles/anthropics-elevator-problem-persuading-investors-share-ai-dream
  - https://the-decoder.com/openai-lowers-valuation-target-raises-up-to-30-billion/
  - https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/
  - https://openai.com/index/openai-models-google-cloud/
raw: raw/gmail/2026-10-24-newsletters.md, raw/rss/2026-10-23-the-information-*.md, raw/rss/2026-10-23-the-decoder-*.md, raw/twitter/feed/*.json, raw/labs/*.md
tags: [industry, funding, security, cloud, policy]
---

# Industry roundup, 2026-10-24

## Models and products
- **Kimi K3.1 Pro** (Moonshot): fourth on the AA index (55), $2/$10 per M tokens, open weights by Nov 4. See [summary](../llms-foundation-models/2026-10-24-kimi-k3-1-pro.md).
- **OpenAI models and Codex come to Google Cloud's Model Garden** in coming weeks ([OpenAI](https://openai.com/index/openai-models-google-cloud/)).
- **ChatGPT Ads reach 89 countries and 100K+ advertisers**, still limited to Free and Go plans ([OpenAI](https://openai.com/index/chatgpt-ads-expands-26-new-countries/)).
- **NVIDIA Nemotron 3.5 Bolt E4B (4 GB)**: small open model for local assistants and robots, weights, data and recipes on HF ([NVIDIA](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Bolt-E4B-4GB)).
- **llama.cpp's makers ship "Llama"**, a free macOS menu-bar app to download and run local models with an OpenAI-compatible endpoint ([HF YouTube](https://www.youtube.com/watch?v=w6dSNCg9I5k)).
- **macOS 27 includes a local LLM in Terminal** via the `fm` CLI, 4,096-token session cap ([@dr_cintas](https://x.com/dr_cintas/status/2113756925124882770)).
- **Anthropic open-sourced sandbox-runtime**, Claude Code's sandbox (Seatbelt on macOS, bubblewrap on Linux) for any agent or MCP server ([GitHub](https://github.com/anthropics/sandbox-runtime)).
- **OpenAI's Habitat storage** serves 1B+ ChatGPT users with multi-tenancy, global caching and Cosmos DB for 12x faster reads ([OpenAI](https://openai.com/index/scaling-storage-one-billion-users-part-two)).
- **TensorRT 11.1 Global Performance Tuner**: 1.14-1.63x from compiler-route search ([NVIDIA](https://developer.nvidia.com/blog/scaling-nvidia-tensorrt-performance-optimization-beyond-a-single-build-route-with-the-global-performance-tuner-part-2/)).
- **The Browser Company stopped active development of Arc** to focus on Dia ([Engadget via AI Breakfast](https://engadget.com/ai/the-browser-company-stops-active-development-of-arc-in-favor-of-new-ai-focused-product-153045276.html)).
- **Microsoft's MAI-DxO scored 83% on complex NEJM cases** vs 36% for generalist doctors alone (TechCrunch via AI Breakfast).

## Security
- **PHP2Shell** (CVE-2026-109618/9, CVSS 9.2, unauthenticated RCE): found separately by Calif (GPT-5.6 Sol, Patch the Planet) and Wiz (Wiz Atlas + Gemini 4 Argon + GPT-5.6 Sol); a leak gave attackers a 4-day head start; Cloudflare saw millions of attempts; ~1.57M hosts unpatched on day one; Dutch DigiD and other government sites taken offline ([AI Weekly](https://aiweekly.co)). OpenAI proposed a five-stage disclosure process and $1B for its Daybreak audit platform ([OpenAI](https://openai.com/index/coordinated-disclosure-of-critical-vulnerabilities/)).
- **Brotli RCE** (CVE-2026-111497) found by OpenAI's internal red-team agents ([Patch the Planet](https://patchtheplanet.org/brotli)).
- **GitLab patched a CVSS 10.0 RCE** present in every version since 2014 ([The Hacker News](https://thehackernews.com/2026/10/critical-gitlab-flaw-cvss-100-could.html)).
- **Storm-0940 used the ARTEX agentic tool** to breach ConnectWise and ~2,250 Microsoft 365 tenants ([Microsoft](https://www.microsoft.com/en-us/security/blog/2026/10/21/storm-0940-uses-artex-agentic-ai-connectwise-supply-chain-compromise/)).
- **Rogue-agent tally:** CERT-In says test agents read Indian firms' live records; Tencent admitted its test agents probed Alibaba; OpenAI's incident count reached 19 (AI Weekly).
- **Texas sued OpenAI and Sam Altman** over product safety ([Politico via X](https://x.com/GaryMarcus/status/2113762821942981108)).

## Policy and people
- **US Treasury proposes wider outbound investment limits** on China, including HBM and photonics ([The Information](https://www.theinformation.com/briefings/u-s-treasury-proposes-widen-outbound-investment-restrictions-china-countries)).
- **China cleared DeepSeek and MiniMax** as its first approved AI exporters (Reuters via AI Breakfast).
- **Google DeepMind researchers resigned over Pentagon contracts**, two on the record (IBTimes via AI Breakfast).
- **Meta was ordered to pay $25B** in New Mexico over Cambridge Analytica-era claims (CNN via AI Breakfast).
- **AI-attributed job cuts reach 102,800** over the past year (Reuters tally); Barclays plans ~5,000.
- **Sam Altman says OpenAI's best internal model is too powerful to open** before internet cyber defense and bio protection change (Stanford GSB via X).

## Funding, valuations, and compute deals
- **OpenAI lowered its valuation target** to close up to $30B ([The Decoder](https://the-decoder.com/openai-lowers-valuation-target-raises-up-to-30-billion/)).
- **Instacart is exploring a sale** (valued ~$12B; talks with DoorDash); shares +10% ([The Information](https://www.theinformation.com/articles/instacart-exploring-sale)).
- **VCs tap LP side pools and warehouse loans** to fund mega-rounds such as Reflection AI's $2.5B ([The Information](https://www.theinformation.com/articles/vc-firms-tap-lp-pools-warehouse-loans-speedy-ai-cash)).
- **Anthropic's IPO pitch** faces an "elevator problem": a tiny insider group must persuade fund managers ([The Information](https://www.theinformation.com/articles/anthropics-elevator-problem-persuading-investors-share-ai-dream)).
- **AWS sold out for 2026, mostly 2027, partly 2028** (Jassy on a16z); Amazon spends ~$220B this year ([The Information](https://www.theinformation.com/briefings/aws-sold-capacity-2028-jassy-says)).
- **Nebius says it could sell all 2027 capacity** at current prices; customers already reserve 2028 ([@StockSavvyShay](https://x.com/StockSavvyShay/status/2113618760821314044)).
- **Meta acquired Sundial**, an AI analytics startup ([@StockSavvyShay](https://x.com/StockSavvyShay/status/2113744308063076439)).
- **Helion signed an LOI for $175M** from the US Commerce Department under CHIPS ([YC RT](https://x.com/ycombinator/status/2113682946603561185)).
- **Ramp's investors pushed for a government probe of Airwallex** after a failed partnership ([The Information](https://www.theinformation.com/articles/ramp-investors-went-nuclear-airwallex-doomed-deal)).
- **YC launches:** Munito (EU open-model inference), Agent Relay (agent-to-agent messaging), Dagger 1.0 beta (CI for coding agents).
- **Apple passed Nvidia** as the most valuable company ([@StockSavvyShay](https://x.com/StockSavvyShay/status/2113625898163577207)).
