# SCOPE: Self-Play via Co-Evolving Policies for Open-Ended Tasks

**TL;DR.** Self-play (a model improving by generating its own training signal) can train LLMs without external supervision, but prior methods need rule-checkable answers. That leaves open-ended tasks, where there is no single correct answer, dependent on curated prompts or frontier-model judges. SCOPE is a DATA-FREE self-play framework for open-ended tasks. It co-evolves two policies: a Challenger that generates document-grounded tasks, and a Solver that answers them via multi-turn retrieval (fetching relevant passages across several steps). A FROZEN copy of the initial model acts as the self-judge: it writes task-specific rubrics from the source document and grades Solver responses against them. Across three 7-8B instruction-tuned models (Qwen2.5, Qwen3, OLMo-3), SCOPE improves open-ended performance up to +10.4 points on eight benchmarks, and matches or exceeds GRPO trained on about 9K curated prompts. Despite training only on open-ended tasks, it also improves held-out short-form QA up to +13.8 points on seven benchmarks.

```
┌────────────┐  doc-grounded tasks  ┌──────────────────────┐
│ Challenger │ ───────────────────► │ Solver               │
│            │ ◄─────────────────── │ (multi-turn retrieval)│
└────────────┘     responses        └──────────┬───────────┘
        ▲                                       │
        │            ┌──────────────────────────▼──────────┐
        └────────────│ frozen self-judge: writes rubric from │
          rewards    │ source doc, grades responses          │
                     └───────────────────────────────────────┘
```

## Key points

- Data-free self-play for open-ended tasks: no curated prompt set and no external frontier judge required.
- Two co-evolving policies: a Challenger that generates document-grounded tasks and a Solver that answers via multi-turn retrieval.
- A frozen copy of the initial model is the self-judge. It writes task-specific rubrics from the source document and grades against them.
- Up to +10.4 points on eight open-ended benchmarks across three 7-8B models, matching or beating GRPO trained on roughly 9K curated prompts.
- Trains only on open-ended tasks, yet transfers: up to +13.8 points on seven held-out short-form QA benchmarks.

## Gaps in the study

- The frozen self-judge caps quality at the initial model's grading ability. A weak starting judge limits the ceiling.
- Document-grounded tasks may not cover all open-ended skills, since every task is anchored to a source document.
- Tested at 7-8B scale only.

## How it relates to prior wiki pages

SCOPE extends the verifier-free, co-evolving self-improvement thread the wiki has been tracking.

- **G-Zero (2026-05-12)** did verifier-free self-improvement using a Hint-delta intrinsic reward, with a Proposer and a Generator. SCOPE shares the no-verifier stance but targets open-ended generation rather than reward signals derived from hints.
- **CoPD (2026-05-01)** introduced co-evolving policy distillation, where experts mutually distill during parallel RLVR. SCOPE's Challenger-Solver pair is the same co-evolution idea applied to task generation and solving rather than expert distillation.

SCOPE pushes the thread into open-ended generation by adding a document-grounded self-judge. It also pairs with **SAVE (today)**, which improves a reward model on-policy without new human labels. Both are same-day attempts to remove the human or external supervision bottleneck, from opposite ends: SCOPE removes the need for curated prompts and external judges, SAVE removes the need for fresh preference data.

## Links

- Paper: [arxiv 2605.31433](https://arxiv.org/abs/2605.31433)
- Related concept pages: [rl-for-llms.md](rl-for-llms.md)
- Raw source: [raw/huggingface/2026-06-01-scope-self-play-via-co-evolving-policies-for-open-ended-task.md](../../raw/huggingface/2026-06-01-scope-self-play-via-co-evolving-policies-for-open-ended-task.md)
