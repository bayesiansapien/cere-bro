---
source: farmer/huggingface
farmed: 2026-08-06T10:35:34.247620Z
arxiv_id: 2608.04349
url: https://huggingface.co/papers/2608.04349
arxiv_url: https://arxiv.org/abs/2608.04349
date: 2026-08-06
---

# Poly-OPD: Heterogeneous Multi-Teacher On-Policy Distillation for Capability-Selectable Flow Models

Leading open text-to-image models often carry complementary strengths: one may lead on preference-aligned aesthetics while another follows compositional instructions more faithfully. However, differences in their autoencoders and noise schedules make it difficult to transfer these strengths across models. In this paper, we present Poly-OPD, a framework that can consolidate complementary strengths of heterogeneous teachers into a single compact flow-matching student. To bridge the incompatible latent spaces of different teachers, Poly-OPD performs on-policy distillation through a pixel bridge. Each student-generated image is re-encoded by a selected teacher's encoder and refined from a noise level matched by magnitude under the teacher's noise schedule. The resulting target is further matched to the student in frozen DINOv2 space, enabling supervision across incompatible latent spaces. To retain complementary capabilities without cross-teacher interference, Poly-OPD uses a gradient compatibility diagnostic to organize its adapters: attention LoRA modules are shared across teachers, whereas feed-forward adapters remain teacher-specific. During distillation, a gap-aware curriculum devotes more training to compositional categories where the student still falls short of the teacher. As each gap narrows, training shifts toward categories with larger remaining gaps. By distilling FLUX.1-dev and Z-Image into a 2.5B SD3.5-Medium student, Poly-OPD improves GenEval from 67.3 to 73.3, surpassing both larger teachers, and raises DrawBench HPSv3 from 9.34 to 11.35, consolidating both strengths within a switchable model.
