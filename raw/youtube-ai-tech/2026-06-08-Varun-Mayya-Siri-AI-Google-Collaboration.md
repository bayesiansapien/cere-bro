# The New Siri Is Secretly Running On Google

**Channel:** Varun Mayya  
**Published:** June 8, 2026  
**Source:** https://www.youtube.com/watch?v=NSvxac85zUY  

## TL;DR
Apple has reportedly "given up" on fixing Siri in isolation, entering a deep collaboration with Google to power the next generation of "Siri AI." While Apple maintains the branding of "Apple intelligence" running on-device and in Private Cloud Compute, the underlying heavy lifting for conversational depth and web-live info is likely handled by Google's Gemini models.

## Key Takeaways
- **The Google Pivot:** Apple is collaborating with Google on its foundation models, a major strategic shift after years of trying to build competitive LLMs entirely in-house.
- **Siri AI Capabilities:** The new Siri is conversational, context-aware (remembers previous turns), and can "see" what's on your screen to take actions across apps (e.g., finding a photo and adding it to an album).
- **Hybrid Inference:** All data is processed with Apple's privacy standards, using a mix of on-device models for personal data and Google-powered cloud models for complex reasoning/web retrieval.
- **On-Device Agency:** Siri can now dig through personal notes, photos, and emails to answer specific context-heavy questions, a feat achieved by local fine-tuning on Apple's silicon.

## Architecture & Optimization Mechanics
For a researcher in AI Optimization, this is a masterclass in **LLM Routing and On-Device vs. Cloud Balance**.
- **The Routing Layer:** Apple must be using a highly efficient "router" to decide which queries stay local (privacy-sensitive, low compute) and which get sent to the Google/Apple Cloud (reasoning-heavy). This is the "fastest/cheapest/best" optimization Amit specializes in.
- **Unified Memory Optimization:** Apple's advantage remains its Unified Memory Architecture (UMA), which allows local models to access large context windows (photos, text, app state) without the PCIe bottlenecks found in traditional PC setups.

## Grounded Context (Web Enrichment)
The collaboration was officially confirmed at WWDC26. Apple's "Private Cloud Compute" uses custom Apple Silicon servers to ensure that even when data is sent to the cloud (potentially hitting Gemini-powered backends), it is never stored or accessible to anyone, including Apple. Google's Gemini 3.5 Flash is rumored to be the primary engine for the "Siri Live" features, providing the low-latency response needed for a voice assistant.

## Real-World Application / Actionable Step
**Edge-Cloud Routing:** Amit should use this "Siri AI" model to design a local-first routing framework. He should focus on building a "Small Language Model" (SLM) that acts as a local "gatekeeper," performing initial PII (Personally Identifiable Information) scrubbing and intent classification before deciding to route to a high-parameter cloud model like Gemini 3.5 or GPT-5.5. This maximizes privacy and minimizes cloud inference costs.
