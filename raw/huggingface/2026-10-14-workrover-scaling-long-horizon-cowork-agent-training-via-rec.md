---
source: farmer/huggingface
farmed: 2026-10-15T09:08:24.500769+00:00
arxiv_id: 2610.18067
url: https://huggingface.co/papers/2610.18067
arxiv_url: https://arxiv.org/abs/2610.18067
date: 2026-10-14
---

# WorkRover: Scaling Long-Horizon Cowork Agent Training Via Recursive Environment Evolution

Scaling interactive environments is important for training long-horizon agents through reinforcement learning. These environments often require further testing and refinement after initial generation, and correcting defects in a task may also require updating its work context and verifier. However, existing construction pipelines offer limited support for such iterative refinement while keeping these components aligned. We introduce WorkRover, a framework for training long-horizon cowork agents through recursive environment evolution. Its harness-driven synthesis enables construction agents to jointly build and validate semantically aligned work contexts, executable tasks, and evidence-grounded verifiers, adapting their actions to workspace state and execution feedback rather than following a fixed construction workflow. To support environment evolution, we introduce Factorial Compatibility Replay (FCR), which uses rollout feedback to evaluate combinations of component revisions through dependency-closed replay and selects the smallest validated repair among tested candidates while preserving task requirements and evaluation constraints. To provide finer-grained training signals, we propose Verifier-to-Turn Credit Assignment (VTCA), which augments trajectory-level GRPO advantages with signals from deterministic workspace-progress checks and assigns a bounded share of positive-progress credit to prerequisite turns using recorded tool-output and artifact dependencies. Using WorkRover, we post-train Qwen3.5-35B-A3B to obtain WorkRover-35B-A3B and evaluate it on several cowork-agent benchmarks. Its reported scores exceed those of Qwen3.5-35B-A3B by 26.27 percentage points on JobBench, 29.32 percentage points on OfficeQA Pro, and 413.25 Elo points on GDPval v2. These results suggest that WorkRover offers a promising foundation for scalable training of long-horizon cowork agents.
