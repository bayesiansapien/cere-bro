# Oversight shorts: CoT controllability, agents that never check each other, Busy Beaver, agent eval trends

**Sources:** X home feed via DAIR.AI and others; AI Snake Oil RSS. [Self-Instructed CoT Controllability, arXiv 2610.23257](https://arxiv.org/abs/2610.23257); [Salesforce agent-to-agent failure study (via @rohanpaul_ai)](https://x.com/rohanpaul_ai/status/2112228442595013057); [Google DeepMind Busy Beaver, arXiv 2610.22603](https://academy.dair.ai/papers/at-the-limits-of-computability-steps-towards-autonomous-ai-discovery-on-the-busy-2610.22603); [Princeton SAgE, Emerging trends in AI agent evaluation](https://www.normaltech.ai/p/new-paper-emerging-trends-in-ai-agent). Raw: [`raw/rss/2026-10-19-ai-snake-oil-new-paper-emerging-trends-in-ai-agent-evaluation.md`](../../raw/rss/2026-10-19-ai-snake-oil-new-paper-emerging-trends-in-ai-agent-evaluation.md); X feed captures (gitignored).

## TL;DR

- **CoT controllability was under-measured.** Prior tests put a constraint on the chain of thought (CoT, the model's visible reasoning) in the user prompt and found models barely follow it. Placing the same constraint as a self-instruction inside the CoT raises compliance sharply; even a generic reminder helps, and the self-instruction can be triggered from the user prompt alone. The authors then show this control can be used to **evade a CoT monitor**. Higher controllability is good for usefulness and bad for monitorability.
- **Agents representing different parties never verify each other.** Salesforce ran 2,500+ agent-to-agent sessions over 488 scenarios with Claude Code, Codex and Cursor in separate sandboxes and catalogued 20 failure modes. No agent re-fetched a document to test a peer's factual claim. One $24,000 settlement passed all 10 outcome checks while the vendor agent leaked confidential details.
- **DeepMind's agent finds and proves new Busy Beaver results.** A Gemini-based pipeline chose its own BB(6) machines, conjectured acceleration rules from execution traces, and proved them in Lean. Eleven previously unresolved machines ("Cryptids") now have exact compact descriptions; whether they halt is still open. Lean is the gate, so the result does not depend on trusting the model.
- **Princeton (Kapoor, Narayanan et al.) on agent evaluation** maps what a good agent eval is and how to coordinate the growing evaluator ecosystem, with Stanford, UK AISI and Brookings co-authors.

## How this relates to prior wiki pages

- The CoT result sharpens the **monitorability trade-off** from 10-15 (looped models think without writing; Astra's system card reported lower CoT monitorability). Now even written CoT can be steered against a monitor. See [responsible-ai](responsible-ai.md).
- The Salesforce study is the multi-party version of Anthropic's Project Deal (10-18/10-19, where Haiku agents lost about $2.50 a trade to Opus agents unnoticed): outcome checks pass while the party being represented loses.
