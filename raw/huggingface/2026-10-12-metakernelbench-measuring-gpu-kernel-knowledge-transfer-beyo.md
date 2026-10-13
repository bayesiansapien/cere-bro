---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.219918+05:30
arxiv_id: 2610.05014
url: https://huggingface.co/papers/2610.05014
arxiv_url: https://arxiv.org/abs/2610.05014
date: 2026-10-12
---

# MetaKernelBench: Measuring GPU Kernel Knowledge Transfer Beyond Code

Recent GPU kernel optimization agents retain what they learn in knowledge bases or as distilled skills. Kernel benchmarks score each attempt's implementation for correctness and speed but leave the reuse value of retained experience unmeasured. We introduce MetaKernelBench, which measures whether experience distilled from an attempt in one kernel domain-specific language (DSL) improves a fresh attempt at the same problem in another. Its 74 problems are fused subgraphs in six families, each posed as a pair of CuTe DSL and TIRx variants that differ only in the DSL. The agent first attempts each variant solo and is instructed to distill what it learns into a natural-language skill, which is transferred whether or not the source attempt passes verification. The skill is the only extra input to a skill-conditioned attempt by the same model in the other DSL. We compare each skill-conditioned attempt with the solo attempt on the same variant under matched per-attempt budgets, scoring correctness and end-to-end runtime. Across six models and both directions, paired lift over solo attempts ranges from -19% to +29%. Four models gain in both directions, yet regressions occur on 16% to 45% of problems in every model and direction. Outcomes follow the source attempt's result relative to the target's solo attempt rather than source success alone, improving in 71% of comparisons when the source stands above and regressing in 54% when it stands below. MetaKernelBench complements implementation-quality metrics by measuring same-problem cross-DSL kernel knowledge transfer.
