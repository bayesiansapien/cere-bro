# Anthropic Project Glasswing: Claude Mythos Preview finds 10,000+ critical vulnerabilities in one month

**Date:** 2026-05-23
**Source:** The Decoder (Matthias Bastian), via Anthropic Project Glasswing update.
**Links:** [The Decoder](https://the-decoder.com/anthropic-warns-claude-mythos-preview-finds-bugs-faster-than-developers-can-patch-them/)
**Raw source:** [raw/rss/2026-05-23-the-decoder-anthropic-warns-claude-mythos-preview-finds-bugs-faster.md](../../raw/rss/2026-05-23-the-decoder-anthropic-warns-claude-mythos-preview-finds-bugs-faster.md)

## TL;DR

Anthropic's Claude Mythos Preview, deployed with about 50 partners under the Project Glasswing umbrella, found over 10,000 critical vulnerabilities across system-critical software in a single month. Notable results: 2,000 bugs at Cloudflare (400 high/critical severity), 271 vulnerabilities in Firefox 150 (10× more than Firefox 148), the first model to solve both UK AISI cyber attack simulations end to end, real-time prevention of a fraudulent $1.5M wire transfer at a partner bank, and a way to forge certificates on a crypto library used by billions of devices (wolfSSL). True-positive rate: 90.6%. Anthropic explicitly warns this opens a high-risk transition period and says no company, itself included, has built safeguards strong enough.

## What happened

Project Glasswing is Anthropic's security-research deployment of Claude Mythos Preview to about 50 partners across browsers (Mozilla Firefox), CDNs (Cloudflare), open-source crypto (wolfSSL), banks, and national security testbeds (UK AI Security Institute). The first official update reports:

- **Cloudflare:** 2,000 bugs, 400 high/critical severity.
- **Mozilla:** 271 vulnerabilities in Firefox 150 vs Firefox 148 (10× increase). This is the model finding bugs faster than the release cadence introduces new ones.
- **UK AI Security Institute:** Mythos became the first model to solve both AISI cyber attack simulations end to end.
- **Partner bank:** Mythos prevented a fraudulent $1.5M wire transfer in real time.
- **wolfSSL:** found a way to forge certificates on a crypto library used by billions of devices.
- **Scanned 1,000+ open-source projects** with a 90.6% true-positive rate.

The framing matters: Anthropic is not just claiming a research result. It is publicly warning that the bug-finding rate now exceeds the patch-deployment rate. No company, Anthropic included, has built safeguards strong enough to prevent misuse of these models.

## Why this matters

Three threads connect.

**First, the resilience case.** The [Kapoor and Narayanan essay (2026-05-21)](../responsible-ai/2026-05-21-ai-snake-oil-resilience-vs-nonproliferation.md) (the AI Snake Oil piece arguing that AI policy should invest in defensive capability rather than chase nonproliferation chokepoints, on the analogy of cybersecurity fuzzers) is now empirically reinforced. Mythos is the existence proof that AI-mediated vulnerability discovery scales beyond anything human fuzzer teams produce. The defensive-investment thesis just acquired a 10,000-bug case study.

**Second, the offensive-defense asymmetry.** Anthropic's own framing is that the bugs are piling up faster than developers can patch them. The Glasswing data demonstrate the lopsided economics of AI-mediated security work: finding bugs scales with compute, patching them scales with humans. Until the patching loop is also automated, every new model release creates a worse defender-attacker asymmetry. The same week, US Cyber Command was [racing to deploy AI on top-secret networks](./2026-05-21-us-cyber-command-classified-networks.md) according to The Decoder.

**Third, the alignment-by-self-warning pattern.** Anthropic is publishing this in the form of a warning ("no company has built safeguards strong enough"). This is the [Mythos policy posture](./2026-04-17-anthropic-mythos-policy.md) made operational: ship the result, warn the world, request defensive investment. The [Anthropic 6-24 month cyber-offense forecast](./2026-04-17-anthropic-mythos-policy.md) tracked in the wiki since April predicted exactly this. Glasswing is the start of that window.

## Connecting to the wiki

The wiki tracked the [first Glasswing announcement](./2026-04-17-anthropic-mythos-policy.md) on 2026-04-17, the [Pentagon eight-tech-giants AI deal (2026-05-01)](./2026-05-01-pentagon-eight-tech-giants-ai-fighting-force.md), and the [Anthropic Q2 profitability story (2026-05-21)](./2026-05-21-anthropic-profitability-spacex-deal-ipo.md). The throughline: Anthropic's commercial moat is increasingly built on cyber-offense and cyber-defense workloads where Mythos-class capability is genuinely differentiated. Glasswing's 10,000-bug month is the data point that justifies the SpaceX-scale compute commitment.

This also intersects with the [SKILL.md supply-chain attacks paper (2026-05-21, surfaced in today's Twitter morning)](../agentic-systems/2026-05-21-skill-md-semantic-supply-chain-attacks.md): if agent skills can be poisoned through natural-language metadata, the same Mythos capability that finds CVEs in C code will eventually be turned against the skill registries that govern agent behavior. Defense and offense are both scaling.

## Industrial implication

For software vendors, the implicit deadline shortens. Any company that ships system-critical software (browsers, CDNs, crypto libraries, banking systems) now needs an AI-assisted defensive pipeline equivalent to whatever the offensive side has access to. Mozilla, Cloudflare, and wolfSSL are partners and so will get pre-release access; everyone else gets the post-release surface.

For governments, the policy framework around model release shifts again. If Mythos-class capability creates a genuinely new offense-defense asymmetry, the "voluntary testing" frame embedded in the rumored Trump executive order ([tracked in the 2026-05-22 digest](../daily-digest/2026-05/2026-05-22.md)) will be tested under pressure. Whether that holds is the [next-30-day question](../daily-digest/2026-05/2026-05-22.md) the wiki is already tracking.

## Worth watching

- Whether a non-Anthropic model (GPT-5.5, Gemini, DeepSeek V4) demonstrates comparable Glasswing-style vulnerability discovery within 60 days.
- Whether the Trump executive order language on frontier-model testing strengthens in response to the 10,000-bug announcement (30 days).
- Whether the Mozilla 10× Firefox increase reproduces across Chrome and Safari (60 days).
- Whether automated patching catches up to automated discovery, or stays one quarter behind (open).

## Related wiki pages

- [Anthropic Mythos policy (2026-04-17)](./2026-04-17-anthropic-mythos-policy.md).
- [Pentagon eight tech giants AI fighting force (2026-05-01)](./2026-05-01-pentagon-eight-tech-giants-ai-fighting-force.md).
- [Anthropic profitability + SpaceX deal (2026-05-21)](./2026-05-21-anthropic-profitability-spacex-deal-ipo.md).
- [AI Snake Oil: resilience vs nonproliferation (2026-05-21)](../responsible-ai/2026-05-21-ai-snake-oil-resilience-vs-nonproliferation.md).
- [US Cyber Command classified networks (2026-05-21)](./2026-05-21-us-cyber-command-classified-networks.md).
