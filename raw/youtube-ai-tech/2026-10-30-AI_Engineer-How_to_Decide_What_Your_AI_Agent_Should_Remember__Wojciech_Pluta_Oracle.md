# How to Decide What Your AI Agent Should Remember (Wojciech Pluta, Oracle)

**Channel:** AI Engineer
**Published:** 2026-10-30
**Source:** https://www.youtube.com/watch?v=qq2Hm4XNRgI

## TL;DR
RAG is the read path and memory is the write path. The hard problem is deciding what gets promoted from a conversation into durable memory. Oracle's answer is a "memory promotion gate": classify the candidate, compare it with existing records, check the evidence needed for that record type, then let the harness (not the model) admit, reject or send it for human review. A mortgage-ops demo shows a formatting preference persisted across sessions, an "approve every application" instruction blocked, and an org-wide operational rule sent for human sign-off. Underneath, it is a pitch for the `oracleagentmemory` package and the claim that "models are shared, memory is yours."

## Key Takeaways
- **Read vs write split:** retrieval doesn't tell you what should *survive* an interaction. Treat memory writes as a governed pipeline, not a side effect.
- **Promotion pipeline:** decision model classifies the candidate (semantic preference, procedural rule, episodic fact), dedups and checks it against existing records, checks evidence thresholds by type, then the harness decides admit / reject / human-review, and the result is persisted with traces.
- **Failure poles:** promote nothing and you get no continuity. Promote everything and you poison the store. Provenance and supersession (newer records replacing old ones) are first-class concerns.
- **Memory taxonomy:** short-term (session), long-term (episodic summaries, procedural toolbox, semantic knowledge/preferences), shared (team or enterprise, human-approved).
- **Context card:** a compact, prompt-ready block per turn holding topics, a running summary, selected relevant records and recent messages. The harness assembles it so the agent doesn't spend attention on housekeeping.
- **Storage argument:** a database over file trees for ACID guarantees, concurrent writers, per-end-user isolation and multi-modal search (vector, JSON, relational) in one engine.

## Architecture & Optimization Mechanics
- **The gate is a cheap classifier in front of an expensive store.** A small "decision model" scores candidates and the harness applies deterministic policy. This is a routing problem: most turns should produce zero writes, and a small model can make that call.
- **Context cards are a context-compression layer.** They bound the prompt to topics, summary, top-k records and a recent window, which keeps KV-cache size and prefill cost roughly constant as sessions grow. The stable parts (topics, summary) are good candidates for prefix caching if ordered first.
- **Harness-owned policy:** the model proposes and the harness disposes. Guardrails sit outside the model so a prompt injection can't talk its way into durable memory.
- **Gaps in the talk:** no numbers on gate precision/recall, write latency, token savings or memory-retrieval quality. The demo is a scripted, pre-recorded happy path.

## Grounded Context (Web Enrichment)
The package is real: `oracleagentmemory` on PyPI (26.4, with 26.6 docs live), covering working, semantic, episodic and procedural memory, with "context cards" mentioned in Oracle's developer blog but thinly documented. Oracle reports 93.8% (469/500) on LongMemEval. That is a vendor-reported figure and should be checked against independent runs before comparing with Mem0, Zep or Letta. The latest release added background extraction.

The talk's central worry is backed by 2026 research. An ICML 2026 study ("From Untrusted Input to Trusted Memory," arXiv 2606.04329) identifies four memory write channels, introduces MPBench, and finds that agents which write memory more aggressively are measurably more exploitable, and that standard prompt-injection defenses miss memory poisoning. An April 2026 lifecycle survey (arXiv 2604.16548) also finds that query-only interaction can permanently change memory state (MINJA). Third-party analyses note that Mem0, Letta and Zep store whatever you write by default. A promotion gate with provenance is now the expected design, not an Oracle innovation.

## Real-World Application / Actionable Step
- **Frame memory-write as a routing decision.** Train or prompt a small model (e.g. a quantized 1-3B classifier) to label each turn as {no-write, preference, fact, procedure, escalate}. Measure precision on poisoning cases from MPBench, not just recall on useful facts.
- **Compress context deterministically.** Add a context-card-style assembler to any long-running agent: fixed slots for summary, top-k memories and the last N turns, ordered for prefix-cache reuse. Log prefill tokens per turn before and after.
- **Put writes behind the harness.** Never let the model call a raw `memory.write`. Route writes through a policy function with type-specific evidence rules and a human-review queue for shared or global memories.
- Skip the vendor lock-in argument unless you're already on Oracle DB. Postgres with pgvector and row-level security gives the same ACID and isolation properties.
