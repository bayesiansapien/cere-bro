---
source: farmer/huggingface
farmed: 2026-05-01T00:00:00Z
arxiv_id: "2604.27505"
url: https://huggingface.co/papers/2604.27505
arxiv_url: https://arxiv.org/abs/2604.27505
date: 2026-05-01
---

# Leveraging Verifier-Based Reinforcement Learning in Image Editing

While Reinforcement Learning from Human Feedback (RLHF) has become a pivotal paradigm for text-to-image generation, its application to image editing remains largely unexplored. A key bottleneck is the lack of a robust general reward model for all editing tasks. Existing edit reward models usually give overall scores without detailed checks, ignoring different instruction requirements and causing biased rewards. To address this, we argue that the key is to move from a simple scorer to a reasoning verifier. We introduce Edit-R1, a framework that builds a chain-of-thought (CoT) verifier-based reasoning reward model (RRM) and then leverages it for downstream image editing. The Edit-RRM breaks instructions into distinct principles, evaluates the edited image against each principle, and aggregates these checks into an interpretable, fine-grained reward. To build such an RRM, we first apply supervised fine-tuning (SFT) as a "cold-start" to generate CoT reward trajectories. Then, we introduce Group Contrastive Preference Optimization (GCPO), a reinforcement learning algorithm that leverages human pairwise preference data to reinforce our pointwise RRM. After building the RRM, we use GRPO to train editing models with this non-differentiable yet powerful reward model. Extensive experiments demonstrate that our Edit-RRM surpasses powerful VLMs such as Seed-1.5-VL and Seed-1.6-VL as an editing-specific reward model, and we observe a clear scaling trend, with performance consistently improving from 3B to 7B parameters. Moreover, Edit-R1 delivers gains to editing models like FLUX.1-kontext, highlighting its effectiveness in enhancing image editing.
