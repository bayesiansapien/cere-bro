---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.919871+00:00
arxiv_id: 2611.26516
url: https://huggingface.co/papers/2611.26516
arxiv_url: https://arxiv.org/abs/2611.26516
date: 2026-11-24
---

# Plan4D: Generative Plannable 4D Worlds

Most world models for future prediction prioritize aestetic quality of generated videos, but offer only weak physical grounding and limited geometric consistency over time, due to the lack of explicit 4D modeling. In this paper, we introduce plan4d, a possible next milestone towards building a generative plannable 4D world model that predicts future RGB videos together with dense 4D geometry, including depth, cameras, point clouds, and scene flow from an observed scene context and text-specified actions. Since training data with paired actions and dense 4D annotations is inherently scarce, plan4d leverages the complementary priors of foundational video generators and 3D reconstructors. Specifically, we propose a model-stitching architecture that couples Depth Anything 3 with LongCat-Video and augments it with an auxiliary DPT head for scene-flow prediction. The resulting model allows us to plan and generate complex, long-horizon, and fine-grained actions in a dynamic 3D scenes, while substantially improving both visual fidelity and geometric accuracy of the generated future videos. Extensive experiments on both synthetic and real-world datasets demonstrate that plan4d achieves state-of-the-art performance in generative 4D modeling of environmental reactions. Project Page: https://fogradio.github.io/plan4d-project
