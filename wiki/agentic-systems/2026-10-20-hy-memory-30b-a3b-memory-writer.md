# Hy-Memory-30B-A3B: a 3B-active memory writer that matches Opus 5

**Source:** Tencent Hunyuan model card and GGUF release on Hugging Face ([GGUF repo](https://huggingface.co/tencent/Hy-Memory-30B-A3B-GGUF), [tech report arXiv 2610.22196](https://arxiv.org/abs/2610.22196)), captured by the lab watcher 2026-10-19. Raw: [`raw/labs/2026-10-20-100728-labs.md`](../../raw/labs/2026-10-20-100728-labs.md)

## TL;DR

Agent memory frameworks (Mem0, MemOS, EverMemOS) use a general LLM on the write path: deciding what to store, how precisely, and how to merge new evidence. Tencent trains a specialist for only that job: a 30B MoE with **~3B active parameters**, trained inside the deployed harnesses in two stages (on-policy distillation from a teacher on the student's own memory chains, then RL with chunk-level credit). Swapping only the writer and holding retrieval, answer model and judge fixed, it averages **55.49 across four harnesses vs 54.62 for Claude Opus 5** and 53.64 for DeepSeek V4.1 Flash, including on EverMemOS, which was held out of training. GGUF quantizations hold up: **Q6_K 58.78%, Q8_0 57.63%, Q4_K_M 56.49%** on a LoCoMo slice, so the 18 GB Q4 file loses about two points.

<div class="dg-title">Only the write path changes</div>
<div class="dg-sub">A small specialist replaces the frontier model where memory gets written; everything downstream stays fixed.</div>

```mermaid
flowchart LR
  I["Conversation chunk<br/><small>new evidence</small>"] --> W["Memory writer<br/><small>3B active, specialist</small>"]
  W --> B["Memory bank<br/><small>Mem0, MemOS, ...</small>"]
  B --> R["Retrieval<br/><small>fixed top-k</small>"]
  R --> A["Answer model<br/><small>unchanged</small>"]
  A --> S["Score<br/><small>55.5 vs Opus 54.6</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class I input
  class W core
  class B,R,A loop
  class S exit
```

<div class="dg-legend">Purple is the only swapped component; amber parts are held fixed for the comparison.</div>

## How this relates to prior wiki pages

- **Role routing again:** Cohere (10-19) found cheap models are safe as planners, not implementers. Tencent finds a small model can own a narrow role (memory writing) at frontier quality once trained in-harness. See [agent-memory](agent-memory.md) and [llm-routing](../ai-routing/llm-routing.md).
- **Echoes Amazon's agent-memory audit** (surfaced on X today: check what actually got stored, QA scores alone mislead). Hy-Memory's eval holds the reader fixed, which is the right control.

## Gaps

- Evaluated on 20% subsamples; per-harness gains over Opus are small (0.0-2.9 points) and within likely noise on some metrics. Opus still wins LoCoMo on Mem0 by about 10 points.
