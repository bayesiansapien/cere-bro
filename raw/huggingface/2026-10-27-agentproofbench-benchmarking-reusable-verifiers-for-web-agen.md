---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.34634
url: https://huggingface.co/papers/2610.34634
arxiv_url: https://arxiv.org/abs/2610.34634
date: 2026-10-27
---

# AgentProofBench: Benchmarking Reusable Verifiers for Web Agents

Reusable Web-agent verification requires a rule to follow changing requirements and support subsequent execution. We introduce AgentProofBench, which connects paired tests of a frozen acceptance rule to execution from identical saved openings. The resource spans 97 tasks, 79 families, and four Web services. Experiments with DeepSeek Flash/Pro establish two linked measurements. Across 48 families, complete-panel and decision-replay tests retain 82/96 Flash and 79/96 Pro source programs; paired reuse-rebuild BA intervals are [-5.47, 1.57] and [-10.16, 0.00] percentage points. Across 22 execution families, deployment-state panel correctness separates program assignments whose two saved openings are both delivered correctly: 32/33 assignments with error-free panels, versus 1/11 with panel errors. All reference-defined program-gate regressions and withheld deliveries occur in the latter group. Neutral continuation attains the highest correct delivery under the tested generic feedback, providing a concrete baseline for measuring the value added by a gate. Released instructions, states, programs, reference rules, and trajectories connect each test failure to its execution consequences. AgentProofBench makes reusable verification assessable at both the requirement and policy levels.
