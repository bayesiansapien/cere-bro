# Claude Code Architecture: A Deep Reading

**Date:** 2026-04-19  
**Source:** HuggingFace Daily Papers  
**Paper:** [arxiv 2604.14228](https://arxiv.org/abs/2604.14228)  
**Raw:** [raw/huggingface/2026-04-19-dive-into-claude-code-design-space-of-todays-and-future-ai-agent.md](../../raw/huggingface/2026-04-19-dive-into-claude-code-design-space-of-todays-and-future-ai-agent.md)

---

## TL;DR

A comprehensive architectural analysis of Claude Code (v2.1.88) via its public TypeScript source, compared against OpenClaw (an independent open-source agent). Identifies five design values, thirteen principles, and maps them to specific implementation choices. The core loop is a simple while-loop; all the interesting code is in the systems around it.

---

## Key Findings

**Five human values driving the architecture:**
1. Human decision authority
2. Safety and security
3. Reliable execution
4. Capability amplification
5. Contextual adaptability

**Thirteen design principles** derived from these values, each traceable to specific code choices.

**Core systems around the while-loop:**
- **Permission system**: 7 modes + an ML-based classifier for deciding what requires approval
- **Compaction pipeline**: 5-layer context management to handle context window limits gracefully
- **Extensibility**: MCP (Model Context Protocol), plugins, skills, and hooks — four distinct extension mechanisms
- **Subagent delegation**: orchestration mechanism for spinning off subagents with scoped permissions
- **Session storage**: append-oriented (write-only log), not mutable state

**Claude Code vs. OpenClaw differences:**
| Dimension | Claude Code | OpenClaw |
|-----------|-------------|---------|
| Safety evaluation | Per-action (ask before each risky step) | Perimeter-level (control at entry) |
| Structure | Single CLI loop | Embedded runtime in gateway control plane |
| Context management | Context-window extensions | Gateway-wide capability registration |
| Use case | Developer CLI | Multi-channel personal assistant gateway |

**Six open design directions for future agents:**
- Verifiable memory
- Multi-agent trust hierarchies
- Adaptive context management
- Cross-session learning
- Principled capability registration
- Policy-grounded safety evaluation

---

## Why It Matters

This is the most rigorous public architectural analysis of a production agentic coding system. The finding that the core loop is trivial (call model, run tools, repeat) and the interesting work is in surrounding systems — permissions, compaction, extensibility — is important for anyone building agent infrastructure. The comparison with OpenClaw makes the design decisions feel deliberate rather than arbitrary.

The ML-based permission classifier is particularly notable: instead of a fixed rule set, Claude Code trains a model to decide what requires human approval. This creates a soft safety boundary that can generalize to novel actions rather than requiring exhaustive rule specification.

---

## Related Pages

- [Corpus2Skill: Knowledge Navigation](2026-04-18-corpus2skill-knowledge-navigation.md)
- [UniDoc-RL: Visual RAG](2026-04-19-unidoc-rl-visual-rag.md)
- [DR3-Eval: Deep Research Benchmark](2026-04-18-dr3-eval-deep-research-benchmark.md)
