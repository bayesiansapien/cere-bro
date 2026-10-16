# Your Fridge Is a Valid Payment Device (Eleonora Drykina & Nina Žižakić, In The Pocket)

**Channel:** AI Engineer
**Published:** 2026-10-14
**Source:** https://www.youtube.com/watch?v=gonAewBZxfU

*Note: the raw transcript was an untranslated Arabic dub; this page is synthesized from it.*

## TL;DR
A clean production case study of agentic RAG over a Belgian payment scheme's rulebooks (anonymized, but almost certainly Bancontact Payconiq): ~270 PDFs, ~6,000 pages, ~3,000 tables, heavy cross-references, strict citation requirements. What worked: structure-preserving non-overlapping chunks with section paths, tables flattened to CSV with spanning cells duplicated, hybrid dense + BM25 retrieval fused with RRF (hit rate 92% to 97% on 63 questions), and an agent with four zoom-level tools instead of a fixed retrieve-then-generate pipeline. The cost is latency (38 s mean per answer), which streaming makes tolerable. Nothing here is novel, but the engineering judgment is sound and the eval lessons (LLM-judge noise, broken rubrics) are the most transferable part. Usage is small so far: ~900 questions from ~34 internal users.

## Key Takeaways
- **Chunking:** paragraphs packed to ~2,000 characters, never splitting a table, no overlap. Regex-detected headings ("Chapter 3", "4.2.1") give each chunk a section path, so a section is exactly the ordered set of its chunks and can be reassembled losslessly. ~4,000 chunks total.
- **Metadata per chunk:** rulebook name and page (for citations and PDF links), section path, chunk index, rulebook ID, an LLM-generated rulebook summary prepended for document context, and business fields (which rules apply, contains-table flag).
- **Tables were the biggest accuracy win.** Plain PDF text extraction mangled merged cells spanning rows, so fee lookups pulled wrong rows. Converting to CSV and duplicating spanning values into every row fixed it.
- **Hybrid retrieval:** dense top-50 + BM25 top-50 in one Qdrant call, RRF to top-30, rerank for section coherence, top-10 to the agent. Dense misses exact rule codes and message names; BM25 misses paraphrase. Hybrid lost zero questions dense already found.
- **Four tools, narrow to wide:** search rulebooks (top-10 chunks), fetch full section, fetch whole rulebook (small ones only), list available rulebooks.
- **Guardrails:** whole-rulebook fetch refuses above ~100K tokens and returns the section list instead; bad section names return valid options rather than failing; a "discipline" instruction makes the agent ask itself before a sixth call whether it is fetching anything new. Most questions need 2 to 4 calls. Added after seeing agents repeat failed searches.
- **Grounding policy:** general knowledge (what a bank is) is fine; facts about other payment schemes must not appear unless in the rulebooks. No advice, neutral on competitors, explicitly say when something is not covered.
- **UI:** generating Pydantic UI components failed because partial JSON cannot stream, so users stared at 38 s of blank screen. Fix: stream markdown token by token, append a structured source card only at the end.
- **Evals:** 86 end-to-end Promptfoo tests with LLM-judge rubrics, citation checks and the retrieval-only set. Lessons: 5 of 12 apparent changes did not reproduce on rerun, and once a "hallucinated date" penalized by the judge was actually in the rulebook. The rubric was the bug.
- **Usage signals:** thumbs up/down died after month one. Sentiment is inferred from follow-ups ("thanks" or new topic is positive, re-asking is negative). Month one was red-teaming; by month three over 90% were genuine questions, including pasted customer emails and protocol messages for drafting replies.

## Architecture & Optimization Mechanics
- **Non-overlapping chunks + section index = free hierarchical retrieval.** Zoom out is a metadata filter plus sort, no second index. Overlap would have broken lossless reassembly.
- **RRF avoids score calibration** between BM25 (unbounded, per-query scale) and cosine similarity. Only ranks matter.
- **Agentic retrieval as adaptive compute.** Simple lookups stop at one search; cross-referenced or fee questions escalate to section or rulebook fetches. This is routing at the retrieval layer: spend context and latency only where the question demands it.
- **Tool-level budget guards** (100K token refusal, call-count self-check) are cheap ways to bound worst-case cost per query without hard-capping capability.
- **Latency budget:** 38 s mean is a multi-call research task. The obvious lever is a smaller, faster model for the search-and-decide loop and the frontier model only for final synthesis.

## Grounded Context (Web Enrichment)
The design matches current best practice. Qdrant's Query API supports exactly this pattern (dense and sparse prefetches fused with top-level RRF), and Qdrant's own docs justify RRF on the same grounds they give: BM25 magnitudes shift per query while dense similarity is bounded. Two caveats from the docs matter for anyone copying it. Fusion can only reorder what the prefetches returned, so prefetch depth (their 50) is the real recall ceiling. And Qdrant's default RRF `k` differs from the original paper's 60 and has changed across versions, so check it explicitly.

The fridge is less absurd than it sounds. Bancontact has supported tokenized contactless payments from wearables (rings, watches, key fobs) since KBC's 2020 launch with Fidesmo, Thales and Mastercard, so a rulebook enumerating form factors as broadly as cufflinks, handbags and fridges is plausible scheme language. The retrieval eval is small (63 questions), so 92% to 97% is about three questions; directionally right, statistically thin. Their judge-noise finding (5 of 12 changes not reproducing) echoes [[2026-10-05-AI-Engineer-Your-LLM-Judge-Is-A-Confident-Liar-Browserbase]].

## Real-World Application / Actionable Step
- **For a paper or internal-docs RAG over arXiv PDFs:** reuse the recipe directly: non-overlapping section-path chunks, tables to CSV with spanning cells duplicated, Qdrant dense + BM25 with RRF, and a "fetch whole section" tool. Benchmark tables in quantization papers have the same merged-cell problem.
- **Treat it as a routing experiment:** log tool-call depth per question and test a small model for the retrieval loop with a large model only for the final answer. Measure latency and accuracy against the 38 s baseline.
- **Rerun every eval change at least 3 times** before believing it, and audit judge failures against the source before blaming the model.
- **Use implicit feedback** (re-ask rate, topic switch) instead of thumbs, which users stop clicking after a month.
- Related: [[2026-10-04-AI-Engineer-Stop-Fine-Tuning-To-Fix-Retrieval-Problems]], [[2026-10-02-Qdrant-Stop-Renting-Your-AIs-Memory-Local-Edge-Memory]].
