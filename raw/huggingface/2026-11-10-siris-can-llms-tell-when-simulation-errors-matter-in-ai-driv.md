---
source: farmer/huggingface
farmed: 2026-11-11T05:06:31.324353+00:00
arxiv_id: 2611.10329
url: https://huggingface.co/papers/2611.10329
arxiv_url: https://arxiv.org/abs/2611.10329
date: 2026-11-10
---

# SIRIS: Can LLMs Tell When Simulation Errors Matter in AI-Driven Systems Research

LLM agents increasingly drive systems research and rely on simulators to evaluate candidate designs at scale. Simulators are imperfect by design: their modeling limitations can distort predictions yet leave the recommended design correct, or change which design should be selected. We introduce Siris to test whether LLMs can tell these cases apart, judging from their systems understanding when a limitation invalidates the simulator's recommendation. By perturbing a simulator, Siris constructs workload pairs with the same candidates, limitation, and simulator recommendation. The perturbation changes predictions on both workloads, yet a reference simulator supports the recommendation on only one. Evaluating thirteen frontier LLMs on LLM serving design problems, we find that identifying a limitation does not ensure a correct choice, and even the strongest models sometimes abandon valid recommendations. Self-correction through a review turn helps these models restore valid choices but introduces new errors in several others. These findings motivate evaluating systems understanding through design decisions under imperfect simulators.
