---
source: farmer/huggingface
farmed: 2026-10-21T21:51:29+05:30
arxiv_id: 2610.21791
url: https://huggingface.co/papers/2610.21791
arxiv_url: https://arxiv.org/abs/2610.21791
date: 2026-10-20
---

# RSIFlow: Adaptive Self-Improvement Workflows with an Evolving Meta-Agent

Large language model (LLM) agents have demonstrated strong capabilities in complex tasks, including code generation, tool use, and multi-hop question answering. Existing self-improvement methods enhance agent performance through model optimization, harness evolution, and executable artifact refinement, while recursive self-improvement (RSI) further extends optimization to the improvement mechanisms themselves. However, adapting self-improvement workflows to evolving performance bottlenecks while improving workflow orchestration through execution feedback remains a key challenge. We propose RSIFlow, a Recursive Self-Improvement framework that integrates adaptive workflow orchestration with meta-agent capability evolution. RSIFlow diagnoses performance bottlenecks from task-agent trajectories and environmental feedback to dynamically select component-specific improvement workflows. The meta-agent then distills workflow outcomes into component-specific skills and cross-component principles, evolving its own harness to improve subsequent workflow orchestration. Experiments across six benchmarks and two backbone models show that RSIFlow achieves the SOTA average performance on all benchmarks. Ablation studies further demonstrate the contributions of adaptive workflow orchestration and meta-harness evolution. Code is available at https://github.com/1HUAN1/RSI-Flow.
