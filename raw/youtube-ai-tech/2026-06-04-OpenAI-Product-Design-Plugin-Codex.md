# Build and share interactive prototypes in Codex

**Channel:** OpenAI  
**Published:** 2026-06-04  
**Source:** https://www.youtube.com/watch?v=_9ImjmzAyus  

## TL;DR
OpenAI has launched a specialized **Product Design plugin** for ChatGPT Codex that streamlines the transition from a design idea (or static image) to a fully interactive, code-based prototype. The plugin can generate multiple visual directions, build functional prototypes, test them across screen dimensions, and export the entire context—including user stories and critique—into **Figma** or a live, shareable URL via the new **Sites** feature.

## Key Takeaways
- **Idea to Interactive:** Converts text descriptions or "visual briefs" (images/sketches) into working code-based prototypes that can be clicked and scrolled.
- **Automated QA:** The model autonomously tests the prototype across different screen dimensions and compares the result against the original reference image to ensure visual fidelity.
- **Figma Integration:** Instead of just screenshots, it sends "Figma artifacts" that include the prototype, user story context, and design critique notes for team collaboration.
- **"Sites" for Instant Hosting:** A new capability allows users to deploy their interactive prototypes as a live website (internal to the workspace) for immediate stakeholder feedback.
- **Human-in-the-loop Refinement:** Designers can annotate specific parts of the generated prototype and ask for iterative refinements.

## Architecture & Optimization Mechanics
- **Self-Testing Loop:** The plugin employs an internal "execution-and-verification" loop where it generates code, runs it in a headless environment, takes screenshots, and uses a vision model to verify alignment with the design brief.
- **Asset Generation:** It automatically generates supporting images and UI assets needed for the experience, reducing the need for external asset pipelines during prototyping.
- **Multimodal Routing:** The workflow likely routes between a creative layout model (for visual directions) and a highly precise code-generation model (for the final interactive prototype).

## Grounded Context (Web Enrichment)
The Product Design plugin was part of a major OpenAI announcement on June 2, 2026, which repositioned **ChatGPT Codex** as a "knowledge-worker automation hub." The release included six role-specific plugins (Design, Sales, HR, Engineering, etc.) aimed at moving beyond simple chat toward complex, multi-step professional workflows. 

The **"Sites"** feature is particularly significant; it marks OpenAI's entry into the "low-code/no-code" hosting market, effectively allowing non-technical users to build and deploy lightweight internal tools in seconds. Currently, Sites is in preview for ChatGPT Business and Enterprise customers, emphasizing secure, private-workspace collaboration over public web hosting.

## Real-World Application / Actionable Step
Amit should use the Product Design plugin to rapidly prototype **AI-native UI concepts**.
- **Action:** Upload a rough sketch of a "Model Compression Dashboard" and ask the plugin to generate an interactive prototype that visualizes pruning results in real-time.
- **Optimization Strategy:** Study the "Self-Testing Loop" mentioned in the video. This pattern (generate -> execute -> verify via vision) can be applied to Amit's work in **Agentic Evals**, where a vision-capable agent verifies if a UI-modifying agent actually achieved the intended visual change.
