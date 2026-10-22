---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.17724
url: https://huggingface.co/papers/2610.17724
arxiv_url: https://arxiv.org/abs/2610.17724
date: 2026-10-20
---

# Evidence-First Agentic Verification

Long-horizon, semi-verifiable agentic tasks often rely on rubric-based evaluation, but the evidence needed to assess these tasks can be spread across the environment state and the execution trace. A judge may overlook this evidence or accept unsupported claims, including an agent's own reports of success. When rubric verdicts serve as reinforcement-learning rewards, such errors can reinforce undesirable behavior. We introduce Sauron, an evidence-first agentic verifier that investigates both state and trace and relies on a claim only after independently validating it against its source. Bounded queries and joint investigation of related criteria reduce context use and redundant work, and each verdict carries an auditable receipt of its supporting evidence. Across 2,586 human-labeled criteria from 100 personal-assistant episodes, Sauron achieves the highest F1 of five verifiers on all eight backbones tested while costing less than Gandalf, the strongest baseline. With GPT-5.6 Sol, it reaches 0.96 F1 versus Gandalf's 0.92 at 23% lower cost, with a wider margin on process criteria. On a paired fault-injection suite covering 13 families, several of which simulate reward hacking, Sauron detects 97% of injected failures while flagging only 2% of clean controls, outperforming baselines even when they are given the full trace. On TRAIL, a benchmark for detecting and localizing real agent errors, Sauron leads both Gandalf and TRAIL's own judge on all three quality metrics.
