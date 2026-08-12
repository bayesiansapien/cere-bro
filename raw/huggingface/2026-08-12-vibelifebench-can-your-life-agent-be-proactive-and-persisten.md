---
source: farmer/huggingface
farmed: 2026-08-12T03:35:42Z
arxiv_id: 2608.10875
url: https://huggingface.co/papers/2608.10875
arxiv_url: https://arxiv.org/abs/2608.10875
date: 2026-08-12
---

# VibeLifeBench: Can Your Life Agent Be Proactive and Persistent in a Living World?

Large language model (LLM) agents are increasingly deployed as personal assistants. Existing evaluations, however, mostly use short, self-contained requests in static environments. Everyday life assistance is different. A task runs for weeks rather than minutes. The world keeps changing while the agent is not being prompted. Many constraints are never stated outright. An agent that merely answers the request in front of it will fail at such a task. What is needed instead is an agent that stays proactive and consistent. It decides on its own when to act, when to ask, and when to stay silent. It notices changes that nobody announced. It keeps one plan coherent from the first day to the last. No current benchmark measures this. We introduce VibeLifeBench, a benchmark of 200 long-horizon tasks across ten everyday-life domains. Each task is a scripted multi-week timeline in a simulated world of 22 mock services. The world advances on its own clock, and many of its changes are silent, so only an agent that re-inspects the world discovers them. Every task is graded by fine-grained, weighted checks that read only what the agent actually left behind, covering the end state, the timeliness of its actions, and whether it upheld the implicit constraints. We evaluate seven frontier models. All of them score low, which shows how far current agents are from assisting with real life. We will open-source all tasks, environments, and the evaluation framework.
