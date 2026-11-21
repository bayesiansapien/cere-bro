---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.390942+00:00
arxiv_id: 2611.23875
url: https://huggingface.co/papers/2611.23875
arxiv_url: https://arxiv.org/abs/2611.23875
date: 2026-11-20
---

# In Situ Training of Optical Neural Networks by Coding Agents

Optical neural networks promise fast, energy-efficient computing, but every device departs from its design and must be trained with the hardware. In situ training relies on an expert-built calibrated digital model of each device or on gradient-free trial and error. Coding agents, large language models that write and run programs, have shown an emergent ability to understand and edit the weights of digital neural networks. Here we introduce optics as code, a method in which a coding agent trains an optical neural network from measurements alone, through a harness that returns camera images of its probes and requires a hypothesis per request. We discovered that the agent forms a physical understanding of the optics and reparametrizes the network with interpretable optical elements tuned on the hardware. It outperforms gradient-free methods in classification and image encoding, approaching backpropagation through a calibrated model at a fraction of the cost. Needing neither per-device calibration nor gradients through the hardware, and improving with more capable models, optics as code offers a practical route to large, scalable optical neural networks and a general tool for calibrating and optimizing optical experiments.
