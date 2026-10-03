---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.817500+00:00
arxiv_id: 2609.35690
url: https://huggingface.co/papers/2609.35690
arxiv_url: https://arxiv.org/abs/2609.35690
date: 2026-10-02
---

# Agent Priors-guided Policy Learning

Robots that learn from a few demonstrations often require two forms of generalization. Compositional generalization recombines skills to solve new tasks, and skill generalization lets the learned policy behind each skill work in new situations. The two depend on each other, yet information is lost between composition and the skills it calls. Where a skill works is determined by the structure its policy is trained with, while composition sees the skill only through a separate description, such as a name, an instruction, or a symbolic operator, that omits this structure. Our key idea is to use each policy's structural prior as part of the interface between composition and the skill. A structural prior states what a behavior depends on, for example that a grasp depends only on the gripper's pose relative to the object. Built into training, it shapes where the policy generalizes; stated in language, it tells composition where the policy applies. We instantiate this idea in Agent Priors-guided Policy Learning (APPL). A construction agent segments complete demonstrations into reusable skills, proposes several structural priors for each skill, and trains and verifies one policy per prior. A runtime agent then selects among these prior-specific policies and composes them toward new task goals using their interfaces. Across MetaWorld and long-horizon ManiSkill tasks, APPL improves out-of-distribution skill generalization and enables previously unseen skill compositions; ablating the interface information substantially reduces performance. These results support the use of training-time structural assumptions as a bridge between skill learning and skill composition.
