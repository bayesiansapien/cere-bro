---
source: farmer/huggingface
farmed: 2026-05-29T09:54:41Z
arxiv_id: 2605.27995
url: https://huggingface.co/papers/2605.27995
arxiv_url: https://arxiv.org/abs/2605.27995
date: 2026-05-29
---

# AsyncTool: Evaluating the Asynchronous Function Calling Capability under Multi-Task Scenarios

Large language model (LLM)-based agents have shown strong capabilities in using external tools to solve complex tasks. However, existing evaluations often overlook the temporal dimension of tool use, especially the impact of tool response latency, and are usually limited to single-task settings. In real-world applications, multiple tasks often need to be executed concurrently, and overall efficiency depends on whether an agent can use idle time while waiting for tool responses. We refer to this capability as asynchronous tool calling. To evaluate it, we propose AsyncTool, a benchmark for assessing LLM-based agents in interactive multi-task tool-use environments with delayed tool feedback. AsyncTool presents multiple heterogeneous tasks simultaneously and simulates realistic tool response latency during execution. Using a hybrid data evolution strategy, we construct a diverse asynchronous multitasking dataset that covers multiple scenarios and tool-use patterns. We evaluate models at the step, sub-task, and task levels, and introduce efficiency-oriented metrics to measure task coordination and completion efficiency. Extensive experiments show that delayed tool feedback poses substantial challenges to current agents and leads to clear performance degradation. Models that better coordinate task switching, dependency tracking, and state maintenance achieve stronger performance on AsyncTool. Our analysis identifies key failure modes of current tool-using agents and provides practical insights for designing future systems with stronger temporal reasoning and coordination capabilities.
