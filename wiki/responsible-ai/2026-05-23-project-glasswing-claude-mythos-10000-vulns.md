# Project Glasswing: Claude Mythos Preview finds 10,000+ critical vulnerabilities

**Source:** The Decoder + Anthropic Project Glasswing update via @ns123abc on X, 2026-05-23.
**Links:** [The Decoder](https://the-decoder.com/anthropic-warns-claude-mythos-preview-finds-bugs-faster-than-developers-can-patch-them/) · [original tweet](https://nitter.net/ns123abc/status/2057930703258427664#m)

## TL;DR

Anthropic has published the first Project Glasswing partner update for Claude Mythos Preview, its frontier reasoning model. Working with about 50 partners over a single month, Mythos Preview has flagged more than 10,000 critical vulnerabilities in system-critical software. Headline partner numbers: Cloudflare 2,000 bugs (400 high or critical), Mozilla 271 vulnerabilities in Firefox 150 (10x more than Firefox 148), UK AI Security Institute the first model to solve both their cyber-attack simulations end to end, a real-time prevented $1.5M wire fraud at one partner bank, and wolfSSL certificate-forgery vector on a crypto library used by billions of devices. Mythos scanned 1,000+ open-source projects with a 90.6 percent true-positive rate. Anthropic's own framing: bugs are piling up faster than anyone can patch them, and no company, including Anthropic, has safeguards strong enough to prevent misuse of these models.

## Why this matters

Two things become true on the same day. First, the Kapoor and Narayanan "resilience versus nonproliferation" thesis (from the May 22 wiki summary) gets its strongest empirical confirmation: a frontier reasoning model can produce defensive vulnerability research at industrial scale, exactly the cybersecurity-fuzzer-superhuman precedent they cited. Second, the offense-defense asymmetry that the same thesis brushed past gets concrete: a model that produces 10,000+ critical findings in one month is also a model that can be used to find 10,000+ exploits, and Anthropic itself is now publicly stating it cannot prevent that misuse.

The wolfSSL finding is the structurally important one. A certificate-forgery vector on a TLS library shipped on "billions of devices" is the class of root-trust failure that resists patching at the deployment side, because the embedded base of devices is enormous and updates are slow. Mythos finding it before adversaries is the optimistic reading. Mythos producing analogous findings privately for adversaries is the pessimistic reading. Both can be true simultaneously.

The UK AI Security Institute partnership is the policy-relevant detail. Mythos is the first model to solve both AISI cyber-attack simulations end to end. That is the kind of capability finding that the Trump executive order frontier-model testing language will react to, and that the Beijing summit guardrails will be measured against.

## Connections to prior wiki state

Project Glasswing was first announced via the [Anthropic Mythos policy framing (2026-04-17)](../ai-industry/2026-04-17-anthropic-mythos-policy.md) as a partner program for "AI-discovered vulnerability disclosure." The April framing was a policy artifact. This is the first delivery report, and the numbers run ahead of what the program described in April.

This also resolves a Worth Watching item from the May 22 digest. AISN #73 reported that AI safety has become bipartisan in Washington after the Beijing summit, with the Sanders dialogue and the CAISI testing agreements. Mythos solving both AISI simulations end to end is the kind of measurable capability finding that the bipartisan framework was assembled to respond to. The political infrastructure exists; the empirical trigger has now arrived.

For the SR^2AM / Maestro story that runs through today's papers: a model with Mythos's capabilities composed into an orchestration framework like [Maestro (today's HF paper)](../ai-routing/2026-05-23-maestro-rl-orchestrated-model-skill-ensemble.md) is the practical face of "small router plus frontier expert." The expert pool just got measurably stronger.

## Gaps

We do not know the inference cost per finding, the per-partner breakdown by severity, the false-positive rate distribution by partner (only the headline 90.6 percent TP rate), the time-to-patch of the reported findings, or whether Anthropic is sharing aggregate vulnerability signatures across partners to amortize defensive cost. We also do not know Mythos's architecture, parameter count, or relationship to the unreleased OpenAI reasoning model that solved the Erdős unit-distance conjecture (covered in yesterday's digest).

## Research angle

The most pressing open problem is the offense-defense composition. If Mythos's vulnerability-finding capability composes additively for defense (every device patched is a marginal gain) and multiplicatively for offense (every device unpatched is a marginal target), the equilibrium is unstable in favor of attackers as long as patch latency exceeds discovery latency. Whether that asymmetry is fundamental or whether the patch side scales with similar models is the question that determines whether 10,000 findings per month is a defensive or an offensive number.

A second angle: Mythos's 90.6 percent true-positive rate is unusually high for any static-analysis or fuzzer-like tool. Understanding what makes a reasoning model better at this than purpose-built tools is the research that will inform the next generation of both offense and defense.

## Raw source

[raw/rss/2026-05-23-the-decoder-anthropic-warns-claude-mythos-preview-finds-bugs-faster.md](../../raw/rss/2026-05-23-the-decoder-anthropic-warns-claude-mythos-preview-finds-bugs-faster.md)
