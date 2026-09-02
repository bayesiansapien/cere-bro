---
source: farmer/huggingface
farmed: 2026-09-02T13:31:46.243214
arxiv_id: 2609.00768
url: https://huggingface.co/papers/2609.00768
arxiv_url: https://arxiv.org/abs/2609.00768
date: 2026-09-02
---

# DiagEvo: Diagnosis-Guided Self-Evolution via Hierarchical Error Memory

Self-play is an effective paradigm for language-model self-evolution, but without guidance, solver performance can plateau or decline across rounds. Unguided methods steer question generation with signals such as difficulty, learnability, or diversity. These signals keep questions challenging and varied but do not specify which unresolved reasoning weaknesses later rounds should target. Guided methods obtain direction from external task resources, including human examples, document corpora, or specified difficulty targets, and therefore rely on task information supplied outside the self-play loop. We show that the needed direction can instead be derived from the solver's own failure history. We introduce DiagEvo, whose diagnostician extracts recurring error causes from this history and stores them in a hierarchical error-cause memory. The memory groups related causes under skill nodes and tracks each as Active or Mastered according to self-consistency on targeted questions. The challenger uses these states and recurrence counts to balance cause-targeted generation with free exploration. Double-confidence filtering retains intermediate-difficulty questions only when the most common solver answer has a clear vote lead. DiagEvo derives its curriculum from information produced during self-play, without external task resources. With the default 4B diagnostician, DiagEvo outperforms every baseline in mean accuracy across all nine benchmarks for each of the three solvers: Qwen3-4B, Qwen3-8B, and OctoThinker-8B. On Qwen3-8B, it reaches 72.3% mean accuracy across five mathematical reasoning benchmarks, 4.5 percentage points above R-Zero. Its mean accuracy across all nine benchmarks is 57.4%, 1.1 percentage points above DARC. Ablations show that the hierarchical error-cause memory and double-confidence filtering both contribute to these gains.
