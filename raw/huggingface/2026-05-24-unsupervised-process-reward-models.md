---
source: farmer/huggingface
farmed: 2026-05-24T05:07:38.368292+00:00
arxiv_id: 2605.10158
url: https://huggingface.co/papers/2605.10158
arxiv_url: https://arxiv.org/abs/2605.10158
date: 2026-05-24
---

# Unsupervised Process Reward Models

Process Reward Models (PRMs) are a powerful mechanism for steering large language model reasoning by providing fine-grained, step-level supervision. However, this effectiveness comes at a significant cost: PRMs require expert annotations for every reasoning step, making them costly and difficult to scale. Here, we propose a method for training unsupervised PRMs (uPRM) that requires no human supervision, neither at the level of step-by-step annotations nor through ground-truth verification of final answers. The key idea behind our approach is to define a scoring function, derived from LLM next-token probabilities, that jointly assesses candidate positions of first erroneous steps across a batch of reasoning trajectories. We demonstrate the effectiveness of uPRM across diverse scenarios: (i) uPRM achieves up to 15% absolute accuracy improvements over the LLM-as-a-Judge in identifying first erroneous steps on the ProcessBench dataset; (ii) as a verifier for test-time scaling, uPRM performs comparably to supervised PRMs and outperforms the majority voting baseline by up to 6.9%, and (iii) when used as a reward signal in reinforcement learning, uPRM enables more robust policy optimization throughout training compared to a supervised PRM trained using ground-truth labels. Overall, our results open a path toward scalable reward modeling for complex reasoning tasks.
