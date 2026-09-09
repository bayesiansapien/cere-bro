---
source: farmer/huggingface
farmed: 2026-09-09T05:28:24.738031+00:00
arxiv_id: 2609.05588
url: https://huggingface.co/papers/2609.05588
arxiv_url: https://arxiv.org/abs/2609.05588
date: 2026-09-09
---

# GE-Act 2.0: Pretraining and Scaling a World-Action Model for Robotic Manipulation

World-action models (WAM) predict future states to guide robot actions, enabling learning from both action-free video and action-labeled interaction. Most inherit pretrained video generators, leaving WAM pretraining and scaling underexplored. We introduce Genie Envisioner Act 2.0 (GE-Act 2.0), a world-action model whose trainable generative and action components are all initialized from scratch on manipulation data. It combines a control-oriented autoencoder (CoAE), a single-step visual planner (SVP), and an inverse dynamics model (IDM). CoAE retains action- and instruction-relevant information under aggressive compression, while SVP produces a complete future state in one differentiable pass, so visual planning and inverse dynamics can be pretrained separately on complementary data. The components are then jointly trained with knowledge-aligned selective optimization (KASO), which reduces mismatched supervision by selecting only predicted futures judged behaviorally compatible with the recorded action. We evaluate pretrained checkpoints directly, without per-task fine-tuning, on 100 tasks across 20 manipulation skill groups with held-out scenes, backgrounds, lighting, and object instances. Scaling co-training data from 300 to 30,000 hours raises success from 17.1% to 44.1% on G1-OP and from 13.4% to 31.1% on G2-90D; despite comprising less than 2% of the co-training data, G2-90D improves by 17.7 points, suggesting cross-embodiment transfer. Gains span 19/20 and 18/20 skill groups, and skill-specific coverage strongly correlates with zero-shot out-of-distribution (OOD) success (Pearson r=0.80; Spearman rho=0.85). Under the same protocol, the model grounds object, color, shape, and position references in at least 90% of trials and follows explicit instructions even when they conflict with an already-committed behavior or a conventional scene association.
