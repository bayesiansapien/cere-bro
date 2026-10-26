# Do Not Let Models Invent Numbers (Vinoo Ganesh, Kepler)

**Channel:** AI Engineer
**Published:** 2026-10-25
**Source:** https://www.youtube.com/watch?v=dZgA6btnb_s

## TL;DR
Kepler's rule for financial AI: **the model cites numbers but never writes them.** The LLM plans. Deterministic retrieval finds the source, human-written code does the arithmetic, and a post-processing filter strips any number that cannot be resolved to a registered citation (value, unit, scale, period, source span). In evals, the filter refused 10,981 citations from plain Claude/ChatGPT-over-RAG outputs, ~3,810 of them outright wrong numbers, and about a third of all citations in production are math the model was prevented from doing. The tradeoff is deliberate: Kepler is less "creative," but the platform (not the model) is structurally unable to emit an untraceable number.

## Key Takeaways
- **Three failure modes of attach-a-source-later RAG:** wrong source (random blog), right source but wrong number (is "17" millions, billions, yen, a prior-year figure, or a page number?), and model mental math.
- **Citation registry:** preprocessed 30M+ SEC documents into typed facts (value, unit, scale, period, entity) with stable IDs, display values, and bounding boxes. Same approach for internal SharePoint/Box/OneDrive/Outlook data.
- **XBRL is not ground truth:** Ganesh claims ~10% error, and most alpha-relevant data is internal anyway.
- **Retrieval stack:** ZeroEntropy embeddings (1280-dim), ANN + BM25 hybrid in turbopuffer, reciprocal rank fusion to ~60 docs, a "trusted source" rerank (10-K outranks an earnings-call remark, and conflicts are surfaced, not hidden), then a cross-encoder.
- **Inference-time dereferencing:** the model emits pointers. A registry resolves them to values. Unresolvable numbers are stripped, or in some cases an agentic "citation repair" step tries to re-ground them.
- **Tenant isolation:** every hit is reauthorized in Postgres. Scoped tokens are issued only by the auth service from signed devices.
- **Idempotence:** same query gives same numbers, since values come from the registry, not sampling.
- **Honest limits:** not for speculation or marketing copy. Does not replace a fund. Ganesh predicts a "quantamental" shift.

## Architecture & Optimization Mechanics
- **Pointer-not-value decoding** is a form of constrained generation. Restricting numeric tokens to registry IDs shrinks the effective output space and removes a whole class of hallucination at near-zero inference cost. It is a cheap, deterministic guardrail compared with self-consistency sampling.
- **Routing implication:** if arithmetic and fact lookup move to tools, the model only needs to plan and pick citations. That is a strong case for routing financial queries to **smaller, cheaper models**, since the hard-to-compress capability (exact recall of figures, math) is no longer required of the LLM.
- **Compression implication:** quantization and pruning tend to hurt numeric recall and arithmetic first. A cite-don't-write architecture makes compressed models far safer in numeric domains. Measure compressed models on "valid citation rate" rather than raw numeric accuracy.
- Weak spot: the 10,981/3,810 figures lack a denominator, model versions, or prompt setup, so the error rate is unknowable. "Citation repair" is undisclosed IP, which reintroduces the model into the trust path.

## Grounded Context (Web Enrichment)
Kepler (founded 2025, CEO formerly at Palantir and Citadel) publicly pitches "atomic provenance" and "scope determinism," consistent with the talk. The claimed Anthropic deep dive could not be located in Anthropic's public customer stories via search, so treat that as unverified. The broader pattern (tool-based math, provenance-linked numbers) matches where financial AI vendors are converging after repeated reports of LLMs misreading units and periods in filings.

The XBRL skepticism is directionally fair but the "~10%" figure is not well sourced. Studies document real XBRL quality problems (e.g. NC State 2009 found scale errors turning millions into billions, and XBRL US's data-quality rules cut flagged errors 64% in 2015 to 2016), but no recent authoritative overall error rate was found. A 2025 dissertation found DQC rule errors had no measurable market effect, suggesting errors are real but often immaterial in aggregate. They do matter for any single DCF input, which is Kepler's point.

## Real-World Application / Actionable Step
- For personal finance research agents, adopt the **"cite, don't write"** pattern: numbers come only from tool calls (filings API, spreadsheet), and a regex post-filter flags any digit not traceable to a tool output.
- In compression evals, add a **numeric-grounding test**: give filings as context and measure the rate of numbers in the output that match a source span. Compare FP16 vs INT4 to see whether quantization degrades grounding.
- For routing research: classify queries by whether they need generation-side numeric fidelity. If a deterministic tool layer exists, route to the cheapest planner model.
- Use hybrid retrieval (ANN + BM25 + RRF + cross-encoder) as the baseline for any document QA. Pure vector search underperforms on tickers, line items, and exact figures.
