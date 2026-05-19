---
source: farmer/huggingface
farmed: 2026-05-19T09:55:00.432604+00:00
arxiv_id: 2605.15764
url: https://huggingface.co/papers/2605.15764
arxiv_url: https://arxiv.org/abs/2605.15764
date: 2026-05-19
---

# GRASP: Learning to Ground Social Reasoning in Multi-Person Non-Verbal Interactions

Understanding social interactions requires reasoning over subtle non-verbal cues, yet current multimodal large language models (MLLMs) often fail to identify who interacts with whom in multi-person videos. We introduce GRASP, a large-scale social reasoning dataset that connects high-level social QA with fine-grained gaze and deictic gesture events. GRASP contains 290K question--answer pairs over 46K videos totaling 749 hours, organized by a 16-category taxonomy spanning gaze, gesture, and joint gaze--gesture reasoning, together with GRASP-Bench for evaluation. Unlike prior resources that focus on either isolated cues or high-level social QA, GRASP builds questions from identity-consistent gaze trajectories, deictic gestures, and their joint compositions into social events. Moreover, we propose Social Grounding Reward (SGR), a learning signal that uses these social events to encourage models to reason about the participants involved in each interaction. Experiments show that SGR improves performance on GRASP-Bench while maintaining zero-shot performance on related social video QA benchmarks.
