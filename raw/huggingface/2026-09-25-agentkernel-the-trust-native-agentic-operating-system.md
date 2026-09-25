---
source: farmer/huggingface
farmed: 2026-09-25T22:51:58.846051
arxiv_id: 2609.29647
url: https://huggingface.co/papers/2609.29647
arxiv_url: https://arxiv.org/abs/2609.29647
date: 2026-09-25
upvotes: 4
---

# AgentKernel: The Trust-Native Agentic Operating System

Modern AI agents routinely cross trust boundaries: they ingest untrusted content, combine it with privileged instructions, persist intermediate beliefs in long-term memory, and invoke privileged tools. This creates an attack surface in which malicious payloads can enter through model inputs and cause harmful tool actions. Yet current governance stacks remain application-level middleware that share a process trust boundary with the agents they monitor. We argue that agents need an operating-system substrate providing mandatory, non-bypassable services for identity, input mediation, memory governance, and execution control.
  We introduce AgentKernel, a trust-native agent operating system built around the premise that security must be a first-class design constraint. AgentKernel wraps the agent lifecycle in a mandatory enforcement boundary organized into four pillars: Identity, Perception, Cognition, and Execution. Each pillar adapts classical OS security principles to failures at the semantic plane, including delegation abuse, prompt injection, memory poisoning, and tool misuse.
  AgentKernel treats structural security as a capability multiplier. Kernel-managed identity supports trustworthy cross-organization collaboration; graduated perception replaces brittle single-point filters; information-flow-controlled memory improves retrieval fidelity while limiting poisoning; and semantic-to-kernel enforcement permits broader tool privileges behind a non-bypassable boundary. We position AgentKernel as the missing OS layer beneath orchestration frameworks, agent runtimes, governance platforms, and execution sandboxes, and use systematic comparison and security analysis to show how a single integrated architecture can enforce security across the full agent lifecycle.
