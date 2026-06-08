---
source: farmer/huggingface
farmed: 2026-06-08T09:23:13Z
arxiv_id: 2606.07508
url: https://huggingface.co/papers/2606.07508
arxiv_url: https://arxiv.org/abs/2606.07508
date: 2026-06-08
---

# Streaming Video Generation with Streaming Force Control

We introduce StreamForce, a streaming video generation framework that enables physically grounded control through continuous force inputs. Unlike prior video models that train separate models for different force types, assume fixed forces, or rely on non-causal processing, StreamForce is a causal and unified model that responds instantly and coherently to both local and global, time-varying forces. To achieve this, we design a unified force representation as a control signal and develop a distillation pipeline for force-controllable video generation. Our model combines autoregressive efficiency with force responsiveness, sustaining stable photometric and dynamic realism. StreamForce runs at up to 16.6 FPS on a single GPU, achieving state-of-the-art performance in both force adherence and motion realism. Project website: https://neu-vi.github.io/StreamForce/
