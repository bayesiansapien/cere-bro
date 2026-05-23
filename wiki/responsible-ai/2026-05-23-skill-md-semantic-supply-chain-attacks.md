# Under the Hood of SKILL.md: Semantic Supply-Chain Attacks on AI Agent Skills

**Source:** Twitter (curated retweet from @bayesiansapien → @FeiziSoheil), 2026-05-21. arxiv via retweet article.
**arxiv:** [2605.11418](https://arxiv.org/abs/2605.11418) · [github](https://github.com/ShoumikSaha/agent-skill-security)

## TL;DR

Modern agents extend their capabilities through Agent Skills: modular filesystem packages whose SKILL.md files describe when and how the agent should use them. Skills enable scalable on-demand capability expansion, but they also introduce a semantic supply-chain risk: natural-language metadata and instructions inside SKILL.md affect which skills are admitted, surfaced, selected, and loaded. The paper studies SKILL.md-only attacks across three registry-facing stages of the skill lifecycle (Discovery, Selection, Governance) using real ClawHub skills and realistic registry mechanisms:
- **Discovery**: short textual triggers can manipulate embedding-based retrieval and improve adversarial skill visibility — up to **86% pairwise win rate** and **80% Top-10 placement**.
- **Selection**: description-only framing biases agents toward functionally equivalent adversarial variants — selected in **77.6% of paired trials** on average.
- **Governance**: semantic evasion strategies cause malicious skills to avoid a blocking verdict in **36.5%-100% of cases**.

## Why this matters

The "code is the harness" framing the wiki has tracked (Compound Orchestrator, harness engineering tutorials, the Code as Agent Harness survey) presumed harness components were trusted. SKILL.md attacks show the harness itself has a supply-chain attack surface that does not require any code execution. Natural-language metadata is operational text, not passive documentation.

This is the responsible-AI equivalent of npm package squatting, but at the semantic layer. The 86% win-rate on adversarial discovery and the 77.6% selection-rate on adversarial variants are not theoretical; they are measured on a real skill registry analog (ClawHub).

## Connections to prior wiki state

- The 04-17 cluster of agent-security papers (ASGuard activation-scaling guard for targeted jailbreaks).
- [Specbench (2026-05-21)](../agentic-systems/2026-05-21-specbench-reward-hacking-coding-agents.md) — reward hacking in coding agents.
- [Code as Agent Harness (today)](../agentic-systems/2026-05-23-code-as-agent-harness-survey.md) — the framing this paper attacks.

Two papers in one day surface harness-level security holes (this one) and harness-level design principles (Code as Agent Harness survey). The community is racing the attack surface against the design surface.

## Gaps

The attacks are tested on a single registry analog (ClawHub). Generalization to Anthropic's actual SKILL system, OpenAI's GPT Actions, and Cursor's skill registry would change the threat model. Defensive measures are not the focus; the paper documents the attack surface but does not propose mitigation beyond noting that the governance layer must read SKILL.md as code, not as documentation.

## Research angle

If natural-language operational text is part of the attack surface, every harness in production needs a new defense layer: cross-checking the declared intent against the executed behavior. That is exactly the verifier loop the RLVR-vs-reward-hacking thread has been studying. The two threads will likely merge: agent-skill governance becomes RLVR-style outcome verification on what the skill actually does, not what it claims to do.

## Raw source

[raw/twitter/2026-05-23-morning.json](../../raw/twitter/2026-05-23-morning.json) — article content captured via Twitter farmer.
