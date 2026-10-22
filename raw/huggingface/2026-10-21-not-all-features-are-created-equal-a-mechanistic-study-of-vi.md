---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.648455
arxiv_id: 2603.19233
url: https://huggingface.co/papers/2603.19233
arxiv_url: https://arxiv.org/abs/2603.19233
date: 2026-10-21
---

# Not All Features Are Created Equal: A Mechanistic Study of Vision-Language-Action Models

A fine-tuned Vision-Language-Action (VLA) policy can easily place the alphabet soup in the basket on command, just as it saw during fine-tuning. However, if the basket is shifted five centimeters to the left, it drops the soup off the table. We developed an interpretability pipeline to investigate what such a policy is computing. Injecting task A's activations into the action expert while the policy looks at task B's scene makes pi0.5 execute task A's motor trajectory in 99.6\% of episodes (n{=}1{,}968). The injected program is bound to absolute workspace coordinates and ignores the visible scene, which provides a mechanistic account of the perturbation brittleness that concurrent benchmarks report. The binding holds on a physical UR10e: directed replay redirects the commanded task in 26/26 rollouts in one direction and 18/26 in the other, with no-injection and random-direction controls at the floor, and once the source object is moved 10--15\,cm the arm grasps and releases at the recorded coordinates in 50/50 trials, picking up the wrong block when one sits there and closing on empty air when none does. Applying the same interventions to six VLAs on LIBERO, MetaWorld, SimplerEnv, and ALOHA over 420{,}000+ rollouts yields three further findings: every architecture encodes the instruction, and four of the five weight it below vision whenever the scene alone identifies the goal; under the standard replacement write-back the SAE pooling that preserves behavior is architecture-specific (pi0.5 per-token, SmolVLA indifferent), and goal selection and motor generation separate into VLM and expert pathways wherever the two are distinguishable. We release Action Atlas (https://action-atlas.com), an interactive platform covering all 520+ trained SAEs, 79 identified concepts, and the scored UR10e rollouts. Code: https://github.com/CWRU-AISM/action-atlas
