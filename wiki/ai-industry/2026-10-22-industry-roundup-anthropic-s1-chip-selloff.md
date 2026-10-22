# Industry roundup 2026-10-22: Anthropic's prospectus numbers, the chip selloff, open-weight week, OpenAI on Google Cloud

**Sources:** Gmail newsletters 2026-10-21/22 (AI Breakfast, AI Weekly, Interconnects, SemiAnalysis, Semiconductor Newsletter, Pragmatic Engineer, Gradient Flow; private raw), RSS (The Information, The Decoder, Simon Willison), AI lab watcher (NVIDIA GTC Berlin, Google, IBM, AWS), X feed. Raw: `raw/gmail/2026-10-2[12]-newsletters.md` (private), `raw/rss/2026-10-2*`, `raw/labs/2026-10-2*`.

## Money and compute

- **Anthropic draft IPO prospectus (WSJ):** H1-2026 revenue $16.3B (from $1.1B); Q3 ~$16.8B, +45% QoQ. Net loss $80.7B, ~$72B of it non-cash convertible revaluation; adjusted loss $8.7B. H1 compute ~$9B vs $7.3B for all 2025. Two customers ~20% of revenue. Cloud commitments ~$450B over 7-10 years (Google $111B, AWS $110B, Microsoft $31B), up to $86B Nvidia rentals via Nscale/Lambda, $160B+ Broadcom/Google leases; total over $600B. Public filing could come within days ([WSJ](https://www.wsj.com/tech/ai/anthropic-revenue-growth-ipo-accaf0f1)).
- **SpaceX "SI" segment** (X, Grok, compute cloud leased to Anthropic and others): Q3 revenue $7.56B, ~3x QoQ, now its largest segment; operating profit $431M; new datacenters pay back in under a year ([The Information](https://www.theinformation.com/articles/spacexs-musk-lauds-soaring-cloud-business-possible-tesla-merger)). Musk: ~200K GB300 GPUs online per month through year-end.
- **Chip selloff:** SOX down 8 sessions, ~$2T lost; SK Hynix -6.58%, Micron -5.63% in one day; CoreWeave -25% on the week with debt above $50B. Drivers: 10-year at 5.09%, Brent at $109.86. SOX still +60% YTD.
- **DeepInfra GPU-hour prices up from Nov 9:** A100 $0.89 to $1.49 (+67%), B200 $3.69 to $4.89 (+33%); serverless token prices unchanged ([pricing](https://deepinfra.com/pricing)). Nebius B200 spot reportedly +55% in a day.
- **Deals:** Tenstorrent $1.5B Series E at $6.2B; Eka Robotics $150M Series A at $1.45B (a16z, F-Prime); Reliable Robotics $115M Series D ext. (>$1B); Otter.ai $320M non-dilutive from General Catalyst; Legora $550M Series E at $8.8B; OpenAI acquires Orchestra Bio; Proofpoint (Thoma Bravo) buys Varonis for $6.3B; Salesforce buys Braze (~$5.66B); Teradyne $300M into FormFactor (HBM test); Nvidia in talks to back neocloud Firmus after its pulled IPO ($170B+ total Nvidia neocloud exposure); Nscale IPO investors want $16-19B vs ~$30B target.
- **Meta Q3:** revenue +26% to $64.6B, FCF -$2.12B, 2026 capex $135-145B, new Class C non-voting stock to fund AI capex; Muse agent app 10M users in 6 weeks.

## Hardware and semiconductors

- **NVIDIA GTC Berlin:** Vera Rubin in full production (node assembly <5 min vs 2 h for GB); DSX POD cuts onsite AI-factory setup from ~6 months to 14 days; ~$10B Europe commitment; Nscale DSX MaxLPS fits 37% more GPUs in the same power; $300B+ power equipment backlog and 200+ GW in US interconnect queues ([keynote](https://blogs.nvidia.com/blog/gtc-berlin-2026-keynote/)).
- **Google Cloud A5X (Vera Rubin NVL72)** GA next month, plans for up to 960K Rubin GPUs.
- **Nvidia substrate deals** with Ibiden, Samsung Electro-Mechanics, Unimicron (six suppliers) including a multibillion-dollar capacity reservation.
- **Semiconductor Newsletter wk 42:** TSMC record Q3 $46.72B (2nm 8% of wafer revenue); ASML record €11.7B; Q3 smartphone shipments -20% on memory costs; Siemens+NVIDIA lithography up to 17x faster for High-NA OPC.
- **Groq** reportedly stacking DRAM on its next LPU to escape SRAM's capacity limit; **Micron** custom HBM4E in 2027, 3D-stacked memory on processors in 2028.
- **Google Coral NPU** design complete (RISC-V, 1 TOPS at ~10 mW target), open RTL.

## Models and platforms

- **Open weights:** Reflection Beam-1.0 (501B-A23B, Apache 2.0; ~80% Terminal-Bench 2.1 at ~25K tokens/attempt vs ~80K for GLM-5.2); Xiaomi MiMo-V2.6-Pro-RL (top open model on Artificial Analysis); NVIDIA Nemotron-3.5-Super-VL NVFP4; Cloudflare clef decision model; Meta Muse-Spark-Open-816B-A42B; Recursive Flint 40B MoE (Apache 2.0, built by an automated research loop); Mistral Large 4 weights due end of October.
- **OpenAI models on Google Cloud** (GPT-6 Astra, 6.1 Sol, 6 Luna in private preview): Google becomes the only major cloud with Gemini, Claude and GPT. ChatGPT ads expand to 26 more countries, 100K+ advertisers.
- **TorchTPU** and vLLM/SGLang-TorchTPU: TPU becomes a native PyTorch device; SGLang-TorchTPU in production at Meta; Qwen 3.5 at 2.01 cents per M tokens on Ironwood (InferenceX). **llm-d 1.0**: prefix-aware router captures 97% of cache reuse on agentic coding; 3,000 concurrent self-hosted agents at 5-10x less than buying API.
- **Voice:** Mistral Voxtral 3 stack; ElevenLabs Eleven Realtime (0.57 s to first audio).

## Engineering economics

- **Pragmatic Engineer, ROI of AI spend (27 companies):** spend peaked June-July and has roughly halved on API plans (Opus 5.5 efficiency, open models); a quant shop went from $500K to $8M/month; PR counts often flat where quality is held; almost no one can measure ROI.
- **Gradient Flow, "the model factory":** Thomson Reuters' own model (200B tokens continued pretraining on Qwen) serves 5-10% of CoCounsel inference; final run under $450K, ~$40M program. The durable asset is the data/eval/RL-environment factory, not the checkpoint.

## Relation to the wiki

Continues [10-20 GPU glut or shortage](2026-10-20-industry-roundup-gpu-glut-or-shortage.md): the shortage side gains (DeepInfra price rises, B200 spot jump, AWS taking racks before power), while the glut side gains in markets (SOX selloff, CoreWeave debt, Nscale markdown). See [compute-economics](../hardware/compute-economics.md).
