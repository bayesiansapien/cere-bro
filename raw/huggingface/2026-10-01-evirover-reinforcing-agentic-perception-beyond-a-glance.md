---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.352473+05:30
arxiv_id: 2609.40230
url: https://huggingface.co/papers/2609.40230
arxiv_url: https://arxiv.org/abs/2609.40230
date: 2026-10-01
---

# EviRover: Reinforcing Agentic Perception Beyond a Glance

Visual perception is conventionally formulated as a one-shot prediction from a single glance at the image, under the assumption that the image content and the model's parametric knowledge suffice to resolve the query. This assumption often fails in real-world scenarios that hinge on fine-grained visual details or require knowledge-intensive and up-to-date information. We term such cases perception under insufficient evidence and formulate perception as an agentic process that can obtain information beyond a single glance. To address the absence of data for this setting, we design two dedicated data generation pipelines, yielding EviRover-SFT-5K and EviRover-RL-12K for training. We further construct EviLens, a human-verified benchmark comprising 688 instances across five perception categories. Building on these data, we present EviRover, to our knowledge the first perception agent explicitly trained to resolve perceptual queries through interaction, using supervised fine-tuning followed by agentic reinforcement learning. Experiments show that the 4B EviRover outperforms its backbone by 30 points on average on EviLens, reaching performance comparable to advanced proprietary models. The gains transfer beyond EviLens to WebEyes, conventional perception benchmarks, and general multimodal benchmarks, including a 15-point improvement on BrowseComp-VL. All code, models, and data are released.
