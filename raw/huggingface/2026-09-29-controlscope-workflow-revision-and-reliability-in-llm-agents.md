---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.935995+00:00
arxiv_id: 2609.34313
url: https://huggingface.co/papers/2609.34313
arxiv_url: https://arxiv.org/abs/2609.34313
date: 2026-09-29
---

# ControlScope: Workflow Revision and Reliability in LLM Agents

How much of a running workflow should a language model agent revise? ControlScope compares continuing generated code, editing the next tool call's data arguments, and replacing the unfinished workflow from the same public execution state. The nested permissions separate available repairs from the actions an agent selects. We evaluate one-time and repeated reviews across filesystem tasks, ALFWorld, and AppWorld. Across two source programs per task and three reasoning-reviewer draws on 20 filesystem tasks, FULL completes 15-16 tasks versus 13 for KEEP; across four fast draws it completes 10-13 versus 13. Fresh student-record confirmation reproduces a batch-read repair. ALFWorld fast panels yield KEEP/ARG/FULL scores of 85/86/87 on 87 tasks across 52 scenes and 134/134/127 on 134 tasks across four scenes; reasoning on the 87-task cohort also yields 85/86/87 with substantial review cost. An AppWorld V1 official-test panel of 585 task instances from 195 scenario templates shows small net differences. Frozen replays expose viable agent-written replacements interrupted by later revision in two failed file-organization runs. An offline source-trajectory midpoint comparison shows later reviews completing an insufficient repair. Five-call protection saves 19.4% of logged model output and loses one success across 20 fresh source runs. An argument-only shortcut shows that the broader sampled policy can overlook a cheaper successful edit available in both operation sets. These outcomes tie repair access to actual choices and subsequent execution.
