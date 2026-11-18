---
source: farmer/huggingface
farmed: 2026-11-18T05:07:04.108833+00:00
arxiv_id: 2611.20218
url: https://huggingface.co/papers/2611.20218
arxiv_url: https://arxiv.org/abs/2611.20218
date: 2026-11-17
---

# SWE-CoWork: Benchmarking Coding Agents as Digital Employees in Organizations

A coding agent working within a software organization must establish what to build, collaborate with colleagues, and verify what it delivers. We introduce SWE-CoWork, a benchmark comprising 101 development assignments across 101 real repositories, 11 programming languages, and 12 application domains. Each assignment places an agent in a simulated engineering organization with 26 colleagues who have distinct responsibilities, bounded knowledge, and controlled collaboration behavior. Starting from a brief handoff, agents must recover requirements distributed across colleagues and workplace records, reconcile conflicting evidence, and implement changes evaluated by private executable tests. We evaluate eleven models and find a substantial gap between partial implementation and complete task delivery. The two leading models satisfy approximately 63% of fail-to-pass (F2P) tests but complete fewer than 8% of assignments. Providing complete requirements upfront improves F2P by approximately 16 percentage points for Seed Evolving and GPT-6 Astra, yet leaves complete task success unchanged. Requirement-level trajectory analysis reveals failures throughout the delivery process: Claude-Opus-5.5 directs a mean of 93% of first questions about queried cards to their accountable owners across runs but obtains only 64% of colleague-held requirements. Deferred questions go unfollowed, implementations remain incomplete even after requirements are acquired, and 31% of requirements reported as completed fail their tests. These findings highlight sustained requirement tracking, from clarification through implementation, verification, and handoff, as a key challenge for reliable autonomous software engineering.
