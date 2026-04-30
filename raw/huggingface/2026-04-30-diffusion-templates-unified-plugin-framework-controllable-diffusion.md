---
source: farmer/huggingface
farmed: 2026-04-30T00:00:00Z
arxiv_id: 2604.24351
url: https://huggingface.co/papers/2604.24351
arxiv_url: https://arxiv.org/abs/2604.24351
date: 2026-04-30
---

# Diffusion Templates: A Unified Plugin Framework for Controllable Diffusion

**Authors:** Zhongjie Duan, Hong Zhang, Yingda Chen (ModelScope Team, Alibaba Group)

Controllable diffusion methods have substantially expanded the practical utility of diffusion models, but they are typically developed as isolated, backbone-specific systems with incompatible training pipelines, parameter formats, and runtime hooks. This fragmentation makes it difficult to reuse infrastructure across tasks, transfer capabilities across backbones, or compose multiple controls within a single generation pipeline. We present Diffusion Templates, a unified and open plugin framework that decouples base-model inference from controllable capability injection. The framework is organized around three components: Template models that map arbitrary task-specific inputs to an intermediate capability representation, a Template cache that functions as a standardized interface for capability injection, and a Template pipeline that loads, merges, and injects one or more Template caches into the base diffusion runtime. Because the interface is defined at the systems level rather than tied to a specific control architecture, heterogeneous capability carriers such as KV-Cache and LoRA can be supported under the same abstraction. Based on this design, we build a diverse model zoo spanning structural control, brightness adjustment, color adjustment, image editing, super-resolution, sharpness enhancement, aesthetic alignment, content reference, local inpainting, and age control. These case studies show that Diffusion Templates can unify a broad range of controllable generation tasks while preserving modularity, composability, and practical extensibility across rapidly evolving diffusion backbones.

## Key contributions

- **Unified plugin framework**: Decouples base-model inference from capability injection via standardized Template cache interface.
- **Three-component architecture**: Template models (encode task-specific inputs) → Template cache (standardized intermediate representation, can be KV-Cache or LoRA) → Template pipeline (loads, merges, injects into base diffusion runtime).
- **Heterogeneous capability support**: KV-Cache and LoRA under the same abstraction — no architectural prescriptions.
- **Model zoo**: 10+ control types — structural, brightness, color, editing, super-resolution, sharpness, aesthetic, content reference, inpainting, age control.
- **Open source**: Code at https://github.com/modelscope/DiffSynth-Studio.
