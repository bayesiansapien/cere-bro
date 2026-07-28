---
source: farmer/huggingface
farmed: 2026-07-28T09:26:01.339781
arxiv_id: 2607.21694
url: https://huggingface.co/papers/2607.21694
arxiv_url: https://arxiv.org/abs/2607.21694
date: 2026-07-28
---

# Oxygen-TryOn: Fashion-Native Foundation Model for Any-item Virtual Try-On

We present Oxygen-TryOn, a unified foundation model for any-item virtual try-on. Rather than repurposing a general-purpose image editor, Oxygen-TryOn is fashion-native, built for try-on through a dedicated data engine and try-on-specific training. Given one or more reference items (clean product shots or in-the-wild worn-on photos) and a single target subject image, it synthesizes a photorealistic image of the subject wearing the items across virtually any fashion category. Prior systems handle a single garment category in a studio setting, and recent multi-reference methods remain garment-centric; in contrast, Oxygen-TryOn supports diverse items and scenarios, including full- and half-body views, a variable number of references, and free multi-item composition, while faithfully preserving both subject identity and item appearance. Instead of mask-based inpainting, we reformulate try-on as a multi-reference, understanding-driven generation task. We build a data engine that collects, manufactures, annotates, and filters high-quality try-on data at scale, and design a three-stage recipe of continued pre-training (CPT), supervised fine-tuning (SFT), and reinforcement learning (RL). The RL stage uses a hybrid reward combining an in-house try-on reward model with a proprietary, rubric-guided general-purpose model, jointly supervising fine-grained consistency and instruction-level quality. It also follows general editing instructions (e.g., pose changes) in the same pass. Across public benchmarks and our in-house Oxygen-TryOn Bench, it achieves state-of-the-art consistency and realism on single-item try-on and leads on multi-item try-on, matching or surpassing both leading proprietary systems (Nano Banana Pro, GPT-Image-2, Seedream5 Lite) and open-source models (FLUX.2).
