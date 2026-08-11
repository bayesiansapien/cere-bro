---
source: farmer/huggingface
farmed: 2026-08-11T07:29:49.637235+00:00
arxiv_id: 2608.07565
url: https://huggingface.co/papers/2608.07565
arxiv_url: https://arxiv.org/abs/2608.07565
date: 2026-08-11
---

# What to Edit Next: Visually Aligned Image-Editing Follow-Up Suggestions in Conversational Systems

Conversational assistants increasingly recommend follow-up edits to help users continue a task. Existing systems primarily target text-only interactions, leaving image-creation conversations underexplored. In image-creation tasks, useful follow-up edit suggestions must reflect user preferences, offer diverse directions, and remain executable on the current image. We collected 100,000 real multi-turn image-creation conversation samples from Qwen App and found that 80.1% are image-dependent, underscoring the need for multimodal recommendation. We address this setting with a three-stage framework. In Stage 1, we use real online data to build a human-reviewed table of appropriate follow-up editing intents, then create SFT targets and fine-tune a multimodal policy. In Stage 2, to align rule-guided SFT suggestions with actual user choices, we use user click feedback to optimize the policy through multi-objective reinforcement learning. In Stage 3, to reduce visual inconsistencies between suggested edits and the current image, we introduce a visual verifier as additional training supervision. Extensive experiments demonstrate that our framework significantly outperforms baselines on both automatic and human evaluations. In a live user-randomized A/B test with millions of users, our final framework reduces visual inconsistency from 3.7% to 0.9%. Furthermore, it significantly improves recommendation CTR by 32.70%, image take-away rate by 16.32%, and average conversation turns per user by 39.90% (all p<0.05).
