---
source: farmer/huggingface
farmed: 2026-06-17T10:05:49Z
arxiv_id: 2606.18216
url: https://huggingface.co/papers/2606.18216
arxiv_url: https://arxiv.org/abs/2606.18216
date: 2026-06-17
---

# Zone of Proximal Policy Optimization: Teacher in Prompts, Not Gradients

Knowledge distillation transfers a teacher's competence to a small student but is brittle in the small-student regime: forcing the student to imitate logits from a much larger teacher concentrates it on the teacher's sharpest modes, hurting generalization on benchmark families beyond the training corpus. Reinforcement learning (RL) avoids logit imitation by training on the student's own rollouts. However, on questions where every rollout fails-yielding zero advantage and being silently discarded-injecting a stronger teacher's response into the policy gradient breaks the on-policy assumption and induces drift. We introduce Zone of Proximal Policy Optimization (ZPPO), inspired by Vygotsky's zone of proximal development, which keeps the teacher inside the prompt rather than the policy gradient. On hard questions, ZPPO constructs two reformulated prompts: a Binary Candidate-included Question (BCQ) pairs one correct teacher response with one incorrect student response as anonymized candidates the student must discriminate, and a Negative Candidate-included Question (NCQ) aggregates the student's wrong rollouts into a single prompt to surface their shared failure modes. A prompt replay buffer recirculates each hard question until it either graduates-the student's mean rollout accuracy on it reaches half- or is FIFO-evicted under finite capacity, amplifying BCQ and NCQ inside the student's current zone of proximal development. On the Qwen3.5 family at four student scales (0.8B-9B) with a 27B teacher, post-trained as vision-language models and evaluated on a 31-benchmark suite (16 VLM, 10 LLM, 5 Video), ZPPO outperforms off/on-policy distillation and GRPO, with the largest gains at the smallest scale.
