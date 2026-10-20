# Why AI Agents Still Won't Pay for Anything | Jan Curn, Apify

**Channel:** AI Engineer
**Published:** 2026-10-18
**Source:** https://www.youtube.com/watch?v=-AOxpwVeIWw

*Conference talk. Apify runs a marketplace of ~80,000 web-automation "actors" and paid creators almost $2M last month. Secondary domain: finance.*

## TL;DR
More than a dozen agent payment protocols launched in 18 months (Coinbase x402, Stripe/Tempo MPP, Google AP2 and UCP, OpenAI/Stripe ACP, Visa TAP, Mastercard Agent Pay, Alipay, UnionPay, OKX), yet real usage is near zero: about $1M per month on x402 and roughly $1.5K on MPP. Supply is not the problem; Apify, Exa and Perplexity together earn far more than that from agents, just via API keys bought by humans. Curn models adoption as a funnel (need, setup, discovery, buy) with friction at every step, and expects three unlocks: always-on personal agents with budgets, the end of subsidized flat-rate tokens (so buying beats rebuilding), and native wallets in Claude/ChatGPT plus curated directories for trust. Pay-per-use only became workable this year via x402 batch settlement and MPP sessions.

## Key Takeaways
- **Real competitor is the API key, not Visa.** Pre-provisioned keys plus a credit card are simpler than autonomous discovery and payment.
- **Why crypto fits:** micro-transactions are uneconomic on cards, and chargebacks are fatal when infinite agents can abuse a service. Stablecoin rails have optional, merchant-controlled refunds only.
- **Need:** better models earn trust step by step ($5, then $50, then $500 per job). Losing $50 is less bad than an agent leaking your email.
- **Token subsidy argument:** a $100/month Claude plan can buy about $14,000 of tokens at list price if maxed out, so agents have no incentive to buy a service instead of building it. When subsidies end (he points to OpenAI and Anthropic IPOs), buy-versus-build flips.
- **Setup:** crypto wallets are still opaque to most people. Fix is native budgets inside major agent platforms.
- **Discovery and trust:** agents need the equivalent of marketplaces and referrals. Curated connector directories (Claude's, OpenAI apps, Apify Store) are the trust layer.
- **Buy:** fixed price per call is not enough. x402 "exact" (fixed), then "upto" (variable, but allowed double-spending before settlement), so Apify used exact-plus-refund (needs buyer trust in seller), now batch settlement (on-chain escrow, cheap micro-charges against it).
- **x402 flow:** request, HTTP 402 with payment-required header, signed payment, facilitator (e.g. Coinbase) verifies, work, settle on-chain. Do the work after settlement if cost is non-trivial.

## Architecture & Optimization Mechanics
- **Payment as a routing signal.** Once agents pay per call, tool selection becomes a cost-aware routing problem: build with tokens vs buy a service vs call a cheaper equivalent. That is LLM routing generalized to tools.
- **Escrow plus micro-settlement** mirrors the lease-and-meter pattern of GPU billing: reserve budget, draw it down per unit, release the rest.
- **Trust via curated registries** is the same pattern as model registries: provenance plus review reduces the need for per-call verification.

## Grounded Context (Web Enrichment)
Independent data backs the "nobody is paying" thesis and suggests even the headline numbers are inflated. x402 passed 200 million transactions by mid-2026, but Artemis Analytics estimates over 95% is protocol testing, not buyer-seller activity, and its wash-trading filter cut one 30-day window to about $1.6M (Allium estimated about $3M; Visa about $19M for a broader window). Real daily volume was near $28K in March, weekly transactions peaked in November 2025, and Coinbase's head of AI product admitted 25 to 30% of transactions may come from leaderboard farming ([Yahoo Finance](https://finance.yahoo.com/markets/crypto/articles/x402-foundation-activated-27-old-152440828.html), [Startup Fortune](https://startupfortune.com/ai-agents-have-moved-over-200-million-payments-on-x402-but-half-may-be-fake/), [Artemis](https://x.com/artemis/status/2031768320081277029), [MEXC](https://www.mexc.com/news/901995), [Chainalysis](https://www.chainalysis.com/blog/x402-agentic-payments-adoption/)). The official x402.org 30-day counter reportedly has not changed since March ([Daniel McGlynn](https://www.danielmcglynn.com/the-x402-counter-has-shown-the-same-four-numbers-since-march/)).

The Gartner figure he cites (about $15T and 80% of B2B activity by 2028) refers to B2B spend intermediated by AI agents, not to agent-native crypto payments; most of that flow will run on existing invoicing and card rails. His crypto-wins thesis is the weakest link. Card networks are building their own agent rails (Visa TAP, Mastercard Agent Pay), and the Claude/ChatGPT "native budget" unlock he wants is more likely to be fiat credits than stablecoins.

## Real-World Application / Actionable Step
- **For routing research:** add "buy a tool call" as an action in your router's action space with an explicit price. Measure when calling an external paid API (search, extraction) beats spending reasoning tokens. This is the buy-vs-build decision Curn says subsidies currently hide.
- **Token economics:** price your agent workloads at API list rates, not subscription rates. If a workload only works because of a flat-rate subscription, it is not production economics.
- **Investing:** treat agent-payment crypto tokens and "agent economy" narratives as pre-revenue. The payable volume today is in the low millions per month. Exposure to this theme is better taken through payment networks (Visa, Mastercard) and Stripe-adjacent public plays, which own both rails.
- Revisit in 6 months: watch filtered x402 volume (Artemis) and whether Anthropic or OpenAI ships native agent wallets.
