# Why No One Agrees on What Their AI Tokens Cost (Pratyusha Duvvuri, Cisco)

**Channel:** AI Engineer
**Published:** 2026-11-09
**Source:** https://www.youtube.com/watch?v=KdG9OSOtJOA

## TL;DR
After surveying about 100 companies, Cisco (via Galileo, acquired by Splunk, acquired by Cisco) found no shared definition of "tokenomics." Their working definition: observability and interpretability of token usage and cost. The hard problems are not metering but attribution: mapping spend across multiple providers with custom negotiated pricing onto both the HR org chart and a separate finance hierarchy (OPEX/COGS), handling provider reconciliation that rewrites past bills, and forecasting volatile spend. The talk is largely a product demo; the useful content is the problem decomposition.

## Key Takeaways
- **Industry mood shift:** from "token maxing" as status (Jensen Huang: a $500k engineer not spending about $250k on tokens is alarming) to efficiency (Ramp burned $1.5M in tokens in one week).
- **Model choice is context-dependent:** internally Cisco kept a cheap Luna model at 96% eval accuracy instead of a frontier model at 99%; for customer-facing flows they would pay for the 3 points.
- **Pricing is bespoke:** enterprises have custom per-credit rates, free tiers up to a threshold, then step pricing. List price is not your price.
- **Three personas:** engineers (which model, am I over budget), engineering managers (team-level adoption vs. KPIs vs. cost), finance (budgets, alerts, ROI to the board).
- **Provider dashboards fail** because spend is fragmented across OpenAI, Anthropic, Copilot and others, and they serve only the engineer persona.
- **Reconciliation:** providers revise bills after the fact (billed $100k, later $120k). Any cost system must handle mutable history.
- **Inputs required:** HR hierarchy as a minimal CSV (customers will not share more), provider API keys/org IDs for daily pulls, finance hierarchy.
- **Product views:** cost and adoption dashboards, org-tree rollups to CEO, consumption by job family (one customer found sales outspending engineering), cost by model and reasoning effort, RBAC. Forecasting and ROI attribution to business outcomes are upcoming. Built to GA in 10 weeks.

## Architecture & Optimization Mechanics
- Cost per reasoning-effort level (low/medium/high) as a first-class dimension is the most relevant signal for routing: effort selection is itself a routing decision, often with larger cost variance than model choice.
- The 96% vs. 99% anecdote is a clean case for quality-aware routing: the optimal model depends on the cost of an error in that context, not on a global leaderboard. A router needs a per-use-case error-cost parameter.
- Attribution requires joining provider usage (daily granularity, mutable) with slowly changing org dimensions. That is a classic SCD (slowly changing dimension) data problem, not an AI problem.
- Missing from the talk: per-request quality attribution. Without linking spend to task outcome, "ROI" stays a spreadsheet exercise.

## Grounded Context (Web Enrichment)
The Ramp anecdote is real and has a sequel. Eric Glyman disclosed in an October 13, 2026 post that Ramp burned $1.5M in tokens in one week in May, and launched Glass, its internal AI workspace, as a product in response. Glyman claims the bill fell 30% overnight after moving work to Router, Ramp's model-routing layer. That figure is self-reported with no baseline or like-for-like comparison, and has not been independently measured at other companies. It coincided with Ramp's $750M raise at a $44B valuation, pitched around AI token spend as a third pillar of corporate spend after people and vendors.

The takeaway: token cost management is now a funded product category (Ramp, Cisco/Splunk, plus FinOps vendors), and routing is being marketed as the primary savings lever. The Cisco product addresses visibility and attribution; it does not itself reduce spend. The talk offers no data on whether visibility changes behavior.

## Real-World Application / Actionable Step
- Routing research angle: the enterprise buyer now has per-team, per-model, per-effort cost data but no per-request quality signal. A router that emits cost and quality-confidence per decision would plug directly into these dashboards. Consider that as the output contract for your routing work.
- Treat reasoning effort as a routing dimension alongside model choice in your next routing experiment; report cost-quality curves over (model, effort) pairs, not models alone.
- Be skeptical of headline routing savings like Ramp's 30%; when citing or benchmarking, require a fixed task mix and quality floor.
