---
source: farmer/huggingface
farmed: 2026-11-06T05:50:41.301097+00:00
arxiv_id: 2611.02857
url: https://huggingface.co/papers/2611.02857
arxiv_url: https://arxiv.org/abs/2611.02857
date: 2026-11-05
---

# Solv3R: 3D Looped Transformer as a Multi-view Solver

Classical structure-from-motion reconstruction proceeds iteratively, refining camera poses and scene geometry from a current estimate. This allows maps to easily expand without recomputing already computed views, or geometry estimates to improve as more observations are provided. Most geometric foundation models, however, predict entire geometry in a single forward pass or update a recurrent state as frames arrive sequentially, making this expansion and refinement non-trivial. We introduce Solv3R, a looped transformer that learns to continue solving multi-view geometry from its current state. Importantly, its update operator is independent of the iteration count, allowing previously refined and newly introduced views to be jointly updated regardless of how ``solved'' they are. We train the operator to preserve accurate reconstructions under continued iteration and correct inaccurate states, enabling refinement of fixed image collections and integration of new observations. Representations of solved views can also be cached once and reused as geometric context across iterations, enabling compact and efficient key-value caching. We analyze the solver dynamics and compare it with the state-of-the-art, demonstrating that a single learned solver supports offline reconstruction, incremental reconstruction, relocalization, and streaming without task-specific training or modules. The code and models will be made publicly available at https://ubc-vision.github.io/solv3r/.
