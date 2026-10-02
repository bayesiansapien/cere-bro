---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.350491+05:30
arxiv_id: 2609.34276
url: https://huggingface.co/papers/2609.34276
arxiv_url: https://arxiv.org/abs/2609.34276
date: 2026-10-01
---

# NavHarness: Towards Lifelong Embodied Navigation

Frontier models can now perform well on individual embodied navigation tasks through multi-round multimodal reasoning with simple tools. Across successive tasks, however, an agent must also rely on an evolving map and earlier search records, both of which may be incomplete or conflict with new observations. We present NavHarness, a training-free embodied harness towards lifelong navigation that makes memory processing part of the navigation loop. During navigation, its multi-round agentic session draws on maps, task records, and house knowledge, checking them against observations and recording corrections to guide its actions. NavHarness preserves this experience across fresh conversations for new tasks or recovery attempts, while outcome verification and run-end summaries support its later reuse. On GOAT-Bench, NavHarness improves s-SR over context-only independent sessions by 18.6 points with Astra and 22.6 with Opus 5. Using SLAM-estimated poses, NavHarness with GPT-6 Astra achieves state-of-the-art task success of 83.7 s-SR with 36.9 e-SR on GOAT-Bench and 85.9 s-SR on IR2R-CE. To understand these gains, we examine how experience is carried between sessions and find that structured recovery handovers outperform length-matched summaries. In extended deployments across houses, consolidation improves navigation beyond retaining maps and task records, with case studies showing how agents use earlier experience to interpret new goals, investigate unresolved questions, and resume failed searches. We suggest that progress towards lifelong navigation depends on how successive reasoning sessions build on prior experience, alongside improvements in single-task capability.
