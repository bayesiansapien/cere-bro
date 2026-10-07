---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.02459
url: https://huggingface.co/papers/2610.02459
arxiv_url: https://arxiv.org/abs/2610.02459
date: 2026-10-06
---

# OpenRUA: Robot-Use Agents Are Zero-Shot Visuomotor Policies

Coding agents are extending their reach into the physical world by writing and executing robot control programs. One might expect the agents to use the existing mature software stack that engineers have developed over decades to access sensors and control motion. Yet prior work primarily engineers complex custom harnesses to orchestrate agents for robot use, particularly by prescribing specialized workflows and providing bespoke interfaces. This raises the question: "Is such additional harness engineering necessary?" We introduce OpenRUA, a zero-abstraction harness that bypasses bespoke abstraction layers by providing off-the-shelf coding agents with only terminal access to the robot's native software interface ROS 2. OpenRUA employs a minimalist workspace-as-harness design, only offering ROS 2 documentation and basic tools while leaving the coding agent to organize its own work without orchestrating any agentic workflow. Within this workspace, OpenRUA recasts perception as file I/O and manipulation as coding. With Claude Code powered by Claude Opus 5, OpenRUA achieves success rates of 99.0% on CaP-Bench and 87.0% on LIBERO-PRO, demonstrating that an off-the-shelf coding agent can serve as a zero-shot visuomotor policy through the robot's native interface, without bespoke primitives or task-specific training. Under this minimalist design, further analysis reveals striking emergent behaviors of coding agents: (1) For perception, the agent spontaneously writes programs that process raw sensory inputs and derive metric measurements in 96.80% of episodes. (2) For manipulation, the agent spontaneously builds motion-control clients (e.g., gripper control) in 95.87% of episodes and closed-loop control programs (e.g., adjusting motion based on sensor feedback) in 50.13% of episodes. Our code is available at https://github.com/terminalworld/OpenRUA.
