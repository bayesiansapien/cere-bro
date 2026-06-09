---
source: farmer/huggingface
farmed: 2026-06-09T11:13:01Z
arxiv_id: 2606.06735
url: https://huggingface.co/papers/2606.06735
arxiv_url: https://arxiv.org/abs/2606.06735
date: 2026-06-09
---

# A Geometric Account of Activation Steering through Angle-Norm Decomposition

Linear activation steering has gained popularity as a simple and empirically effective way to control language model behavior. More recently, spherical steering paradigms have been proposed to address limitations of additive interventions, often motivated by the assumption that hidden-state norm does not carry concept-relevant information. In this work, we revisit this assumption through a controlled empirical study designed to disentangle the roles of angular and radial components. We show that steering methods differ mainly in how they couple two geometric effects: changing a token's angular alignment with a concept direction and changing its hidden-state norm. Across seven language models, we find that concepts are represented primarily in angular structure, supporting the motivation for spherical methods, but that norm remains important for the stability and downstream effects of steering. Our results explain why interventions with similar concept-level effects can behave differently, and suggest that activation steering should be parameterized by interpretable angular and radial components of the intervention, rather than by a single additive coefficient that entangles these two effects.
