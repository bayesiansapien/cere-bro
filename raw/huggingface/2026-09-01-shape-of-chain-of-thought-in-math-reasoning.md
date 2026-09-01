---
source: farmer/huggingface
farmed: 2026-09-01T08:46:18.970698+00:00
arxiv_id: 2608.28600
url: https://huggingface.co/papers/2608.28600
arxiv_url: https://arxiv.org/abs/2608.28600
date: 2026-09-01
---

# SHAPE of Chain-of-Thought in Math Reasoning

Large language models (LLMs) achieve strong performance on mathematical reasoning benchmarks, yet the mathematically meaningful skills underlying their reasoning remain underexplored. We introduce SHAPE, a framework that analyzes Chain-of-Thought (CoT) trajectories through two lenses developed in mathematics education: (1) semantic spaces: the model's evolving mathematical interpretations of a problem (e.g., algebraic, geometric), and (2) heuristics: the specific mathematical actions taken within those spaces (e.g., simplifying the problem, working backward). We first use SHAPE to analyze the reasoning patterns of various models. Our findings reveal that the mathematical heuristics employed by a model better explain final answer correctness than traditional CoT features. Furthermore, models are likely to reach correct solutions by concentrating their reasoning effort within a few semantic spaces rather than exploring many disparate ones -- a pattern consistent with human behavior. Next, we utilize the SHAPE lens to evaluate whether post-training truly enhances mathematical proficiency. We find that reinforcement learning induces mode-seeking in heuristic usage. Lastly, we post-train LLMs by promoting diverse heuristics and demonstrate its effectiveness in improving accuracy. Overall, SHAPE provides a theoretically-grounded diagnostic framework for decoding LLM reasoning and offers a new path toward post-training LLMs for math reasoning. The code for our model is available at https://github.com/holi-lab/SHAPE-of-CoT
