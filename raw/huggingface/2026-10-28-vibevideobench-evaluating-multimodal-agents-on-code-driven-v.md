---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.993448+05:30
arxiv_id: 2610.35864
url: https://huggingface.co/papers/2610.35864
arxiv_url: https://arxiv.org/abs/2610.35864
date: 2026-10-28
---

# VibeVideoBench: Evaluating Multimodal Agents on Code-Driven Video Generation

Diffusion video models produce striking clips, but they cannot reliably render an exact formula, a correct chart, a rule-consistent game or narration synchronized to on-screen events. A different route is emerging: multimodal agents that write code to render every frame and synthesize every sound. We introduce VibeVideoBench, a benchmark for evaluating agents on code-driven video generation. Its 239 self-contained tasks in English and Chinese span 12 categories, from data stories and music-driven pieces to classroom lessons and paper explainers; each asks an agent, running in its native harness inside a sandbox with no image or video generation model, to deliver a finished MP4 with sound within one hour. Evaluation is hierarchical and evidence-based: program checks of the delivery spec, about 13k task-specific rubric checks traced to the requirements they enforce, and five quality dimensions anchored per task, scored by three VLM judge panels. Across nine frontier agent systems and 2,151 scored rollouts, GPT-6 Astra and Claude Opus 5.5 rank first and second with both the judges and human annotators, and the strongest system satisfies every core requirement on 76.3% of tasks. Delivery is a second axis: counting missing videos as zero changes the ranking, and three quarters of the lost videos are final renders that started too late, ran too slowly or never started, a failure of how agents plan their hour. Agents build their own rendering pipelines and inspect their own frames, yet how much they look does not predict quality. The judges' ranking of the systems closely matches blind human preferences.
