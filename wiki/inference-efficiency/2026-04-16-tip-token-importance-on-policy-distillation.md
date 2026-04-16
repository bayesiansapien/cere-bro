---
date: 2026-04-16
source: huggingface
arxiv: 2604.14084
---

# TIP: Token Importance in On-Policy Distillation

**TL;DR:** TIP identifies two regions of high learning signal in on-policy knowledge distillation: high-entropy tokens (uncertain student) and low-entropy + high-divergence tokens (overconfident but wrong student). Entropy-based selection retaining 50% of tokens matches full training while cutting peak memory by 47%; including overconfident tokens enables near-full performance with <10% of tokens.

## Key Findings

- **Two-axis taxonomy** (TIP): student entropy × teacher-student divergence. High signal comes from both ends.
- **High-entropy tokens**: student is uncertain — obvious learning signal.
- **Low-entropy, high-divergence tokens**: student is overconfident and wrong — dense corrective signal, nearly invisible to entropy-only rules.
- Retaining 50% of tokens via entropy sampling: matches all-token training, reduces peak memory by **47%**.
- Training on <10% of tokens (targeting overconfident tokens) nearly matches full-token baselines.
- Validated across Qwen3, Llama, Qwen2.5 on MATH-500 and AIME 2024/2025; also on DeepPlanning for agentic long-horizon tasks.

## Related Pages

- [Knowledge Distillation](knowledge-distillation.md)

**Raw source:** [../../raw/huggingface/2026-04-16-tip-token-importance-in-on-policy-distillation.md](../../raw/huggingface/2026-04-16-tip-token-importance-in-on-policy-distillation.md)
