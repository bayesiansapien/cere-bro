---
source: farmer/huggingface
farmed: 2026-06-16T00:00:00Z
arxiv_id: 2606.17043
url: https://huggingface.co/papers/2606.17043
arxiv_url: https://arxiv.org/abs/2606.17043
date: 2026-06-16
---

# Hierarchical Advantage Weighting for Online RL Fine-Tuning of VLAs from Sparse Episode Outcomes

When pretrained VLA policies are fine-tuned through online RL, each rollout episode produces only a single binary outcome (success or failure), yet the actor update requires per-transition supervision. Existing approaches commonly reduce this sparse outcome to a single scalar reward or advantage signal, which conflates distinct forms of transition-level feedback and provides limited guidance once basic task success becomes achievable. First, a single scalar signal conflates the two objectives of viability and efficiency; once basic success is achieved, the binary label provides no gradient to distinguish efficient completions from slow ones. Second, real-world rollouts mix autonomous and intervention segments; naively assigning episode outcomes across these boundaries introduces incorrect credit assignment. To address these issues, we propose Hierarchical Advantage-Weighted Behavior Cloning (HABC), which trains separate critic heads for these two objectives on different data subsets and combines their outputs with a state-adaptive balance. A state-adaptive gate g_t merges their one-step advantages, prioritizing viability when success is uncertain and shifting to efficiency only when viability is high, and converts the result into per-transition weights on the actor loss. Intervention-aware credit assignment further restricts outcome labels to segments executed by the current policy, preventing supervision from leaking across intervention boundaries. In real-robot experiments on three contact-rich bimanual tasks, HABC raises success from supervised fine-tuning (SFT) baselines of 36%, 44%, and 12% to 92%, 88%, and 38%.
