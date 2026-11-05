# Why Datasite Stopped Building Its Own Parsing (Adit Abraham, Reducto & Raj Bakhru, Datasite)

**Channel:** AI Engineer
**Published:** 2026-11-04
**Source:** https://www.youtube.com/watch?v=0PqGT2L6cZM

## TL;DR
Datasite hosts the virtual data rooms behind roughly 60% of M&A deals over $100M (55,000 rooms a year, billions of pages, 500k+ MAU, over a trillion tokens a year). Its global CTO, Raj Bakhru, explains why Blueflame (his vertical AI startup, acquired by Datasite) abandoned its in-house parsing pipeline for Reducto. Document parsing is an endless tail of edge cases that consumes scarce senior engineers. Moving it to a vendor lifted RAG recall by 22% on an internal benchmark. His core claim: in document-heavy AI, most of the quality is won on extraction, not on the answering model.

## Key Takeaways
- **Parsing is all edge cases.** Real failures: a VLM misreading a pie chart because legend shades of blue nearly matched (the same data as a bar chart was read correctly), merged cells in finance spreadsheets, XLSB and macro-enabled files, templates.
- **Extraction dominates quality.** On VDR Bench, Reducto parsing improved recall by 22%. "Most of the work is on the extraction side. Get that right and everything else follows."
- **Proprietary data near the model is the moat.** Datasite's VDRs plus Grata (about 20M private companies) give Blueflame data no frontier lab or competitor has. Moving data closer to the models cut token cost and runtime and raised quality on their benchmarks.
- **Acquisition rationale:** staying independent meant raising hundreds of millions with heavy dilution while frontier labs moved into financial services verticals. Proprietary data access was the deciding factor.
- **Build vs buy rule:** 250 engineers go to five revenue-generating initiatives; as few as possible work on the layers underneath. Datasite needs about $200M in new revenue a year to grow 20% at roughly $1B top line.
- **Barbell hiring:** AI coding gives the largest leverage to senior engineers with strong codebase mental models and meaningful leverage to juniors (LLMs fill missing docs). The middle gains least.
- **Pipeline:** Reducto runs inside Datasite's Azure environment (data rooms never previously left it), with bursts of up to a terabyte per deal. Output goes to Turbopuffer, then GraphRAG queries executed as Python.
- **VDR Bench:** a common data room of hundreds of documents with a few hundred known-answer questions, rerun on every change. The bar is beating the same files dropped into Claude or ChatGPT Projects. Open-sourcing and a paper with OpenAI are under consideration.
- **Open pain point: agent model routing.** A much cheaper GPT-6.1 Sol spams tool calls where Opus 5.5 does not, blocking migration. Finance users will "pay any amount for the best answer," so quality is fixed and cost and speed are optimized around it.

## Architecture & Optimization Mechanics
- **Data plane:** ingestion, then a parsing service (Reducto, in-tenant), then a vector store (Turbopuffer), then GraphRAG over extracted entities, then agents producing diligence analyses, IC memos and decks.
- **Modality choice is part of parsing.** Rendering choice (chart as image vs structured table) changes VLM accuracy on identical data. Before Reducto, the team hand-tuned which model to use per chart and document type, which is effectively a per-input router. Outsourcing removed that routing problem at the ingestion layer but it persists at the agent layer.
- **Cheap-model failure mode is behavioral, not knowledge-based.** Tool-call spamming by the cheaper model is a harness and policy issue, so it can plausibly be fixed with constraints (tool-call budgets, dedup, stop criteria) rather than by staying on the expensive model.

## Grounded Context (Web Enrichment)
The deal history checks out. Datasite bought Grata in June 2025 and announced the Blueflame acquisition on July 23, 2025 (terms undisclosed), placing it in Datasite's Intelligence Unit with Bakhru leading. Blueflame was founded in 2023 by Bakhru and Henry Lindemann. Reducto raised a $24.5M Series A (Benchmark) in April 2025 and a $75M Series B led by a16z in October 2025, for $108M total, and has since shipped its own r-1 parsing model priced around one cent per page (launch timing reported inconsistently).

Treat the 22% recall gain with care. It comes from Datasite's private, unpublished VDR Bench, measured against its own earlier scrappy pipeline, and was shared in a vendor-hosted fireside chat. It is still directionally consistent with the broad industry finding that retrieval quality in enterprise RAG is bounded by parsing quality, especially for tables and charts. The "60% of $100M+ deals" and "trillion tokens" stats are company claims without independent verification.

## Real-World Application / Actionable Step
- **For routing work, treat tool-call behavior as a routing feature.** The GPT-6.1 Sol vs Opus 5.5 case is a live example where cost-optimal routing fails on agent behavior, not answer quality. Add per-model tool-call efficiency (calls per resolved task, redundant-call rate) to router training signals.
- **Test harness fixes before routing back up.** Cap tool calls, dedupe identical calls, and add explicit stop conditions for the cheaper model. Measure whether it then clears the quality bar. That converts a model-cost problem into a harness problem.
- **Benchmark compressed VLMs on adversarial document cases.** Charts with near-identical legend colors and merged-cell tables are cheap stress tests where quantization of vision encoders is likely to show degradation before aggregate metrics move.
- **When evaluating RAG systems, ablate the parser first.** Before attributing gains to the generator or a routed model, check how much recall changes with parsing alone.
