---
source: farmer/huggingface
farmed: 2026-11-04T11:17:37.426675+00:00
arxiv_id: 2610.39278
url: https://huggingface.co/papers/2610.39278
arxiv_url: https://arxiv.org/abs/2610.39278
date: 2026-11-03
---

# WorldFlow: Joint Video and 3D Motion Prediction via Large-Scale Pretraining

Predicting future physical states stands as a central challenge in embodied intelligence. Existing video world models leave 3D dynamics implicit, action-based formulations remain tied to specific robot configurations, and 3D motion prediction models use flow-only supervision, providing a limited learning signal for physical dynamics. To circumvent these limitations, we introduce , a generative world model that jointly predicts future video and query-based 3D trajectories. By parameterizing 3D motion as continuous displacement tokens aligned with the video grid, a unified Mixture-of-Transformers (MoT) backbone jointly denoises both modalities under a rectified-flow objective. This formulation couples explicit geometric dynamics with visual evolution, effectively unlocking the physical commonsense embedded within pretrained video models. To empirically scale and validate this unified architecture, we train  on a heterogeneous mixture of 1.44 million object-level samples spanning simulated and real-world domains. We further introduce WorldFlowBench, comprising 1,678 evaluation samples from 11 data sources across simulated and real-world interactions, including spatial reasoning tasks. Across all three evaluation sets, WorldFlow achieves the lowest average displacement error (ADE) and final displacement error (FDE) among the evaluated learning-based methods. Notably, on the challenging SpatialCog set, WorldFlow achieves an ADE of 0.060 m, a 54.2\% reduction compared with the strongest external baseline. It also reduces ADE and FDE by 55.9\% and 68.5\%, respectively, compared with its flow-only variant. Project page: https://worldflow-rbs.github.io/.
