# TAO: schedule agent sessions by when their tools will return

**Sources:** [arXiv 2610.37230](https://arxiv.org/abs/2610.37230) (HuggingFace 2026-10-29) · context: [Intel CEO on CPU:GPU ratio](https://x.com/StockSavvyShay/status/2115924406094700702). raw: `raw/huggingface/2026-10-29-tao-tool-aware-joint-scheduling-for-llm-based-agentic-servin.md`.

**TL;DR.** Agent serving alternates between model inference on GPU clusters and tool calls on distributed CPUs. Existing serving systems decide which waiting session to admit and which GPU to place it on with heuristics, and they ignore whether a session's tool result is even back yet, so GPU slots and cache get spent on sessions that will just stall. TAO scores each waiting session with a value function built from three terms: near-term tool readiness, node-specific cache credit (how much of this session's KV cache a node already holds, decayed over time), and token footprint. A dynamic program then jointly selects and places sessions under capacity limits. Across 12 model-workload-concurrency settings it cuts latency by up to 26.8%, mean TTFT (time to first token) by up to 36.3%, and raises decode throughput up to 29.5% against the best baseline per metric.

<div class="dg-title">Admit the session whose tool is about to return</div>
<div class="dg-sub">Tool readiness and cache locality enter one score, and placement is solved jointly.</div>

```mermaid
flowchart LR
  W["Waiting sessions<br/><small>mid tool call</small>"] --> V["Value score<br/><small>readiness, cache, tokens</small>"]
  V --> DP["Dynamic program<br/><small>select and place</small>"]
  DP --> G["GPU nodes<br/><small>warm KV reused</small>"]
  G --> O["Lower TTFT<br/><small>up to -36.3%</small>"]
  G -->|tool call| C["CPU tools<br/><small>distributed</small>"]
  C -->|returns| W
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class W,C input
  class V,DP loop
  class G core
  class O exit
  linkStyle 5 stroke:#f08c00,stroke-width:2px
  linkStyle 6 stroke:#f08c00,stroke-width:2px
```

<div class="dg-legend">Blue is sessions and tools, amber is the scheduling decision and the tool loop, purple is the GPU pool, green is the latency win.</div>

## Gaps

- Abstract reports best-case "up to" numbers against the best baseline per metric; medians are not given.
- Tool latency must be predictable for "near-term readiness" to be estimated; heavy-tailed tools (web search, human approval) may break the estimate.

## How it relates to prior wiki pages

- **Confirms** that agent serving is a distinct workload. The 10-29 AKV paper added cache operations for agents; DeepInfer (10-29) moved prefix KV to SSD with 3-day agent retention. TAO adds the scheduler that decides who gets the warm cache. See [KV cache](kv-cache.md).
- **Industry tie.** Intel's CEO says the server CPU:GPU ratio went from 1:8 to 1:4 as agents run more tools. TAO is the research version of the same observation: the CPU side now gates GPU utilization.

## Related

[KV cache](kv-cache.md) · [Prefix-aware routing](../ai-routing/2026-10-30-agentbaton-capable-to-cheap-handoff.md) · [Compute economics](../hardware/compute-economics.md)
