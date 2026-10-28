---
source: farmer/huggingface
farmed: 2026-10-28T10:37:11+05:30
arxiv_id: 2610.33861
url: https://huggingface.co/papers/2610.33861
arxiv_url: https://arxiv.org/abs/2610.33861
date: 2026-10-27
---

# ReGE: Stronger Agents through Experience Synthesis

Repeated attempts at interactive tasks uncover facts, useful operations, and failures that can inform subsequent execution. We introduce ReGE, a framework for turning this recorded experience into guidance for a fresh attempt. Its main implementation, ReGE-Syn, uses a single coach call to jointly synthesize bounded execution records and available artifacts into self-contained guidance, connecting task-specific findings with proposed actions and relevant pitfalls. A student starts from the task's initial environment state and adapts this guidance to current observations. Source generation, synthesis, and student execution use the same base model, without parameter updates or a stronger teacher. Across four benchmarks, ReGE improves accuracy by an average of 9.9 percentage points for GPT and 8.8 percentage points for Claude compared with unguided execution. On matched BrowseComp-Plus subsets, ReGE-Syn reduces guidance-construction tokens by 98.2\% on GPT and 95.5\% on Claude relative to adapted AggAgent, with observed success. Combined construction and execution tokens decrease by 15.7\% and 35.4\%, respectively, counting input plus output and excluding source generation. BrowseComp-Plus ablations further associate access to process information with fewer student steps and show that joint synthesis produces substantially shorter guidance than Direct history or Independent summaries, with observed success. These results demonstrate how agents can use their own recorded experience to improve subsequent task completion, and suggest a low-cost way to consolidate the execution records of parallel agent systems such as agent swarms.
