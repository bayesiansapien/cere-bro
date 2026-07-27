---
source: farmer/huggingface
farmed: 2026-07-27T13:15:36.767293
arxiv_id: 2607.14277
url: https://huggingface.co/papers/2607.14277
arxiv_url: https://arxiv.org/abs/2607.14277
date: 2026-07-27
---

# Multi-Head Latent Control: A Unified Interface for LLM Agent Decision Making

Large language models are increasingly deployed as agents, but reliable agentic behavior requires more than next-token prediction. At inference time, it is preferred that an agent can decide whether to proceed with its current reasoning, defer to a stronger model, request additional information, invoke external tools, or abstain under the given setup. Existing approaches address these decisions through prompt-level routing, external orchestration, or task-specific fine-tuning, which primarily rely on input-side signals, and are often costly and difficult to maintain as model backbones evolve. We ask whether such control decisions can be inferred directly from a model's latent generation process. We introduce Multi-Head Latent Control, a lightweight layer that reads hidden-state trajectories from a frozen LLM or VLM to produce deployment-time control signals. A Capability Head predicts whether the current model can solve the instance or should defer to a stronger collaborator, while a Resolution Head predicts appropriate resolution decision Clarification, Tool Use, Abstention, or Direct Answering. Both heads are trained only on latent traces from the same frozen LLM backbone, enabling post hoc adaptation without modifying the model. Across language and vision-language settings, Multi-Head Latent Control consistently improves the quality-cost tradeoff of multi-model systems, enabling early handoff from partial generations and more accurate intervention decisions. In routed execution (small + large model), it reduces large-model usage by up to 90.7 percent on AndroidWorld and 27-53 percent on average across benchmarks, while retaining most of large-model performance. Additionally, the learned control signals improve tool-use decision quality, yielding up to +158 percent relative score gain and 65.5 percent fewer missed-required tool calls.
