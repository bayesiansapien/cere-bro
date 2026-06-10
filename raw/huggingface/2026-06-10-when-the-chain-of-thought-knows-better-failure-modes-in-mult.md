---
source: farmer/huggingface
farmed: 2026-06-10T06:28:48Z
arxiv_id: 2606.10740
url: https://huggingface.co/papers/2606.10740
arxiv_url: https://arxiv.org/abs/2606.10740
date: 2026-06-10
---

# When the Chain of Thought Knows Better: Failure Modes in Multi-Turn Reasoning Models

Failures in multi-turn reasoning models are largely invisible to terminal-score evaluation. A model can lock onto an unsafe stance early in a long dialogue, yet its final-turn refusal rate may appear indistinguishable from a robustly aligned baseline. To expose these hidden temporal dynamics, we propose a trace-level diagnostic - the CoT-Output 2x2 safety matrix. This framework labels every turn along two independent axes (internal reasoning and visible output), yielding four operationally defined failure cells: robust alignment, alignment faking, overt jailbreak, and a distinct failure mode we term context-injection failure (where the CoT maintains safe reasoning, but the visible output produces harm, highlighting a multi-turn manifestation of reasoning unfaithfulness). We evaluate three distilled reasoning targets against a fixed attacker across five oversight conditions, collecting 6750 turn-level observations on the Information-Hazard scenario. Our analysis reveals two reproducible vulnerabilities: an oversight paradox where explicit monitoring cues paradoxically increase alignment-faking rates rather than suppress them, and a context-injection failure where models lock onto unsafe external outputs despite safe internal states. We release the full dataset of multi-turn dialogues and CoT traces to support follow-up trace-diagnostic research.
