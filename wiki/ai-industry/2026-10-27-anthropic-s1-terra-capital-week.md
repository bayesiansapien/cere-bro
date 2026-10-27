# Anthropic's S-1, GPT-6.1 Terra, and a quarter-trillion-dollar capital week

**Date:** 2026-10-27 (covers US Monday 2026-10-26) · **Sources:** [Anthropic S-1 announcement](https://www.anthropic.com/news/s1-sec) · [S-1 on EDGAR](https://www.sec.gov/Archives/edgar/data/2130357/000162828026067168/anthropicpbc-sx1.htm) · AI Breakfast (Gmail) · [The Information](https://www.theinformation.com/articles/anthropic-spacex-meta-cash-grabs) · [The Decoder](https://the-decoder.com/anthropic-opens-its-books-for-wall-street-showing-record-revenue-and-mounting-obligations/) · [Marcus on AI](https://garymarcus.substack.com/p/what-anthropic-left-out-of-their) · [OpenAI: GPT-6.1 Terra](https://openai.com/index/introducing-gpt-6-1-terra) · [Simon Willison](https://simonwillison.net/) · [Import AI 478](https://importai.substack.com/p/import-ai-478-math-for-alignment)
**Raw:** `raw/gmail/2026-10-27-newsletters.md` (private), `raw/rss/2026-10-2[67]-*.md`, `raw/labs/2026-10-2[67]-*.md`, `raw/twitter/feed/`

## TL;DR

On one US Monday, Anthropic, Meta and SpaceX unveiled plans that together could raise almost a quarter of a trillion dollars, and OpenAI cut the price of its mid-tier model in half. The S-1 is the first audited look inside a frontier lab: revenue $41M (2023), $386M (2024), $4.6B (2025), **$16.3B in H1 2026**. The $80.7B H1 net loss is almost all a $72.4B non-cash charge on convertible notes and SAFEs; GAAP operating loss is $693M and adjusted operating income $1.6B (10% margin). It spent **$8.9B on compute in the half**, holds $131.7B in cash and short-term investments, counts ~250 customers paying $10M+ a year, and about a fifth of revenue comes from two customers. It plans more than $450B of cloud spending ahead; The Decoder puts long-term compute commitments near $800B.

## Anthropic S-1: the numbers that matter for compute economics

- **Revenue per compute dollar:** H1 revenue $16.3B against $8.9B compute is ~1.8x. Feed accounts report ~$2.08 revenue per $1 of compute in the latest quarter vs $0.40 in Q1 2025 (secondhand, not checked line by line).
- **Commitments:** ~$121B with SpaceX (monthly payments reaching ~$3B, roughly 0.7 GW at SpaceX pricing) and ~$115B of Google TPUs through 2033 (feed reports). Nscale and Anthropic are reportedly near a second $45B deal.
- **Payment processing** costs rose $222M year over year (The Information).
- **Control:** a Founder LLC of the seven co-founders holds one Class F share with 50.1% of the vote; the Long-Term Benefit Trust's Class T share elects a board majority; Amazon and other strategics get non-voting Class N; public buyers get Class A. Nasdaq "ANT", Goldman Sachs lead-left, Morgan Stanley stabilization agent, 22 banks. Target debut the week of Nov 16 at a reported $1.5-2T valuation; raise could reach $100B (Reuters).
- **Risk factors:** models "may behave in misaligned or autonomous ways"; an export-control directive forced it to cut Fable 5 and Mythos 5 off for foreign nationals; ongoing suit over the Pentagon's supply-chain-risk designation. The founders pledge to keep Claude ad-free.
- **Counter-read (Gary Marcus):** the draft omits Q3, the quarter after the "tokenmaxxing" peak and the shift to cheaper alternative models. He names Nov 11 as the date a Q3 update is due. OpenRouter data shows Anthropic's 7-day token average up ~3.5x since Sep 22 to ~2.25T/day, but Marcus notes token prices hit a record low the same week.

## GPT-6.1 Terra: the mid-tier halves

- $1 per million input tokens and $5 per million output, about half of GPT-5.6 Terra and GPT-6.1 Sol and ~10x GPT-6 Luna (Simon Willison).
- OpenAI: matches GPT-6 Astra on Agents' Last Exam at one-tenth the price per token, finishes tasks over 3x faster than Astra and GPT-6.1 Sol. Emphasis is visual reasoning and computer use. GA in GitHub Copilot the same day; in Arena's Agent Arena.
- OpenAI's Ted Sanders: better than Astra and Sol at technical communication, similar on vision and computer use but much faster, a bit worse on most else.

## Funding, valuations and compute deals

- **Meta** plans up to $95B of equity sales; the first $35B is $22.5B common stock and $12.5B mandatory convertible preferred, after its first negative free-cash-flow quarter in over a decade. NVIDIA, AMD and Broadcom reportedly may invest up to $5B combined.
- **SpaceX** signed a binding ~$40B commitment to lease NVIDIA Vera Rubin GPUs from an Apollo-managed vehicle that buys them with private bonds (largest GPU financing ever, off balance sheet per The Information), deliveries from early 2027. Musk: debt markets have shut for AI-only neoclouds; "200+ neoclouds are going to see guppy-level death and consolidation".
- **Apollo's chief economist** Torsten Slok: AI has delivered "zero financial payoff to corporate America outside of tech".
- **Intel** reportedly acquiring quantum-software startup Classiq for ~$2.3B.
- **DoorDash** in advanced talks to buy Instacart for ~$17B.
- **Microsoft** offers voluntary buyouts to ~60,000 employees (27% of staff) to cut costs amid AI spending.
- **Daytona** raised $60M at a $1B valuation for agent cloud infrastructure; **Paradev** (ex-Superset, YC) raised an $11.5M seed for a multi-agent code editor.
- **Toyota** commits ~$6.4B a year to humanoid robots and factory automation; **Rivian** acquired Third Dimension AI; **Jane Street and Hudson River Trading** race for compute and back chip startups.
- **SambaNova** (first close of $1B at $11B, per its site) now serves MiniMax M3.1 Flash at 200+ tok/s, ~3x faster and 70% cheaper than the predecessor.
- **Wafer** reports 1 trillion tokens a day on OpenRouter; **You.com** launched an Inference Router for open-weight models (99.9% SLA, zero data retention, "up to 75% lower" cost).

## Other items

- **Mirendil-Base** (Import AI 478): one researcher pretrained a 100B-500B model in 3.5 months on under $10M of compute, beating Nemotron-550B-Base, GLM-5.3 and DeepSeek-V4-Pro-Base but not Kimi K3. **Resolution** autoformalized resolution of singularities in about a week for ~$135K of tokens (100B input, 90% cache reads; ~600K lines of Lean).
- **Nanbeige 4.3 33B** (BOSS Zhipin's lab), Apache 2.0, 524K context, beats Qwen 27B on most agentic benchmarks.
- **Sweden's Government Offices** block ChatGPT and Claude on staff machines, leaving Copilot; **r/opensource** bans AI projects; **Stripe** leads agent payments via one-time virtual cards, worrying Visa and Mastercard; **Cathedral** (ex-DOGE founders) says its agents accessed Anthropic internal systems.
- **Hyperscaler earnings:** Alphabet and Microsoft Wednesday, Amazon Thursday, with $800B+ of capex under scrutiny.

## Relation to prior wiki

- **Resolves** the 10-22 and 10-26 S-1 watch items (compute payments, customer concentration): concentration is ~20% in two customers; compute is $8.9B per half against $450B+ planned.
- **Confirms** the [compute-economics](../hardware/compute-economics.md) squeeze recorded 10-26: token prices fall (Terra, OpenAI's 90% discounts) while GPU rents rise and credit closes for neoclouds. Capital is flowing only to balance sheets that do something besides rent compute.
- Concept page: [compute-economics](../hardware/compute-economics.md).
