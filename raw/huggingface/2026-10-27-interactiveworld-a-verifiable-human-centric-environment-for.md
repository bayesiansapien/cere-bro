---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.33966
url: https://huggingface.co/papers/2610.33966
arxiv_url: https://arxiv.org/abs/2610.33966
date: 2026-10-27
---

# InteractiveWorld: A Verifiable Human-Centric Environment for Building Better Interactive MLLM Assistants

People have long dreamed of an assistant that is always there to guide them and remind what they forget, from new dishes to lost keys. Powered by multimodal large language models (MLLMs), egocentric AI assistants on wearable devices are bringing this dream within reach: they see what the user sees and give instructions for user's physical work when necessary. However, testing such assistance is challenging and usually requires real people. The expensive and rare real interaction data leaves a key question unanswered: Can today's MLLMs truly help people in physical world? To answer this question, we propose InteractiveWorld, the first verifiable environment for closed-loop interaction between human and AI assistant. Unlike existing robot-centric simulators, InteractiveWorld lets the assistant guide a human agent who observes the scene, understands instructions, and acts independently. It thus realistically simulates how AI assistant collaborates with human: the assistant instructs, the human acts, and the environment executes actions and updates what they see next. Building on it, we introduce InteractiveBench, the first dynamic benchmark for egocentric AI assistants, with 120 multi-turn tasks across six categories. In each task, the assistant guides the human in real time, and every instruction shapes the outcome, which is scored by verifiable, state-based rewards. Experiments with 12 frontier MLLMs show they are still far from reliable assistants. Even the strongest model, Claude Fable 5.1, achieves at most 20% and 25% on long-horizon Guidance and Planning tasks, respectively. Overall, our work offers a verifiable platform and a rigorous evaluation set, laying a solid foundation for research on interactive MLLM assistants that truly help people in the physical world.
