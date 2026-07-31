---
source: farmer/huggingface
farmed: 2026-07-31T19:58:50.731985
arxiv_id: 2607.27816
url: https://huggingface.co/papers/2607.27816
arxiv_url: https://arxiv.org/abs/2607.27816
date: 2026-07-31
---

# Beyond Borrowed Histories: Person-Aligned User Simulation for Interactive Role-Playing Evaluation

Role-playing agents (RPAs) have become one of the most important consumer applications of large language models. Users engage in multi-turn conversations with RPAs for experiences such as emotional comfort, making reliable evaluation essential for measuring capability, comparing systems, and guiding further improvement. Existing benchmarks, however, typically require an RPA to continue a fixed dialogue history and then evaluate the continuation using a fixed rubric detached from the user. We identify and empirically demonstrate two limitations of this design. First, an RPA's output is shaped by the preceding dialogue history, preventing a scientifically grounded assessment of its role-playing ability in real multi-turn settings. Second, user experience varies substantially across individuals, and conventional fixed rubrics need not align with user satisfaction. We therefore introduce PALATE (Person-Aligned LLM-Simulated-User Assessment with Tailored Evaluation), a scalable RPA benchmark built on user simulators. PALATE is accompanied by a pool of 300 character profiles. Its main evaluation trains five per-user simulators and lets them engage candidate RPAs in free-form, multi-turn conversations over a pre-frozen panel of character profiles. Alongside a general quality rubric, we construct personalized rubrics to measure user satisfaction; on held-out annotated data, the personalized rubrics show higher agreement with human judgments than the general rubric. In the main evaluation of 16 candidates, PALATE separately characterizes generic turn quality, long-horizon session capability, and per-user experience on multi-turn trajectories co-constructed by each candidate. It thereby produces interpretable evaluations of specific user-RPA pairs rather than compressing systems into a single user-independent ranking.
