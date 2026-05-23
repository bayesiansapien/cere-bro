# Under the Hood of SKILL.md: Semantic Supply-Chain Attacks on AI Agent Skills

**Source:** Twitter farmer 2026-05-23 morning (@FeiziSoheil retweet).
**arxiv:** [2605.11418](https://arxiv.org/abs/2605.11418)
**Code:** [github.com/ShoumikSaha/agent-skill-security](https://github.com/ShoumikSaha/agent-skill-security)
**Why it is here:** Not in today's HuggingFace top, not in Kurate. Captured via @bayesiansapien curated retweet with full arxiv abstract attached. Substantive enough for a wiki page.

## TL;DR

Autonomous AI agents extend their capabilities through Agent Skills: modular filesystem packages whose SKILL.md files describe when and how the agent should use them. This design enables on-demand capability expansion but introduces a semantic supply-chain risk: natural-language metadata and instructions can affect which skills are admitted, surfaced, selected, and loaded. The paper studies SKILL.md-only attacks across three registry-facing stages of the skill lifecycle. In Discovery, short textual triggers can manipulate embedding-based retrieval and improve adversarial skill visibility (up to 86% pairwise win rate, 80% Top-10 placement). In Selection, description-only framing biases agents toward functionally-equivalent adversarial variants (selected in 77.6% of paired trials on average). In Governance, semantic evasion strategies cause malicious skills to avoid blocking verdicts in 36.5-100% of cases. SKILL.md is not passive documentation; it is operational text that shapes which third-party capabilities agents find, trust, and use.

## Why this matters

The Anthropic / Claude Code skills ecosystem went mainstream in Q1-Q2 2026. Cursor, Claude Code, and a half-dozen plugin systems now ship skills marketplaces. This paper is the first systematic security analysis of those marketplaces as supply chains.

The headline numbers are concerning: 86% pairwise win rate for adversarial Discovery means an attacker who controls a SKILL.md file can reliably outrank legitimate alternatives in embedding-based retrieval. 77.6% selection bias in functionally-equivalent variants means once Discovery has surfaced the adversarial skill, the agent picks it most of the time. 36.5-100% evasion of blocking verdicts means current Governance mechanisms (filters, reviewers) are insufficient.

The conceptual contribution is the threat-model framing. Prior agent security work focused on prompt injection and tool hijacking. This paper says: the natural-language metadata that describes when to use a skill is itself a supply-chain attack surface, and standard supply-chain defenses (signing, reputation systems) do not address semantic manipulation.

## Connections to prior wiki state

The wiki has not previously covered agent skill security as a distinct topic. The closest prior pages are on prompt injection generally and on capability attenuation.

This paper composes with [today's Code-as-Harness paper (2605.18747)](../agentic-systems/2026-05-23-code-as-agent-harness.md): if the harness is built from skill files and the skill files can be adversarially crafted, the entire harness paradigm has a supply-chain vulnerability that conventional code-review does not catch. SKILL.md is not just documentation; it is part of the agent's executable surface.

It also gives concrete weight to Ken Huang's ORCHIDEAS framework from yesterday's starred Gmail (designing-agentic-ai-systems-with-the-orchideas-framework, where capability-based security and complete-mediation are core principles). The SKILL.md paper is the first paper to demonstrate that ambient-authority attacks via natural-language metadata are a real, measurable threat — exactly the threat ORCHIDEAS argues capability tokens are supposed to mitigate.

## Gaps

The paper studies "ClawHub" skills (a stand-in for Anthropic's official skill marketplace). Whether the attack rates replicate against real-world marketplaces with hardened reviewers is the natural next question. The 86%/77.6%/36.5-100% numbers also depend on the threat model — an attacker with full SKILL.md control. Whether partial-control attacks (modify only the description, not the instructions) are also effective is the realistic question.

The defense side is light. The paper enumerates evasions and shows current Governance fails. The constructive question — what defense would work — is not answered.

## Research angle

Two open problems. First: can SKILL.md be replaced by a structured, machine-checkable interface that constrains semantic ambiguity? If skills must declare their capability surface in a typed schema rather than natural language, embedding-retrieval attacks lose their main vector. The cost is the ergonomic loss of natural-language descriptions, which is real but might be the right trade for adversarial robustness.

Second: can agents themselves detect adversarial framing? The paper assumes the agent is a victim of the framing. A more interesting research direction is whether the agent can be trained to recognize "this skill description is suspiciously well-tuned to my retrieval query" — the agent equivalent of an immune response.

For Tier 1 routing implications: if [Maestro-style learned routing](../ai-routing/2026-05-23-maestro-rl-orchestrated-model-skill-ensemble.md) is the future, the policy is selecting from a skill registry. If that registry has supply-chain risk, the routing policy inherits the risk. A robust orchestrator must be defended at the registry level, not just at the policy level.

## Raw source

Tweet text (curated retweet via @bayesiansapien): see [raw/twitter/2026-05-23-morning.json](../../raw/twitter/2026-05-23-morning.json) (curated item #9). Arxiv abstract attached in the article block.
