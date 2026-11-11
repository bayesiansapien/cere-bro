# Your Sub-Agents Are a Distributed System. Treat Them Like One.

**Channel:** AI Engineer (Girish Konda, Microsoft, personal views)
**Published:** 2026-11-10
**Source:** https://www.youtube.com/watch?v=DxP5aW4VknQ

## TL;DR
An orchestrator fanning work out to concurrent sub-agents that share mutable context and call real tools is a classic distributed system. The usual failures follow: partial failure, dirty reads, unbounded fanout, and non-idempotent retries. The interface makes it worse, since every sub-agent is a `string -> string` function that reports failure as fluent, success-shaped text. Konda proposes a consistency model, **SAFE**: Source facts, At-most-once effects, Fanout budgets, Explicit outcomes. The orchestrator enforces it in code, not in prompts.

## Key Takeaways
- **Failure modes mapped to classic theory:**
  - Half-finished sub-agent is effectively Byzantine. It answers fluently and wrongly. Three triage paths (actually checked telemetry, matched a familiar title, did nothing) all returned "benign" with equal confidence.
  - Timeouts are indistinguishable among slow, crashed, and lost reply (FLP 1985). Use Chandra-Toueg style *suspicion*: record timeout as `unknown`, keep the real cause.
  - Shared context gives dirty reads (Berenson et al. 1995). One inferred "error rate fell 80%" gets reused by two other workers, and the orchestrator sees three "agreeing" artifacts.
  - Quorum is fake when voters share a source. Gifford's weighted voting works because R+W>N guarantees overlap with the latest write. Three agents reading the same guess is one source counted three times.
  - Retries replay side effects (e.g. a duplicate PR). MCP's `idempotentHint` is only a hint and defaults to false.
- **SAFE model:**
  - **S, source facts:** every handed-off fact is a record with claim, revision, source, version, scope, and three timestamps (data-as-of, read-at, used-at). Freshness is checked at use (e.g. a 5-min limit). Observation has a source; inference does not.
  - **A, at-most-once effects:** every write has an identity, approval binds that exact action once (approval as a fencing token, per Kleppmann), and outcome is read back, never replayed. "Submitted is not confirmed."
  - **F, fanout budgets:** per-downstream gate, bounded wait, refusal counted as failure. His MCP bridge gates npx cold starts 2 at a time with a 15 s bounded wait (availability chosen on purpose), and a session cap with a 10 s wait then refuse. Reserve capacity before the async start to avoid check-then-act overbooking.
  - **E, explicit outcomes:** named terminal states (A2A has completed/failed/canceled/rejected/input-required; MCP has `isError`). "Checked and got no" is distinct from "could not check." Recompute numbers: 10/1000 vs 6/600 errors is 1% both times, so "error rate fell" is refused.
- **Limits:** SAFE does not make facts true, give exactly-once delivery, roll back (design sagas, Garcia-Molina 1987), or give global order. It costs latency (PACELC). Overkill for draft-only agents, and it assumes a single orchestrator.

## Architecture & Optimization Mechanics
- **Agent outputs are untrusted input.** Schema validation, evidence presence, freshness, and numeric recompute all live in orchestrator code. "If the same model can skip a check and declare it passed, you have a request, not a boundary."
- **Correlated errors break ensembles.** This applies directly to LLM-judge and self-consistency ensembles: votes conditioned on shared context are not independent samples, so the effective sample size is near 1. Real independence needs separate contexts and ideally different models.
- **Fanout budgets equal admission control.** Same principle as vLLM scheduler limits and KV-cache admission. Unbounded parallel sub-agents create provider 429s that surface only as prose to the model, never to orchestrator code.
- **Latency cost of consistency:** each freshness check is an extra read. For latency-sensitive routing, apply SAFE only to write-bearing paths.

## Grounded Context (Web Enrichment)
The protocol claims check out. MCP tool annotations (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`) are advisory, `idempotentHint` defaults to false, and write-related hints are ignored when `readOnlyHint` is true. A2A defines completed, failed, canceled, and rejected as terminal states and `input-required` as a non-failure pause, though SDK naming varies (kebab, snake, uppercase). Neither protocol enforces that status matches content, which is exactly the gap Konda targets.

The theoretical citations (Lamport 1978, Gifford 1979, Birrell-Nelson RPC 1984, FLP 1985, Chandra-Toueg 1996, Berenson 1995, Kleppmann on fencing tokens) are correctly applied. The talk's value is the mapping, not novelty. Similar arguments appear in recent "agentic systems as distributed systems" writing, but SAFE is a concise, implementable checklist backed by real bugs in his MCP Pacemaker bridge.

## Real-World Application / Actionable Step
- Make every sub-agent return a typed envelope: `{status: completed|partial|failed|unknown|refused, did, did_not, evidence[], side_effects[]}`. Reject free-text-only returns in the orchestrator.
- For eval and judge ensembles in routing experiments, give each judge an isolated context and a different model, and measure inter-judge correlation before trusting majority votes.
- Add a numeric recompute gate: any sub-agent claim of "X improved" (latency, perplexity, accuracy after quantization) must include raw numerator and denominator, and the orchestrator recomputes.
- Cap concurrent sub-agents per downstream API with a bounded queue and surface 429s as structured failures.
