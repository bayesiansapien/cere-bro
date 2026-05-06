# AgentSPEX: An Agent Specification and Execution Language

**Date:** 2026-04-22  
**Source:** [HuggingFace](https://huggingface.co/papers/2604.13346) | [Paper](https://arxiv.org/abs/2604.13346)  
**Raw:** [raw/huggingface/2026-04-22-agentspex-an-agent-specification-and-execution-language.md](../../raw/huggingface/2026-04-22-agentspex-an-agent-specification-and-execution-language.md)

## TL;DR

Current agent orchestration frameworks (LangGraph, DSPy, CrewAI) tightly couple workflow logic to Python, making agents hard to inspect and modify. AgentSPEX is a declarative YAML-based language for specifying agent workflows with explicit control flow, typed steps, branching, loops, parallel execution, reusable submodules, and explicit state management. Workflows run in a sandboxed harness with checkpointing and verification. A visual editor provides synchronized graph and code views. User study shows more interpretable and accessible than existing frameworks.

## Key Findings

- Decouples workflow logic from Python implementation — workflows are inspectable/modifiable without reading Python source
- **Typed steps, branching and loops, parallel execution, reusable submodules, explicit state management**
- Execution harness provides: tool access, sandboxed virtual environment, checkpointing, verification, logging
- Visual editor with synchronized graph and workflow views for authoring and inspection
- Ready-to-use agents for deep research and scientific research included
- Evaluated on 7 benchmarks; user study confirms interpretability advantage

## Architecture

```
AgentSPEX workflow (YAML):
  step: search_query
    type: tool_call
    tool: web_search
    output_type: SearchResult[]
  
  step: filter_results
    type: branch
    condition: len(results) > 0
    branches: [synthesize, request_more]
  
  step: synthesize
    type: llm_call
    prompt_template: "..."
    output_type: Summary

Runtime harness:
  workflow YAML → parser → execution graph → sandboxed env
                                           → checkpointing
                                           → verification
```

## Relation to Prior Wiki Knowledge

AgentSPEX addresses the same "harness matters" problem that **GTA-2 (04-20)** documented from the evaluation side: execution harness engineering accounts for up to 15.7pp of agent performance. GTA-2 measured this as an eval concern; AgentSPEX proposes a principled solution — make the harness explicit and declarative rather than buried in Python glue code.

**Connection to Claude Code architecture (04-17, 04-19)**: Claude Code's permission pipeline (static allow/deny → classifier → interactive dialog) is exactly the kind of explicit control flow that AgentSPEX formalizes for workflows. The difference is that Claude Code's control flow is embedded in TypeScript; AgentSPEX makes it inspectable as a YAML specification.

**Connection to AiScientist File-as-Bus (04-21 parallel digest)**: AiScientist uses files as state containers to make agent context inspectable. AgentSPEX uses explicit state management in the workflow spec. Both are responses to the same problem: agentic systems are opaque because their state and control flow are implicit.

## Open Questions

- How well does YAML-based workflow specification handle dynamic agent behavior that depends on intermediate outputs? Declarative languages have expressive limits for highly adaptive agents.
- Does the sandboxed environment add overhead that makes SDVG-style fast agent loops impractical?
- Can AgentSPEX workflows be automatically generated from natural language descriptions, or does it require manual authoring?

## Related Pages

- [Agent Benchmarks](agent-benchmarks.md)
- [GTA-2 Benchmark](2026-04-20-gta-2-tool-agent-benchmark.md)
- [Claude Code Architecture](2026-04-17-claude-code-architecture.md)
