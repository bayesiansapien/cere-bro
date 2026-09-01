---
source: farmer/huggingface
farmed: 2026-09-01T08:46:18.970698+00:00
arxiv_id: 2608.30396
url: https://huggingface.co/papers/2608.30396
arxiv_url: https://arxiv.org/abs/2608.30396
date: 2026-09-01
---

# Scaffolding Foundation Models into Physical-World Agents Pushes the Frontier of Long-Horizon Navigation

Long-horizon physical-world agents must reason over distant goals while grounding decisions in reliable closed-loop behavior. Today's foundation models split these capabilities: vision-language models (VLMs) infer missing information and adapt high-level plans but remain brittle and inefficient at repeated navigation grounding, while navigation foundation models (NFMs) robustly execute semantic goals but operate as bounded episodes without persistent task-level reasoning. We introduce NavMCP, an agentic scaffolding framework that couples a VLM reasoning agent with an NFM executor for long-horizon exploration. The VLM decides what evidence to seek, where to search, and when to stop, while the NFM grounds each semantic sub-goal into closed-loop navigation. Three channels structure their collaboration: intent translates evidence needs into navigation calls, observation converts rollouts into source-grounded trajectory evidence, and memory accumulates findings, negative evidence, and unresolved goals across calls. This design turns isolated navigation rollouts into persistent embodied interaction without retraining either model. On Embodied Question Answering, NavMCP achieves state-of-the-art results on HM-EQA, MT-HM3D, and EXPRESS-Bench. Under matched agent and executor backbones, it outperforms an episodic interface by 14.9 percentage points on HM-EQA. On a Unitree Go2, NavMCP reaches 78.3% success, with its margin over the strongest baseline growing from 10 to 45 points as the task horizon increases. These results demonstrate the potential of scaffolding complementary foundation models into long-horizon physical-world agents.
