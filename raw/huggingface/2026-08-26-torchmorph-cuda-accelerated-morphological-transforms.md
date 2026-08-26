---
source: farmer/huggingface
farmed: 2026-08-26T12:46:47.908232
arxiv_id: 2608.24738
url: https://huggingface.co/papers/2608.24738
arxiv_url: https://arxiv.org/abs/2608.24738
date: 2026-08-26
upvotes: 0
---

# TorchMorph: CUDA-accelerated Morphological Transforms

Morphological transforms are long-standing tools for shape and mask processing, but the de facto reference implementation in the Python ecosystem, i.e. scipy.ndimage, is CPU-only, single-array, and therefore unusable inside a GPU training loop without an expensive device-to-host round trip. GPU vision libraries built on PyTorch cover a narrow subset of these operators, typically restricted to two spatial dimensions and flat structuring elements. We present TorchMorph, a lightweight PyTorch extension that closes this gap. TorchMorph exposes 22 public operators covering binary morphology, greyscale morphology, exact and approximate distance transforms, and entropy-regularised optimal transport, all implemented as fused CUDA kernels that operate directly on (B, C, Spatial...) CUDA tensors with up to eight spatial dimensions. The API deliberately mirrors scipy.ndimage argument-for-argument, including border modes, structuring-element origins and pre-allocated outputs, so that existing pipelines port with a change of import. We describe the layered architecture and the kernel designs behind each operator family. Against single-threaded CPU references, batched execution reaches up to 1.1e3 times the throughput of scipy.ndimage on greyscale morphology and up to 350x on exact Euclidean distance transforms, while the Sinkhorn solver runs up to 42x faster than POT. Binary and chamfer operators reproduce their SciPy counterparts exactly, and every float-valued operator agrees with the CPU reference to within 1.8e-6 absolute error. TorchMorph is released under the MIT licence at https://intcomp.github.io/tm.
