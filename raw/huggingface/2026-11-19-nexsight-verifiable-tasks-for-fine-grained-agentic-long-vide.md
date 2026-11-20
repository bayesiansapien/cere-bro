---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.146865+00:00
arxiv_id: 2611.22790
url: https://huggingface.co/papers/2611.22790
arxiv_url: https://arxiv.org/abs/2611.22790
date: 2026-11-19
---

# NexSight: Verifiable Tasks for Fine-Grained Agentic Long-Video Understanding

Fine-grained questions about long videos ask how many times an action occurs, in what order events unfold, or exactly when a state changes. Answering them can require finding brief moments scattered across hours of footage. Agentic models that decide when and where to look promise to find these moments, yet this ability is hard both to measure and to learn. Sparse supporting evidence may establish that an action occurred without establishing its total count; verifying timeline-wide claims requires checking for missed occurrences and double counting. Answer-only supervision, in turn, does not explicitly supervise the search for evidence. We present NexSight, which builds verifiable tasks to both evaluate and train agentic long-video understanding. Its agentic pipeline, SightForge, accepts a task only if a verifier blind to the draft answer can reconstruct it from evidence densely reacquired from the raw video and counterexample checks fail to refute it. This yields SightLine, 310 evidence-traceable tasks from 108 long videos, evaluated through SightLoop, a shared multiscale harness supporting temporal exploration, local inspection, evidence integration, and revisiting while recording returned observations. On disjoint videos, solver trajectories on verified tasks become step-level supervision for observation decisions. The strongest model reaches only 54.52% on SightLine, yet 79.35% when given the annotated evidence. With under 6K examples, Sight-35B nearly doubles its base model's interactive accuracy (21.29% to 42.26%), outperforms the 397B model of its family, begins using explicit spatial inspection after post-training, which its base model never uses, and gains over 8 points on two external long-video benchmarks.
