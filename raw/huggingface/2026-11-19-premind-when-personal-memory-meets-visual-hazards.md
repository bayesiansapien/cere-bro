---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.142797+00:00
arxiv_id: 2611.23808
url: https://huggingface.co/papers/2611.23808
arxiv_url: https://arxiv.org/abs/2611.23808
date: 2026-11-19
---

# PReMind: When Personal Memory Meets Visual Hazards

Personalized vision-language assistants use visual observations and personal memories to provide advice tailored to the user. When the observed scene contains a physical hazard, personal context, such as allergies, medical conditions, or mobility constraints, can change what help is appropriate. Responding appropriately therefore requires recognizing the visible hazard and applying the relevant person's information. We introduce PReMind-Bench, a diagnostic benchmark that evaluates this combination across diverse hazards and personal-memory conditions. It separately measures memory access, grounding, abstention, and hazard response, and assesses joint success on interdependency cases. Existing models often satisfy one requirement while failing the other, and training only for safety or personalization leaves a gap in joint success. We therefore propose PReMind, a two-phase reinforcement learning framework that combines on-demand and forced-call interactions (memory always retrieved) to jointly train grounded memory use and hazard response. At 4B, PReMind raises joint success from 12.9% to 28.6% over its base on the interdependency set and improves hazard adequacy and correct abstention on the main test. Joint-success gains persist under forced-call evaluation and under a second LLM judge across three Phase II seeds; averaged over these seeds, joint success also improves on unseen hazard groups. These findings highlight the need to evaluate and train personal assistants to connect visual evidence with the relevant person's context.
