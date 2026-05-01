# Pragmatic Engineer: AI Load Breaks GitHub; Anthropic's Trust Speedrun

**Source:** Gergely Orosz / Pragmatic Engineer (2026-04-30)
**Link:** [Post](https://newsletter.pragmaticengineer.com/p/the-pulse-github-breaks)
**Tier:** 2 — AI industry / engineering practice
**Raw:** [../../raw/rss/2026-04-30-pragmatic-engineer-the-pulse-ai-load-breaks-github-why-not-other-vendors.md](../../raw/rss/2026-04-30-pragmatic-engineer-the-pulse-ai-load-breaks-github-why-not-other-vendors.md)

## TL;DR

Two threads. **(1) GitHub reliability has collapsed** — third-party trackers measured GitHub at "one nine" (90%) last month and *zero nines* (86%) this month. GitHub leadership blames a 3.5× load increase from AI traffic; Mitchell Hashimoto (Ghostty, ex-Hashicorp) is publicly leaving GitHub citing professional unsuitability. Other AI-heavy vendors aren't seeing comparable degradation, suggesting the cause is partly self-inflicted. **(2) Anthropic's trust speedrun** — silent Claude Code nerfing, banning companies, baffling price rises in the past month, contributing to a perception that Anthropic is in its "extraction era."

## Why it matters

The GitHub reliability story is the **first major operational data point that AI-heavy load is breaking foundational dev infrastructure**. If correct, this has knock-on effects:
- CI/CD pipelines (most teams pull from GitHub) become flaky.
- Claude Code, Cursor, Codex CLI agents that rely on `git` operations against GitHub face baseline noise.
- The "build on AI to develop AI" loop becomes more fragile.

The Anthropic story is the **first Pragmatic Engineer post critical of Anthropic** after months of mostly favorable coverage. Combined with the Bun fork divergence (04-30), the Cerebras IPO filing (LWiAI 242, 04-30), and the SemiAnalysis "lab pricing power" framing, it suggests the "Anthropic can do no wrong" narrative phase has ended. Specific concrete actions cited:
- Silent Claude Code nerfing (capability degradation users perceived but Anthropic didn't disclose).
- Banning specific companies from Claude.
- Price rises that don't track usage tier transparently.
- Locking Claude Code behind $100+/mo subscription.
- Blocking third-party harnesses (e.g., OpenClaw).

## Connection to prior wiki

- **SemiAnalysis: AI Value Capture (05-01)** — predicted exactly this. SemiAnalysis explicitly named that "Anthropic is already alienating large swathes of the market" by locking Claude Code and blocking OpenClaw. Pragmatic Engineer is the developer-community confirmation of that prediction *the same week*.
- **Bun fork divergence (04-30)** — Anthropic's industrial behavior at the OSS layer. Same pattern: industrial-strength priorities ahead of community continuity.
- **Claude Code postmortem caching bug (04-23-24)** — silent Claude Code nerfing concerns are partly downstream of these architectural shifts where small changes silently change behavior.
- **Anthropic Mythos / Pentagon standoff (04-23)** — government-side trust strain. Pragmatic Engineer captures the developer-side trust strain. Both happening in the same 10 days is the broader pattern.

## What's important to track

The "AI-heavy load breaks GitHub but not other vendors" claim is the most checkable. If true, the natural follow-up is *which other vendors are next*. Codex / Anthropic API endpoints, npm registry, package managers, container registries — anywhere with high-frequency, low-latency access patterns AI agents now generate.

## Research angle

The reliability gap creates a routing opportunity. **Agent-trajectory-aware routing for git operations** — caching, mirroring, fallback to alternate hosts when GitHub is flaky — is now a real engineering surface. The Tier 1 routing thesis applies: when a load-spiked source has 86% reliability, a router that distributes traffic across mirrors / caches / alternate hosts has measurable ROI.
