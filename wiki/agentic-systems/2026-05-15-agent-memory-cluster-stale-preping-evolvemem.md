# Agent Memory Cluster: STALE + Preping + EvolveMem + MemEye + MemLens + BOOKMARKS

**Date ingested:** 2026-05-15
**Tier:** 2. Agent memory architecture, evaluation, cold-start, self-evolving retrieval
**Cluster of six HF papers on agent memory landing the same day.**

## TL;DR

Six papers on agent memory landed today on HuggingFace. They split into three roles: **evaluation** (STALE for staleness/conflict resolution, MemEye and MemLens for multimodal memory, BOOKMARKS for role-play storyline memory), **construction** (Preping for pre-task synthetic practice memory), and **adaptive infrastructure** (EvolveMem for self-evolving retrieval configuration). The shared diagnosis across all six: current memory systems treat retrieval infrastructure as fixed and treat stored content as static facts, both assumptions break under realistic multi-session, multimodal, or staleness-prone conditions. Best frontier model on STALE: **55.2%**. Memory-augmented agents on MemLens cap multi-session reasoning **below 30%**. The agent memory layer is the next layer where the eval crisis bites.

## The six papers

### 1. STALE: Can LLM agents know when their memories are no longer valid?

[arXiv 2605.06527](https://arxiv.org/abs/2605.06527). 400 expert-validated conflict scenarios, 1,200 evaluation queries across three probing dimensions (State Resolution, Premise Resistance, Implicit Policy Adaptation), 100+ everyday topics, contexts up to 150K tokens. Failure mode: **Implicit Conflict** — a later observation invalidates an earlier memory without explicit negation, requiring contextual inference. Best model overall: **55.2%**. Models accept outdated assumptions embedded in user queries and fail to propagate state changes across related memories. CUPMem prototype proposed: structured state consolidation + propagation-aware search at write time.

### 2. PREPING: Building Agent Memory without Tasks

[arXiv 2605.13880](https://arxiv.org/abs/2605.13880). Pre-task memory construction via proposer-guided synthetic practice. Proposer state shapes future practice; Solver executes; Validator filters trajectories for memory insertion. On AppWorld, BFCL v3, MCP-Universe: competitive with playbook-based methods built from offline or online experience, with **2.99x lower deployment cost on AppWorld and 2.23x on BFCL v3** than online memory construction. The proposer-side control over feasibility/redundancy/coverage is the load-bearing piece, not the synthetic volume.

### 3. EvolveMem: Self-Evolving Memory Architecture via AutoResearch

[arXiv 2605.13941](https://arxiv.org/abs/2605.13941). Most memory systems freeze retrieval scoring, fusion, and answer-generation policies at deployment while only the *stored content* evolves. EvolveMem exposes the entire retrieval configuration as a structured action space, then uses an LLM-powered diagnosis module to read per-question failure logs and propose targeted adjustments. Guarded meta-analyzer with automatic revert-on-regression and explore-on-stagnation. On LoCoMo: **+25.7% relative over the strongest baseline, +78.0% over minimal baseline**. On MemBench: +18.9% over strongest. Evolved configurations transfer across benchmarks with positive (not catastrophic) transfer.

### 4. MemEye: Visual-Centric Multimodal Agent Memory Evaluation

[arXiv 2605.15128](https://arxiv.org/abs/2605.15128). Two-dimensional framework: visual-evidence granularity (scene-level to pixel-level) × usage (single evidence to evolutionary synthesis). 8 life-scenario tasks with ablation-driven validation gates (answerability, shortcut resistance, visual necessity, reasoning structure). Across 13 memory methods on 4 VLM backbones: current architectures struggle to preserve fine-grained visual details and reason about state changes over time.

### 5. MemLens: Multimodal Long-Term Memory Benchmark

[arXiv 2605.14906](https://arxiv.org/abs/2605.14906). 789 questions across five memory abilities at four context lengths (32K-256K tokens). Image ablation: removing evidence images drops two frontier LVLMs below 2% accuracy on the 80.4% of questions with image evidence. Long-context LVLMs achieve high short-context accuracy through direct visual grounding but degrade as conversations grow; memory agents are length-stable but lose visual fidelity under storage-time compression. **Multi-session reasoning caps most systems below 30%**. Neither approach alone solves the task.

### 6. BOOKMARKS: Efficient Active Storyline Memory for Role-playing

[arXiv 2605.14169](https://arxiv.org/abs/2605.14169). Abstract not yet available; the title is enough to place the paper in the role-play storyline memory category. Tier 3 unless follow-up evidence elevates.

## The shared diagnosis

Three failures are common across the six papers.

1. **Memory systems freeze the retrieval mechanism.** EvolveMem names this directly: stored content evolves but retrieval scoring, fusion, and answer policies are fixed at deployment. The fix is to co-evolve them.
2. **Implicit invalidation is not detected.** STALE makes this crisp: a later observation invalidates an earlier memory without explicit negation. The best model gets 55.2%. The failure cascade is that downstream actions use stale state.
3. **Multimodal memory loses visual fidelity.** MemEye and MemLens both find that long-context and memory-augmented agents cap below 30% on multi-session multimodal reasoning. Compression destroys fine-grained visual evidence that later queries need.

The three failure modes are independent of each other. STALE's implicit conflict can happen in pure text. MemLens's visual-fidelity loss can happen even when no memory is stale. EvolveMem's retrieval-mechanism freeze affects both.

## Why this matters

The wiki has tracked KV cache as a programmable substrate for two months ([Make Each Token Count](../inference-efficiency/2026-05-12-make-each-token-count-kv-eviction.md), [Orthrus](../inference-efficiency/2026-05-14-orthrus-dual-view-diffusion-ar.md), today's [Forcing-KV](../inference-efficiency/2026-05-15-forcing-kv-video-diffusion-kv-cache-compression.md)). Today the substrate-as-programmable thread jumps to the next layer: agent memory as a programmable, co-evolving system, not a frozen RAG database. Six papers in one day is enough to call this a cluster.

The agent-eval crisis the wiki has been tracking ([AgentLens](2026-05-14-agentlens-lucky-pass-swe-eval.md), AssetOpsBench, Soohak, today's [WildClawBench](2026-05-15-wildclawbench-native-runtime-agent-benchmark.md)) now extends into the memory layer. STALE's 55.2% best, MemLens's sub-30% multi-session reasoning, and MemEye's structural failures across 13 methods on 4 VLMs are the memory-side version of the same diagnosis: aggregate metrics over-aggregate; the underlying systems are weaker than scoring suggests.

## Connections to prior wiki pages

- [Make Each Token Count](../inference-efficiency/2026-05-12-make-each-token-count-kv-eviction.md) — KV cache eviction is policy-aware. Memory retrieval (EvolveMem) is now the analogue at the long-term memory layer.
- [δ-mem](../inference-efficiency/2026-05-13-delta-mem-online-memory.md) — Twitter signal 05-14. Lightweight 8x8 frozen-backbone associative memory. Same architectural principle as Preping/EvolveMem: don't retrain the backbone; structure the memory layer.
- [AgentLens](2026-05-14-agentlens-lucky-pass-swe-eval.md) — process-quality measurement for SWE-bench. STALE/MemLens/MemEye are the memory-layer analogues.
- [WildClawBench](2026-05-15-wildclawbench-native-runtime-agent-benchmark.md) — same-day. Native-runtime cap at 62.2%. Memory benchmarks cap lower (STALE 55.2%, MemLens <30%). The agent-eval ceiling depends on which layer you test.
- [agent-memory.md](agent-memory.md) — concept page should be promoted to first-class given six papers in one day.

## Research angle

1. **EvolveMem composed with STALE.** EvolveMem auto-discovers retrieval configurations. STALE diagnoses implicit conflicts. Combining: EvolveMem could specifically search for retrieval policies that detect stale state, using STALE-style probes as the training signal. This is the natural composition; no paper has shipped it.
2. **Preping for cold-start in production.** The cold-start gap is real: every new environment starts with empty memory. Preping's pre-task practice with 2-3x lower deployment cost is directly applicable to production agent rollouts.
3. **MemLens hybrid architecture.** MemLens explicitly motivates "hybrid architectures that combine long-context attention with structured multimodal retrieval." This is the next paper.

## Why it matters

Memory was the next layer up from KV cache. Today the wiki gains its first cluster of evidence that memory deserves the same architectural treatment as the cache: programmable, policy-aware, co-evolving, evaluated under realistic conditions. The eval ceilings (55.2% on STALE, <30% on multi-session multimodal) are evidence that this is unsolved.

## Links

- STALE: [paper](https://arxiv.org/abs/2605.06527) · [raw](../../raw/huggingface/2026-05-15-stale-can-llm-agents-know-when-their-memories-are-no-longer-valid.md)
- Preping: [paper](https://arxiv.org/abs/2605.13880) · [raw](../../raw/huggingface/2026-05-15-preping-building-agent-memory-without-tasks.md)
- EvolveMem: [paper](https://arxiv.org/abs/2605.13941) · [raw](../../raw/huggingface/2026-05-15-evolvemem-self-evolving-memory-architecture-via-autoresearch-for-l.md)
- MemEye: [paper](https://arxiv.org/abs/2605.15128) · [raw](../../raw/huggingface/2026-05-15-memeye-a-visual-centric-evaluation-framework-for-multimodal-agen.md)
- MemLens: [paper](https://arxiv.org/abs/2605.14906) · [raw](../../raw/huggingface/2026-05-15-memlens-benchmarking-multimodal-long-term-memory-in-large-vision-l.md)
- BOOKMARKS: [paper](https://arxiv.org/abs/2605.14169) · [raw](../../raw/huggingface/2026-05-15-bookmarks-efficient-active-storyline-memory-for-role-playing.md)
- Related: [Make Each Token Count](../inference-efficiency/2026-05-12-make-each-token-count-kv-eviction.md), [WildClawBench](2026-05-15-wildclawbench-native-runtime-agent-benchmark.md), [δ-mem](../inference-efficiency/2026-05-13-delta-mem-online-memory.md)
