---
source: farmer/huggingface
farmed: 2026-09-09T05:28:24.738031+00:00
arxiv_id: 2609.06758
url: https://huggingface.co/papers/2609.06758
arxiv_url: https://arxiv.org/abs/2609.06758
date: 2026-09-09
---

# Agentic Visual Generation: From Generative Models to Agentic Control

Visual generation is evolving from generative models used through a single invocation into agentic control processes that can plan, select tools, inspect intermediate synthesized outputs, revise failures, and reuse prior experience. In most existing systems, the controller is an LLM or VLM, while visual generation models serve as tools or executors. However, existing work lacks a consistent criterion for determining when a generation system becomes agentic. Planning depth, tool use, multi-role collaboration, and reinforcement learning are often treated as evidence of agenticity, even though none of them necessarily determines which generation decisions the controller can make. We organize the field according to what the controller can directly control in the generation process. At L1 Conditioning Control, the controller prepares the input to a predetermined generator but does not control which visual operation is executed. At L2 Execution Control, it selects and invokes actual generation, editing, rendering, or other content-modifying operations. At L3 Outcome-Adaptive Control, it observes an intermediate outcome and uses that observation to change a subsequent operation within the current task. At L4 Experience-Adaptive Control, it retains experience from completed tasks and uses that experience to change decisions on future tasks. L0 Fixed Support separately denotes generators, editors, evaluators, reward models, benchmarks, and fixed pipelines without a deployed controller that makes generation-level decisions. These levels describe a progressively broader decision-making scope rather than model size, system complexity, output quality, tool or role count, or training method. Applying this framework across image, video, editing, 3D, world, slide, and user-interface generation reveals how controller capabilities have evolved and how their mechanisms are distributed across levels.
