# Claude Fable 5 built a Mumbai local simulator in one shot

**Channel:** Varun Mayya  
**Published:** 2026-06-13  
**Source:** https://www.youtube.com/watch?v=ncc-6Hka6kQ  

## TL;DR
Claude Fable 5 demonstrated its "Mythos-class" reasoning by generating a complex, 3D Mumbai local train network simulator in a single "one-shot" prompt. The simulation includes live data mapping, physics-based movement, a functional UI dashboard tracking passenger metrics and delays, and localized 3D visualizations with authentic station announcements.

## Key Takeaways
- **One-Shot Simulation:** Fable 5 can architect, code, and deploy multi-component simulations (3D visuals, data engines, UI) from a single natural language description.
- **Live Data Integration:** The simulator maps real-time train data to visualize passenger movement (persons per hour) and average delays across the network.
- **Localized Multimodality:** Beyond code, the model successfully implemented localized audio triggers (e.g., Churchgate platform announcements) in its one-shot build.
- **Spatial Reasoning:** The ability to render a 3D Churchgate station visualization implies a high degree of spatial-to-code mapping, a key differentiator for the Fable 5 model.
- **Zero Effort Engineering:** The demo highlights the shift from "writing code" to "describing systems," where the AI handles the boilerplate and complex logic of 3D rendering and state management.

## Architecture & Optimization Mechanics
- **Long-Horizon Engineering:** Fable 5 ranks #1 on **SWE-bench Pro (80.3%)**, indicating its proficiency at maintaining architectural integrity across massive codebases. For Amit, this suggests that the model’s internal attention mechanisms are optimized for coherent multi-file generation.
- **Autonomous Experiment Loops:** Using the `/goal` command, Fable 5 doesn't just generate text; it runs internal simulation/correction cycles. This is a form of "Inference-time Search" or "Chain of Thought Simulation" that allows it to verify the physics of its own 3D outputs before presenting them.
- **Context Management:** With a **500,000 token context window**, Fable 5 can hold an entire 3D library (like Three.js or Babylon.js) and the project's logic in active memory simultaneously, minimizing "forgetting" errors during the generation of complex shaders or network logic.

## Grounded Context (Web Enrichment)
Released on June 9, 2026, Fable 5 is Anthropic's bridge between general-purpose assistants and autonomous engineering agents. While it has been widely lauded for "one-shotting" games like Minecraft and Pokémon Gen-1, its real-world utility is being proven in enterprise-scale migrations (e.g., Stripe’s 50M line Ruby migration).

However, as of June 12, 2026, the US government has suspended access to Fable 5 due to its capability to "read codebases and find software flaws," a side effect of its high-level reasoning. This makes the Mumbai Local Simulator demo one of the last public showcases of the model's full capabilities before its temporary shutdown.

## Real-World Application / Actionable Step
- **Prompting for Complexity:** When Fable 5 returns (or when using equivalent models like MiniMax M3), Amit should stop prompting for "functions" and start prompting for "autonomous systems" (e.g., "Build a real-time visualization of our inference pipeline latency across 10 regions").
- **Visual Optimization Research:** Study how Fable 5 maps spatial data to code. If the model can "one-shot" 3D simulations, it likely uses a high-density tokenization strategy for geometric primitives that could be applied to optimizing 3D AI workloads.
- **Redundancy with Open Models:** Given the recent ban, any mission-critical simulator should be built using a **reproducible script** that can be run against open-weights models if proprietary APIs are revoked.
