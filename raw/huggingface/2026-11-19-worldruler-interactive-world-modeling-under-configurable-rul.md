---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.141092+00:00
arxiv_id: 2611.24869
url: https://huggingface.co/papers/2611.24869
arxiv_url: https://arxiv.org/abs/2611.24869
date: 2026-11-19
---

# WorldRuler: Interactive World Modeling under Configurable Rules

Rules govern how player actions change interactive worlds. Different rules create distinct gameplay experiences within similar scenes and action spaces. For customizable gameplay, generative world models must follow user-defined rules beyond real-world behaviors. However, realizing user-defined rules presents two challenges: Rule-State Persistence and Rule-to-Visual Realization. The former requires preserving rule definitions, dependencies, and world states across saving and loading, so that restored worlds follow the established rules. The latter requires accurately realizing rule-induced changes on designated objects and attributes, particularly when affected objects are unseen. In this paper, we propose WorldRuler, which organizes rule definitions, dependencies, and object states in an executable 3D rule graph and connects rule execution, video generation, and perceptual feedback in a closed loop. The graph supports joint saving and restoration of rules and world states, while dynamic object binding grounds rule-specified entities in visual instances and uses stored states to constrain generation from their first appearance. We further introduce object attribute state replacement and counterfactual reconstruction training, enabling accurate attribute control and compatible appearance and motion changes while limiting interference with unrelated content. We develop an automated data collection and annotation pipeline using GTA-V and Habitat to construct RuleVerse, a dataset of rule-driven interactions with detailed state and event annotations, including cases where rules take effect before affected objects become visible. Extensive experiments demonstrate the effectiveness of WorldRuler in preserving rule-state consistency across saving and loading and accurately realizing rule outcomes on designated objects and attributes.
