---
source: farmer/huggingface
farmed: 2026-09-25T17:06:04.306887+00:00
arxiv_id: 2609.27321
url: https://huggingface.co/papers/2609.27321
arxiv_url: https://arxiv.org/abs/2609.27321
date: 2026-09-24
upvotes: 8
authors: ["Xinjie Shen", "Wei Fan", "Xudong Guo", "Jianhong Tu", "Yang Su", "Chuqiao Kuang", "Yinger Zhang", "Dayiheng Liu"]
---

# Verifiable Hidden Dynamics Play: Generating Agentic RL Environments from Solved Mechanisms

**Authors:** Xinjie Shen, Wei Fan, Xudong Guo, Jianhong Tu, Yang Su, Chuqiao Kuang, Yinger Zhang, Dayiheng Liu

**Upvotes:** 8

**Links:** [HuggingFace](https://huggingface.co/papers/2609.27321) · [arXiv](https://arxiv.org/abs/2609.27321)

Language-model agents increasingly face long-horizon tasks with evolving state, interdependent decisions, and delayed outcomes. Scaling their training requires diverse agentic environments, dependable outcome signals, and low extension cost. Existing generation pipelines commonly construct an environment before defining its outcome rule or annotating its trajectories, leaving dynamics and evaluation to be aligned post hoc. VHD-Play reverses this dependency by sampling and solving a mathematical model before a corpus-grounded setter renders its decision process as stateful tools. The executable dynamics and trajectory-scoring reference are inherited from the same solved model. The pipeline produces 3,300 diverse agentic environments at a cost of a few cents each. Training Qwen3.6-35B-A3B on three families raises its mean agentic score from 0.204 to 0.815 in a five-family diagnostic. Gains also appear on held-out instances from all three training families and eight unseen mechanism families, then extend beyond the generated substrate to external benchmarks for general function calling, travel planning, and 365-day e-commerce. On E-Commerce Bench, the trained checkpoint completes every run without bankruptcy and exceeds Qwen3.7-Max. We compare written-out problems with stateful versions that reveal or hide their parameters. The comparison shows that most of the learnable gap lies in stateful interaction rather than underlying problem solving. A frozen 35B setter realizes larger environments, and scale-matched training retains gains as mechanism size and horizon grow, indicating the potential for an evolving training substrate.
