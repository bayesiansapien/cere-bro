# Your PR Says the Tests Passed. Prove It.

**Channel:** AI Engineer (Stephen Chin & Cassandra Chin)
**Published:** 2026-11-10
**Source:** https://www.youtube.com/watch?v=gbeuC0ud1p4

## TL;DR
AI-written PR descriptions get rejected because they are reconstructed from a compacted, lossy session context and so contain false claims (e.g. "tests passed" when they never ran correctly). TraceTune, an open-source tool, rebuilds PRs from the raw agent session traces with an independent writer/reviewer loop. Adding Relate, a new Rust embedded in-memory graph database, to precompute an "evidence graph" and a "neighborhood brief" cut tokens by about half and lifted judged quality by 2 to 4 points on a 100-point scale.

## Key Takeaways
- **Failure mode:** the agent writes the PR from its own inflated, auto-compacted context, so accuracy decays as the session grows. Most AI PRs read as line-by-line diff narration rather than explaining why.
- **Concrete false claim caught:** the PR said checks passed, but the trace showed `bun test` and `bunx tsc` run concurrently, which cannot both pass. Evidence must come from the trace, not the agent's memory.
- **Origin:** Showtale, an education research tool for tracing student AI-assisted work, since the prompts are the work but only the final code gets submitted.
- **Naive cost cut fails:** swapping the writer to Haiku lowered quality. A cheap writer turns prose into a mechanical checklist no matter how much feedback it gets.
- **Counterintuitive model allocation:** expensive writer (Sonnet-class), cheap reviewers (several Haiku-class). Cross-checking claims against a structured brief is mechanical, writing is not.
- **Graph layer (Relate):** zero LLM cost. Stores code, checks, and attributions as relationships and returns a connected multi-hop "neighborhood brief" so writer and reviewers share one compact evidence packet.
- **Results (PRBench, their own benchmark with LLM judges plus human review):** 74 to 76 on one agent, 82 to 86 on the other (Claude Code and Codex), about 50% fewer tokens.

## Architecture & Optimization Mechanics
- **Deterministic preprocessing replaces LLM research loops.** The token saving comes from moving evidence retrieval and linking out of iterative agent loops into a local graph query. It is classic precompute-then-condition: spend CPU, not tokens.
- **Asymmetric model routing per role** is the transferable insight. Route generation-heavy, style-sensitive steps to a strong model and verification steps against structured evidence to small models. Verification gets cheap once the evidence is structured.
- **Shared compact context** also improves prompt-cache reuse across multiple reviewers reading the same brief.
- **Caveats:** a +2 to +4 point gain on a self-built benchmark with LLM judges is modest and within plausible judge variance. No confidence intervals, sample sizes, or inaccuracy rates were shown. The 50% token cut is the stronger claim. Stephen Chin's long association with graph databases (Neo4j DevRel) is worth noting when reading "add a graph" as the answer.

## Grounded Context (Web Enrichment)
Searches found no public footprint yet for TraceTune, PRBench, or the "Relate" database. Relate was announced as launching the same week as the talk (NODES conference), so independent benchmarks do not exist. The embedded Rust graph DB niche is crowded: Grafeo (embedded or server, ACID, Neo4j Bolt compatibility), SparrowDB (Cypher, MIT, self-reported benchmarks slower than warmed Neo4j on deep traversals), LoraDB, and cqlite. Relate will need to show why it beats these for agent workloads.

The broader point holds up independently. Context compaction in long agent sessions is a known source of hallucinated state, and grounding summaries in raw tool-call logs is the standard mitigation (also the logic behind trace-based provenance in Claude Code and Codex session logs).

## Real-World Application / Actionable Step
- For any agent writing experiment reports (e.g. quant/pruning sweep results), generate claims from raw logs and tool outputs, not from the agent's session memory. Require every "passed"/"improved" claim to cite a log line.
- Test the asymmetric allocation in your router: strong model for synthesis, N small models for claim verification against structured evidence. Measure accuracy per dollar against "strong reviewer, weak writer."
- Before adding LLM retrieval loops, ask whether a deterministic index (graph, SQL, or simple JSON of run to config to metric) can build the brief for free.
