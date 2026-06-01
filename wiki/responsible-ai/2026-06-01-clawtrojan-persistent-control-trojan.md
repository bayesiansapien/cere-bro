# From Prompt Injection to Persistent Control: ClawTrojan and DASGuard

**TL;DR.** LLM agents running in local harnesses can read and write files, call tools, and reuse workspace state across sessions. An attacker can embed a prompt injection (a hidden instruction smuggled into text the agent reads) inside a file or a tool output. The agent reads it, STORES it, and executes it LATER in a different session. This multi-step trojan attack is dangerous because no single step looks malicious, but together the steps turn untrusted text into persistent control of the agent. Existing defenses inspect each step in isolation, so they may block an obviously harmful action while missing the earlier benign-looking WRITE that planted the backdoor. The paper introduces ClawTrojan, a benchmark for multi-step trojan attacks in local agentic harnesses. In an OpenClaw-style simulated workspace with GPT-5.4, ClawTrojan reaches 95.5% attack success rate (ASR), while existing single-turn prompt-injection attacks get near-zero ASR on the same model. The defense, DASGuard, scans control-like text in sensitive local files, traces its origin, and removes control content that does not come from a trusted source. It is a provenance and data-flow defense, not per-step inspection.

```
untrusted file / tool output
        │ agent reads hidden instruction
        ▼
agent WRITES to sensitive local file   (looks benign)
        │
        ▼
later session READS the file ──► executes persistent control
        ▲
   DASGuard intercepts here: provenance check on control-like text
```

## Key points

- The attack is multi-step: read untrusted text, write it into a trusted location, execute it in a later session. Each step alone looks harmless.
- ClawTrojan is a benchmark for these multi-step trojans in local agentic harnesses.
- In a simulated OpenClaw workspace with GPT-5.4, ClawTrojan reaches 95.5% ASR, versus near-zero ASR for classic single-turn prompt-injection attacks on the same model.
- DASGuard defends by provenance: it scans control-like text in sensitive files, traces where it came from, and strips control content not sourced from a trusted origin.
- The core lesson: per-step inspection fails because the malicious payload is planted in one step and triggered in another.

## Gaps in the study

- Tested in a simulated OpenClaw workspace with a single model (GPT-5.4). Generalization across harnesses and models is open.
- Provenance tracking assumes you can reliably label which sources are trusted.
- The real-world false-positive rate on legitimate control files (configs, scripts, automation) is unknown.

## How it relates to prior wiki pages

This is one of three agent-security items surfacing today, and all three make the same argument. Chain-of-Authorization (Tsinghua) bakes authorization directly into the model's reasoning chain so the agent reasons about who is allowed to see each piece of data, and reports cutting a 98.5% attack success rate to 0%. Anthropic's "Zero Trust for AI Agents" framework lays out foundation, enterprise, and advanced tiers, and names the same failure modes: prompt injection via external data, tool poisoning via MCP metadata, memory-based privilege retention across sessions, and multi-agent pivot attacks. ClawTrojan and DASGuard add the empirical multi-step trojan case and a provenance defense.

The shared claim across all three: agent security must be cross-step, provenance-aware, or baked into reasoning, because per-step prompt-level guards fail against multi-step and memory-persistent attacks. The memory-persistence angle (a payload that survives across sessions) is exactly the agent-memory attack surface.

## Links

- Paper: [arxiv 2605.31042](https://arxiv.org/abs/2605.31042)
- Related concept pages: [responsible-ai.md](responsible-ai.md), [agent-memory.md](../agentic-systems/agent-memory.md)
- Raw source: [raw/huggingface/2026-06-01-from-prompt-injection-to-persistent-control-defending-agenti.md](../../raw/huggingface/2026-06-01-from-prompt-injection-to-persistent-control-defending-agenti.md)
