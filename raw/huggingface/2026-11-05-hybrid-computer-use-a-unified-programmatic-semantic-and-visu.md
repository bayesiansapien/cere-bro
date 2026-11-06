---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.302003+00:00
arxiv_id: 2610.41432
url: https://huggingface.co/papers/2610.41432
arxiv_url: https://arxiv.org/abs/2610.41432
date: 2026-11-05
---

# Hybrid Computer Use: A Unified Programmatic, Semantic, and Visual Interface for General Agents

Computer-use agents increasingly tackle tasks ranging from everyday desktop activities to long-horizon professional workflows. Yet interfaces centered on screenshots and mouse-and-keyboard actions can impose a human-interaction prior, requiring repeated screen interpretation while leaving the computer's semantic and programmatic capabilities underexposed. We argue for exposing these capabilities and letting models choose and combine them. We introduce Hybrid Computer Use (HCU), a unified interface for general agents that combines three complementary channels: programmatic interaction through code and command-line tools, semantic interaction through accessibility (AX), and visual interaction through graphical user interfaces (GUI). Our HCU supports efficient AX interaction and guards against stale-state actions during channel switching. A supplementary HCU skill guides agents in selecting and coordinating channels to use the unified interface effectively. Our designed AX tools return compact observations, execute actions in batches, and report their effects as AX diffs, so the model needs fewer round trips. On OSWorld 2.0, HCU achieves the highest Partial and Binary scores among the compared systems. Analyzing agent trajectories, we find that all evaluated models improve with HCU yet allocate work across the channels differently and consistently outperform compared baselines in terms of both efficiency and task success, highlighting the value of unified computer-use interfaces that allow flexible channel selection and combination.
