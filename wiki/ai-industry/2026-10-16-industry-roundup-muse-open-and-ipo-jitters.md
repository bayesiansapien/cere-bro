# Industry roundup 2026-10-16: open weights from Meta, IPO jitters, and the cost of tokens inside companies

**Date:** 2026-10-16 · **Sources:** The Decoder, The Information, Simon Willison, Algorithmic Bridge, Pragmatic Engineer, AI Weekly Espresso, SemiAnalysis, AI lab watcher, X following feed
**Raw:** `raw/rss/2026-10-1[56]-*.md`, `raw/gmail/2026-10-16-newsletters.md`, `raw/labs/2026-10-16-*.md`, `raw/twitter/feed/2026-10-1[56]-*-ranked.json`

## Models and products

- **Meta Muse Spark Open**: 816B-A42B open weights, 1M context, Meta-made NVFP4, Apple MLX tie-up ([page](../llms-foundation-models/2026-10-16-muse-spark-open-and-nemotron-35.md)).
- **NVIDIA Nemotron 3.5 Super VL (120B-A12B) and Bolt 74B-A9B in 24GB** ([page](../llms-foundation-models/2026-10-16-muse-spark-open-and-nemotron-35.md)); Nemotron 3.5 Rerank 8B on HF.
- **Black Forest Labs FLUX 3 Image Klein**: 5.6B open-weight image model, native 4K, 8GB VRAM, NVFP4 variant ([The Decoder](https://the-decoder.com/black-forest-labs-open-weights-image-model-flux-3-image-klein-runs-on-consumer-gpus-with-just-8-gb-of-vram/)).
- **Xiaomi MiMo V2.6 Pro** takes #1 among open models in Agent Arena (+3.8%, $0.11/task); Pro and Flash ($0.05/task) are the only open models on the cost frontier.
- **Gemini 4 Argon**: ARC-AGI-3 97.5% at $4.8K with a provider harness vs 49.8% with the standard one (ARC Prize repost); robotics demos still need heavy prompting ([The Decoder](https://the-decoder.com/google-wants-gemini-4-argon-to-be-the-only-ai-model-robots-need/)).
- **GPT-6-Astra** solves 49 of 50 unpublished theoretical-physics problems at ~$2.40 each on TheoPhysEval; experts' references were wrong in some "failures" ([The Decoder](https://the-decoder.com/gpt-6-astra-solves-49-of-50-physics-research-problems-at-2-40-apiece/)).
- **OpenAI**: GPT-Live-1.1 voices; GPT-Rosalind to academic labs; Sullivan & Cromwell legal deployment.
- **IBM Granite Switch 4.1** (8B, 30B): chat, decision aLoRA and speech from one endpoint ([HF blog](https://huggingface.co/blog/ibm-granite/granite-switch-4-1)). **Mistral Timestral** time-series family (5M-209M).
- **Microsoft Research Magnetar**: proof-based general-purpose computing.
- **pwn.ai + SingularityNET's Omega agent** report a Linux kernel flaw reachable from a KVM-hosted sandbox via virtual networking (vendor claim).

## Money and companies

- **Anthropic Q3**: $4.8B Q1, $11.5B Q2, $16.8B Q3; $1.70 revenue per $1 compute; 11% adjusted operating margin; distillation by rival labs was 5-7% of revenue before a Q3 clampdown ([Simon Willison on FT](https://simonwillison.net/2026/Oct/15/anthropic-tells-investors/)). Some investors now expect an IPO valuation below $1.5T ([The Decoder](https://the-decoder.com/anthropics-q3-revenue-hits-16-8b-but-growth-slows-ahead-of-planned-november-ipo/)); The Information asks whether it missed its peak IPO window ([link](https://www.theinformation.com/articles/anthropic-miss-peak-ipo-moment)).
- **Mueon raises $65M** for rack layouts claiming up to 10x compute per unit power ([The Information](https://www.theinformation.com/briefings/exclusive-mueon-raises-65-million-rework-data-centers-put-together)).
- **Private vs public split**: Morgan Stanley's private-tech conference stayed ebullient (inference and defense hot, Fireworks AI's growth cited) while Firmus pulled its IPO ([The Information](https://www.theinformation.com/articles/party-still-going-strong-private-tech)).
- **CoreWeave and Broadcom object** to OKX/ICE tokenized trading of their shares.
- **OpenAI ads**: ~140 ad staff, nearly half hired July-September, Meta the top source, rates cut ([The Information](https://www.theinformation.com/articles/openais-accelerates-ad-sprint-meta-hires-slashed-prices)).
- **Cognition** rations AI usage per engineer by measured efficiency (human-hour equivalent per dollar) ([The Information](https://www.theinformation.com/articles/cognitions-plan-limit-tokenmaxxing-efficient-engineers)).
- **Cursor** staff investigated whether confidential test data reached SpaceX's AI unit during Grok Bot development ([The Information](https://www.theinformation.com/articles/cursor-staff-investigated-whether-confidential-data-reached-spacex-ai-training)).
- **Bank of America** has 4,000 people (1,000 contractors) fixing vulnerabilities found by Mythos and other models ([The Decoder](https://the-decoder.com/bank-of-america-puts-4000-people-on-fixing-vulnerabilities-uncovered-by-anthropics-mythos-and-other-ai-models/)).
- **Nvidia**: software licensing at roughly a couple thousand dollars per GPU per year (Jensen on Bg2); content per 1GW site up from ~$18B to $40B+; Volvo partnership expanded.
- **Pragmatic Engineer**: Anthropic built "Scion" to replace Git at 30,000 PRs/day; Meta and Google add AI-assisted coding interview rounds; Netflix cut 6%; a16z disbanded recruiting; internal "Lovables" (Ramp Glass, Stripe Harbor) ([Pulse](https://newsletter.pragmaticengineer.com/p/the-pulse-new-trend-of-building-internal-aeb)).

## Essays

- **Algorithmic Bridge, "You Have No Idea How Close the AI Bubble Is to Popping"**: Anthropic's 46% QoQ is extraordinary yet reads as a sigmoid against a 145% prior quarter; with the AI trade resting on its IPO, naive extrapolation misses the $100B run-rate target ([post](https://www.thealgorithmicbridge.com/p/you-have-no-idea-how-close-the-ai)).
- **SemiAnalysis on ASML hybrid bonding** ([page](../hardware/2026-10-16-asml-hybrid-bonding-tool.md)).
