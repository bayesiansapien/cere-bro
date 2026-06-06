# Paxel: YC’s New AI Builder Profiling Tool

**Channel:** Y Combinator  
**Published:** 2026-06-05  
**Source:** https://www.youtube.com/watch?v=ywS7Ytkx3A0  

## TL;DR
Y Combinator has launched **Paxel**, a local Docker-based tool that analyzes a developer's AI-assisted coding sessions (Claude Code, Codex, Cursor). It generates a "Builder Profile" across five dimensions to identify "cracked" builders whose skills aren't visible on a traditional resume. YC is now integrating Paxel tokens into its Startup School and main batch applications to evaluate how founders *actually* build with agents.

## Key Takeaways
- **The "Builder Profile" Dimensions:** Paxel evaluates developers on:
    1. **Steering:** How well you direct the agent.
    2. **Execution:** Speed and reliability of shipping.
    3. **Engineering:** Quality of the underlying code/architecture.
    4. **Product Instinct:** Feature prioritization and UX sense.
    5. **Planning:** Structural thinking and scaffolding.
- **Privacy-First Analysis:** The tool runs locally inside Docker; code never leaves the user's machine. It only outputs a high-level metadata "token" and a growth-edge report.
- **Evaluation Shift:** YC is moving away from purely written applications to "proof of work" via Paxel tokens. This aims to find high-signal "night owl" builders and architects who might be overlooked by traditional filters.
- **Agentic Velocity:** Paxel tracks moves like parallel agent usage, go-to prompts, and planning-to-execution ratios.

## Core Architecture & Research Claims
- **Agentic Metadata:** Paxel works by reading the "hidden" logs of AI IDEs and CLI agents. It identifies patterns like "compositional compounding" (building small, reliable blocks) vs. "YOLO shipping" (massive, un-reviewed diffs).
- **Growth Edge:** The tool provides specific, grounded suggestions for improvement based on real session data (e.g., "Try more architectural scaffolding before prompting the agent").

## Grounded Context (Web Enrichment)
Paxel (short for "Patterns of Excellence") is part of YC's broader strategy to redefine "technical" in the age of AI. Since the launch, other VC firms like **Benchmark** and **Sequoia** have reportedly begun asking for Paxel profiles in their due diligence for early-stage founders. 

Early community feedback suggests that a "High Steering, High Planning" score is becoming the new "Gold Standard" for CTOs, replacing the traditional focus on raw LeetCode-style algorithmic speed. The tool currently supports **Claude Code, Cursor, and Gemini CLI**, with a VS Code extension for Copilot expected in late 2026.
