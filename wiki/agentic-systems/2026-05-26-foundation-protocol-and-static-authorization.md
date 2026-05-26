# Foundation Protocol + Static Authorization: the agent coordination + governance pair

**Sources:**
- [arXiv:2605.23218](https://arxiv.org/abs/2605.23218) — Foundation Protocol: A Coordination Layer for Agentic Society, via HuggingFace Daily Papers 2026-05-26.
- [Ken Huang Substack](https://kenhuangus.substack.com/p/why-static-authorization-is-failing) — Why Static Authorization Is Failing in the Age of AI Agents, via Gmail starred RSS 2026-05-25.
- [AI Agents under EU Law](https://nitter.net/LuizaJarovsky/status/2058628835172655555#m) — Luiza Jarovsky AI Ethics Paper Club, via @bayesiansapien Twitter retweet 2026-05-24.

## TL;DR

Three sources on three different surfaces landed within a 48-hour window with the same diagnosis: the substrate around autonomous agents (how they coordinate, how they get authorized, how they are regulated) is the bottleneck, not the agents themselves. Foundation Protocol proposes a graph-first coordination layer with policy, provenance, and audit as first-class concerns. Ken Huang's static-authorization piece argues that RBAC and ABAC structurally cannot govern agents that plan, adapt, chain actions, and operate at machine speed; the fix is intent-based access control (IBAC) at the tool-call gateway. Luiza Jarovsky's compliance architecture paper says EU AI law treats agentic systems as a distinct category that needs different governance scaffolding from classical software. Three independent angles, one shared frame: agent infrastructure is now the load-bearing problem.

## What each piece says

### Foundation Protocol (HF arxiv 2605.23218)

A graph-first coordination layer for the emerging human-AI society. FP unifies heterogeneous entities (agents, tools, resources, humans, institutions, organizations) and supports native multi-party organization with event-based collaboration. Provides economic primitives (metering, receipts, settlement), and treats policy, provenance, and audit as first-class. Designed to wrap and bridge existing protocols rather than replace them, so adoption can be incremental.

Key claim: as autonomous agents scale, the bottleneck shifts from raw model capability to coordination. Coordination needs to be shared infrastructure, not a per-vendor lock-in.

### Static Authorization (Ken Huang)

RBAC and ABAC were designed for predictable bounded actors. Human employees and deterministic services have repeatable behavior; permissions can be enumerated at provisioning time and enforced at access time. Agents break this because they plan dynamically, adapt to runtime context, chain actions across trust boundaries, and operate at machine speed. The natural failure mode is **privilege drift**: permissions granted for one purpose persist as agent behavior evolves, leaving the effective access surface much larger than any current task requires.

The proposed model is IBAC (Intent-Based Access Control). The agent's intent at session start is parsed into structured form, mapped to fine-grained authorization tuples, and enforced at every tool call via a gateway. Reva.AI's AMP is the example deployment: an intent parser, policy mapper, authorization engine (Cedar/OPA/OpenFGA), and tool gateway. The session boundary is now declared purpose, not identity.

### EU AI Law for Agentic AI (Luiza Jarovsky)

Compliance architecture for AI providers under EU law, treating agentic systems as a distinct regulatory category. The piece argues that the agentic-AI regulatory frame needs different scaffolding from the classical AI Act provisions, and lays out an architecture for providers to satisfy compliance obligations on autonomous systems.

## The shared frame

All three pieces accept that the relevant unit of regulation, authorization, and coordination is now the **agent's intent and trajectory**, not the model that runs underneath it or the identity that authenticates it. This is a structural shift: the prior unit (model + user identity) is too coarse to govern agentic behavior. The new unit (intent + tool-call trajectory + accountability chain) needs new infrastructure.

```
   Prior frame                              New frame                        
                                                                            
   user ─auth─► model ─call─► tool          user ─intent─► agent             
                                                          (plan, adapt,     
                                                           chain)            
   auth scope = user identity                                                
   audit = call log                          ┌────────────────────────┐     
                                             │ Foundation Protocol    │     
                                             │ coordination + audit   │     
                                             │ provenance + economic  │     
                                             │ primitives             │     
                                             └────────────────────────┘     
                                             ┌────────────────────────┐     
                                             │ IBAC (intent-based)    │     
                                             │ tool-call gateway      │     
                                             │ continuous enforcement │     
                                             └────────────────────────┘     
                                             ┌────────────────────────┐     
                                             │ EU AI Law for agents   │     
                                             │ provider compliance    │     
                                             │ architecture           │     
                                             └────────────────────────┘     
```

## How this relates to prior wiki pages

The agentic-systems thread has been moving here for weeks. SkillOpt (2026-05-25) and Life-Harness (2026-05-23) established that the model's external state (skill, harness, prompt) is the trainable surface. Foundation Protocol, IBAC, and the EU agentic-law piece extend that frame to a fourth axis: the coordination, authorization, and accountability surface around the agent. Together: stable model + portable harness + portable skill + portable prompt + governed coordination layer.

This also connects to the Decoder routing piece from 2026-05-25 (Adam Kucharski's experiment showing default model selection in Copilot was making analysis answers wrong). The same diagnosis appears at every layer of the stack: defaults are wrong, static decisions made at session start cannot keep up with the agent's evolving runtime behavior.

## Research angle

The cleanest open problem is the formal connection between intent parsing for authorization (IBAC) and skill abstraction (SkillOpt/SkillEvolBench/SkillOS). Both reduce to the same operation: take a natural-language request and project it onto a structured artifact (intent tuples or skill steps) that governs subsequent execution. If a single intermediate representation can serve both authorization scope and skill structure, the agent architecture simplifies materially. No one has published this composition yet.

## Industrial implication

Foundation Protocol is a position paper, not a deployable spec. IBAC via Reva.AI is a production pitch. The EU regulatory framing is forced movement on a 12-18 month timeline. The three together signal that the agent-infrastructure stack is now where vendor positioning matters most, with model-layer competition (the focus of 2024-2025) ceding ground to infrastructure-layer competition through 2026-2027.
