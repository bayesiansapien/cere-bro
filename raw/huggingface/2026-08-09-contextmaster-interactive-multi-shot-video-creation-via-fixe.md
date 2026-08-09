---
source: farmer/huggingface
farmed: 2026-08-09T07:10:01.249497+00:00
arxiv_id: 2608.04956
url: https://huggingface.co/papers/2608.04956
arxiv_url: https://arxiv.org/abs/2608.04956
date: 2026-08-09
---

# ContextMaster: Interactive Multi-Shot Video Creation via Fixed-Budget Sparse Context Routing

Recent video models increasingly support generation, reference conditioning, and editing within a single model, yet typically expose them as separate operations over fixed inputs. Practical creation unfolds across multiple shots, requiring one model to generate from text, follow a reference, or edit source footage while maintaining shared history. We formalize this setting as interactive multi-shot video creation (IMVC) and introduce ContextMaster, a unified model with a role-aware context representation for these operations. An interactive model must retain access to an expanding history without allowing the context read cost at each denoising step to grow. ContextMaster combines reusable clean context states with fixed budget sparse context routing and uses ConstraintSink to keep task constraints visible. To address the dual challenges of sparse context access and inference with few denoising steps, we propose a two-stage privileged context distillation framework, which transfers full context behavior from a dense teacher through consistency distillation and then refines deployment rollouts with distribution matching. Experiments on the three primitive tasks demonstrate improved task fulfillment and consistency across shots over specialized baselines. User studies further validate flexibly composed workflows, while the model reaches 16 FPS on a single GPU.
