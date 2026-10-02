---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.353400+05:30
arxiv_id: 2609.37824
url: https://huggingface.co/papers/2609.37824
arxiv_url: https://arxiv.org/abs/2609.37824
date: 2026-10-01
---

# The Geometry of Inference in Transformer Residual Streams

Transformer language models build predictions through successive residual updates, but how their representations become specific to an eventual outcome remains unclear. We study this process by comparing intermediate residual states with their own final states and an empirical bank of final states from other contexts. Across six pretrained language models, the own endpoint becomes preferable to the average alternative early, while many individual endpoints remain closer. These competing sets generally shrink with depth, but their membership changes and their surviving endpoints need not become more similar to one another. Directional alignment and endpoint rank can therefore improve while Euclidean distance to the final state changes little. We develop a simple high-dimensional model that separates the roles of norm, alignment, and endpoint geometry, showing how gradual directional changes can produce sharp reductions in competition. We also prove that a straight path toward the own endpoint cannot introduce new competitors under either Euclidean or cosine distance; observed entries thus establish departures from straight-line convergence. Finally, endpoints associated with lower-ranked output tokens tend to lie farther away in cosine distance across all studied models, connecting residual geometry to output organization. Together, these findings characterize increasing geometric specificity during transformer inference and explain why distance, competitor count, and concentration of the surviving endpoints provide distinct views of that process.
