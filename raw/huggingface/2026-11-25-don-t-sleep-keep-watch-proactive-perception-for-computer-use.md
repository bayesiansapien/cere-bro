---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.28947
url: https://huggingface.co/papers/2611.28947
arxiv_url: https://arxiv.org/abs/2611.28947
date: 2026-11-25
---

# Don't Sleep, Keep Watch: Proactive Perception for Computer-Use Agents

Computer-use agents (CUAs) built on vision-language models are increasingly entrusted with long-horizon tasks in live desktop, web, and mobile environments, where the screen keeps changing on its own. However, current CUAs lack real-time situational awareness: they perceive the environment through discrete snapshots, and the substantial inference latency of VLMs, compounded by highly dynamic interfaces, opens a perception-action gap in which the observed state frequently becomes stale before the corresponding action is executed. To bridge this gap, we present NightWatch, a plug-and-play framework that endows any CUA with continuous, temporally grounded perception without changing the agent's model, prompt, or action space. NightWatch couples the VLM agent with NightWatch-0.8B, a lightweight System-1 model that performs streaming monitoring of the interface state and keeps the agent synchronized with the evolving environment at low computational cost and latency, thereby grounding each decision in the current state rather than an outdated snapshot and reducing both stale actions and idle waiting while preserving task success. Experiments on desktop and dynamic web environments (OSWorld-Verified and DynaCU-Bench) show that NightWatch, driven by a watcher of only 0.8B parameters, reduces non-reasoning wall-clock time by 33% and wasted time by 53% on OSWorld while keeping task success on par, raises success on DynaCU-Bench from 39.5% to 44.2% with the large VLM agent, and is more efficient than passive-watching baselines such as AOI and PUSV under the same screenshot-only input, as well as a System-1 decision model more than 30times its size. Overall, NightWatch demonstrates that the timing of perception is as critical as its content, marking a step toward agents that maintain continuous awareness of their environment rather than perceiving it turn by turn.
