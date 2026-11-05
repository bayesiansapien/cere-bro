---
source: farmer/huggingface
farmed: 2026-11-05T20:36:55.365979+05:30
arxiv_id: 2611.01927
url: https://huggingface.co/papers/2611.01927
arxiv_url: https://arxiv.org/abs/2611.01927
date: 2026-11-04
---

# Is Your Long-Horizon Benchmark Really Deep? Measuring and Synthesizing Depth in Terminal Tasks

Long-horizon terminal tasks are used to evaluate and train agents. Human-curated datasets are scarce, so many synthesis methods have emerged. They usually measure the length of a task by the turns a model needs to pass it, and its difficulty by labels the LLM sets during generation. We find, however, that the turn count largely reflects the habits of the model, not only the demands of the task, and that the labels barely track how often models pass. We describe a terminal task by its work, the number of operations it requires, and its depth, the number of turns that must happen in sequence because the commands of each turn can only be chosen after reading the output of the previous one. Estimating depth as the smallest turn cap, stated to the agent, under which the task passes, we audit 734 tasks from six existing datasets. Synthesis has mostly added work, not depth: 94% of the solved synthetic tasks pass within three turns, yet depth, unlike the turn count, predicts difficulty beyond work. We propose DEPTH, in which a generation agent writes each task one segment at a time in a real software environment, carrying out each segment before writing it and starting the next from the state it leaves. Our 105 tasks exceed every audited dataset in depth and work, and none of six current models passes half of them. Fine-tuning Qwen3-8B on runs from these tasks improves it on two terminal benchmarks.
