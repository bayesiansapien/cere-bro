---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.230353+05:30
arxiv_id: 2610.17638
url: https://huggingface.co/papers/2610.17638
arxiv_url: https://arxiv.org/abs/2610.17638
date: 2026-10-15
---

# Acting Through Registers

World Action Models (WAMs) use generative visual representations to condition robot actions, yet how these representations organize action-relevant information remains poorly understood. We identify persistent high-norm spatial outliers in WAM representations and find that their action relevance persists even after normalization and K/V projection attenuate their extreme magnitude. Motivated by this observation, we introduce RegisterWAM, which adds learnable non-spatial registers to the world model and uses them directly for action conditioning. Registers alone do not fully eliminate spatial outliers; pairing them with observation flow-matching (FM) loss supervision suppresses spatial outliers while concentrating high-norm responses in registers. Beyond this reorganization, observation FM loss supervision also improves action learning without registers, motivating an additional noised-observation FM objective that learns current-scene recovery from corrupted inputs. The resulting model achieves 81.64\% success on LIBERO-Plus without additional embodied pretraining data or foundation models, reaches 93.0\% average success on RoboTwin 2.0, and improves real-world manipulation performance.
