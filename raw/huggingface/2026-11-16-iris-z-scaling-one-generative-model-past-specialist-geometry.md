---
source: farmer/huggingface
farmed: 2026-11-17T08:29:02.003490+00:00
arxiv_id: 2611.16010
url: https://huggingface.co/papers/2611.16010
arxiv_url: https://arxiv.org/abs/2611.16010
date: 2026-11-16
---

# Iris-Z: Scaling One Generative Model Past Specialist Geometry Models

Language moved from many task-specific models to one unified model: a single generative model with a single generative training task that handles all of them within the same backbone, and keeps improving with data, parameters and compute. We believe the bitter lesson applies just as much to computer vision, 3D and spatial understanding, in the end to visual intelligence: the effort should go into general architectures that solve all these tasks in a unified way, and into scaling them, rather than into task-specific designs. We test this on monocular geometry, a task that has belonged to specialised architectures for years. Iris-Z is a general image generator that produces appearance and geometry together. A single backbone denoises, reasons about and understands the image and its depth at the same time, and one set of weights generates images with their depth, estimates depth from photographs and paints images onto a given depth. At enough scale it surpasses state-of-the-art specialists on established depth benchmarks while keeping the generative abilities of the backbone it started from without specialized layers. We release two models for the community.
