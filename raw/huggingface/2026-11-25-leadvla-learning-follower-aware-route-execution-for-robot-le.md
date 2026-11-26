---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.30149
url: https://huggingface.co/papers/2611.30149
arxiv_url: https://arxiv.org/abs/2611.30149
date: 2026-11-25
---

# LeadVLA: Learning Follower-Aware Route Execution for Robot Leading

Robot leading requires executing a route while continuously adapting to a designated follower. Existing robot-leading systems often mediate follower understanding and physical route execution through explicit states, planners, or modular interfaces; directly learning this coupling through end-to-end trajectory prediction can instead entangle route execution with follower response. We introduce LeadVLA, a structured multimodal policy that preserves the route as an explicit Path reference while learning a Pace for route progress and a Residual for local follower- and scene-conditioned adaptation. To make this problem trainable and measurable, we develop LeadInfra, a configurable Unreal Engine-based closed-loop data-generation infrastructure from which we instantiate an approximately 4M-sample training corpus, and LeadBench, a standardized benchmark with 108 fully held-out closed-loop episodes. LeadVLA achieves the highest task success (39.6%) among evaluated robot policies on LeadBench while maintaining strong route fidelity and follower responsiveness, and transfers to unseen real-world environments without real-world policy fine-tuning. Project Page: https://louiszengCN.github.io/LeadVLA_PAGE/
