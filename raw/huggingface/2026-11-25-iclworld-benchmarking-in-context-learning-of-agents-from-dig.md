---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.32649
url: https://huggingface.co/papers/2611.32649
arxiv_url: https://arxiv.org/abs/2611.32649
date: 2026-11-25
---

# ICLWorld: Benchmarking In-Context Learning of Agents from Digital to Physical Worlds

In-context learning (ICL) lets agents acquire new rules from context and adapt to user-specific requirements at inference time. The same frontier agents now operate both computers and robots, yet their ICL remains insufficiently assessed: existing benchmarks are largely offline, rely on text or static images, and risk training-data contamination, while robot evaluations are limited to method-level ablations. We present ICLWorld, an online benchmark that evaluates the ICL of agents from digital to physical worlds, covering computer use and robot use, together with UIverse, a unified harness that turns every environment into a user interface. We build 30 environments, record 630 demonstration videos (10+ hours), and design 160 tasks with customized, often counter-intuitive rules that cannot be satisfied without learning from the context. Each task comes with three rule versions, given as text or video, and we test generalization at three levels, from replaying the demonstration to new instances and unseen environments. Across six frontier models, the strongest agents, Claude Opus 5.5 and GPT-6 Astra, succeed on 82% and 76% of computer-use runs but only 27% and 26% of robot-use runs, and a no-rule control reduces success to at most 8%. GPT-6 Astra succeeds under all three rule versions on only 38% of computer-use tasks, half its rate under a single rule, and answers 98% of robot rule questions correctly yet completes only 20% of these tasks. Frontier agents learn rules comparably well from video and from text and transfer them across environments, whereas weaker agents rely on text and lose most of their video-based success once the demonstrated situation is resampled. These findings reveal substantial gaps between the digital and the physical world and between identifying a rule and acting on it.
