---
source: HuggingFace Daily Papers
arxiv_id: 2605.05242
date: 2026-05-09
tier: 2
topics: [agentic-search, retrieval, rag, grep, agent-tools]
---

# Beyond Semantic Similarity: Direct Corpus Interaction (DCI)

## TL;DR

The best retriever for an agentic search system is no retriever. DCI replaces the embedding model, vector index, top-k retrieval, and rerankers with raw corpus access via terminal tools (grep, file reads, shell pipelines). Sonnet 4.6 jumps from 69.0% to 80.0% on BrowseComp-Plus (+11.0 points, $424 cheaper). Outperforms strong sparse, dense, and reranker baselines on multiple BRIGHT and BEIR datasets, with average gains of +30.7% on multi-hop QA and +21.5% on IR ranking. From Texas A&M, Waterloo, Stanford, Washington, UIUC, UCSD, Verdent AI, Lambda.

## Why this matters

This is a real architectural retreat. The entire RAG industry has been built on the bet that you need to compress a corpus into a similarity-searchable index before the model touches it. DCI says: that compression is the bottleneck, not the bandwidth limit. If the model has agent capability, it can search the corpus directly with shell tools, the same way a coding agent navigates a codebase. The +11 point jump on BrowseComp-Plus is large enough to take seriously. The cost reduction (-$424) means it's not even paying for the headline number with extra inference.

## Mechanism

```
Standard RAG:
  query ──► embed(query) ──► top-k(index, query_emb) ──► prepend ──► generate
                              │
                              └─► single similarity step, lossy
                                  evidence filtered out is unrecoverable

DCI:
  query ──► agent loop:
              │  grep "exact term" raw_corpus/
              │  cat raw_corpus/file.txt | head -100
              │  find raw_corpus/ -name "*.md" | xargs grep "constraint"
              │  shell pipelines, lightweight scripts
              │  iterative refinement, exact constraints
              ▼
            generate
            
  no embedding model, no vector index, no offline indexing
```

The agent does what a senior engineer does in an unfamiliar codebase: navigate by structure, grep for exact strings, read context around hits, refine the search based on what it finds. This is exactly the loop coding agents already run. DCI's contribution is recognizing that the same loop generalizes to non-code corpora, and that doing so beats the entire prior pipeline.

## Connections to prior wiki

**Connects to coding-agent architecture work.** Claude Code architecture (04-17, 04-19), agent permissions (04-23), and the underlying observation that 98.4% of agent code is operational infrastructure (Twitter repost cluster on 05-08) all point at the same thing: agents already navigate raw repos with shell tools. DCI is the formalization of that pattern as a retrieval primitive.

**Coordination layer connection (dair.ai, 05-07).** That paper argued multi-agent systems fail at coordination, not capability. DCI is the single-agent dual: the agent's capability (grep, shell) is sufficient if you stop forcing it through a similarity bottleneck.

**Repost-amplified signal.** This is the only paper today that surfaces in both HuggingFace AND in your @bayesiansapien retweet feed (Zhuofeng Li, the first author, posted it directly on 05-08). A repost-amplified HF paper is a strong signal of community uptake.

**Composition with MiA-Signature (also today).** The agent doing the grepping needs to know what concepts to search for. MiA-Signature provides a global concept-space view that could guide DCI's exploration policy. DCI plus MiA-Signature is a candidate post-RAG retrieval stack.

## Research angle

1. **Cost regime where DCI loses.** On a 1TB corpus, grep is slow. The +11 points come at the cost of much higher tool-call latency. The paper does not (yet) characterize when DCI breaks. That's the next paper.
2. **Lower-capability models.** DCI works on Sonnet 4.6. Does it work on a 7B agent? If the agent isn't smart enough to refine its own searches, the bottleneck shifts back to something like a learned retriever. The capability threshold is the deployment question.
3. **Hybrid systems.** The cleanest production answer is probably DCI for the precise, multi-hop, constraint-heavy queries plus traditional RAG for the broad-recall queries. A learned router that picks between them is the obvious next paper.

## Source

- Paper: https://arxiv.org/abs/2605.05242
- HuggingFace: https://huggingface.co/papers/2605.05242
- Code: https://github.com/DCI-Agent/DCI-Agent-Lite
- Demo: https://huggingface.co/spaces/DCI-Agent/demo
- Raw: `raw/huggingface/2026-05-09-beyond-semantic-similarity-rethinking-retrieval-for-agentic.md`
