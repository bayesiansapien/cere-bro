---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.25861
url: https://huggingface.co/papers/2610.25861
arxiv_url: https://arxiv.org/abs/2610.25861
date: 2026-10-20
---

# ActionRoPE: action as coordinates for spatially consistent control in planar-camera game world models

Game world models have made rapid progress toward real-time interactive generation. Yet action control is still predominantly implemented as feature conditioning, leaving the model to learn from training data how each action should move the visual world. This formulation is poorly matched to a broad class of planar-camera worlds, such as top-down and isometric games. In these worlds, player motion induces a geometrically well-defined planar camera displacement. We observe that the key to spatially consistent control in such worlds is to represent the effect of each action directly in world coordinates. To this end, we introduce ActionRoPE, a parameter-free action interface that converts action-driven camera displacement into world-coordinate rotary positions. As a result, tokens corresponding to the same world location retain the same positional address across time. These world coordinates further expose a spatial asymmetry in generation: regions covered by the initial observation are geometrically known, while newly revealed regions remain to be synthesized. We therefore propose Coordinate-Conditioned Noise Scheduling (CNS), which assigns token-wise denoising schedules according to this known-new structure. It allows observed regions to stabilize earlier, while new content is generated with reference to them. Compared with four representative action-conditioning mechanisms, our approach follows the commanded motion more faithfully and reduces the revisit drift by 66% over the strongest baseline. The same interface transfers across video backbones from 1.3B to 33B parameters and to out-of-distribution scenes. Project Page: https://teawhite.cn/ActionRoPE/
