---
source: farmer/huggingface
farmed: 2026-09-11T21:57:41.002444
arxiv_id: 2609.11499
url: https://huggingface.co/papers/2609.11499
arxiv_url: https://arxiv.org/abs/2609.11499
date: 2026-09-11
---

# Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs

Code world models represent worlds as executable programs, but this representation alone does not determine how to construct a complex world. We introduce Recursive Code World Models (RCWM), a framework for reconstructing complex 3D worlds in code from a single reference image. RCWM couples a Recursive Scene Program (RSP) representation with a construction solver that recursively calls itself. An RSP represents the executable world as compositional scene code, while each solver call follows the same complete process: establish the whole, recursively reconstruct unresolved parts, and revisit the whole to refine their composition. This global-local-global recursion gives fine-scale structures their own perception-and-editing loops while preserving scene-wide geometry and relationships. Reference-aligned views propagate a shared camera projection across levels, while parent revisitation addresses boundaries, spatial relations, and shared errors that emerge after local refinement. A vision-language coding agent directly compares reference images with scene renders to guide refinement, recursive descent, and return. Across complex scenes, RCWM outperforms prior code-based image-to-scene reconstruction methods. Ablation studies further support the benefits of recursive construction and suggest that deeper calls can improve finer-scale reconstruction. RCWM provides a recursive construction principle for building complex executable worlds from visual evidence.
