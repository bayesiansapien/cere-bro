---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.07237
url: https://huggingface.co/papers/2605.07237
arxiv_url: https://arxiv.org/abs/2605.07237
date: 2026-05-13
---

# Teaching Language Models to Think in Code

Tool-integrated reasoning (TIR) has emerged as a dominant paradigm for mathematical problem solving in language models, combining natural language (NL) reasoning with code execution. However, this interleaved setup has three key limitations: code often acts as a post-hoc verifier, intermediate NL computations are error-prone, and NL and code play overlapping rather than clearly distinct roles. We propose ThinC (Thinking in Code), a framework in which code itself serves as the reasoner rather than as a tool invoked by NL. A ThinC trajectory begins with a brief NL planning step, after which all reasoning unfolds through code blocks connected only by their execution outputs. We distill 12.2k code-centric trajectories from a teacher model and train ThinC-1.7B and ThinC-4B with supervised fine-tuning followed by reinforcement learning. ThinC-4B consistently outperforms every TIR baseline on five competition-level math benchmarks and even surpasses the much larger Qwen3-235B-A22B-Thinking. Further analysis shows that ThinC reasons through code: 99.2% of its final answers are grounded in interpreter output, and the model recovers reliably from code execution failures without intermediate NL reasoning. Our code and models will be released soon.
