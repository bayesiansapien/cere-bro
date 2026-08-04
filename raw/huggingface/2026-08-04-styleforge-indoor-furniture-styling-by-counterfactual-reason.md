---
source: farmer/huggingface
farmed: 2026-08-04T09:04:58.435121+05:30
arxiv_id: 2608.01954
url: https://huggingface.co/papers/2608.01954
arxiv_url: https://arxiv.org/abs/2608.01954
date: 2026-08-04
---

# StyleForge: Indoor Furniture Styling by Counterfactual Reasoning in a Hypergraph Field

Fixed-layout indoor furniture styling requires selecting assets that form a coherent room without changing the prescribed furniture categories, positions, orientations, or scales. Existing approaches typically retrieve each asset independently or rely on static local relations, making them prone to shape, material, and color conflicts after scene composition. We introduce StyleForge, a scene-level structured selection framework built on a dynamic hypergraph style field. A frozen multimodal large language model extracts structured style priors from an open-ended style request and the fixed layout, while StyleForge maintains a learnable candidate distribution for each furniture slot. Conditioned on the target style, the dynamic hypergraph style field adaptively activates and weights layout-induced hyperedges to capture higher-order dependencies among furniture. Counterfactual style preference learning then treats each candidate as a local substitution in the current style field and evaluates its contextual compatibility using Mahalanobis energies. Training alternates between optimizing the style field and the candidate logits. At inference, the model remains frozen and test-time training updates only room-specific candidate logits, progressively correcting cross-slot style conflicts as the global scene context evolves. Experiments on 3D-FRONT demonstrate state-of-the-art furniture retrieval and scene-level style coherence, producing more coherent fixed-layout furniture arrangements than object- and scene-level retrieval baselines.
