---
source: farmer/huggingface
farmed: 2026-06-02T09:40:06Z
arxiv_id: 2606.00090
url: https://huggingface.co/papers/2606.00090
arxiv_url: https://arxiv.org/abs/2606.00090
date: 2026-06-02
---

# Silent Failures in Physical AI: A Literature Review of Runtime Action Authorization for Autonomous Systems

Physical AI systems increasingly map multimodal observations, language instructions, and learned world representations into physically consequential actions. Robotics foundation models, vision-language-action models, and world-model-based autonomous systems can condition decisions that move vehicles, robots, drones, and industrial machines. This transition exposes a safety problem that is not fully captured by conventional AI content moderation or by classical robot safety alone: a black-box model may issue a physically consequential action while appearing confident, plausible, and semantically aligned. The resulting failure can be silent, arising from sensor drift, occlusion, state-estimation error, distribution shift, hallucinated affordances, or invalid physical assumptions before downstream hardware controllers detect a violation.
  Across embodied foundation models, world models, robotics simulation, embodied safety benchmarks, safe control, runtime assurance, uncertainty estimation, verification, and guardrail evaluation, model capability and safety mechanisms have advanced along largely separate technical tracks. A recurring gap synthesized here is that no single stream surveyed in this review supplies a complete runtime authorization boundary between black-box Physical AI models and physical execution. The resulting analysis develops a bounded problem formulation, a definition of silent physical-action failure, a taxonomy of runtime guardrail functions, and evaluation requirements for comparing guardrails as Physical AI assurance mechanisms.
