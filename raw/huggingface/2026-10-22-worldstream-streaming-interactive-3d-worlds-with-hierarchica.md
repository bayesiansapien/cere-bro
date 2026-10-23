---
source: farmer/huggingface
farmed: 2026-10-23T08:19:34.194493+00:00
arxiv_id: 2610.28827
url: https://huggingface.co/papers/2610.28827
arxiv_url: https://arxiv.org/abs/2610.28827
date: 2026-10-22
---

# WorldStream: Streaming Interactive 3D Worlds with Hierarchical Planning and Persistent State

We present WorldStream, an open-ended 3D world model with three simultaneous capabilities: it extends playable terrain beyond any pre-specified map, acts on open-ended language in the running world, and restores visited places with their edits. A hierarchical planner over a typed decision model emits structured decision state: Macro fixes settlement, ecology, transport, and hydrological structure across a group of tiles; Micro specializes that contract into tile semantics under measured terrain and accepted neighbor commitments. Deterministic local code compiles accepted plans into terrain, roads, settlements, vegetation, and entities. Streaming separates their reach: plans run ahead along the predicted corridor, compilation only where movement will soon need it, geometry behind the user released. One world record retains plans, seeds, object identities and mutable state, boundary commitments, and edits by attribute, revised as the user advances and edits; returning tiles recompile from it. The same record grounds interaction: the model acts on existing entities, including stateful NPCs that update as they act, edits the present region, or attaches intent to unplanned regions. Together they yield a world expanding under bounded budgets, connected across independently planned tiles, and interactive.
