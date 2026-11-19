---
title: "Gemini 4 Neon (model release + model card) and Genie 4"
date: 2026-11-19
type: summary
topic: llms-foundation-models
source: ../../raw/labs/2026-11-19-111240-labs.md
---

# Gemini 4 Neon and Genie 4 (Google DeepMind, 2026-11-18)

**TL;DR.** Gemini 4 Neon is Google's fourth Gemini 4 model in a month, slotted between Carbon (hardest long-horizon work) and Hydrogen (fast everyday execution). It is adapted from Carbon, takes text, images, audio, video and PDFs in a 1M-token context, and outputs up to 64K tokens synchronously or up to 1M via "background long decode". Price: **$3 input, $0.15 cached input (a 95% discount), $15 output per million tokens**, above earlier Gemini 4 tiers. Headline numbers: Artificial Analysis Intelligence Index 61 (#3 overall), #1 on the AA Coding Agent Index (58.6), Terminal-Bench 4.1 65.2%, Vals Index 70.9% (#2), Agent Arena Index 1336 (#2 across 4,200+ real sessions), HLE-Diamond 71.3%. On SWE-sweep it scores 12.8% in the mini-SWE harness but 39.0% inside Google Antigravity, a 3x harness effect Google reports itself. GitHub Copilot made it GA the same day, describing quality close to Carbon at lower token cost per task.

## Model card: safety findings

- **No full critical-capability evaluation.** Google ran a Material Capability Change (MCC) assessment against Gemini 4 Argon. Neon showed a general capability increase, but below the MCC threshold, so under the Frontier Safety Framework a full suite of CCL (critical capability level) evals was not required.
- **Carried-forward determinations from Argon:** CBRN biological uplift CCL "cannot be ruled out"; cybersecurity uplift CCL "cannot be ruled out"; mitigations continue. A full Safety & Security Report is "coming soon".
- Knowledge cutoff March 2026. Google reports its lowest fabrication rate yet in internal Antigravity testing.

## Genie 4

A real-time world model: 720p video at up to 24 fps with synchronized audio, editable by text while running, built on Gemini Omni Flash with Gemini for reasoning and steering. Rolled out to Google AI Ultra subscribers in Project Genie with chainable worlds and a community gallery.

## How it relates to prior wiki pages

- **The cached-input line is the agent price.** Yesterday's [GPT-6.2 release](2026-11-18-gpt-6-2-astra-sol.md) cut cached input 60% to $0.40/M after Harvard measured [94.8% of a coding agent's tokens as cached re-reads](../agentic-systems/2026-11-18-where-agent-compute-goes.md). Neon's $0.15 cached rate is the cheapest frontier-tier cached price the wiki has recorded. Two frontier launches in two days priced primarily on cache.
- **Harness dependence, measured by the vendor**: Neon's 12.8% vs 39.0% SWE-sweep gap is the same "the harness is half the model" effect as the [agent harness engineering](../agentic-systems/agent-harness-engineering.md) concept page tracks.
- **Contrast with OpenAI's system card**: GPT-6.2 Astra was rated High for AI self-improvement and Critical for cyber. Google's MCC route means Neon ships without new dangerous-capability numbers at all, a governance gap worth noting.

**Sources:** [DeepMind blog](https://deepmind.google/blog/introducing-gemini-4-neon/) · [Neon model card](https://deepmind.google/models/model-cards/gemini-4-neon/) · [Genie 4 model card](https://deepmind.google/models/model-cards/genie-4/) · [The Decoder](https://the-decoder.com/google-ships-gemini-4-neon-its-fourth-new-gemini-model-in-a-month/) · [GitHub Copilot](https://github.blog/changelog/2026-11-18-gemini-4-neon-in-github-copilot/) · raw: [labs 11-19](../../raw/labs/2026-11-19-111240-labs.md)
