---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.527183+00:00
arxiv_id: 2611.15131
url: https://huggingface.co/papers/2611.15131
arxiv_url: https://arxiv.org/abs/2611.15131
date: 2026-11-13
---

# Duo: A Reciprocal World Model for Full-Duplex Interaction

In this report, we introduce the Reciprocal World Model (RWM) and present Duo v1, a full-duplex world model that continuously perceives audiovisual inputs while responding to users in real time. The RWM treats intelligence and physical reality as equally fundamental to what constitutes a world. Existing world models largely focus on simulating the latter, leaving reasoning and decision-making as external controls rather than intrinsic parts of the world itself. In RWM, we identify two equally fundamental capabilities: Intent, which provides the cognition underlying world interactions, and Realization, which generates coherent audio-visual behavior. To realize this formulation, Duo v1 introduces three key technical designs: (1) Leveraging autoregressive modeling for continuous interaction reasoning and participation decisions, rather than restricting it to instruction understanding for diffusion models. (2) Constructing chunk-specific conditions and synchronize tokens across Intent and Realization on a unified timeline. Module-specific attention masks enforce causal dependencies both within and across chunks, preventing access to future inputs. (3) Mitigating distribution shift in both modules through dual rollout distillation, training on autoregressively generated Intent tokens and synthesized audiovisual histories from Realization. Both modules continuously perceive real-time audio, video, and text, enabling full-duplex interaction with spontaneous conversations and interruptions. Beyond conversation, users can share real objects, reshape virtual scenes, guide assistants, or play audiovisual games without mouse or keyboard controls. The release of Duo v1 makes our first step, with the next version coming soon. We look forward to broader exploration of this emerging field.
