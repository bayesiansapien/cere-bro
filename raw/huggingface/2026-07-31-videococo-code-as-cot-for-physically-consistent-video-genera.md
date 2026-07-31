---
source: farmer/huggingface
farmed: 2026-07-31T19:58:50.731985
arxiv_id: 2607.27380
url: https://huggingface.co/papers/2607.27380
arxiv_url: https://arxiv.org/abs/2607.27380
date: 2026-07-31
---

# VideoCoCo: Code-as-CoT for Physically-Consistent Video Generation via an Agentic Dual-Engine System

Text-to-video models have achieved remarkable visual quality, yet they still struggle to generate physically consistent dynamics because the temporal evolution of a scene must be inferred implicitly from a highly compressed text prompt. Existing chain-of-thought approaches introduce intermediate plans or visual states, but these representations are typically non-executable or temporally sparse, limiting their ability to instantiate and control the complete spatiotemporal process. To address this limitation, we introduce VideoCoCo, an agentic dual-engine framework in which executable Blender code serves as a process-level chain of thought. Given a text prompt, a coding agent synthesizes a Blender program that explicitly specifies the scene and its temporal evolution. The executable simulation engine runs the program to produce a deterministic spatiotemporal draft, which is subsequently transformed into a photorealistic video by a generative video engine through draft-conditioned editing. This decomposition separates process-level reasoning from high-fidelity visual realization. To adapt the video editor to simulated drafts, we construct VideoCoCo-3K, a curated dataset of draft-instruction-target triplets. VideoCoCo improves the OmniWeaving baseline from 0.475 to 0.558 on PhyGenBench and from 52.18 to 77.88 on VBench-2.0, achieving the best average score on both benchmarks. These results demonstrate that executable code provides an effective, controllable, and inspectable intermediate representation for physically consistent video generation.
