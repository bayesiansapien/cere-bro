---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.06090
url: https://huggingface.co/papers/2610.06090
arxiv_url: https://arxiv.org/abs/2610.06090
date: 2026-10-07
---

# Execution-Aligned Progressive Noise for Consistent Asynchronous Replanning in Generative Robot Policies

Continuous asynchronous replanning is essential for real-time generative robot policies, but independent stochastic initialization can cause mode switching and inconsistent continuation across action chunks. We propose Execution-Aligned Progressive Noise (EAPN), which introduces structured stochasticity at both inter-chunk and intra-chunk levels. Across replanning steps, EAPN propagates a shared noise trajectory and aligns it with the actual execution displacement, establishing execution-aligned inter-chunk correlation. Within each action chunk, it models temporal correlation along action time. The aligned stochastic history is further combined with committed action context to condition subsequent generation, allowing new chunks to continue from execution-consistent generative states rather than restart from independent noise. We evaluate EAPN on D3IL, Kinetix, LIBERO, and real-world manipulation tasks. EAPN improves multimodal behavior consistency on D3IL and achieves an average success rate of 88.59% on Kinetix. On LIBERO, it remains robust and maintains strong task performance even under long inference delays. Real-robot experiments further achieve 90.0% success on Object Storage and 96.7% on bimanual Cloth Folding, demonstrating reliable continuous execution under asynchronous replanning.
