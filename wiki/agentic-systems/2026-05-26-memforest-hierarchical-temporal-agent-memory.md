# MemForest: Hierarchical Temporal Indexing for Agent Memory

**Source:** [arXiv:2605.23986](https://arxiv.org/abs/2605.23986), via HuggingFace Daily Papers 2026-05-26.
**Topic:** Agent memory systems / long-context LLM agents / temporal indexing.

## TL;DR

Existing agent memory systems suffer from two structural problems: coarse-grained state management (full-state rewrites on each update) and sequential update pipelines (memory construction tightly coupled to LLM inference). Together these produce growing latency and bad scaling as memory accumulates. MemForest reformulates agent memory as a write-efficient temporal data management problem. Two contributions: (1) parallel chunk extraction decouples memory construction into concurrent independent operations, breaking the sequential bottleneck; (2) MemTree, a hierarchical temporal index that organizes memory as time-ordered trees rather than flat global summaries, replacing full-state rewrites with localized per-node updates. On LongMemEval-S, MemForest hits 79.8 percent pass@1, the best stateful baseline result reported, while sustaining ~6x higher memory construction throughput than state-of-the-art systems including EverMemOS.

```
Existing systems (flat global summary):           MemForest (MemTree):
                                                                            
   new chunk arrives                              new chunk arrives          
        │                                              │                    
        ▼                                              ▼                    
   ┌──────────────┐                              ┌──────────────┐           
   │ rewrite      │ sequential                   │ parallel     │           
   │ global       │ tightly coupled              │ chunk        │           
   │ summary      │ to LLM inference             │ extraction   │           
   └──────┬───────┘                              └──────┬───────┘           
          │                                             │                    
          ▼                                             ▼                    
   full-state O(N) update                       ┌──────────────┐            
                                                 │ MemTree      │            
                                                 │ (time tree)  │            
                                                 └──┬─────┬─────┘            
                                                    │     │                  
                                                  per-node localized update  
                                                  6x throughput vs flat      
```

## What it does

- Memory is organized as a temporal forest: each tree is a time-ordered hierarchy of summaries, with leaves being raw chunks and internal nodes being progressively higher-level summaries.
- An update to a new chunk only touches the affected tree paths from the new leaf up to the root, not the global summary. The rest of the structure stays fixed.
- Memory construction is parallel: multiple chunks are extracted concurrently rather than fed sequentially through a single LLM pass.
- Retrieval traverses the tree, returning evidence at the time and resolution the query implies.

## Key results

- LongMemEval-S: 79.8 percent pass@1, best among stateful baselines.
- ~6x higher memory construction throughput than EverMemOS and other SoTA.
- LoCoMo: also strong (full numbers in paper).

## How this relates to prior wiki pages

MemForest lands inside an active memory thread. The most direct prior is MeMo (Memory as a Model, covered in 2026-05-24's DAIR.AI Top Papers via Gmail starred), which argued memory should be a separately trained learned subsystem with explicit read/write/integrate interfaces, decoupled from base-model weight updates. MeMo and MemForest differ on what the structural commitment is: MeMo trains the memory module as a neural net; MemForest treats memory as a temporal data structure with a discipline borrowed from database systems. Both refuse the assumption that memory should be a vector store with a global summary on top, the architecture that has dominated agent memory since 2023.

The wiki's agent-memory concept page covers the longer arc:

- **2026-04-17 SuperLocalMemory** (biologically-inspired local memory)
- **2026-05-15 EvolveMem cluster** (continual memory updates without catastrophic forgetting)
- **2026-05-24 MeMo** (memory as a separately trained model)
- **2026-05-26 MemForest** (memory as a temporal data structure)

These are four different structural commitments. They converge on rejecting the flat-summary-plus-vector-store baseline; they diverge on what to put in its place. The wiki's view is that the three-way split (neural memory module à la MeMo, temporal data structure à la MemForest, runtime artifact à la Life-Harness 2026-05-23) will not collapse to a winner; production systems will compose them.

## Research angle

The most interesting open problem is the read side. MemForest's update side is genuinely better; the retrieval side still routes through an LLM that has to interpret the tree. The natural next paper learns a retrieval policy directly over the tree structure, the way a database query planner does over an index. Whether the tree can be made the query plan and the LLM call can be eliminated from retrieval is the load-bearing question.

## Industrial implication

For any team building a multi-day or multi-week agent (developer assistants, deep research agents, customer-support bots with conversation continuity), the 6x throughput claim on memory construction is what gets DevOps attention. The pass@1 ceiling of 79.8 percent on LongMemEval-S is also what the next memory-system paper will try to beat. Expect MemForest's MemTree structure to be a baseline in agent-memory papers for the rest of 2026.
