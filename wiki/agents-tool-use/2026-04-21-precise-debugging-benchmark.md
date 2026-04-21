# Precise Debugging Benchmark: Models Regenerate, They Don't Debug

**Date:** 2026-04-21  
**Source:** HuggingFace Daily Papers  
**Paper:** [arxiv 2604.17338](https://arxiv.org/abs/2604.17338)  
**Raw:** [raw/huggingface/2026-04-21-precise-debugging-benchmark-is-your-model-debugging-or-regene.md](../../raw/huggingface/2026-04-21-precise-debugging-benchmark-is-your-model-debugging-or-regene.md)

---

## TL;DR

PDB (Precise Debugging Benchmark) measures not just whether bugs are fixed but *how precisely*: edit-level precision (necessary edits only) and bug-level recall (all bugs resolved). Frontier models (GPT-5.1-Codex, DeepSeek-V3.2-Thinking) achieve >76% unit test pass rates but precision below 45% — they regenerate correct but over-edited solutions rather than making targeted fixes. Iterative and agentic debugging strategies don't improve precision or recall.

---

## Key Findings

- **Two new metrics**: edit-level precision (fraction of edits that are necessary), bug-level recall (fraction of bugs actually resolved, not just masked)
- **Unit test pass rate is misleading**: models that pass 76%+ of tests have precision below 45% — they're rewriting code, not debugging it
- **Over-editing is the dominant failure mode**: models replace large code sections that don't need to change
- **Agentic strategies don't help**: iterative debugging with tool use doesn't improve precision or recall — the fundamental failure is in the post-training objective, not the inference strategy
- **Two benchmarks released**: PDB-Single-Hard (single-line bugs) and PDB-Multi (multi-line bugs)

---

## Connection to Prior Wiki Work

This is the fourth consecutive benchmark in the wiki measuring the same meta-failure: frontier models appear to solve a task by conventional metrics but avoid the hard, targeted reasoning the task actually requires.

| Benchmark | What models avoid | Surface metric | Real metric |
|-----------|------------------|----------------|-------------|
| AIMO 3 (04-17) | Hard reasoning under fixed compute | Majority vote score | pass@20 gap |
| DR3-Eval (04-18) | Genuine multi-source synthesis | Recall | Citation accuracy |
| GTA-2 (04-20) | Multi-step tool coordination | Single-step pass rate | Workflow completion |
| PDB (04-21) | Targeted fault localization | Unit test pass | Edit precision |

The pattern: **passing the benchmark ≠ doing the thing the benchmark is meant to test.** In every case, models find a shortcut that satisfies the surface metric without solving the underlying cognitive task.

---

## Implications for Coding Agent Post-Training

The PDB result is a direct indictment of coding model post-training pipelines. If models are trained to maximize unit test pass rate, they learn to regenerate correct solutions — which is correct behavior under that reward signal but wrong behavior for a debugging assistant. The fix requires a post-training objective that explicitly rewards *surgical editing*, not just correctness.

---

## Related Pages

- [DR3-Eval: Deep Research Benchmark](2026-04-18-dr3-eval-deep-research-benchmark.md)
- [GTA-2: Tool Agent Benchmark](2026-04-20-gta-2-tool-agent-benchmark.md)
- [Claude Code Architecture](2026-04-19-claude-code-architecture.md)
