---
source: farmer/huggingface
farmed: 2026-09-15T10:58:02.142912
arxiv_id: 2609.13318
url: https://huggingface.co/papers/2609.13318
arxiv_url: https://arxiv.org/abs/2609.13318
date: 2026-09-15
---

# Attention-DP3: Spatially Object-aware 3D Diffusion Policy via Geometry-aligned Attentional Conditioning

3D point-cloud observations are inherently ambiguous in complex, cluttered manipulation scenes, where target objects may be partially occluded or tightly intermingled with visually similar distractors. As a result, standard 3D diffusion policies often struggle to localize and exploit task-relevant geometry as scene complexity grows. We propose Attention-DP3, a spatially object-aware 3D diffusion policy that injects object-level geometric cues via attention while keeping the DP3 diffusion backbone unchanged. Our pipeline performs open-vocabulary 2D segmentation on RGB images, then lifts predicted target masks into 3D using calibrated camera geometry to obtain object-centric geometric priors. We incorporate these cues through Tri-field Attentional Conditioning, which constructs three complementary fields: (i) a targetness field to anchor the target object, (ii) an intra-target saliency field to emphasize task-relevant geometry within the target, and (iii) a backgroundness field to suppress distractors and clutter. Experiments on Adroit, DexArt, MetaWorld, and the real-world SO101 platform show consistent improvements over DP3, achieving state-of-the-art performance across benchmarks. Notably, as distractor objects increase, DP3 drops sharply, whereas Attention-DP3 remains stable and outperforms DP3 by up to 31\% under heavy clutter. The code is publicly available at https://github.com/zhangzhongbo2213/Attention-DP3.
