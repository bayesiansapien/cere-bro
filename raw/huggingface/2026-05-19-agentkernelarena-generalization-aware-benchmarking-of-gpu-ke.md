---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.16819
url: https://huggingface.co/papers/2605.16819
arxiv_url: https://arxiv.org/abs/2605.16819
date: 2026-05-19
---

# AgentKernelArena: Generalization-Aware Benchmarking of GPU Kernel Optimization Agents

GPU kernel optimization is increasingly critical for efficient deep learning systems, but writing high-performance kernels still requires substantial low-level expertise. Recent AI coding agents can iteratively read code, invoke compilers and profilers, and refine implementations, yet existing kernel benchmarks evaluate single LLM calls rather than full agent workflows, and none include both kernel-to-kernel optimization and unseen-configuration generalization testing. We present AgentKernelArena, an open-source benchmark for measuring AI coding agents on GPU kernel optimization. The benchmark contains 196 tasks spanning HIP-to-HIP optimization, Triton-to-Triton optimization, and PyTorch-to-HIP translation, and evaluates complete agent workflows in isolated workspaces using gated compilation, correctness, and performance checks, centralized scoring and an unseen-configuration generalization protocol that tests whether optimizations transfer to input configurations the agent never observed. Across production agents including Cursor Agent, Claude Code, and Codex Agent, we find near-perfect compilation and high correctness rates on most task categories, with the strongest configurations achieving mean speedups of up to 6.89x on PyTorch-to-HIP, 6.69x on HIP-to-HIP, and 2.13x on Triton-to-Triton tasks. Our unseen-configuration evaluation shows that HIP-to-HIP and Triton-to-Triton optimizations largely transfer to unseen input shapes, while PyTorch-to-HIP exhibits substantial correctness drops, indicating that agents generating kernels from scratch frequently hardcode shape-specific assumptions. AgentKernelArena is designed as a modular, extensible framework for rigorous evaluation of agentic GPU kernel optimization across agents, tasks, and hardware targets.
