---
source: farmer/huggingface
farmed: 2026-10-10T05:09:51.420779+00:00
arxiv_id: 2609.38527
url: https://huggingface.co/papers/2609.38527
arxiv_url: https://arxiv.org/abs/2609.38527
date: 2026-10-09
---

# Behavioral Persistence and Incomplete Functional Transfer of Co-evolved Communication in Evolutionary Robotics

This work evaluates the direct transfer of a co-evolved communication protocol from a 2D simulation to a 3D physical environment, without retraining the network weights. Two e-puck-type robots, controlled by a GRU network with residual connection, were evaluated in a food-seeking task with social signaling. The sensory and motor translation layer required three corrections for stable physical operation, including the calibration of a hunger term based on a measurable asymmetry in the trained residual weights. Even with these corrections, the transfer was partial and asymmetric: one agent reached the food source in one of thirty tested seeds, while the other did not reach it in any. Task success was measured by both agents reaching the food area. An additional experiment incorporating explicit directional information in the social channel produced observable changes in the trajectory of the receiving agent and improvements in several specific cases. However, these improvements were not enough to allow the second agent to reach the food source, suggesting that the limitation may not be explained solely by signal translation, but also by the ability to navigate under the new physical constraints. The results suggest that successful transfer of emergent communication may depend not only on preserving the signaling process itself, but also on preserving the ecological and navigational conditions under which the protocol evolved.
