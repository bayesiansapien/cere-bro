---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.933752+00:00
arxiv_id: 2609.33148
url: https://huggingface.co/papers/2609.33148
arxiv_url: https://arxiv.org/abs/2609.33148
date: 2026-09-29
---

# DroneWAM: Efficient World Action Model for Drone Visual Navigation

World-action models give visual navigation agents a way to anticipate how candidate actions will change future observations and to act from the predicted consequences. For drones, this capability must operate under tight accuracy and efficiency constraints. We present DroneWAM, an efficient world-action model for drone visual navigation. DroneWAM adopts a JEPA-based architecture to model future states directly in representation space, avoiding the cost of explicit future image generation. A pretrained Resampler further compresses dense encoder features into fewer latent tokens, reducing the computation repeated at each imagined step. We also introduce adaptive rollout, where a preference-trained Gate adaptively allocates prediction depth according to the current scene. To support learning under richer aerial motion, we construct DroneNav-6D, a simulated visual navigation dataset with synchronized RGB observations, 6-DoF flight trajectories, control commands, and randomized wind disturbances. On DroneNav-6D, DroneWAM achieves the best trajectory accuracy among the compared methods. Adaptive rollout further reduces the average prediction depth from 8 to 4.58 while improving trajectory accuracy, demonstrating that predictive computation can be allocated more effectively across scenes. https://github.com/1e12Leon/DroneWAM{Codes and data} will be released.
