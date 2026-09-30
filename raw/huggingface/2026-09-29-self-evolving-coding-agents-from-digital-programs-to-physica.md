---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.928441+00:00
arxiv_id: 2609.35432
url: https://huggingface.co/papers/2609.35432
arxiv_url: https://arxiv.org/abs/2609.35432
date: 2026-09-29
---

# Self-Evolving Coding Agents: From Digital Programs to Physical-World Intelligence

Vision-language-action (VLA) and world-action (WAM) models map observations and instructions directly to robot actions. This directness ties a policy to training: minor layout or viewpoint changes cause failure, and instructions generalize poorly. The root cause lies in representation: task requirements, conditions, progress, and failure recovery are implicitly encoded in action sequences, making them difficult to inspect or revise. Digital coding agents offer a precedent: LLMs call tools, verify results, and revise from feedback as executable code. The same working pattern of explicit state, manageable execution, and revisable procedures underlies generalization and long-horizon execution in the physical world, letting physical experience return as reusable programs, memory, or evidence. We propose Physical Coding, representing task state and execution as code. Code as World records objects, relations, constraints, and progress; Code as Policy organizes planning, verification, recovery, and execution. We build HexaAnything, which calls perception, planning, and control tools, including VLA/WAM policies, and makes in-the-loop decisions from external feedback. Verified traces become data and memory, enabling evolution from tools and Harness to model weights, architectures, and ultimately hardware and task design. On RoboCasa365, HexaAnything improves Composite-Unseen and overall success over XR-1 VLA, and its Harness-trained HexaModel beats the base on every split, indicating code traces internalize physical execution. On PhyBench and a dual-arm AgileX robot, the agent autonomously completes physics experiments and most tabletop tasks, often faster than published results. We observe data, model, and tool self-evolution; future work targets weight internalization, autonomous redesign of architectures, languages, representations, and tasks, and deployment in manufacturing and science.
