---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.928340+00:00
arxiv_id: 2611.30573
url: https://huggingface.co/papers/2611.30573
arxiv_url: https://arxiv.org/abs/2611.30573
date: 2026-11-24
---

# Write, Evolve, Read: Streaming Cameras into a Persistent World State for 4D Occupancy Forecasting

4D occupancy forecasting predicts the 3D semantic occupancy of a driving scene seconds ahead. Over a few seconds, the scene changes little while the vehicle moves, so most of the space ahead has already been seen. Sorting the future into unchanged, changed, and unseen space, we find that current camera-based world models fall short on the unchanged part: they fail to hold on to what they have already seen, rather than to forecast what will change. We therefore make what the model has seen its state. PersistWorld streams camera frames into a persistent 3D world state anchored in the scene, writing each frame once instead of rebuilding the state from past frames. The state is learned end to end with the forecast, and an evolver predicts it at any queried time along the ego trajectory. On Occ3D-nuScenes, PersistWorld raises the IoU of the best camera-based world model by 19 points at 1-3 s and by 18 to 24 points up to 8 s, while running more than twice as fast. Code and models: https://github.com/wangzian828/PersistWorld. Project page: https://wangzian828.github.io/PersistWorld
