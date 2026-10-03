---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.821849+00:00
arxiv_id: 2610.00313
url: https://huggingface.co/papers/2610.00313
arxiv_url: https://arxiv.org/abs/2610.00313
date: 2026-10-02
---

# Rules to Tools: Executable Checks for LLM Agents in Scientific Computing

Scientific coding agents receive equations, boundary conditions, and output requirements in writing, then must assess the programs they revise. Rules to Tools (R2T) supplies prepared executable checks of public scientific requirements. Matched SciCode repair groups share written checks, starting programs, model, and budgets; the tool group receives a callable implementation. Across two task-ID cohorts, complete repair is 26/30 with text and 29/30 with the prepared checks. Three task IDs favor tools, one favors text, and eleven tie. The eight-ID cohort scores 13/16 versus 15/16, with a task-cluster bootstrap 95% interval of [-12.5, 43.75] percentage points for the difference. The larger shared-definition SciCode cohort ties at 13/24 per group. Five development-exposed tasks with alternate starting programs score 3/10 versus 7/10. The tool group favors tasks 17, 77, and 11; initial checks flag task 17 and report no violation for tasks 77 and 11. Task 37 favors text and has no initial reported violation. A fresh source-through-Python arm also reaches 15/16, matching the dedicated command's aggregate. In a matched PDE comparison, detailed text scores 23/24 and checks score 24/24, with 31.2% lower reported model output for checks. Agent-side output savings vary by cohort, while public CPU use rises in both task-ID cohorts. These results measure task-dependent repair outcomes and agent-side costs with prepared checks.
