---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.364796+05:30
arxiv_id: 2611.02017
url: https://huggingface.co/papers/2611.02017
arxiv_url: https://arxiv.org/abs/2611.02017
date: 2026-11-04
---

# Switch-SWE: Do Coding Agents Hold Focus When Switching Between Unfinished Tasks?

Software development sessions often involve several unfinished tasks rather than one issue carried through to completion. As coding agents take on repository-level development, they need to recover an earlier task's requirements and partial progress after intervening work. Existing repository-level benchmarks typically score one issue-to-patch episode and do not directly measure whether an agent can resume a task after advancing other unfinished work in the same repository. We introduce \ourmethod, a benchmark for focus-task resumption in sessions that interleave unfinished tasks drawn from the same source repository, with a persistent checkout for each task. Each focus task is evaluated in matched uninterrupted and switched sessions with identical focus requirements and executable verifiers. The switched session interleaves ordered stages from other unfinished tasks in the same repository, while only the final focus patch is scored. \ourmethod~contains 200 focus tasks from 19 Python repositories, reconstructed from issue, pull-request, and review histories and rendered as 400 matched session specifications. Across 7 coding agents, interleaved unfinished work produces an average focus-task resolution gap of 11.5 percentage points, ranging from 6.0 to 15.0 percentage points. Trajectory analysis identifies cross-task requirement confusion and loss of task state as recurrent resumption behaviors. We introduce a plug-in context-management module that selects task-relevant history and maintains concise task-state summaries. On OpenCode, the module improves focus-task completion under same-repository task switching by 5.5 to 15.5 percentage points across the evaluated models. Code is available at github.com/Miraclecsc/Switch-SWE.
