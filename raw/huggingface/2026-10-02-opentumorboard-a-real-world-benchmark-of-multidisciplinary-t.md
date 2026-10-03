---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.820570+00:00
arxiv_id: 2609.32810
url: https://huggingface.co/papers/2609.32810
arxiv_url: https://arxiv.org/abs/2609.32810
date: 2026-10-02
---

# OpenTumorBoard: A Real-World Benchmark of Multidisciplinary Tumor Board Discussion Trajectories

Multidisciplinary tumor boards integrate multimodal clinical observations and longitudinal patient histories through specialist discussions, yet benchmarks rarely capture these real-world trajectories. We introduce OpenTumorBoard, a benchmark with 611 patient cases and 19,157 discussion turns across ten specialist roles, transcribed from 12,534 minutes of publicly available tumor board recordings on YouTube. The benchmark evaluates two settings: SPECIALIST TURN, in which an LLM responds to a clinically significant question posed during a real discussion, and BOARD SIMULATION, in which it generates an entire back-and-forth discussion and reaches a consensus on therapy recommendations, surgical plans, next actions and clinical trial matching. Evaluation of 14 general-purpose frontier and medical LLMs reveals substantial limitations: the best models score 3.43 out of 5 in clinical equivalence to specialist answers and 2.78 out of 5 in alignment with recorded board conclusions. Supervised finetuning and reinforcement learning improve performance on a held-out test set, suggesting that real-world discussion trajectories can support model adaptation. Three M.D. experts review a subset of the benchmark, finding high information coverage and factuality of patient cases and strong fidelity of extracted consensus conclusions. We will release OpenTumorBoard and its automated curation pipeline to support the development and evaluation of LLMs for multidisciplinary, personalized cancer decision-making.
