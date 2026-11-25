---
source: farmer/huggingface
farmed: 2026-11-25T05:07:08.917899+00:00
arxiv_id: 2611.31201
url: https://huggingface.co/papers/2611.31201
arxiv_url: https://arxiv.org/abs/2611.31201
date: 2026-11-24
---

# Embo-Harness: Towards Understanding Frontier-Model-as-Policy Harness

Frontier multimodal models exhibit extraordinary generalization in generating robot actions from observations and instructions, enabling a new paradigm in which they serve directly as policies within closed-loop robotic harnesses. However, the design principles of such harnesses, and the capabilities underlying their strong performance, remain unclear. We present Embo-Harness, a framework for systematically studying frontier-model-as-policy harnesses. We investigate four components of the robotic agentic loop, namely, prompting, planning, action execution, and tool use, and distill six empirical findings into a practical recipe. This recipe prioritizes interfaces that exploit the model's native visual reasoning and tool-use capabilities over handcrafted plans, skills, or action priors, and identifies effective choices for action representation, chunking, reasoning effort, visual observations, short multi-action sequences, and policy refinement. On RoboLab-120, Embo-Harness achieves an 83.3\% success rate, outperforming the strongest reported baseline by 26.2 percentage points. It also succeeds in 15 of 20 zero-shot trials across four real-world manipulation tasks. Beyond performance, controlled interventions indicate that the studied model depends more strongly on accurate spatial target estimation than on explicit low-level joint or trajectory generation. These results provide both a practical recipe for building strong frontier-model-as-policy harnesses and a clearer account of the capabilities that drive their performance.
