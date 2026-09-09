---
source: farmer/huggingface
farmed: 2026-09-09T05:28:24.738031+00:00
arxiv_id: 2609.05594
url: https://huggingface.co/papers/2609.05594
arxiv_url: https://arxiv.org/abs/2609.05594
date: 2026-09-09
---

# SceneMosaic: Efficient and Diverse Simulation-Ready Scene Generation via Hybrid Agentic Layout Evolution

Diverse and simulation-ready indoor scenes are essential for interactive entertainment and embodied AI, yet their scalable generation remains challenging. Recent agentic text-to-3D scene pipelines that rely on vision-language models (VLMs) can generate scenes of high fidelity but require costly iterative object placement and refinement. Another mainstream paradigm, parametric image-to-3D scene models, produces scenes efficiently from strong priors learned from 2D images but often leads to imprecise and physically invalid scenes. More importantly, both paradigms struggle to output diverse scenes for a single input, making it hard for them to reflect the dynamically changing nature of real scenes. In this paper we propose SceneMosaic, a framework that combines the merits of both paradigms. It obtains the initial candidate from the learned image-based prior, and subsequently evolves the result through VLM agents, ensuring both efficiency and physical validity. Within the evolution process, SceneMosaic exploits the locality of natural scenes and decomposes a scene into independent local units, allowing separate evolution within each unit before composing the global scene via Cartesian product. On SceneEval-100, SceneMosaic matches the strongest agentic baseline in semantic layout quality with a 24x speedup, substantially reduces physical violations, and receives the highest human ratings. Our code is publicly available at https://github.com/rxjfighting/SceneMosaic.
