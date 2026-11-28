---
source: farmer/huggingface
farmed: 2026-11-28T10:45:04+05:30
arxiv_id: 2611.32238
url: https://huggingface.co/papers/2611.32238
arxiv_url: https://arxiv.org/abs/2611.32238
date: 2026-11-27
---

# Boundary-Aware Policy Learning for Agent-Orchestrated Robot Manipulation

Agent-orchestrated robot systems combine the general reasoning capability of multimodal agents with the precise physical control of learned visuomotor policies. Yet such systems often fail at the moment of handoff: a policy is reliable only from a limited set of start states, while the agent may invoke it outside this region. We call this region the policy's handoff boundary. Existing whole-task policies typically have handoff boundaries that are narrow and difficult for an agent to characterize, making reliable coordination challenging. We propose Boundary-Aware Policy Learning, which explicitly shapes and then expands the handoff boundary of a visuomotor policy. First, Boundary-Explicit Training fine-tunes the policy on contact segments with diverse start poses, yielding a wide and well-defined boundary that can be communicated to the agent through a simple handoff protocol. Second, Boundary-Expanding Self-Improvement retrains the policy on curated successful system rollouts, extending the boundary toward earlier stages of each task and allowing the agent to hand over sooner with fewer language-model calls. Across RoboTwin 2.0 and RoboDojo, our system outperforms the strongest baseline by over 26 percentage points, reaching 98.4% success in randomized RoboTwin 2.0 scenes, while further reducing its API cost and execution time by 41.3% and 37.5%, respectively. These results suggest that the key to robust agent-policy orchestration lies not only in improving either component individually, but also in explicitly shaping the boundary between them.
