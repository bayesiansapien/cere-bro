---
source: farmer/huggingface
farmed: 2026-09-09T05:28:24.738031+00:00
arxiv_id: 2609.08183
url: https://huggingface.co/papers/2609.08183
arxiv_url: https://arxiv.org/abs/2609.08183
date: 2026-09-09
---

# NeoHorse-1: Towards Recursive Self-Improvement via Agentic Post-Training with Routing Harness

Recursive self-improvement (RSI) requires a concrete mechanism through which an AI system observes its capabilities and converts that evidence into the next round of learning. We present NeoHorse-1, a family of agent-native models developed to explore this path through agentic post-training. Our system combines a heterogeneous model pool with intelligent routing, recording the predicted capability demand, selected service tier, and subsequent interaction for each user turn. These records are converted into training examples that preserve interleaved reasoning, tool calls, and harness context, and are admitted through structural validation, six-dimensional semantic evaluation, and subscene-level labeling. Routing signals organize supervised fine-tuning into a three-stage curriculum and extend to routing-guided on-policy distillation, where a teacher supervises student-generated responses under the same progression. Capability-guided allocation then converts evaluation feedback into the next training mixture, closing an evaluation-selection-update loop in which what the system learns to do shapes what it learns from next. Across eleven benchmarks covering harness-based agents, tool use, coding, and instruction following, post-training raises the macro-average from 58.94 to 64.87 at 4B and from 65.60 to 69.04 at 9B, substantially narrowing the aggregate gap between the post-trained 4B model and the 9B base model. NeoHorse-1 provides an initial prototype of this feedback-driven process and a path toward harness-mediated RSI across successive iterations.
