---
date: 2026-10-17
type: source-summary
topic: llms-foundation-models
sources:
  - raw/gmail/2026-10-17-newsletters.md
  - raw/labs/2026-10-17-035202-labs.md
  - raw/twitter/feed/2026-10-17-morning-ranked.json
---

# MAI-Base-2, Reflection Beam, Elorian Glimpse: three models, three cost stories

**TL;DR.** Three model announcements in the window, each mostly a cost claim.

- **Microsoft MAI-Base-2** ([pre-training report](https://microsoft.ai/news/frontier-pre-training-at-microsoft-ai/), via AI Breakfast): MoE with 2.8T total / 80B active, MoE in every layer, 50T-token mix (vision-language 4.5T unique tokens, 18% of the mix), March 2026 web cutoff. Trained on 16,000 GB200 GPUs for 38 days at 21% average MFU (model FLOPs utilization) and 89% goodput. Microsoft claims 4.2-12.3x better pre-training FLOP efficiency than DeepSeek-V4-Pro-Base and lower bits-per-byte than every open model it tested. The efficiency figures are scaling-law-fit estimates, not direct measurements. Still in post-training; weights go to trusted Foundry partners only. Pairs with Maia 300 (40% more tokens per watt claimed, production 2027).
- **Reflection AI Beam 1.0** ([AWS post](https://aws.amazon.com/blogs/machine-learning/introducing-reflection-beam-an-open-weight-model-for-agentic-coding-on-aws/)): open-weight (Apache-2.0) sparse MoE for agentic coding, 501B total / 23B active, 1M effective context, BF16 / FP8 / NVFP4 checkpoints. FP8 runs on p5 (H100) or p5e/p5en (H200); NVFP4 on p6-b200. Debuted at #13 overall in Agent Arena (#6 among US labs). NVIDIA reported serving throughput rising from 70K to ~90K tokens/s within hours of launch.
- **Elorian Glimpse** ([blog](https://elorian.ai/blog/introducing-glimpse)): a "visual thinking" model from a small team with a few hundred GPUs, post-trained on an open-weight base. It can run recurrent computation over latent visual representations instead of only text chain-of-thought, re-inspect images and video while reasoning, and spawn subagents that exchange internal visual states. Claimed to match or beat GPT-6 Astra on 5 of 12 benchmarks at 17x lower token prices.

## Relation to prior wiki pages

- **MFU baseline for the compute-economics page.** 21% MFU at 16K GB200s is a rare public number for a frontier MoE run. It means roughly four of every five peak FLOPs went unused on a fleet-scale MoE run, a useful anchor for any claim about compute per token. See [compute-economics](../hardware/compute-economics.md).
- **Open-weight MoE density keeps falling.** Muse Spark Open (10-16) is 816B/42B active (5.1%); Beam is 501B/23B (4.6%); MAI-Base-2 is 2.8T/80B (2.9%). Lower active fraction means more memory per useful FLOP, which is why every release now ships NVFP4.
- **Glimpse's latent visual recurrence** is the multimodal cousin of looped models ([looped-transformers](looped-transformers.md)) and Dory (today): spend compute in latent space, not in output tokens.

## Gaps

- MAI-Base-2: no evals in text, efficiency is fitted, no release.
- Beam: no independent long-context eval yet.
- Glimpse: vendor benchmarks only; the "17x cheaper" compares list prices, not cost per solved task.

Concept pages: [scaling-laws](scaling-laws.md), [compute-economics](../hardware/compute-economics.md).
