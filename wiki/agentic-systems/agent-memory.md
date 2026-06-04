# Agent Memory

Agent memory is the long-term, cross-session store an agent uses to preserve facts, preferences, traces, and state between interactions. It is structurally distinct from the KV cache (which is per-context, short-term, attention-internal) and from the prompt window (which is per-request).

## Current State (as of 2026-06-04)

**Memory becomes a self-supervised skill, removing the annotated-data bottleneck (2026-06-04).** [MemTrain](2026-06-04-memtrain-self-supervised-context-memory.md) (arxiv 2606.03197) attacks the exact problem the 05-15 cluster flagged: memory systems are data-starved because the default recipe (end-to-end RL on annotated memory-intensive tasks) needs expensive, low-diversity labeled data. MemTrain trains memory as a generic skill on *unlabeled* Wikipedia via two coupled proxy tasks optimized jointly with GRPO: masked-entity reconstruction after multiple memory-update rounds (outcome view) and intermediate recall of masked history from memory states (process view, rewarding faithful compression and completeness). As a general pre-step before task-specific post-training it lifts long-text and search QA by up to 17.67 points. This is the opposite cold-start strategy to [Preping](2026-05-15-agent-memory-cluster-stale-preping-evolvemem.md) (05-15, proposer-guided synthetic practice): both reject "collect annotated tasks then RL," but Preping synthesizes the practice while MemTrain mines free text for proxy supervision. The intermediate-recall objective is a direct training signal for the faithful-compression property that [STALE](2026-05-15-agent-memory-cluster-stale-preping-evolvemem.md) (55.2% ceiling) and MemLens (sub-30% multi-session) measured current systems lacking; the masked-entity setup is the MLM objective lifted into the multi-round memory loop.

## Current State (as of 2026-05-15)

**The agent-memory layer is now a programmable substrate, not a frozen RAG database.** Six HF papers on agent memory landed in one day (2026-05-15), splitting cleanly into three roles: evaluation (STALE, MemEye, MemLens, BOOKMARKS), construction (Preping), and adaptive infrastructure (EvolveMem). The shared diagnosis across all six: current memory systems treat retrieval as a fixed component and stored content as static facts, both assumptions break under realistic conditions. → [cluster summary](2026-05-15-agent-memory-cluster-stale-preping-evolvemem.md)

**The eval ceilings tell the structural story.** Best frontier model on STALE (implicit-conflict detection over 150K-token contexts): **55.2%**. Multi-session reasoning on MemLens caps **below 30%** across 27 LVLMs and 7 memory-augmented agents. Visual-fidelity preservation across 13 memory methods on 4 VLM backbones (MemEye): consistently degraded. These are not implementation gaps; they are architectural ones. The memory layer is where the agent-eval crisis ([AgentLens](2026-05-14-agentlens-lucky-pass-swe-eval.md), AssetOpsBench, Soohak, [WildClawBench](2026-05-15-wildclawbench-native-runtime-agent-benchmark.md)) extends.

**The construction side now has concrete cold-start recipes.** Preping demonstrates pre-task synthetic-practice memory at 2-3x lower deployment cost than online memory construction, with the load-bearing piece being proposer-side control over feasibility/redundancy/coverage rather than synthetic volume. δ-mem (05-13) provides the lightweight associative-memory baseline that operates *under* the long-context retrieval layer.

**Retrieval mechanisms are now co-evolved with content.** EvolveMem exposes the entire retrieval configuration (scoring, fusion, answer policy) as a structured action space optimized by an LLM-powered diagnosis module reading per-question failure logs. +25.7% relative on LoCoMo over the strongest baseline; evolved configurations transfer with positive (not catastrophic) transfer. This is the agent-memory analogue of [Make Each Token Count](../inference-efficiency/2026-05-12-make-each-token-count-kv-eviction.md)'s learned eviction at the KV-cache layer: same substrate-as-policy move, one layer up.

## Architectural axes

The 2026-05-15 cluster makes the structural axes explicit:

1. **Storage substrate** — short-term context cache (KV), long-term external memory (vector DB / playbook), online associative memory (δ-mem-style). Each has different staleness and update properties.
2. **Retrieval mechanism** — fixed scoring/fusion (typical RAG), co-evolved scoring (EvolveMem), proposer-guided pre-task (Preping).
3. **Write-time policy** — append-only, structured state consolidation (CUPMem from STALE), trajectory validation (Preping's Validator role).
4. **Staleness handling** — naive (most current systems), explicit state consolidation + propagation-aware search (CUPMem).
5. **Visual fidelity** — naive caption-only (most current), pixel-evidence preserving (open problem per MemEye/MemLens).

## Key Papers

**STALE (2026-05-15)** — Memory staleness benchmark: 400 expert-validated implicit-conflict scenarios, 1,200 queries across three probing dimensions (State Resolution, Premise Resistance, Implicit Policy Adaptation). Best model: 55.2%. Proposes CUPMem (structured state consolidation + propagation-aware search at write time). → [cluster summary](2026-05-15-agent-memory-cluster-stale-preping-evolvemem.md)

**Preping (2026-05-15)** — Pre-task memory construction via proposer-guided synthetic practice. Proposer state shapes future practice; Solver executes; Validator filters trajectories. Competitive with playbook methods at 2.99x lower deployment cost on AppWorld, 2.23x on BFCL v3. → [cluster summary](2026-05-15-agent-memory-cluster-stale-preping-evolvemem.md)

**EvolveMem (2026-05-15)** — Self-evolving retrieval configuration via AutoResearch. LLM-powered diagnosis module reads per-question failure logs and proposes config adjustments; guarded meta-analyzer applies them. +25.7% on LoCoMo over strongest baseline. Evolved configurations transfer with positive (not catastrophic) transfer. → [cluster summary](2026-05-15-agent-memory-cluster-stale-preping-evolvemem.md)

**MemEye (2026-05-15)** — Visual-centric multimodal agent memory evaluation. Two-dimensional: visual-evidence granularity × usage. 13 memory methods on 4 VLM backbones consistently fail to preserve fine-grained visual evidence. → [cluster summary](2026-05-15-agent-memory-cluster-stale-preping-evolvemem.md)

**MemLens (2026-05-15)** — Long-term multimodal-memory benchmark, 789 questions across 5 memory abilities at 4 context lengths (32K-256K). Multi-session reasoning caps below 30%. Motivates hybrid long-context + structured retrieval architectures. → [cluster summary](2026-05-15-agent-memory-cluster-stale-preping-evolvemem.md)

**δ-mem (2026-05-13)** — Lightweight 8x8 frozen-backbone associative memory state updated by delta rule; readout produces low-rank corrections to attention. +1.31x on MemoryAgentBench, +1.20x on LoCoMo without fine-tuning. The architectural baseline for the "augment frozen backbone" approach. → [summary](../inference-efficiency/2026-05-13-delta-mem-online-memory.md)

**SuperLocalMemory (2026-04-17)** — Earlier wiki entry on agent memory. → [summary](2026-04-17-superlocalmemory-agent-memory.md)

## Open Problems

1. **Implicit conflict detection.** Best frontier model at 55.2% on STALE. The signal seems to be in propagation across related memories, not retrieval accuracy.
2. **Multi-session multimodal reasoning.** Caps below 30%. Neither long-context attention nor memory-augmented agents alone suffices.
3. **Cold-start cost.** Preping's 2-3x cost reduction is promising; whether it generalizes beyond AppWorld/BFCL is unknown.
4. **EvolveMem + STALE composition.** EvolveMem auto-discovers retrieval; STALE diagnoses conflicts. A retrieval policy that EvolveMem evolves *specifically* to detect stale state is unwritten.
5. **Memory-as-routing-signal.** If memory staleness can be detected per-query, it can route to retrieval, refresh, or fallback paths. Untested.

## Related Pages

- [KV Cache](../inference-efficiency/kv-cache.md) — the short-term, attention-internal sibling
- [Agent Benchmarks](agent-benchmarks.md) — STALE/MemEye/MemLens are agent-memory benchmarks
- [LLM Routing](../ai-routing/llm-routing.md) — memory staleness as a potential routing signal
