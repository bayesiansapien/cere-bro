---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.04929
url: https://huggingface.co/papers/2610.04929
arxiv_url: https://arxiv.org/abs/2610.04929
date: 2026-10-06
---

# RobotUse: Allocating Computation, Context, and Decisions

Robot agents must connect their intended actions to observed outcomes while retaining the context needed to revise their choices over repeated attempts. Existing interfaces often leave these choices inside predefined tools or require agents to manage detailed execution code and its growing history. We introduce RobotUse, a robot agent harness that organizes computation, context, and decisions around specifying and revising physical actions. Agents visually select targets and poses, while the backend handles geometry, motion planning, and control. Subagents retain detailed interactions within each subgoal and return the information needed for subsequent decisions. Continual harnessing lets agents learn from execution by updating a persistent playbook. On RoboLab, RobotUse achieves 45% task success, outperforming CaP-X by 6.7 percentage points while maintaining compact decision contexts and reducing reliance on predefined action abstractions. Furthermore, we show that RobotUse learns from real-world execution despite imperfect feedback and transfers what it learns to subsequent tasks. Project page is available at https://robotuse-team.github.io/.
