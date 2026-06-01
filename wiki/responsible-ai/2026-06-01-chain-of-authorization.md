# Chain-of-Authorization

**TL;DR.** Tsinghua University work, surfaced via a curated Twitter repost. The claim is that every enterprise AI agent shares one structural flaw: LLMs treat all accessible data as equally fair to share, with no built-in concept of ownership or who is allowed to see what. The permission system bolted on top is "just a prompt", and prompts get bypassed. Chain-of-Authorization bakes authorization INTO the reasoning chain itself. The model reasons about whether the requester is authorized for each piece of data as part of its chain-of-thought (its step-by-step reasoning), rather than relying on an external prompt-level guard. The reported result is an attack success rate cut from 98.5% to 0%. This page is short because it is tweet-sourced, with no full paper text.

```
external prompt guard:   request → [prompt: "do not leak X"] → model   (bypassable)

chain-of-authorization:  request → model reasons per data access:
                         "is requester authorized for this?" → answer  (in-chain)
```

## Key points

- Diagnosis: LLMs have no native concept of data ownership, so they treat all accessible data as equally shareable.
- A prompt-level permission layer is bypassable because it is just more text the model can be talked around.
- Chain-of-Authorization moves the authorization check inside the reasoning chain: each data access is checked in-chain.
- Reported attack success rate drops from 98.5% to 0%.

## Gaps in the study

- Tweet-level evidence only. No paper text or independent evaluation is available here.
- The "98.5% to 0%" figure is the authors' claim.
- Generalization across tasks and the false-deny rate (legitimate requests wrongly blocked) are unknown.

## How it relates to prior wiki pages

This is part of today's agent-security cluster. ClawTrojan and DASGuard showed a multi-step trojan attack where a payload is planted in one step and triggered later, defended by tracing data provenance. Anthropic's "Zero Trust for AI Agents" framework names prompt injection, tool poisoning, memory-based privilege retention, and multi-agent pivot attacks. Chain-of-Authorization is the reasoning-level member of the same family. The shared theme across all three: per-step and prompt-level guards fail, so security must be structural. Either it lives in the reasoning (Chain-of-Authorization) or in data provenance (DASGuard).

## Links

- Source: [Twitter repost by @alex_prompter](https://nitter.net/alex_prompter/status/2061171784800665696#m) (curated by @bayesiansapien, 2026-05-31)
- Related concept pages: [responsible-ai.md](responsible-ai.md), [multi-agent-systems.md](../agentic-systems/multi-agent-systems.md)
- Raw source: [raw/twitter/2026-06-01-afternoon.md](../../raw/twitter/2026-06-01-afternoon.md)
