---
source: raw/rss/2026-05-01-the-decoder-gpt-55-matches-claude-mythos-in-cyber-attack-tests-uk-a.md
date: 2026-05-01
url: https://the-decoder.com/gpt-5-5-matches-claude-mythos-in-cyber-attack-tests-uk-ai-security-institute-finds/
---

# UK AISI: GPT-5.5 Matches Claude Mythos on Full Network Attack Simulation

## TL;DR

The UK AI Security Institute reports that OpenAI's GPT-5.5 is the second model capable of *autonomously solving a full network attack simulation*. Performance is nearly on par with Anthropic's Mythos, which remains restricted to a small group. GPT-5.5 is generally available in ChatGPT and the API. The capability gating that was justified for Mythos no longer holds across the frontier — a GA model has reached the same offensive-cyber bar.

## Key findings

- **Second model to autonomously complete a full network attack simulation.** The first was Anthropic Mythos.
- **Capability nearly on par with Mythos** on UK AISI's cyber benchmark.
- **GA model.** GPT-5.5 ships in ChatGPT and through the OpenAI API.
- **Mythos remains restricted access** despite the parity.

## Why it matters

The justification for Mythos's restricted release was its offensive cyber capability. With GPT-5.5 reaching the same level and being publicly available, the policy logic of capability-based withholding is empirically broken: an attacker has had access to the equivalent capability via a different lab the whole time. The defender-product response (Anthropic Claude Security, 05-01) is the immediate commercial consequence; the policy response is undefined.

## Relation to prior wiki knowledge

**Closes the Anthropic Mythos withholding thread (04-17).** The wiki noted from 04-17 onward that Mythos's restricted release was the load-bearing policy claim. That claim is now empirically falsified — a GA frontier model from a different lab has the same capability.

**Pairs same-day with Anthropic Claude Security launch (05-01).** Anthropic shipped a defender product the same week. The narrative ordering is: restrict offensive capability → competitor reaches parity in a GA product → ship a defender product instead. The market is doing the policy work.

**Pairs with FlashRT (05-02).** FlashRT improves the optimization-based attack pipeline 2–7×. Combined with a GA GPT-5.5 capable of full network attack simulation, the cost of high-quality cyber-offensive prompting just dropped on two vectors at once.

**Reframes the CAIS AI Dashboard ranking (AISN #72, 05-01).** GPT-5.5 ranks first overall in text and vision; ranks fourth on the risk index, behind all Anthropic models. The risk index is now the primary capability differentiator on the public dashboard — capability proper is converged.

## Open threads

1. **Reproducibility of UK AISI's benchmark.** Single-evaluator capability claims need a second evaluator. METR or Apollo running the same simulation on GPT-5.5 in the next 30 days would resolve.
2. **Mythos vs GPT-5.5 hands-on comparison.** The "nearly on par" qualifier hides the actual delta — failure modes likely differ even if pass rates match.
3. **Policy response.** The Mythos-restriction logic doesn't survive this finding; whether the policy framework adapts (capability-gap-based gating, time-limited gating, defender-side balancing) is the open question.

## Links

- Raw: [raw/rss/2026-05-01-the-decoder-gpt-55-matches-claude-mythos-in-cyber-attack-tests-uk-a.md](../../raw/rss/2026-05-01-the-decoder-gpt-55-matches-claude-mythos-in-cyber-attack-tests-uk-a.md)
- Related: [2026-04-17-anthropic-mythos-policy.md](./2026-04-17-anthropic-mythos-policy.md) · [2026-05-01-anthropic-claude-security-launch.md](./2026-05-01-anthropic-claude-security-launch.md) · [2026-05-02-flashrt-efficient-red-teaming.md](../inference-efficiency/2026-05-02-flashrt-efficient-red-teaming.md)
