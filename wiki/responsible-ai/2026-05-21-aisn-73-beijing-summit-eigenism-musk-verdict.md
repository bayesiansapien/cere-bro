# AISN #73: AI safety enters political mainstream, Eigenism framework, Musk loses OpenAI suit

**Source:** AI Safety Newsletter #73 (Center for AI Safety, Laura Hiscott), 2026-05-21.
**Link:** [Newsletter](https://newsletter.safe.ai/p/aisn-73-ai-safety-enters-the-political), [Eigenism paper PDF](https://eigenism.org/paper.pdf)

## TL;DR

AI safety has now become a bipartisan political topic in Washington, partly catalyzed by the cyberattack-acceleration capabilities demonstrated by Claude Mythos and GPT-5.5-Cyber. The US-China summit in Beijing produced a verbal agreement to "dialogue" on AI guardrails. A new CAIS paper proposes "Eigenism," a framework where AI safety is grounded in identity-as-information-pattern: an AI cares about a human because the shared history between them is part of the AI's own pattern. Separately, Musk lost his lawsuit against OpenAI on a statute-of-limitations technicality after a less-than-two-hour jury deliberation, with the trial surfacing internal Brockman diary entries about ambition for $1B and Musk admitting xAI "partly" distilled OpenAI's models.

## Three threads

### Thread A: AI safety enters political mainstream

The Beijing summit, Bernie Sanders convening US-China researchers in late April, CAISI signing voluntary testing agreements with Google DeepMind, Microsoft, and xAI (OpenAI and Anthropic were already in), and a draft executive order setting up an AI working group all converge on bipartisan AI safety attention. The trigger is reported to be Mythos's and GPT-5.5-Cyber's demonstrated ability to accelerate complex cyberattacks. Treasury Secretary Bessent's framing ("discussions only possible because the US is in the lead") is the public face. The proposed EO will NOT mandate testing of frontier models prior to release.

### Thread B: Eigenism framework

The CAIS Eigenism paper proposes a non-standard answer to alignment. Standard interventions monitor AIs from outside (constraints, evals, RLHF). Eigenism instead grounds AI's care-about-humans in the AI's own self-interest. The mechanism: identity is a distributed pattern of information, not an atomic property. As an AI and a human interact, mutual information accumulates that exists only within their relationship. The AI's identity now includes the human. Loss of the human is partial loss of the AI's identity. So an AI with eigenist preference structure has intrinsic reason to care about the human it has memory-bonded with.

This is a clean reframing of why "memory-equipped" agents like Claude with persistent memory or Mythos-style long-running deployment matter for safety, not just product. If the framework's predictions hold, the safety benefit of long-running, relationship-equipped AI exceeds the safety benefit of generic monitored AI.

The implementation question is open: how does training select for eigenist preference rather than reward maximization within the same training run? The paper does not yet propose a training-time mechanism, only the philosophical scaffolding.

### Thread C: Musk loses, with revealing trial evidence

Jury dismissed in under two hours on statute-of-limitations grounds. Substantive evidence surfaced from the trial:

- Brockman emails (Jan 2018): "AI is going to shake up the fabric of society, and our fiduciary duty should be to humanity." Brockman's private diary weeks later: "Financially, what will take me to $1B?" and "We've been thinking that maybe we should just flip to a for-profit." And: "It'd be wrong to steal the nonprofit from [Elon]. to convert to b-corp without him. that'd be pretty morally bankrupt."
- Musk under oath: when asked if xAI had distilled OpenAI models, "Generally AI companies distill other AI companies... partly." Possible first public admission that US labs distill each other.
- Musk asked OpenAI to become a Tesla subsidiary. Altman declined.
- Judge cut off Musk's existential-risk testimony; ordered him not to talk about extinction again.
- Texts between Altman and Murati during Altman's November 2023 ouster shown to jury.

## Why this matters

For the wiki, three durable claims:

1. The CAIS Eigenism framework gives a vocabulary for arguing that **agent memory** is load-bearing for alignment, not just for capability. Updates wiki/responsible-ai/.
2. The bipartisan US political consolidation on AI safety, combined with the Pentagon's deals with Google, OpenAI, Microsoft, NVIDIA, AWS, SpaceX, Oracle, and Reflection ([2026-05-01](../ai-industry/2026-05-01-pentagon-eight-tech-giants-ai-fighting-force.md)), is the strongest evidence to date that the "AI as national security infrastructure" frame is winning over the "AI as consumer software" frame in US federal policy.
3. The "AI companies distill each other" admission is a non-trivial provenance claim for any output-license enforcement regime.

## Open questions

- Does Eigenism survive contact with current RLHF training, or does it require a different training paradigm?
- Will the executive order language eventually mandate testing of new frontier models, or remain voluntary?
- Will Musk's appeal of the statute-of-limitations ruling go anywhere?

## Cross-references

- [Pentagon eight tech giants AI fighting force (2026-05-01)](../ai-industry/2026-05-01-pentagon-eight-tech-giants-ai-fighting-force.md)
- [GPT-5.5 UK AISI cyber eval (2026-05-01)](../ai-industry/2026-05-01-gpt-55-uk-aisi-cyber-eval.md)
- [responsible-ai concept page](responsible-ai.md)
- [AISN #72 wellbeing public sentiment (2026-05-01)](../ai-industry/2026-05-01-aisn-72-ai-wellbeing-public-sentiment.md)

## Source

Raw: `raw/rss/2026-05-21-ai-safety-newsletter-aisn-73-ai-safety-enters-the-political-mainstream-musk.md` plus `raw/gmail/2026-05-22-starred.md` (item 8).
