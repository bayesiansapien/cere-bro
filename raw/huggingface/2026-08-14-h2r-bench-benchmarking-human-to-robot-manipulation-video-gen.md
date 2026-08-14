---
source: farmer/huggingface
farmed: 2026-08-14T11:17:27.766803
arxiv_id: 2608.13049
url: https://huggingface.co/papers/2608.13049
arxiv_url: https://arxiv.org/abs/2608.13049
date: 2026-08-14
---

# H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models

Large-scale manipulation data is essential for robot learning, yet collecting robot demonstrations remains expensive and difficult to scale. Meanwhile, abundant egocentric human manipulation videos provide rich behavioral experiences, but transferring them across embodiments remains challenging due to differences between human hands and robotic end-effectors. Recent advances in video world models offer a promising pathway to synthesize robot-centric manipulation videos from human observations, while their cross-embodiment transfer capability remains largely unexplored. Therefore, we introduce H2R-Bench, a benchmark for evaluating cross-embodiment human-to-robot manipulation video generation, where models transform egocentric human demonstrations into robot manipulation videos under specified embodiments. Each benchmark instance contains a human demonstration video, target embodiment constraints, and source-grounded annotations covering task goals, action events, functional contacts, and object responses. H2R-Bench evaluates generated videos through five dimensions, including goal-state completion, action-event completion, functional contact transfer, embodiment correctness, and general video quality. We benchmark eleven state-of-the-art video generation models across six manipulation families and two robot embodiments. Our evaluation reveals that current video world models remain limited in human-to-robot manipulation transfer: even leading models often fail in embodiment consistency, functional interaction, and task execution. H2R-Bench provides a systematic diagnostic framework for evaluating whether video world models can bridge the human-to-robot embodiment gap and convert human manipulation observations into robot-centric training resources.
