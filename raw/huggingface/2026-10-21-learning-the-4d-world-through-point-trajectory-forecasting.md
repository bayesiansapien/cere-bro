---
source: farmer/huggingface
farmed: 2026-10-22T12:58:52.639944
arxiv_id: 2610.28594
url: https://huggingface.co/papers/2610.28594
arxiv_url: https://arxiv.org/abs/2610.28594
date: 2026-10-21
---

# Learning the 4D World through Point Trajectory Forecasting

Reliable multi-view forecasting requires videos from different cameras to describe the same evolving 3D scene. To this end, we introduce Video-Point Model (VPM), a world model that conditions on multi-view video histories and a language instruction to jointly forecast future videos from arbitrary viewpoints and the 3D trajectories of persistent scene points. We extend a pretrained world model with camera-conditioned multi-view processing that integrates complementary observations across cameras, and add a trajectory head that predicts how physical points move through time. Each trajectory tracks a single point across all views, and supervising these trajectories alongside video generation therefore anchors appearance changes in every camera to a shared description of 3D motion. To support training and evaluation, we build VPM-Data, a simulation corpus pairing synchronized multi-view videos with persistent point trajectories, and VP-WorldBench, a forecasting benchmark spanning simulated and real environments. We further extend VPM to robot control by adding robot actions as a token modality in the generator. Action tokens share the point-supervised backbone and are denoised jointly with future videos, thereby grounding the policy in the same 3D-aware representation. On VP-WorldBench and existing 4D generation benchmarks, point supervision improves both video fidelity and 3D motion accuracy over a video-only counterpart, and in simulated and real-robot experiments, it also raises the manipulation success of the action-enabled model.
