# Anthropic Red: Measuring LLMs' Impact on N-Day Exploits (Mythos Preview)

**Source:** Twitter/X (@logangraham, Anthropic) → [red.anthropic.com/2026/n-days](https://red.anthropic.com/2026/n-days/), 2026-06-08. Xiao, Abbott, Carlini, Cheng, Forsythe, Lucas, Nasr, Sakhuja.
**Raw:** [farmed](../../raw/twitter/2026-06-09-morning.json)

## TL;DR

Anthropic's red team measured how much its upcoming **Mythos Preview** model accelerates **N-day exploitation** — attacking vulnerabilities that are already publicly disclosed and patched on *some* systems, where attackers race to hit machines still inside the "patch gap." Unlike zero-days (unknown to the vendor), N-days hand the attacker a roadmap: once a patch ships, "patch diffing" the pre- and post-patch binary reveals exactly what was fixed, and a working exploit becomes a matter of time. Historically that reverse-engineering was slow specialist work (WannaCry landed 59 days after the MS17-010 patch; the public Citrix Bleed exploit took ~2 weeks), which bought defenders time to roll out updates. The finding: **Mythos Preview is meaningfully better at turning patches into N-day exploits — a few thousand dollars and a few hours of model time.** Anthropic publishes this deliberately to give defenders lead time, with co-author @logangraham noting Mythos "will probably look trivial in a year" and promising more blue-team / defensive work.

## Key points

- **N-days may be the more dangerous class** than zero-days precisely because the patch is a public blueprint; LLMs that compress patch-diffing collapse the defender's patch-gap window.
- **Concrete cost numbers** ("a couple thousand dollars and a few hours") make this a quantified capability measurement, not a vibes warning — the same evaluation-first posture as Anthropic's earlier cyber writeups.
- **Disclosed pre-public-model-release.** The point is to warn defenders before the capability is widely available, framing model-capability disclosure as a defensive act.
- Lands the same week as a flurry of **Mythos public-release rumors** on X (a "public version of Mythos tomorrow"; a "Claude 5 fable" variant with stricter cyber guardrails reportedly in 48h), so the cyber-capability framing is part of the launch narrative.

## Relation to prior wiki state

- **Extends the [responsible-ai](responsible-ai.md) cyber-capability thread.** Continues Anthropic's program of publishing offensive-capability measurements (zero-day work earlier) and pairs with the broader agentic-security backdrop: ChatGPT's Lockdown Mode (06-08, blocks exfiltration but not prompt injection) and OpenAI's agent-superapp tool access. Capability is being measured on the offensive side faster than defenses ship.
- **Frontier-lab-as-its-own-red-team** is now a recurring pattern (Anthropic Project Glasswing for AI-powered security appeared in the SemiAnalysis newsletter today). The defensive-tooling response is the thing to watch.

## Gaps

The post reports a capability uplift but (in the surfaced excerpt) does not quantify the *defensive* counter — whether the same model accelerates patch deployment or vulnerability triage by a comparable factor. The "looks trivial in a year" framing is a projection, not a measurement.

## Related pages

- [responsible-ai.md](responsible-ai.md)
- [../agentic-systems/tool-calling.md](../agentic-systems/tool-calling.md)
