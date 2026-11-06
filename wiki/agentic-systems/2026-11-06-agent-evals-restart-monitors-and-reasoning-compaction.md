# Agent shorts: restart monitors, turn budgets, reasoning compaction, latent thinking, and new research benchmarks

**Sources:** [Monitor Accuracy Isn't the Answer, arXiv:2610.36544](https://arxiv.org/abs/2610.36544) · [What Does Multi-Turn RL Really Improve?, arXiv:2611.06483](https://arxiv.org/abs/2611.06483) · [Why Pay for Long Reasoning, arXiv:2611.03852](https://arxiv.org/abs/2611.03852) · [TAC-CoT, arXiv:2611.01926](https://arxiv.org/abs/2611.01926) · [Hybrid Computer Use, arXiv:2610.41432](https://arxiv.org/abs/2610.41432) · [SleuthVLM, arXiv:2611.06083](https://arxiv.org/abs/2611.06083) · [FrontierPhysics, arXiv:2611.06910](https://arxiv.org/abs/2611.06910) · [HarnessGrad](https://github.com/zjunlp/HarnessGrad) · raw: [raw/huggingface/](../../raw/huggingface/2026-11-05-monitor-accuracy-isn-t-the-answer-a-decision-value-framework.md)

**TL;DR.** The shared theme is measuring what an agent spends against what it actually gets. Restart monitors are judged by the wrong metric. Multi-turn RL gains vanish when turn budgets tighten. Rewriting a model's earlier reasoning into compact notes shortens its later reasoning without retraining. Three new research benchmarks show frontier agents still mostly fail end-to-end research.

## Items

- **Restart monitors (2610.36544).** A monitor with a fixed 90% accuracy can swing from a 5-point loss to a 35-point gain, depending only on how likely a fresh attempt is to succeed with the remaining budget. In 194 executions on SWE-bench Verified SymPy issues, a 2.29-point apparent gain traced to one surviving attempt, a second model lost 42.29 points, and none of 103 live comparisons met the certification bar. The paper offers a decision-sufficiency test for whether a compressed summary keeps the information needed to act.
- **Multi-turn RL (2611.06483).** Pass@(K,T) evaluates sampling breadth and turn depth together. RL's gains depend on sufficient turn budgets and concentrate in error recovery, not better single-step decisions. BudgetMix RL varies budgets in training for robustness.
- **Reasoning compaction (2611.03852).** Rewriting prior reasoning into compact state records before tool results arrive usually shortens later reasoning in open-weight models, with less repeated verification. It can cut total spend, though quality and rewrite-inclusive time depend on the target and compressor.
- **TAC-CoT (2611.01926).** Replaces explicit reasoning with latent segments and keeps text only for tool calls, observations and answers. Up to +8.8 points and up to 6.8x fewer forward passes.
- **Hybrid Computer Use (2610.41432).** Unifies code, accessibility and GUI channels, with batched actions and accessibility diffs to reduce round trips. Top Partial and Binary scores on OSWorld 2.0.
- **SleuthVLM (2611.06083).** A vision agent over transcribed speech beats omni models that hear audio: 75.0% on four benchmarks, 2.6 points above Gemini 3.8 Flash. "Hearing is not the bottleneck, agentic ability is."
- **FrontierPhysics (2611.06910).** 56 tasks from 42 physicists. No configuration passes more than 46 of 168 rollouts. Weakness is rigor and expert intuition, not knowledge.
- **Science's Last Exam ([@omarsar0](https://x.com/omarsar0/status/2118392657651057140), [@rohanpaul_ai](https://x.com/rohanpaul_ai/status/2118419224616128901)).** 113 tasks in 9 disciplines, graded by hidden checks and against studies published after training cutoff. DeepSeek V4.1 Flash led hypothesis generation at 21.28%.
- **DeepFinance ([@ycombinator](https://x.com/ycombinator/status/2118539585433284626)).** A long-horizon benchmark of 21 high-finance problems.
- **HarnessGrad (ZJU).** A platform crossing 8 harnesses, 19 self-improvement methods and 56 benchmarks, with the model held fixed so only the harness learns.
- **Claude Code status-line fix ([@b1rkh0ff](https://x.com/b1rkh0ff/status/2118091433538166951)).** Background subagents were re-reading the entire conversation every 30 seconds to update a status line. The fix cuts that cost about 99%, or roughly 5% of total limit use.

## How this relates to prior wiki pages

- **Extends** [NVIDIA's frequent compaction (11-05)](../inference-efficiency/2026-11-05-context-budget-compaction-and-context-rot.md) from tool history to the model's own reasoning. The restart-monitor paper's decision-sufficiency test is the missing way to check whether a compaction lost anything that matters.
- **Parallels** [DEPTH (11-05)](2026-11-05-agent-environments-and-harness-shorts.md), which found that task depth, not turn count, predicts difficulty.
- **Confirms** [agent benchmarks](agent-benchmarks.md): SemiAnalysis's GDPx (11-05, no agent above 12%) and today's three benchmarks all keep research-grade work far from solved.
- **Tension:** on the harness thread, HarnessGrad treats the harness as a learner while KernelSeek ([summary](../hardware/2026-11-06-kernelseek-question-driven-kernel-optimization.md)) strips it down.

## Gaps

The restart study is on 19 SymPy issues only. Reasoning compaction has no fixed quality guarantee. Benchmark scores are initial and self-run by their authors.
