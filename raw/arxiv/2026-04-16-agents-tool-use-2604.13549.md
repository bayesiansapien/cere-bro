---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13549
category: cs.CV
concept: agents-tool-use
url: https://arxiv.org/abs/2604.13549
published: 2026-04-16
authors: Elton Cao, Hod Lipson
---

# Reconstruction of a 3D wireframe from a single line drawing via generative depth estimation

**arXiv:** https://arxiv.org/abs/2604.13549
**Authors:** Elton Cao, Hod Lipson

## Abstract

arXiv:2604.13549v1 Announce Type: new  Abstract: The conversion of 2D freehand sketches into 3D models remains a pivotal challenge in computer vision, bridging the gap between human creativity and digital fabrication. Traditional line drawing reconstruction relies on brittle symbolic logic, while modern approaches are constrained by rigid parametric modeling, limiting users to predefined CAD primitives. We propose a generative approach by framing reconstruction as a conditional dense depth estimation task. To achieve this, we implement a Latent Diffusion Model (LDM) with a ControlNet-style conditioning framework to resolve the inherent ambiguities of orthographic projections. To support an iterative "sketch-reconstruct-sketch" workflow, we introduce a graph-based BFS masking strategy to simulate partial depth cues. We train and evaluate our approach using a massive dataset of over one million image-depth pairs derived from the ABC Dataset. Our framework demonstrates robust performance across varying shape complexities, providing a scalable pipeline for converting sparse 2D line drawings into dense 3D representations, effectively allowing users to "draw in 3D" without the rigid constraints of traditional CAD.
