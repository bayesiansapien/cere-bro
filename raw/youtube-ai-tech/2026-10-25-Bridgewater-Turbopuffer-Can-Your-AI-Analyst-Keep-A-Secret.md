# Can Your AI Analyst Keep a Secret? (Aaron Linsky, Bridgewater & Nikhil Benesch, turbopuffer)

**Channel:** AI Engineer
**Published:** 2026-10-25
**Source:** https://www.youtube.com/watch?v=u_jvuCjuvEk

## TL;DR
An enterprise AI analyst must search private documents where every email, memo, and licensed research note carries its own ACL. Bridgewater's Vault (100M docs, ~400 to 450M vectors, 135 licensed sources with varying entitlements) broke its first permission-filtered vector search as the corpus grew. turbopuffer solves it with "native filtering": the permission index knows which ANN clusters (~200 docs each) contain at least one doc the user can see, skips the rest, then scans only the nearest accessible clusters. Result: ~120ms P90 across 450M vectors, with permissions expressed as simple filters (`viewers contains user1 OR groups containsAny [B, C]`).

## Key Takeaways
- **Public web has no permission problem. Private data is the hard part:** per-document ACLs via groups or direct grants.
- **Napkin math:** 100M docs × 1KB at ~20 GB/s memory bandwidth = 5s brute force. Target is ~100ms. From S3 cold, a minute or more.
- **Post-filter fails on recall:** for a user with narrow access, the top-k neighbors may contain few visible docs. You spiral outward and give up with 40 of 100 results.
- **Pre-filter fails on latency:** a user with access to 50M of 100M docs reduces to a brute-force scan.
- **Native filtering = cluster-level pruning plus local scan.** Combines both strategies.
- **turbopuffer architecture:** object storage (S3/GCS/Azure Blob) as source of truth, SSD/memory as cache for hot namespaces. Claims ~10x cheaper than disk-based systems at comparable hot latency. Supports vector, keyword (BM25), and regex.
- **Known limitation:** nested groups remain hard to express and plan.
- **Bridgewater stack:** Delorean (bi-temporal macro time-series DB) plus Vault (unstructured). Agent and investor output is written back into the Vault.
- **Broader framing:** "isolation-native search," covering per-doc ACLs, region locking, BYO-VPC, and customer-managed encryption keys.

## Architecture & Optimization Mechanics
- **Native filtering is sparse routing.** Cluster selection under a permission mask is structurally identical to top-k expert gating with a hard availability mask. The same cost model applies: prune at the coarse level, compute densely only inside selected partitions. Cluster size (~200) is the "expert granularity" knob trading pruning precision against scan efficiency.
- **Tiered storage = KV-cache offloading logic.** Cold on object storage, hot in SSD/RAM on access. Same pattern as vLLM/LMCache offloading of KV blocks to CPU or disk with prefix-aware reuse.
- **1KB per 1024-dim int8 vector** is the right napkin unit. Quantizing embeddings to int8 or binary is what makes brute-force math tractable, a direct compression win in retrieval.
- Weak spot: no recall numbers under highly selective permissions (e.g. a user who sees 0.01% of docs). Latency P90 alone does not prove recall. Native filtering's recall depends on how many accessible clusters are probed.

## Grounded Context (Web Enrichment)
turbopuffer's own published benchmark on native filtering shows the tradeoff numerically: post-filter 0% recall at ~20ms, pre-filter 100% recall at ~10s, native filtering targeting ~90% recall at ~25ms on an SPFresh-based index tuned for 90 to 100% recall. No independent benchmark of this specific method was found, so treat the 120ms P90 at 450M vectors as a vendor claim, though it is consistent with their ANN v3 claims (100B+ vectors at ~200ms P99).

The security framing is well supported. 2026 practitioner writing on permission-aware RAG converges on retrieval-time ACL enforcement, since post-retrieval filtering lets unauthorized text enter the model's context ("security theater"). Remaining open risks the talk does not cover: **permission sync lag** (revoked access persisting until reindex), **nested group explosion** when flattening hierarchies into metadata (where ReBAC/graph approaches are proposed), and **prompt injection** from poisoned documents, which filtering does not address.

## Real-World Application / Actionable Step
- When benchmarking RAG retrieval for compressed embedding models, test **filtered recall at multiple selectivities** (50%, 1%, 0.01%). Quantized embeddings plus aggressive cluster pruning can compound recall loss on narrow filters.
- Borrow the cluster-pruning idea for MoE inference: precompute, per request class or tenant, which experts are ever activated, and skip loading or prefetching the rest. It is the same mask-then-scan optimization.
- If building an internal research agent, enforce ACLs **inside** the retrieval query, propagate end-user identity (not a service account), and set an SLA on ACL sync.
- Use the napkin-math habit (bytes × docs ÷ bandwidth) before adding index complexity. Below ~1M docs, brute force with int8 vectors is often good enough.
