---
source: farmer/huggingface
farmed: 2026-09-02T13:31:46.243214
arxiv_id: 2609.00092
url: https://huggingface.co/papers/2609.00092
arxiv_url: https://arxiv.org/abs/2609.00092
date: 2026-09-02
---

# Safin-1: Safety from Within through Memory-Native State Evolution

Long-horizon complex tasks require foundation models to accumulate information, maintain internal states, and adapt over extended interactions. Safety should be an intrinsic property of the model itself, rather than a behavioral constraint relying solely on external safeguards or post-hoc alignment such as supervised fine-tuning. This motivates Safety from Within, where safety-relevant capabilities are represented and invoked through the model's native computation. We present Safin-1, a family of foundation models realizing this principle through memory routing and state evolution. Safin-1 is built on Memory-Anchor Routing across Context History (MARCH), a network architecture that maintains structured memory states and selectively retrieves relevant historical information through content-conditioned routing. It supports test-time adaptation of persistent capability states without repeatedly modifying the backbone, enabling controlled specialization over a shared foundation. We investigate this interface on downstream safety tasks through a Safety State, demonstrating effective state-based adaptation with substantial safety improvements. More broadly, the routed-state interface unifies contextual memory and persistent capability adaptation within the model's native computation, reframing memory from a passive record of prior context into an active substrate for maintaining and evolving model behavior. Evaluations across general capabilities, long-context understanding, retrieval, and efficiency further validate Safin-1. These findings provide a path toward safety as a state-native and adaptively maintainable capability. This work is only an initial architectural exploration of Safety from Within, and substantial further work is needed to realize this broader vision.
