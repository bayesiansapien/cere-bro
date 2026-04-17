---
source: raw/huggingface/2026-04-17-cross-tokenizer-llm-distillation-through-a-byte-level-interf.md
arxiv: https://arxiv.org/abs/2604.07466
date: 2026-04-17
---

# Cross-Tokenizer LLM Distillation via Byte-Level Interface

## TL;DR

Distilling knowledge from a teacher model to a student model is easy when both use the same tokenizer. When they don't (cross-tokenizer distillation, CTD), the vocabulary mismatch makes token-level supervision impossible. This paper proposes the simplest fix: convert to bytes first, distill at the byte level, convert back. Competitive with or better than much more complex CTD methods.

## Key Findings

- **Problem**: token vocabularies differ between models — you can't align a teacher's probability distribution over its tokens with a student's distribution over different tokens
- **BLD (Byte-Level Distillation)**: converts teacher's output distribution to byte-level probabilities, attaches a lightweight byte-level decoder head to the student, distills through the shared byte-level interface
- **Performance**: competitive with and on several benchmarks surpasses significantly more complex CTD methods; validated from 1B to 8B parameters
- **Honest limitation**: consistent improvements across all tasks remain elusive — CTD is still an open problem

## How It Works

```
Teacher model (vocab A)          Student model (vocab B)
       │                                  │
       ▼                                  ▼
Token probs (vocab A)          Byte-level decoder head (new)
       │                                  │
       ▼                                  │
Byte-level probs  ────── distillation ───►│
(shared interface)                        │
                                          ▼
                                  Student learns from
                                  teacher's byte distribution
                                  (vocabulary-agnostic)
```

## Why It Matters

As models proliferate with different tokenizers (Llama, Qwen, Gemma, etc.), cross-tokenizer distillation becomes practically important. Most approaches use complex vocabulary alignment heuristics. BLD replaces that complexity with a universal shared representation — bytes — that all models can map to. Simple, works, open problem remains.

## Related Pages

- [Knowledge Distillation](knowledge-distillation.md)
