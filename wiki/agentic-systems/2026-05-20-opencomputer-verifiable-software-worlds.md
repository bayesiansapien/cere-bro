# OpenComputer: Verifiable Software Worlds for Computer-Use Agents

**Source:** HuggingFace Daily Papers 2026-05-20 · [arXiv 2605.19769](https://arxiv.org/abs/2605.19769) · [raw](../../raw/huggingface/2026-05-20-opencomputer-verifiable-software-worlds-for-computer-use-age.md)

## TL;DR

A verifier-grounded framework for constructing verifiable software worlds for computer-use agents. Four components: (1) app-specific state verifiers that expose structured inspection endpoints over real applications; (2) a self-evolving verification layer that improves verifier reliability using execution-grounded feedback; (3) a task-generation pipeline that synthesizes realistic and machine-checkable desktop tasks; (4) an evaluation harness that records full trajectories and computes auditable partial-credit rewards. Coverage: 33 desktop applications, 1,000 finalized tasks spanning browsers, office tools, creative software, development environments, file managers, and communication. Hard-coded verifiers align more closely with human adjudication than LLM-as-judge, especially when success depends on fine-grained application state. Frontier agents struggle with end-to-end completion despite partial progress; open-source models drop sharply from their OSWorld-Verified scores.

## Why it matters

OSWorld-Verified scores have been the headline number for computer-use agents. OpenComputer's verifier-grounded harness shows the OSWorld numbers do not transfer cleanly to a wider verifier surface. The pattern (in-distribution accuracy decoupled from out-of-distribution capability) matches AgentKernelArena (2026-05-19), PAGER (2026-05-18), DiagnosticIQ (2026-05-18), CurveBench (2026-05-17), and WildClawBench (2026-05-15). Six benchmarks in six days showing the same structural gap.

## Connections

- **EnvFactory (today)** synthesizes environments from docs; OpenComputer builds deeper environments with hard-coded verifiers over real applications. Different scales of the same idea.
- **AgentKernelArena (2026-05-19)** found shape-specific hardcoding in GPU-kernel agents. OpenComputer finds the analogous pattern (in-distribution capability not transferring) for desktop applications. The pattern is now six benchmarks in six days, and the failure mode (configuration-specific hardcoding masquerading as capability) is the running structural diagnosis.
