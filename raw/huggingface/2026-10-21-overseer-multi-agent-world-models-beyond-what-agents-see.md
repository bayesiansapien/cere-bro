---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.646403
arxiv_id: 2610.28554
url: https://huggingface.co/papers/2610.28554
arxiv_url: https://arxiv.org/abs/2610.28554
date: 2026-10-21
---

# OverSeer: Multi-Agent World Models Beyond What Agents See

Despite the success of video world models, extending them to multiple agents is difficult because it requires generating several agent-specific video streams that are consistent in time and between agents. To address this gap, we introduce OverSeer, a multi-agent world model that augments egocentric agent views with auxiliary camera views. We suggest that, by fixing the auxiliary views in space, they act as a proxy for a world-centric representation: Unlike the agents' views, which can change entirely due to a simple change in agent position, changes in the auxiliary views directly map to localized changes in the world state. We show that these fixed views substantially help the model to maintain consistency. We also show that, due to their redundant and semi-static nature, the auxiliary views can be efficiently compressed with a delta-VAE that encodes only the changes relative to a static reference image, reducing the number of tokens required to process them. Experiments in Minecraft and Doom demonstrate improved world and agent consistency, with qualitative results on real-world multi-camera captures indicating that the approach is not tied to game engines. Our compression analysis further shows that delta-VAE substantially reduces the computational overhead of auxiliary-view generation. We conclude that these fixed views provide a simple and efficient way to improve multi-agent world models.
