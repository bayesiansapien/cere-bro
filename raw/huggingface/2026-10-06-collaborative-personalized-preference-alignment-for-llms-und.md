---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.05898
url: https://huggingface.co/papers/2610.05898
arxiv_url: https://arxiv.org/abs/2610.05898
date: 2026-10-06
---

# Collaborative Personalized Preference Alignment for LLMs under Data Deficiency

Real-world users often exhibit highly heterogeneous preferences over multiple objectives for LLM responses. A lightweight aligner can tailor these responses to individual preferences, but scarce user-specific feedback makes personalized training difficult. Learning shared initializations across users can support few-shot adaptation. However, heterogeneous preferences and competing objectives cause gradient conflicts across users and within each user, hindering effective initialization learning. This raises a central question: how can we collaboratively learn aligner initializations that support few-shot adaptation to diverse user preferences? To answer this question, we propose Approximate Pareto Optimality (APO). We first group users whose updates are compatible, so that their information can be combined with less interference. Within each group, we combine gradient descent with controlled ascent to coordinate competing objectives and move towards preference-specific points on the Pareto front. This produces an initialization that is close to the optima of the users in the group. We then iteratively refine it using updates from few-shot local adaptation, making it more effective for personalization. Furthermore, we establish conditional suboptimality bounds for a one-local-step collaborative update and characterize how initialization error affects subsequent stochastic adaptation. Experiments on Fed-ChatbotPA and UltraFeedback show consistent improvements over existing methods using only 20 local examples.
