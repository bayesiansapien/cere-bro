# OncoAgent: Dual-tier multi-agent framework for privacy-preserving oncology decision support

**Source:** [HuggingFace blog (lablab-ai-amd-developer-hackathon)](https://huggingface.co/blog/lablab-ai-amd-developer-hackathon/oncoagent-official-paper) · [raw](../../raw/rss/2026-05-09-huggingface-blog-oncoagent-a-dual-tier-multi-agent-framework-for-privacy.md)
**Tier:** 3 — domain-specific multi-agent (medical)

## TL;DR

A hackathon-origin multi-agent framework for oncology clinical decision support, with an explicit privacy-preserving (dual-tier) architecture. Read for the architecture pattern, not the empirical claims.

## Why this matters (lightly)

The dual-tier structure (sensitive data isolated from agent reasoning) is the same pattern Google DeepMind described for their AI co-clinician research initiative ([covered 2026-05-08, via @TheTuringPost retweet](../../raw/twitter/2026-05-08-night.md)): a "Talker" agent interacts with the patient, a "Planner" agent monitors the conversation. The OncoAgent / DeepMind framings make the dual-agent privacy/safety boundary look like an emergent design pattern in clinical multi-agent systems. Worth flagging as a candidate for a concept page once a third example lands.

## Open questions

- **Is the dual-tier-for-privacy pattern actually generalizable?** Three examples (DeepMind, OncoAgent, plus older oncology pilots) is the threshold. Two does not yet make a pattern.
- **Is the empirical evaluation rigorous?** Hackathon-origin papers typically have small evaluation surface. Worth checking the actual writeup before treating any specific number as load-bearing.

## Related pages

- [Multi-agent systems concept page](multi-agent-systems.md)
