# From Raw Documents to AI-Ready Data (Leo Platzer & Jeff Koss, Deasy Labs / Collibra)

**Channel:** AI Engineer
**Published:** 2026-10-05
**Source:** https://www.youtube.com/watch?v=wzWNYDY7toc

## TL;DR
Deasy Labs (acquired by Collibra in July 2025) pitches automated curation of unstructured enterprise documents before they hit a RAG index: LLM-driven tagging taxonomies, sensitivity scanning, duplicate/conflict/freshness filtering, and scheduled "data slices" that keep the vector store current. The one technically interesting claim: if 30% of a corpus is stale or duplicated, up to 80% of retrieved context can be junk, and removing it roughly doubles recall@1 and lifts multi-hop RAG task completion 10 to 15%. The thesis is sound and matches independent 2026 work on redundancy in retrieval, but the numbers are vendor-run with no published methodology, and the customer story (North River Manufacturing, "four months to days") is a demo persona, not a case study.

## Key Takeaways
- **Pilot-to-production gap is a data problem:** 40 hand-picked files work fine; 80,000 SharePoint files fail on discovery, leaked PII, duplicates, conflicting versions and expired contracts.
- **Taxonomy-driven tagging:** user-defined, library-reused, or AI-suggested tags (from a pasted use-case description), with conditional sub-tags (only tag contract type if category is legal). Each tag carries a prompt, optional allowed values, evidence spans, confidence score and thumbs up/down few-shot feedback. Filtering cut 339 files to 20 in the demo.
- **Sensitivity scanning:** AI-based plus regex-with-context detectors; the LLM generated a Finnish national ID regex plus nearby Finnish keywords to cut false positives.
- **Document quality is not table quality:** the relevant dimensions are duplication, conflict, freshness and required-metadata completeness, not the classic six DQ dimensions.
- **Data slices:** filtered, scheduled, auto-refreshing subsets fed through an SDK into the vector DB with tags attached as retrieval metadata.
- **Core quantitative claim (vendor eval):** 30% stale/duplicative corpus can mean up to 80% polluted top-k; cleaning roughly doubles recall@1 and adds 10 to 15% task completion on multi-hop RAG. Argued as use-case independent because duplication and staleness hurt regardless of domain.
- **Agent context files:** SDK walks a SharePoint site and writes a per-folder context.md (document types, topics, when to use, example questions) plus a global index, so coding agents like Claude Code or Codex can navigate without opening files, cutting token cost.

## Architecture & Optimization Mechanics
The mechanism behind the 80% figure is straightforward and worth internalizing: near-duplicates land at nearly identical cosine distance from a query, so a handful of redundant versions monopolize top-k and crowd out the complementary chunks a multi-hop question needs. Embeddings are also temporally blind, so a superseded contract scores the same as the current one. Recall@1 doubling is plausible when the right document was previously tied with its own stale copies. Note that this is a retrieval-side problem MMR or diversity reranking only partly fixes; MMR removes redundancy but cannot decide which of two conflicting versions is true. That requires metadata (version, effective date) applied upstream, which is the actual product here.

The per-folder context.md pattern is hierarchical routing for agents: a cheap summary index decides which subtree to read, the same shape as a coarse-to-fine retriever or a router choosing a cheap path before an expensive one. It trades a one-time LLM summarization pass for lower per-query token spend, and its risk is summary staleness, which the scheduled refresh is meant to cover.

Weak spots: no disclosure of the eval dataset, retriever, k, or how "stale" was injected; "up to 80%" is a worst case, not a mean; and LLM-generated tags with per-file confidence scores are only as calibrated as the underlying model, which the talk does not address.

## Grounded Context (Web Enrichment)
The acquisition is confirmed: Collibra bought Deasy Labs (NYC, founded 2023 by ex-McKinsey developers) on July 25, 2025, terms undisclosed, to extend its structured-data governance catalog to unstructured files. Collibra's "first and only platform" claim for unified structured plus unstructured governance is marketing; Microsoft Purview already applies sensitivity labels across SharePoint, and Databricks Unity Catalog governs files and volumes. Collibra's own pages still describe the Deasy "unstructured data agent" as coming soon, so production maturity inside Collibra is unclear.

The duplication thesis holds up independently. An April 2026 paper, RARE (Redundancy-Aware Retrieval Evaluation), shows standard benchmarks overrate retrievers because they lack the near-duplicate density of real legal, financial and patent corpora, and that strong benchmark retrievers generalize poorly to highly redundant collections. Practitioner write-ups in 2026 make the same point about stale retrieval: embedding similarity encodes nothing about supersession, so freshness must be enforced via metadata filters or deletion. Neither source reproduces Deasy's specific 2x recall@1 number.

Sources: [Collibra acquires Deasy Labs](https://www.collibra.com/company/newsroom/press-releases/collibra-acquires-deasy-labs), [TechTarget on the acquisition](https://www.techtarget.com/searchdatamanagement/news/366627998/Collibras-acquisition-of-Deasy-targets-unstructured-data), [BigDATAwire: what Collibra gains](https://www.hpcwire.com/bigdatawire/2025/07/25/what-collibra-gains-from-deasy-labs-in-the-race-to-govern-ai-data/), [Collibra + Deasy blog](https://www.collibra.com/blog/collibra-deasy-labs-unlocking-the-value-of-unstructured-data-for-the-ai-era), [RARE redundancy-aware retrieval eval](https://www.emergentmind.com/papers/2604.19047), [Stale retrieval in RAG](https://tianpan.co/blog/2026-04-15-stale-retrieval-rag-data-quality), [Corpus curation sets the RAG quality floor](https://tianpan.co/blog/2026-04-14-corpus-curation-rag-document-quality-floor)

## Real-World Application / Actionable Step
- **Measure top-k redundancy before tuning retrievers or rerankers:** for an eval query set, compute the fraction of top-k chunks that are near-duplicates (for example, cosine above 0.95 or MinHash overlap). If it is above roughly 30%, dedup and versioning will beat any model swap.
- **Treat corpus dedup as compression:** removing redundant chunks shrinks the index, the context window and prefill cost at once. Report it alongside quantization and routing savings in cost-per-correct-answer terms.
- **Attach version and effective-date metadata at ingest** and filter on it at query time; do not rely on rerankers to resolve conflicting versions.
- **Prototype the context.md index for routing:** build per-folder summaries over a document tree and test whether a small model can route queries to the right subtree, sending only ambiguous ones to a larger model. It is a cheap testbed for difficulty-aware routing.
- **Discount vendor numbers:** before buying, demand the eval set and protocol behind the "2x recall" claim, or run their one-week PoC on your own corpus with a held-out QA set.
