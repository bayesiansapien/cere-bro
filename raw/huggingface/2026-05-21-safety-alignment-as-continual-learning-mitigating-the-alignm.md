---
source: farmer/huggingface
farmed: 2026-05-22T10:21:55.060746+00:00
arxiv_id: 2602.07892
url: https://huggingface.co/papers/2602.07892
arxiv_url: https://arxiv.org/abs/2602.07892
date: 2026-05-21
---

# Safety Alignment as Continual Learning: Mitigating the Alignment Tax via Orthogonal Gradient Projection

Safety post-training can improve the harmfulness and policy compliance of Large Language Models (LLMs), but it may also reduce general utility, a phenomenon often described as the alignment tax. We study this trade-off through the lens of continual learning: sequential alignment stages expose the model to shifted data distributions and objectives, and their gradients may interfere with directions that support previously acquired general capabilities. This view does not claim that all alignment degradation has a single cause; rather, it provides a useful first-order mechanism for mitigating one important source of capability regression. We propose Orthogonal Gradient Projection for Safety Alignment (OGPSA), a lightweight update rule that estimates a low-rank reference subspace from gradients on a small set of general-capability data and removes from each safety gradient the component lying in this subspace. The resulting update is the steepest local safety-descent direction subject to first-order preservation constraints on the reference objectives. OGPSA is compatible with standard post-training pipelines and avoids large-scale replay, although it introduces periodic reference-gradient computation. Across Supervised Fine-Tuning (SFT), Direct Preference Optimization (DPO), and sequential SFTrightarrowDPO settings, OGPSA improves the observed safety--utility trade-off over standard baselines. Under the sequential SFTrightarrowDPO pipeline, the average performance gain increases from 33.98\% to 42.74\% on Qwen2.5-7B-Instruct and from 19.74\% to 32.98\% on Llama3.1-8B-Instruct. We have open sourced our code at https://github.com/SunGL001/OGPSA.
