# The Investor's Edge Lives in Their Head (Anekha Sokhal, Moshi)

**Channel:** AI Engineer
**Published:** 2026-10-20
**Source:** https://www.youtube.com/watch?v=UHbODjuviAU
**Domains:** ai-tech (primary), finance (secondary)

## TL;DR
A former J.P. Morgan derivatives trader turned ML engineer (Fulbright, ICLR paper with NASA) argues that when every fund has the same models, prompts, MCP connectors, and skills files, "edge" is the one thing you cannot download: the decades of pattern-matching in a trader's head. Her product, Moshi, is a six-agent deterministic pipeline that does the grind (watching 2.4B data points, reading PDFs and emails, cross-checking sources, scoring hallucination and traceability) and pushes context to the human, who keeps the decision. Thesis: feed the 20-watt brain, do not replace it. The talk is a product pitch wrapped in a defensible philosophy.

## Key Takeaways
- **Data vs attention paradox:** 175 zettabytes created in 2025; attention is flat. More data does not mean more information; it means everyone gets the same flood. For people paid on synthesis, the gap widens.
- **The human brain runs on ~20W, 86B neurons.** The systems trying to imitate a sliver of it need a power plant. So the question is where in the decision loop you point the machine, not whether it replaces the human.
- **Edge = three things:** know what is happening before others, know your blind spots (second- and third-order effects), have conviction to size up.
- **Everyone has the same tools now,** so skills files, MCPs, prompts, and models are not edge. What is left is tacit knowledge, and it walks out the door when the trader leaves.
- **Two kinds of tools:** pull (you prompt a frozen model and you are the context; it tells you to go to bed when it is 3pm Wednesday) and push (data floods you; a data-engineering problem). Different failure modes.
- **The quiet cost of one-person pods:** the apprenticeship model (sit next to a senior trader, one ear on the desk) breaks if everyone runs their own agent swarm. Nobody is pricing the lost next generation of context.
- **Accountability constraint:** in finance the other side of the trade is a client, a cargo, or a company. A human must stand up and say "I made this decision because X." An agent that leaks an API key says "oops, rotate it." Errors in agents compound; you cannot hand the loop to them.
- **Split the work:** grind (reading, gathering, cleaning, cross-checking, watching) to machines; judgment (the decision) to humans.
- **Moshi specifics:** six agents built "in a deterministic manner," 2.4B data points and growing, ~300 new facts learned in the four seconds it takes to read the slide, each claim scored for hallucination and traceability, assumptions surfaced to the user. Claimed up to 35% efficiency gain. Pilots with large trading firms; first public opening.
- **Weekend dashboard to infrastructure:** the moment you share your weekend tool with one more person you need security, storage, reliability, and a credits budget. Pricing has moved from per-tool to per-API-call.

## Architecture & Optimization Mechanics
- **"Deterministic" multi-agent pipelines are a routing and caching story.** Six agents with fixed roles and fixed handoffs means you can precompute which model tier each stage needs. Ingestion and dedup do not need a frontier model; claim scoring and traceability might. Sokhal does not disclose the model mix, but a push-architecture that "learns 300 things in four seconds" is only economical if most of those facts flow through small models and only contested ones escalate.
- **Hallucination and traceability scoring per claim is a verifier layer,** the same pattern as Kormos's "the loop is only as trustworthy as the check" (Coinbase unsupervised-agents page) and Al Chen's second-judge design (Cisco banks page). The cost question is identical: what does it cost to score every claim, and can the scorer be a cheap model calibrated against a human-labeled slice?
- **Push beats pull on token efficiency.** A pull model re-sends the user's context every query; a push model indexes once and sends deltas. For a 24/7 market-watching workload, the KV-cache and retrieval-index economics strongly favor push.
- **The 20W comparison is rhetorically effective and technically misleading.** Brains are efficient at what they do, but the relevant comparison for an inference engineer is energy per useful decision under a latency budget, and a human cannot read 2.4B data points. Her own product concedes this. The honest version of her thesis is "humans are the efficient component for judgment under ambiguity," which is a routing claim: the human is the expensive, high-quality fallback.

## Grounded Context (Web Enrichment)
Sokhal's background checks out against her speaker profile (CEO and ML engineer at Moshi, former derivatives trader at J.P. Morgan, Fulbright at Rice). PitchBook lists a Moshi founded in 2025 in Houston, venture-backed by Mercury Fund, described as an attention-optimization platform for real-time trading insights for institutional traders. No funding amounts or customer names are public, and the "2.4B data points," "35% efficiency," and "biggest players in trading" claims are unverified vendor statements. Do not confuse this Moshi with Kyutai's open-source voice model of the same name.

The broader claim that "everyone has the same models" is weaker than she states. Firms with proprietary data, custom fine-tunes, and co-located inference do have model-level edge; what has commoditized is the general-purpose chat layer. Her stronger point survives: in a world of near-identical LLM access, the differentiator is the curated, verified context pipeline feeding the model and the human, which is exactly what she is selling. The "lost apprenticeship" concern is echoed in recent coverage of junior-analyst hiring cuts at banks, though the long-run effect is unmeasured.

## Real-World Application / Actionable Step
- **Build your own push pipeline for the one domain where you make decisions** (for Amit, likely personal investments). A small set of fixed agents that ingest filings, macro data, and news, dedupe, score each claim for source and confidence, and surface only deltas. The point is to feed judgment, not replace it. This is a weekend project that becomes infrastructure, which is her warning as much as her pitch.
- **Instrument claim-level verification with a cheap model.** Whatever scorer you use for hallucination/traceability, benchmark a small quantized model against a frontier model on 100 labeled claims. If agreement is high, the whole pipeline runs at a fraction of the cost.
- **Do not hand the final decision to the agent.** In any system where you are the one accountable for the outcome, keep the human at the decision node and let the machines own the grind. That is the same design Kormos lands on from the compliance side.
