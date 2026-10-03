---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.823670+00:00
arxiv_id: 2609.37690
url: https://huggingface.co/papers/2609.37690
arxiv_url: https://arxiv.org/abs/2609.37690
date: 2026-10-02
---

# Honeycomb: Constant-Size Scene Memory Representation for Video World Models

Video world models require persistent scene memory to maintain consistency during long-horizon video generation. Existing spatial memories accumulate RGB observations or latent features, increasing storage requirements as generation proceeds. We introduce Honeycomb, a video world model built on HexMemory, our proposed low-rank representation for storing scene features in a fixed-size memory with a total of six spatial and spatiotemporal planes. A feed-forward writer maps each generated chunk into new plane features. As the spatial coverage or temporal range expands, we warp the previous planes while preserving their dimensions, then fuse them with the new features through confidence-weighted pooling and a learned residual correction. A reader retrieves latents from HexMemory to condition subsequent video generation. The writer processes only observations from the new chunk, avoiding per-scene optimization and repeated processing of the full history. Experiments on WorldScore and RealEstate10K demonstrate strong video generation quality and robust revisit consistency while keeping HexMemory feature storage constant throughout generation. Code and additional visualizations are available on our project page at https://jackswl.github.io/honeycomb/.
