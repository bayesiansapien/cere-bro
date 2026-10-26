# How to Build Financial Agents That Work Across the Web (Jay Sahnan & Arik Bird, Browserbase)

**Channel:** AI Engineer
**Published:** 2026-10-25
**Source:** https://www.youtube.com/watch?v=DZ24Xbm9Joc

## TL;DR
Much financial data (receipts, vendor payment portals, Secretary of State KYC records) lives behind logins and anti-bot defenses with no API or MCP, so agents need a real browser. Browserbase's pitch rests on three fintech cases: **Ramp** (scale/access: receipt fetching after each card swipe, 30k+ manual hours saved, 5x scale), **Bill** (control: one agent across thousands of differently-shaped payment portals), and **Stripe** (KYC lookups). The tech: a forked Chromium for data-center use, plus Stagehand, an open-source Playwright superset with natural-language `act`/`observe`/`extract` primitives that compresses a page from ~122k tokens of raw HTML to ~4k tokens of accessibility tree.

## Key Takeaways
- **Why headless Chromium in a data center gets blocked:** fresh fingerprint and cookies on every launch, data-center IP reputation, `navigator.webdriver=true`, "HeadlessChrome" identity. Proxies fix IP but not fingerprint.
- **Their fork:** removes the automation flag, aligns identity to regular Chrome, keeps the browser process alive between tasks (closing windows, not the process). Upstream Chromium ships every ~2 weeks, so maintaining the fork is the moat.
- **Playwright breaks on UI drift** (moved buttons, renamed fields). Stagehand mixes deterministic `page.click` with LLM-resolved actions.
- **Token compression:** DOM → accessibility tree reduces ~122k to ~4k tokens (~30x) and returns direct selectors, cutting cost and latency.
- **Co-location:** Stagehand runs as a Chrome extension inside the hosted browser, removing agent ↔ browser round trips.
- **`extract` into Zod schemas** turns messy pages into typed data. Demo: one script pulled website, IR page, SEC filing, and NYSE listing for 20 companies in parallel.

## Architecture & Optimization Mechanics
- **Context compression as a first-class optimization.** HTML → a11y tree is lossy, task-aware pruning of the input, conceptually like token pruning or KV eviction (drop what the model will not attend to). 30x fewer tokens means proportionally less prefill compute, and it lets small models handle the click-target selection.
- **Routing opportunity:** the deterministic-first, LLM-on-fallback design (`page.click` when the selector works, `act` when it fails) is a cascade router. Cache resolved selectors so the LLM is invoked only on drift. That is the cheapest-model-first pattern applied to UI automation.
- **Co-location = reduced network hops,** the same principle as placing the router next to the inference server.
- Weak spot: "remove the automation flag and claim to be Chrome" is anti-bot evasion. It works until sites tighten detection, and it raises ToS and legal exposure, especially for financial portals. The durable path is signed agent identity.

## Grounded Context (Web Enrichment)
Browserbase reported 35M+ browser sessions per month in June 2026, with Ramp, Shopify, and Lovable named as customers. The specific "30,000 hours" Ramp figure was not independently found and is a vendor claim. Stagehand v4 (Aug 2026) re-architected Stagehand as an extension running inside remote browsers, matching the co-location claim, with vendor benchmarks of ~2x faster than Playwright and ~80% more token-efficient.

Notably, Browserbase also offers **Web Bot Auth** through Cloudflare's Signed Agents program: cryptographically identified sessions that site owners can explicitly allow. That is the opposite philosophy of the stealth fork shown in the talk. Industry direction (Cloudflare, Akamai) is toward verified, declared agents rather than human impersonation, so the "verified browser" stealth approach is likely to have a shrinking shelf life for well-defended sites.

## Real-World Application / Actionable Step
- For any agent that reads web pages, preprocess to an **accessibility tree or simplified DOM** before the LLM. It is a 10 to 30x token reduction with little quality loss, and it makes small or quantized models viable for navigation.
- Use Stagehand `extract` + schema to build a personal **filings/IR scraper** for portfolio companies, run on a schedule rather than manually checking IR pages.
- In routing research, test a **cascade: deterministic → small model → large model** on UI tasks, with a selector cache. Measure LLM-call rate after warmup as the key cost metric.
- Prefer signed-agent identity over stealth for anything touching financial accounts.
