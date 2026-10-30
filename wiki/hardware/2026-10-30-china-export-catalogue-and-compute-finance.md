# China's AI export catalogue, Samsung's HBM quarter, and who is financing the compute

**Sources:** [AI Safety in China Brief #31](https://aisafetychina.substack.com/p/brief-31-what-chinas-new-ai-export) · [AI Weekly Espresso (Samsung, DOE-Constellation, Microsoft)](https://aiweekly.co) · [The Information: Nvidia backstops Nscale](https://www.theinformation.com/articles/nvidia-talks-provide-billions-credit-support-cloud-providers-45-billion-anthropic-deal) · [The Information: Intel drops 20%+](https://www.theinformation.com/briefings/intel-shares-drop-20-weak-sales-forecast) · [The Information: DeepSeek's $16B round](https://www.theinformation.com/articles/behind-deepseeks-16-billion-funding-chinese-tech-titans-state-players) · [The Information: Solving for AI's power problem](https://www.theinformation.com/articles/solving-ais-power-problem) · [@rohanpaul_ai on Anthropic and SpaceX](https://x.com/rohanpaul_ai/status/2115938869082542548) · [@StockSavvyShay on Intel CPU:GPU](https://x.com/StockSavvyShay/status/2115924406094700702). raw: `raw/rss/2026-10-29-ai-safety-china-brief-31-*.md`, `raw/gmail/2026-10-30-newsletters.md`, `raw/rss/2026-10-29-the-information-*.md`, `raw/rss/2026-10-30-the-information-*.md`.

**TL;DR.** China's MOFCOM and MOST published a draft revision of the export catalogue on 10-16 that adds 23 AI items: certain LLMs, agents, chip designs, compute clusters and offensive cyber tooling. Six are prohibited (J codes) and 17 restricted (X codes, license needed). Open-sourcing now counts as an export, but already-open technology is exempt and future open releases in the restricted tier get "file and go" automatic licenses. Exporters must already register catalogued technology; DeepSeek and MiniMax reportedly have. The real question is whether frontier open models land in the restricted or prohibited tier. On the money side, Samsung posted 107.4T won (about $80.5B) Q3 operating profit, up 783%, with HBM shipments up nearly 50% quarter on quarter and HBM4 at 60% of HBM sales. Nvidia is in talks to give Nscale billions in credit guarantees for a 460 MW data center backing a $45B Anthropic compute contract, financing power and construction rather than GPUs. Anthropic was 34.5% of SpaceX's $14.575B Q3 revenue ("Customer B"), renting Nvidia GPUs in Memphis. Intel fell more than 20% after hours on a weak forecast even as its CEO argued agents double the CPU:GPU ratio from 1:8 to 1:4.

## Key facts

- **Export catalogue.** 40 new items, 23 AI-related. MOFCOM cites AI-driven autonomous malicious code generation by non-state actors. The TikTok precedent (a 2020 catalogue addition that blocked a sale for five years) shows a restricted license is not a formality.
- **DeepSeek's ~$16B round**, its second ever: Tencent and CATL remain top investors, plus memory maker CXMT and its chairman, and state-backed institutions.
- **Memory.** Samsung is the first tech company to top 100T won operating profit in a quarter. Combined with 10-29's CXMT HBM3E at 20-30% yields, the HBM premium is still widening.
- **Financing.** Nvidia's guarantee is credit support for neocloud debt, after similar signals for CoreWeave and Firmus. Anthropic's SpaceX deal runs up to $120.5B into 2029 (~$3.1B a month once delivered in December 2026) but is a *maximum* with 90-day termination, unlike its hyperscaler *minimums* ($114.5B Google, $110B Amazon, $44.9B Microsoft).
- **Power.** DOE committed a $5B loan to Constellation for a 1.1 GW uprate across 11 reactors, mostly pre-sold to Google, Meta and Amazon. At The Information's power panel, Cloverleaf's Brian Janous argued the grid runs about 45% underused because it is sized for peaks; microgrids (ERock built 350 MW in 16 months) bridge the 3-4 years a substation takes.
- **Second-hand compute.** A 300-rack ex-hyperscaler cluster with up to 9,600 A100s is listed on eBay at $59.7M (about $6.2K per GPU with everything included).
- **Smuggling.** Bloomberg on Megaspeed's GPU flows to China; NYT reports US intelligence believes someone in Jensen Huang's circle informs for China.

## How it relates to prior wiki pages

- **Extends** [compute economics](compute-economics.md) (10-26: "credit closes on neoclouds"): the response is vendor credit. Nvidia is now underwriting the customers of its customers.
- **Confirms** the 10-24 "memory carries the premium" entry with the largest data point yet.
- **Gap.** The wiki has tracked US export controls on chips; this is the first entry on China controlling *model and agent* exports. It interacts with the distillation fight ([WM-Basin](../inference-efficiency/2026-10-30-watermark-basins-distillation-detection.md)): weights flowing out of China become licensable while outputs flowing in from US labs are the contested input.

## Related

[Compute economics](compute-economics.md) · [Memory hierarchy](memory-hierarchy.md)
