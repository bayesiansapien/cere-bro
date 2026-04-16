---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13191
category: cs.LG
concept: inference-efficiency
url: https://arxiv.org/abs/2604.13191
published: 2026-04-16
authors: Javier Fabre, Carlos Castillo, Carlos Rodriguez-Pardo
---

# Fast Voxelization and Level of Detail for Microgeometry Rendering

**arXiv:** https://arxiv.org/abs/2604.13191
**Authors:** Javier Fabre, Carlos Castillo, Carlos Rodriguez-Pardo

## Abstract

arXiv:2604.13191v1 Announce Type: cross  Abstract: Many materials show anisotropic light scattering patterns due to the shape and local alignment of their underlying micro structures: surfaces with small elements such as fibers, or the ridges of a brushed metal, are very sparse and require a high spatial resolution to be properly represented as a volume. The acquisition of voxel data from such objects is a time and memory-intensive task, and most rendering approaches require an additional Level-of-Detail (LoD) data structure to aggregate the visual appearance, as observed from multiple distances, in order to reduce the number of samples computed per pixel (E.g.: MIP mapping). In this work we introduce first, an efficient parallel voxelization method designed to facilitate fast data aggregation at multiple resolution levels, and second, a novel representation based on hierarchical SGGX clustering that provides better accuracy than baseline methods. We validate our approach with a CUDA-based implementation of the voxelizer, tested both on triangle meshes and volumetric fabrics modeled with explicit fibers. Finally, we show the results generated with a path tracer based on the proposed LoD rendering model.
