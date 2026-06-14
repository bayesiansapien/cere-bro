# Agent Memory

Agent memory is the long-term, cross-session store an agent uses to preserve facts, preferences, traces, and state between interactions. It is structurally distinct from the KV cache (which is per-context, short-term, attention-internal) and from the prompt window (which is per-request).

## Current State (as of 2026-06-13)

**The bottleneck is compliance, not recall: compile preferences into gates, don't just remember them (TRACE, 2026-06-13).** [TRACE](2026-06-13-trace-compiling-user-corrections.md) (arxiv 2606.13174) reframes a failure the whole memory line has implicitly assumed away. The wiki has tracked memory systems on the premise that better recall yields better behavior (MemForest 05-26, SAM 05-27, MemTrain 06-04, InKH 06-07). TRACE shows that even with Mem0 memory, 57.5% of applicable user-preference checks are still *violated*: the agent can recall the rule and ignore it. The fix is to mine user chat corrections, rewrite each as an atomic rule, and compile them into runtime checks that must pass before a task completes, an enforcement layer rather than a retrieval layer. Cuts held-out preference violation from 100% to 2.0% on out-of-distribution coding tasks (and to 37.6% in-distribution), though only to 60.5% on fuzzier MemoryArena tasks where preferences resist clean compilation. The reframing matters: "preference access ≠ preference compliance" splits the memory problem in two, and most of the wiki's prior work optimized only the access half. Pairs with the same-week kilocode REVIEWS.md and Cursor Auto-review product launches, which independently compile review standards into agent gates. → [summary](2026-06-13-trace-compiling-user-corrections.md)

## Current State (as of 2026-06-07)

**Staleness gets attacked at the systems layer, not the training-objective layer (InKH, 2026-06-07).** [InKH](2026-06-07-inkh-financial-agent-knowledge-harness.md) (interaction-native knowledge harness, arxiv 2606.01886) targets the stale-memory failure the 05-15 cluster measured (STALE capped frontier models at 55.2% on implicit-conflict detection) with engineering rather than a new objective: a temporal graph memory, passive knowledge injection that assembles a bounded working-context buffer *before* the model step, and background extraction with maturity, decay, and **write-time invalidation**. The load-bearing piece is write-time invalidation — invalidate stale knowledge when written, rather than hoping retrieval filters it later. Against a temporal-graph system without invalidation it still improves quality by 0.050 and cuts stale-memory use by 96.58% at comparable cost; against agent-driven wiki-walk memory it cuts latency 82.95% and token cost 82.29% while raising traceability by 0.461 (a human-readable wiki audit surface for governance). This is the complement to the training-objective approaches the page tracks: [MMPO](2026-06-05-mmpo-metacognitive-memory-policy-optimization.md) (06-05) penalizes summaries that muddy belief, [MemTrain](2026-06-04-memtrain-self-supervised-context-memory.md) (06-04) rewards faithful compression; InKH engineers the *store* to expire correctly. The blunt takeaway for builders: a large fraction of agent-memory quality is plumbing (invalidation, decay, bounded buffers), not modeling. Benchmark is synthetic, so generalization to noisy real streams where "what is stale" is itself uncertain is open. → [summary](2026-06-07-inkh-financial-agent-knowledge-harness.md)

## Current State (as of 2026-06-05)

**Memory optimization shifts from outcome reward to belief clarity (MMPO, 2026-06-05).** [MMPO](2026-06-05-mmpo-metacognitive-memory-policy-optimization.md) (Metacognitive Memory Policy Optimization, arxiv 2605.30159) makes the same critique of recursive-summary memory that the wiki has made of agent evals: outcome-based RL gives one reward at the end of a long trajectory, so it cannot localize *which* intermediate summary degraded memory quality, and ambiguous summaries silently accumulate until belief deviation derails the run. MMPO introduces **Belief Entropy**, a self-supervised proxy for how uncertain the model remains about the latent task state given its current memory, and uses it to densely penalize summaries that raise epistemic uncertainty. Result: beats outcome-only methods and holds 97.1% performance at 1.75M-token contexts. This is the control complement to yesterday's [MemTrain](2026-06-04-memtrain-self-supervised-context-memory.md) (which *acquires* a memory skill self-supervised): MemTrain rewards faithful compression throughout the interaction, MMPO penalizes summaries that muddy belief. Belief Entropy is the memory-side analogue of [DRIFT/TELBench](2026-06-04-drift-telbench-span-error-localization.md)'s span-level error localization (06-04) — both replace a single end-of-trajectory verdict with per-step signal. MMPO also belongs to today's six-paper **self-evolving-agents cluster** (keystone: [Rethinking Continual Experience Internalization](2026-06-05-continual-experience-internalization.md), which found naive iterative self-evolution *collapses* unless experience is principle-level, step-wise-injected, and off-policy-internalized; siblings [MLEvolve](2026-06-05-mlevolve-self-evolving-ml-discovery.md), [EvoDS](2026-06-05-evods-self-evolving-data-science-agent.md), [SePO](2026-06-05-sepo-self-evolving-prompt-agent.md), DataCOPE). The cluster's shared message: self-improving memory/skills only compound if the supervision is state-aligned and the internalized signal is abstract, not instance-specific.

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

## Self-supervised memory training (2026-06-04)

- **MemTrain ([06-04](2026-06-04-memtrain-self-supervised-context-memory.md))** removes the data bottleneck. Prior memory agents are RL-trained on scarce, low-diversity annotated tasks. [MemTrain](2026-06-04-memtrain-self-supervised-context-memory.md) trains memory ability self-supervised on raw Wikipedia via two coupled GRPO-optimized proxies: (1) masked reconstruction after several memory-update rounds (outcome-side *maintenance*) and (2) intermediate memory recall (process-side *faithful compression*). +17.67 downstream over task-specific post-training.
- **Learned memory is colonizing other stacks too.** Echo-Infinity ([06-04](../inference-efficiency/2026-06-04-echo-infinity-evolving-memory-video.md)) replaces handcrafted KV schedules and heuristic compression with a learnable evolving memory state for infinite video at constant cost. Agent text memory and generative visual memory are converging on the same principle: learn the compression/eviction policy end-to-end rather than hand-tuning it.

## Memory must track environment evolution, not just facts (2026-06-14)

- **EvoMem ([06-14](2026-06-14-evoarena-evomem-memory-evolution.md))** reframes the memory problem for dynamic environments. Prior memory work (MemTrain 06-04; the STALE/MemEye line) assumes the world holds still and the job is to recall the right fact. EvoArena (same paper) shows that when the environment changes as a sequence of progressive updates, current agents crater to 39.6% average accuracy. EvoMem stores memory as *structured patch histories* — state n is "state n-1 plus these deltas" — so the agent reasons about change itself, not just current state. Gains: +1.5% EvoArena, +6.1% GAIA, +4.8% LoCoMo, +3.7% chain-level (consecutive evolving subtasks, the hardest setting). This extends "learn the compression policy, don't hand-tune it" to a new axis: represent the deltas, not just the snapshot.

## Related Pages

- [KV Cache](../inference-efficiency/kv-cache.md) — the short-term, attention-internal sibling
- [Agent Benchmarks](agent-benchmarks.md) — STALE/MemEye/MemLens are agent-memory benchmarks
- [LLM Routing](../ai-routing/llm-routing.md) — memory staleness as a potential routing signal
