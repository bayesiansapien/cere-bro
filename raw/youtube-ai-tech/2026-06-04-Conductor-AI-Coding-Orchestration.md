# Conductor CEO Charlie Holtz Walks Us Through His AI Coding Setup

**Channel:** Y Combinator  
**Published:** 2026-06-04  
**Source:** https://www.youtube.com/watch?v=fQmlML9Lay4  

## TL;DR
Charlie Holtz, CEO of Conductor (YC S24), demonstrates a high-velocity development workflow where code is treated as "sawdust"—a byproduct of describing what you want. His setup centers on parallel agent orchestration, using Git worktrees to allow multiple instances of Claude Code to work simultaneously on different features or experiments. He advocates for a "conductor" mindset: managing, reviewing, and merging agent outputs rather than writing raw code by hand.

## Key Takeaways
- **Parallelism via Worktrees:** Conductor uses Git worktrees to spin up isolated workspaces for each task. This enables running multiple agents in parallel without file conflicts.
- **"Code as Sawdust":** The core value is in the prompts and high-level descriptions. If a new model version drops, you should be able to rerun your prompts to regenerate better code, making the old code disposable.
- **Human-only Zones:** Maintain "slot-free zones" or "human eyes only" sections in the codebase to prevent AI from introducing low-quality patterns that then get amplified in a "vicious cycle."
- **Experimental Velocity:** Holtz kicks off many parallel workspaces for "random ideas." Most are discarded, but the speed of experimentation allows for rapid discovery of the best implementation path.
- **Tool Selection:** Reaches for **Claude Opus** for creative partnering and architecture, and **GPT-5 Codex** as the "workhorse" for powering through specific debugging or tool-heavy tasks.

## Architecture & Optimization Mechanics
- **Conductor Tech Stack:** Built using **Tauri** (Rust backend, TypeScript frontend) for the desktop app, with a **Phoenix (Elixir)** web backend.
- **Context Management:** Uses massive `cloud.md` and `skills` files (hundreds of lines) to define engineering practices and "guardrails" for the agents.
- **Inference Setup:** Runs local models (like **Parakeet** for speech-to-text) on a high-spec machine (128GB RAM) but advocates for cloud-based agent environments to avoid local CPU/battery constraints.

## Grounded Context (Web Enrichment)
Conductor (YC S24) is positioned as a "CEO dashboard" for AI agents. Since this video was recorded, **Conductor Cloud** has entered public beta, allowing agent sessions to persist in the cloud even when the local laptop is shut. This aligns with the trend of moving agentic execution away from local dev machines toward high-compute, isolated server environments. 

The industry is seeing a shift toward "Malleable Software," a concept Holtz touches on. Similar to video game "modding," software is becoming something that users can customize on the fly by tweaking the underlying AI prompts that generate the interface and logic.

## Real-World Application / Actionable Step
Amit should leverage the **Parallel Experimentation** workflow for his inference optimization research.
- **Action:** Use Git worktrees (or a tool like Conductor) to simultaneously test 3 different quantization techniques (e.g., GPTQ vs. AWQ vs. GGUF) on the same model.
- **Action:** Implement a "Human-only" guardrail in his optimization scripts—specifically for the mathematical kernels or attention mechanism logic—to ensure the AI doesn't "hallucinate" incorrect numerical optimizations.
