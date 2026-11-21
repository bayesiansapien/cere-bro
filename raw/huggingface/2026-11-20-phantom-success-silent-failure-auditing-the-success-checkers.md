---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.388578+00:00
arxiv_id: 2611.25179
url: https://huggingface.co/papers/2611.25179
arxiv_url: https://arxiv.org/abs/2611.25179
date: 2026-11-20
---

# Phantom Success, Silent Failure: Auditing the Success Checkers of Simulated Manipulation Benchmarks

Simulated manipulation benchmarks measure policy performance using hand-written success checkers that label each episode as a success or failure. Passing an expert demonstration shows that a checker accepts one way of completing the task. Learned policies, however, may stop after partial progress or complete the task in a different way. A checker may then accept an incomplete execution (phantom success) or reject an execution that satisfies the instruction (silent failure). In this paper, we introduce SimAudit, an LLM-based pipeline that audits success checkers against task instructions. SimAudit analyzes the instruction and checker code to identify scenarios where the two may disagree, recreates those scenarios in simulation, and runs the original checker. Multi-view renderings are then used to verify whether the observed behavior satisfies the instruction. Across RoboTwin 2.0, RoboCasa365, and RoboDojo, 183 simulated test cases produced the predicted checker verdict. Visual verification and deduplication yielded 61 distinct defects across 49 tasks, including 40 phantom successes and 21 silent failures. Most defects in RoboCasa365 accepted incomplete executions, most in RoboDojo rejected valid executions, and both error types were common in RoboTwin 2.0. These findings suggest that validating success checkers requires testing both incomplete executions and valid alternatives to expert demonstrations, and motivate more rigorous evaluation protocols for future benchmarks.
