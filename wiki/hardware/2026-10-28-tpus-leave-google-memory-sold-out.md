# TPUs leave Google; memory is sold out to 2028

**TL;DR.** In one day, Google's TPU went from an in-house chip to a merchant product. **Oracle** will be the first hyperscaler outside Google to offer TPUs from its own data centers, deploying from calendar 2027 (Oracle supplies power, cooling and networking; Google claims 12.6 PFLOPS FP4 per 8th-gen chip, >97% productive time on large training runs, up to 80% better performance per dollar for low-latency serving, and a TorchTPU stack that runs PyTorch, vLLM and SGLang without rewrites). **OpenAI**, long Nvidia's marquee customer, plans to buy TPUs (The Information, Bloomberg); its chip lead Richard Ho previously worked on TPUs. **Anthropic's S-1** quantifies the demand: $114.5B planned with Google Cloud, another $125-150B possible on TPUs with Google and others, and $161.2B for TPU compute with Broadcom. On memory, SK hynix reported a record Q3 (86% gross margin, DRAM ASP +28% QoQ, NAND +25%) and says it signed 5-year agreements with 14 customers covering over 50% of 2027-2028 capacity, with memory demand outpacing supply through 2030. Alibaba, Tencent and ByteDance are reportedly seeking 10-year DDR5/LPDDR5 contracts.

## Why it matters
- The serving-cost lever moves from GPU pricing to accelerator choice. Google's 80% perf/$ claim is for low-latency serving, the decode regime where custom silicon competes (Trainium3 note, 10-24).
- Memory, not FLOPs, is the binding input: H200 rents rose 160% vs 40% for H100 (10-24), and SK hynix is now pre-selling two years out.
- Onsemi is in talks to buy Ferric (~$1B), after Analog Devices bought Empower ($1.5B, May): power delivery for AI chips is the next consolidation target.

## Relation to prior wiki pages
- [Compute economics](compute-economics.md): 10-27's S-1 entry noted ~$115B of Google TPU commitments; today adds Broadcom's $161.2B and a second and third TPU buyer.
- [Memory hierarchy](memory-hierarchy.md): HBM capacity displacing commodity DRAM is the mechanism behind the 10-year contract push.

Sources: [The Information: TPU moment](../../raw/rss/2026-10-28-the-information-google-is-having-a-tpu-moment.md) · [OpenAI buys TPUs](../../raw/rss/2026-10-27-the-information-openai-a-longtime-nvidia-customer-plans-to-buy-google-s.md) · [Oracle TPU details](https://x.com/rohanpaul_ai/status/2115228163408314757) · [SK hynix Q3](https://x.com/StockSavvyShay/status/2115226231918809337) · [Onsemi/Ferric](../../raw/rss/2026-10-28-the-information-chipmaker-onsemi-in-talks-to-buy-startup-for-about-1-bi.md)
