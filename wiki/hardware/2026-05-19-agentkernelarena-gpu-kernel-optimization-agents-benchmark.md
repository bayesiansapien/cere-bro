# AgentKernelArena: Generalization-Aware Benchmarking of GPU Kernel Optimization Agents

**arXiv:** [2605.16819](https://arxiv.org/abs/2605.16819) · **HF:** [paper page](https://huggingface.co/papers/2605.16819) · **Tier:** 1 (GPU kernels, agentic systems, benchmarks)

## TL;DR

AgentKernelArena is the first GPU-kernel-optimization benchmark designed for full agent workflows (read code, invoke compilers, run profilers, iterate) rather than single-shot LLM calls. 196 tasks across HIP-to-HIP, Triton-to-Triton, and PyTorch-to-HIP translation, evaluated in isolated workspaces with gated compilation / correctness / performance checks, plus an unseen-configuration generalisation protocol. Across Cursor Agent, Claude Code, and Codex Agent, best configurations reach mean speedups of 6.89x (PyTorch-to-HIP), 6.69x (HIP-to-HIP), and 2.13x (Triton-to-Triton). HIP-to-HIP and Triton-to-Triton optimisations largely transfer to unseen input shapes; PyTorch-to-HIP exhibits substantial correctness drops, meaning agents generating kernels from scratch frequently hardcode shape-specific assumptions.

## Key findings

- Existing GPU kernel benchmarks evaluate single LLM calls. None included kernel-to-kernel optimisation, none tested unseen-configuration generalisation, and none evaluated full agent workflows where the agent reads code, runs compilers and profilers, and iterates.
- AgentKernelArena's 196 tasks span three workflows: HIP-to-HIP optimisation (same language, optimise existing kernel), Triton-to-Triton optimisation (same), and PyTorch-to-HIP translation (cross-language, generate a kernel from a PyTorch reference).
- Evaluation is in isolated workspaces with gated compilation, correctness, and performance checks plus centralised scoring. The unseen-configuration protocol tests whether the agent's optimised kernel still runs correctly on input shapes the agent never observed during the optimisation loop.
- Best configurations of Cursor Agent, Claude Code, and Codex Agent reach mean speedups of 6.89x (PyTorch-to-HIP), 6.69x (HIP-to-HIP), and 2.13x (Triton-to-Triton). Correctness rates are near-perfect on most task categories.
- Unseen-configuration evaluation: HIP-to-HIP and Triton-to-Triton optimisations largely transfer to unseen shapes. PyTorch-to-HIP exhibits substantial correctness drops, meaning agents that generate kernels from scratch tend to hardcode shape-specific assumptions.
- Framework is modular and extensible across agents, tasks, and hardware targets.

## Relationship to prior wiki entries

The wiki's GPU-kernel agent thread now has three stable entries. KernelBench-X (2026-05-09, the LLM GPU-kernel benchmark covering 16 frontier models on 250 PyTorch operations measuring correctness, speedup, hardware utilisation, and cross-GPU consistency) was the single-call benchmark. Cutile-rs (2026-05-17, the Rust-based CUDA tile programming substrate flagged in last week's social-stream) is on the authoring side. Fournex GPU bottleneck analyser (2026-05-18 Industry Pulse, the open-source tool that turns Nsight Compute output into evidence-backed CUDA optimisation recommendations classified by bottleneck type) is on the diagnostic side.

AgentKernelArena fills the third leg: the agentic-workflow benchmark. The 6.89x mean speedup on PyTorch-to-HIP and 6.69x on HIP-to-HIP is the first time the wiki has tracked agentic kernel optimisation hitting the 6x range on a curated benchmark; it indicates that the agent-harness improvements the field has been making in coding agents (Composer 2.5 today, Claude Code at large-codebase scale, Codex CLI's RL with textual feedback) translate to GPU-kernel-specific tasks.

The PyTorch-to-HIP correctness drop on unseen shapes is the load-bearing failure mode finding. It echoes the wiki's broader thread on deployment-calibration brittleness: WildClawBench (2026-05-15, the 18-point harness spread), CurveBench (2026-05-17, the visual-reasoning RLVR-recoverable gap), PAGER and DiagnosticIQ (2026-05-18, the GUI-and-industrial-rule calibration benchmarks). All five say: agents look strong on the configurations they saw, fragile on configurations they did not. AgentKernelArena now extends that pattern from text-domain tasks to GPU-kernel generation.

## Why it matters

GPU kernels are the substrate of inference and training cost. The cost of human kernel-authoring time on H200, B200, and now Blackwell B300 is the primary bottleneck for porting research code to production. A benchmark that measures agentic kernel optimisation under realistic workflow conditions, with generalisation testing, is the missing measurement infrastructure for that bottleneck. The 6x speedups on HIP-to-HIP and PyTorch-to-HIP at near-perfect correctness on seen configurations are large enough to justify the human-time investment in setting up AgentKernelArena harnesses inside production teams.

The shape-hardcoding failure on PyTorch-to-HIP is the deployment caveat. Frontier serving stacks have heterogeneous shapes across workloads. A kernel that runs 6x faster at the optimised shape but breaks at adjacent shapes is not deployable. The benchmark is the diagnostic; the open question is which agent-harness recipe (parameterised generation, shape-aware prompting, explicit unseen-configuration training) closes the gap.

## Research angle

- **What harness-level change closes the shape-hardcoding gap?** The current failure is in the agent's coding pattern, not the underlying LLM. Whether explicit shape-parameterisation prompts, dimensional-symbol training, or shape-aware autotuning solves it is the natural follow-up.
- **Cross-hardware generalisation.** The benchmark targets HIP (AMD) and Triton (cross-vendor). Whether the same agents transfer to CUDA-native kernels with H200 / B200 / Blackwell-specific intrinsics is the next question. AgentKernelArena is extensible across hardware targets; the wiki should track the first CUDA-on-Blackwell results.
- **Composing with the kernel-diagnostic stack.** The 2026-05-18 Fournex bottleneck analyser produces evidence-backed remediations. The natural recipe is to give the agent that analyser's output as a tool call. Whether the agent that has tooling beats the agent that does not, and by how much, is the deployment-relevant compose.

## Source

`raw/huggingface/2026-05-19-agentkernelarena-generalization-aware-benchmarking-of-gpu-ke.md`
