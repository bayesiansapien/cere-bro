---
title: "Alignment below the model: FATCAT fault injection; plus RLVB, Mancelle steering and InstructReplay"
date: 2026-11-26
source: https://arxiv.org/abs/2611.31129
raw: ../../raw/huggingface/2026-11-25-fatcat-fault-injection-attacks-targeting-chip-level-alignmen.md
raw2: ../../raw/huggingface/2026-11-25-lazy-agents-answer-against-their-own-beliefs-reinforcement-l.md
raw3: ../../raw/huggingface/2026-11-25-steerable-by-design-conditional-pretraining-for-robust-contr.md
raw4: ../../raw/huggingface/2026-11-25-instructreplay-replaying-assistant-turns-to-preserve-general.md
tags: [hardware-security, fault-injection, alignment, refusal, rl, steering, catastrophic-forgetting]
signal: HuggingFace 11-25 (Lazy Agents 98 upvotes, the day's #2); RLVB also on X via @rohanpaul_ai
---

# FATCAT, RLVB, Mancelle-3B, InstructReplay

## FATCAT ([2611.31129](https://arxiv.org/abs/2611.31129)): alignment assumes the hardware is honest

- First physical fault-injection attack that removes refusal in LLMs and vision-language models. Non-invasive electromagnetic faults on GPU-accelerated systems-on-chip, with physical access but **no software privileges or model access**.
- An autonomous RF side-channel trigger times the faults to the **prefill** phase. The faults corrupt safety-critical memory transactions across off-chip LPDDR5 DRAM and on-chip LPDDR interfaces without crashing the system and while keeping output coherent.
- NVIDIA Jetson Orin Nano and AGX Thor running Llama 3.2 1B and Gemma 3 1B: localized faults reliably force restricted requests to be fulfilled. On a 6-DoF arm driven by a SmolVLA policy, the attack caused abrupt lunges; twice the arm tried to pinch an author.
- **Why it matters for this wiki:** it moves alignment into the [memory hierarchy](../hardware/memory-hierarchy.md). Refusal is a property of a few memory reads during prefill. Edge deployments without ECC or fault tolerance on the LPDDR path have no alignment guarantee under physical access.

## Lazy Agents / RLVB ([2611.32884](https://arxiv.org/abs/2611.32884))

- Agents commit to an answer while their own written belief still lists several possibilities ("laziness"). Outcome reward cannot fix it: a lucky guess gets the same reward as an evidence-backed answer.
- In a simulator the exact posterior over answers is computable at every step. **RLVB** rewards taking more steps while the posterior still allows several answers and committing once evidence suffices. No judge, critic or reward model, and it never reads the agent's stated belief.
- New Pro Worlds benchmark (large world seen through a small window). Three VLMs, three benchmarks (two unseen in training): **+17.1% on average across all nine settings**.
- Connects to [LMArena's decision-dodging measure (11-25)](../daily-digest/2026-11/2026-11-25.md), the opposite failure (handing decisions back). RLVB rewards committing at the right time, which is the calibrated middle.

## Mancelle-3B ([2611.32199](https://arxiv.org/abs/2611.32199)): steering built in at pretraining

- Separates control from content from the start: an encoder reads high-level semantic features of upcoming text and feeds the token stream via cross-attention that cannot write back. The model learns to depend on this channel to predict the next token, so it becomes a steering handle.
- Steers more strongly than prompt and activation steering on comparable open models while staying fluent, and resists adversarial black-box and soft-prompt counter-steering that defeats those baselines. Reproduced at 400M.

## InstructReplay ([2611.32918](https://arxiv.org/abs/2611.32918))

- Fine-tuning a model on new facts usually erodes general behavior. The initial model answers a set of general instructions once; during fine-tuning the model is kept close to its own answers on those.
- Across three families and two domains, average decline on five general benchmarks falls **from 28.1 to 2.4 points**, answer length stays close to the original, and new facts are learned as well as standard fine-tuning. Controlled comparisons credit replaying the model's own answers, not the loss form.
- Same mechanism as CoT-Proxy's replay buffer KL (same day) and the 11-25 finding that outcome rewards make models memorize their own hallucinations: what the model already says is the cheapest regularizer.

## Relation to prior wiki pages

- FATCAT extends the [responsible AI](responsible-ai.md) page's agent-security thread (Siren sandbox escapes 11-25, poisoned pretraining 11-24) down to the physical layer.
- Mancelle is the pretraining-time answer to the 11-25 hidden-reasoning result (silent multi-step reasoning evades CoT monitors): if you cannot monitor the trace, build a control channel the token stream cannot overwrite.

Raw: [FATCAT](../../raw/huggingface/2026-11-25-fatcat-fault-injection-attacks-targeting-chip-level-alignmen.md) · [RLVB](../../raw/huggingface/2026-11-25-lazy-agents-answer-against-their-own-beliefs-reinforcement-l.md) · [Mancelle](../../raw/huggingface/2026-11-25-steerable-by-design-conditional-pretraining-for-robust-contr.md) · [InstructReplay](../../raw/huggingface/2026-11-25-instructreplay-replaying-assistant-turns-to-preserve-general.md)
