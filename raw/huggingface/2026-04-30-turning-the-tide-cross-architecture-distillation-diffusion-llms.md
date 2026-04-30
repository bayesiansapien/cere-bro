---
source: farmer/huggingface
farmed: 2026-04-30T00:00:00Z
arxiv_id: 2604.26951
url: https://huggingface.co/papers/2604.26951
arxiv_url: https://arxiv.org/abs/2604.26951
date: 2026-04-30
---

# Turning the TIDE: Cross-Architecture Distillation for Diffusion Large Language Models

**Authors:** Gongbo Zhang, Wen Wang, Ye Tian, Li Yuan (Peking University, Zhejiang University)

Diffusion large language models (dLLMs) offer parallel decoding and bidirectional context, but state-of-the-art dLLMs require billions of parameters for competitive performance. While existing distillation methods for dLLMs reduce inference steps within a single architecture, none address cross-architecture knowledge transfer, in which the teacher and student differ in architecture, attention mechanism, and tokenizer. We present Tide, the first framework for cross-architecture dLLM distillation, comprising three modular components: (1) Tidal, which jointly modulates distillation strength across training progress and diffusion timestep to account for the teacher's noise-dependent reliability; (2) CompDemo, which enriches the teacher's context via complementary mask splitting to improve predictions under heavy masking; and (3) Reverse Calm, a cross-tokenizer objective that inverts chunk-level likelihood matching, yielding bounded gradients and dual-end noise filtering. Distilling 8B dense and 16B MoE teachers into a 0.6B student via two heterogeneous pipelines outperforms the baseline by an average of 1.53 points across eight benchmarks, yielding notable gains in code generation, where HumanEval scores reach 48.78 compared to 32.3 for the AR baseline.

## Key contributions

- **First cross-architecture dLLM distillation**: Handles teacher-student differences in architecture, attention mechanism, and tokenizer — not just step compression within a single architecture.
- **Three modular components**:
  - *Tidal*: Dynamic distillation-strength scheduling across training progress and diffusion timestep (the "pacemaker").
  - *CompDemo*: Complementary mask splitting to enrich teacher context under heavy masking.
  - *Reverse Calm*: Inverted chunk-level likelihood matching for cross-tokenizer transfer with bounded gradients.
- **Two heterogeneous pipelines**: (A) cross-tokenizer from 16B MoE LLaDA2; (B) shared-tokenizer from 8B dense WeDLM — both distilled into 0.6B BD3LM student.
- **Results**: +1.53 avg across 8 benchmarks; HumanEval 48.78 vs 32.3 AR baseline; 22x memory reduction, 5x faster inference vs teacher.
