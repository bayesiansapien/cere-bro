# Beyond Components: Designing Generative UI for MCP Apps — Ruben Casas, Postman

**Channel:** AI Engineer  
**Published:** 2026-06-03  
**Source:** https://www.youtube.com/watch?v=hCMrEfPG2Yg  

## TL;DR
Ruben Casas (Postman) outlines the evolution of AI interfaces from basic chat windows to **Generative UI** and **Collaborative Canvases**. He identifies the **Model Context Protocol (MCP)** as the critical infrastructure for this shift, providing the necessary sandboxing (double iFrame) and message-passing standards to deliver dynamic, third-party UI safely. The ultimate goal is moving "beyond components" to shared artifacts where humans and agents co-create in real-time.

## Key Takeaways
- **The "Terminal" Phase:** Current AI interfaces are in a "pre-GUI" state. Chat is a temporary bridge, not the final form.
- **Three UI Paradigms:**
    1. **Static:** Agent fills props in pre-built components (predictable but rigid).
    2. **Declarative:** Agent generates JSON/YAML mapped to components at runtime (e.g., **Vercel JSON Render**).
    3. **Generative:** Agent writes raw HTML/CSS/JS on demand (maximum flexibility, higher token cost).
- **Sandboxing is Mandatory:** Generative UI requires strict isolation. MCP's double iFrame standard is the industry's answer to executing untrusted agent-generated code safely.
- **Strategic Validation:** Anthropic’s decision to build "Claude Artifacts" using the MCP app pattern (rather than a proprietary engine) validates MCP as the universal delivery mechanism for generative UI.

## Core Architecture & Research Claims
- **Collaborative Artifacts:** The next frontier is not just "showing" UI, but "working together" on it. The **Excalidraw MCP app** is cited as the primary example, allowing agents to stream diagrams that humans can then manually edit on a shared canvas.
- **The "Radio-to-TV" Analogy:** We are currently treating AI like "radio shows with cameras"—limiting new tech to old paradigms (chat). True AI-native UI will involve floating, context-aware windows and persistent shared spaces.
- **Postman’s MCP Suite:** Postman has released an **MCP Inspector** and **MCP Generator** to help developers bridge existing APIs into this new "generative" ecosystem.

## Grounded Context (Web Enrichment)
As of June 2026, the **Model Context Protocol (MCP)** has achieved widespread adoption as the "GUI for the new computer." The shift towards **Collaborative Canvases** is being led by tools like **Excalidraw** and **Postman**, which allow for bidirectional interaction between the agent’s logic and the user’s manual adjustments. 

Furthermore, **Vercel’s JSON Render** has emerged as the preferred "middle ground" for enterprise apps, allowing for "Declarative Generative UI." This approach provides the flexibility of AI-driven layout changes while maintaining strict adherence to corporate design systems and minimizing the security risks associated with raw code execution. Ruben Casas’s vision suggests that the "Jarvis moment" will not come from a better chatbot, but from a persistent, sandboxed environment where agents can generate the exact tool a user needs in the moment.
