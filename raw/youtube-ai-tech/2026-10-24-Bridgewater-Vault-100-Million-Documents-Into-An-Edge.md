# How Bridgewater Turned 100 Million Documents Into an Edge (Sam Green & Aaron Linsky, Bridgewater)

**Channel:** AI Engineer
**Published:** 2026-10-24
**Source:** https://www.youtube.com/watch?v=CLve4Nx_RwI

## TL;DR
Bridgewater built "the Vault," a governed index of 100M+ unstructured documents (135 external sources plus all internal memos and transcripts), each tagged against the firm's ontology with countries, markets, concepts, and, most importantly, the time period discussed. Web-connected chat answered a Korean won question from 1 to 2 stale sources. The Vault-connected agent found 52 candidates in the right date window and cited 7. Lessons: humans and agents need different things from search, adoption requires migrating old habits, and the payoff is agents that proactively surface topics and write their synthesis back into the corpus.

## Key Takeaways
- **Two readers, five dimensions:** recall, precision, filtering, entitlements, scale. Humans read ~300 wpm and need precision. Agents read ~30k wpm, tolerate noise, and need scale (100+ QPS, swarms in the thousands vs ~100 human queries/hour).
- **Benchmark first:** ~200 hand-labeled queries (including plausible-but-wrong docs) built in under a week. Baseline precision@10 was ~60%. After five iterations ending in agentic search: 90 to 95%.
- **Filtering is the norm, not the exception:** production traces showed nearly every query had a date, source, or asset constraint.
- **Filtered ANN tradeoff:** post-filter is fast but recall collapses under restrictive filters. Pre-filter has full recall but is slow. They moved to turbopuffer's "native filtering" (filter-aware cluster traversal).
- **Adoption via habit migration:** broker email subscriptions became saved searches, folders became collections. Only then did new habits (cross-corpus Q&A, topic feeds, hand-off to agents) stick. Then distribution everywhere: chat, phone, Slack, IDE, and a CLI for agents.
- **Products on top:** "pocket analyst" (hours of research in minutes for dollars), multi-day "researcher," a custom-model macro "forecaster," and Vault-derived tradable signals.
- **Investor workbench:** always-on agent proposes topic cards with summary plus evidence. Human-agent synthesis is auto-captured back into the Vault, creating a compounding loop.

## Architecture & Optimization Mechanics
- **Point-in-time tagging is the real moat.** Tagging "period discussed," not just publish date, prevents look-ahead leakage in backtests and stale answers in live use. This is metadata engineering, not model work.
- **Filtered ANN is a systems problem.** Native filtering lets the attribute index know the vector index's cluster hierarchy and skip clusters with no matches. It is effectively a sparse-routing problem over IVF partitions, analogous to MoE top-k gating with a hard mask.
- **Agent vs human retrieval budgets differ.** Agents absorb larger top-k cheaply, so recall dominates. Humans need reranked precision. One index, two retrieval policies: a natural place for a router (cheap ANN for agents, expensive reranker for humans).
- Weak spot: no numbers on hallucination, citation faithfulness, or signal performance of the "investment signals." The 90 to 95% figure is measured against a 200-query internal set they built themselves.

## Grounded Context (Web Enrichment)
turbopuffer's own native-filtering write-up quantifies the tradeoff Bridgewater described: on a restrictive filter, post-filtering returned 0% recall at ~20ms, pre-filtering 100% recall at ~10s, and native filtering targets ~90% recall at ~25ms, on an SPFresh index tuned for 90 to 100% recall. Independent filtered-HNSW studies (e.g. on Weaviate) confirm post-filtering collapses under selective filters, but there is no independent benchmark of turbopuffer's specific method yet. Treat vendor numbers as directional.

No public Bridgewater disclosure beyond conference talks was found on the Vault or the AIA forecaster's performance. This aligns with the firm's AIA Labs fund (launched 2024 with ML-driven decision making), but returns attributable to unstructured-data signals are not public.

## Real-World Application / Actionable Step
- For any RAG over time-sensitive data, add a **"period discussed" field** extracted at ingestion and filter on it by default. Cheap, high-leverage.
- When building a retrieval eval, include **hard negatives** (docs that look relevant but are not), as Bridgewater did. 200 examples in a week is enough to drive decisions.
- For routing research: treat human vs agent consumers as distinct routing targets. Agent calls get high-recall, cheap retrieval and smaller models. Human-facing calls get rerankers and stronger models.
- Benchmark your vector DB on **filtered** queries at realistic selectivity (1%, 0.1%), not unfiltered recall@10. Most production queries are filtered.
