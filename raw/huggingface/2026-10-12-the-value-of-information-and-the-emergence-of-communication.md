---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.222986+05:30
arxiv_id: 2610.13118
url: https://huggingface.co/papers/2610.13118
arxiv_url: https://arxiv.org/abs/2610.13118
date: 2026-10-12
---

# The value of information and the emergence of communication in evolved e-puck robots

We study when communication emerges between autonomous agents and what role an innate action selection architecture plays. Two e-puck robots, reconstructed in PyBullet from their Webots model and validated against it, must find a feeding zone that can only be detected when a robot passes over it. Each robot can emit a one-bit signal whose direction is detected by the receiver. Control is provided by a GRU recurrent network with a residual path, either operating alone or as a channel within an Embedded Action Selection Architecture (EASA). Fitness measures only the time the robots spend over the food. When the robots receive a compass pointing to the food, use of the signal disappears completely. Without a compass, in a small arena, three independent runs achieved similar performance using different strategies: a referential signal, a permanent beacon, or no use of the signal. As the arena expands, the strategy based on a referential signal generalizes best. In contrast, evolving directly in the large arena does not increase the frequency of communication, but it does separate the strategies, and the referential signal clearly outperforms solitary searching. Within EASA, innate reflexes constrain the network and reduce performance. As its priorities evolve, evolution consistently weakens those reflexes. The results suggest that communication emerges in proportion to the value of the information it transmits, and that an innate scaffolding designed for isolated agents can be an impediment in a social task.
