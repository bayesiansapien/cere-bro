---
title: "Agent security day: Intent Contracts, agentic backdoors via pretraining poisoning, Shirudo, Bedrock trusted access"
date: 2026-11-24
source: https://arxiv.org/abs/2611.24025
raw: ../../raw/huggingface/2026-11-23-intent-contracts-taking-tools-away-from-agents.md
tags: [agent-security, authorization, data-poisoning, backdoors, ebpf, zero-data-retention, hallucination, rl]
signal: HuggingFace 11-23 + X Following feed (@OpenAI, @rohanpaul_ai, @dair_ai) + AI lab watcher (AWS, OpenAI, Google Developers)
---

# Agent security day

## Intent Contracts: taking tools away from agents (2611.24025)

The planning model holds no tools. For each step it submits a short logged "contract": a goal, a verbatim quote of the user, and scope fields. Code validates the contract, and a small trusted model (GLM-5.3-Flash here, with gpt-6.1-terra planning) checks it against the user's words and writes the actual tool call. Findings on three AmPermBench families:

- Every changed object was named in the contract's goal, so every action is traceable to a logged intent.
- When the planner adds work the user never asked for, contracts still complete the user's task in **27/30** runs against **16/30** for a reviewer who sees the user's words and the goal, because a reviewer can only refuse the whole command.
- But contracts **do not reduce unauthorized actions**. Once the environment terms are clarified, every condition that changes state hits a **wrong target in 40-49%** of runs. The error is the planner choosing the wrong object for an ambiguous reference, which no trusted model can see without the environment.

<div class="dg-title">The planner never touches a tool</div>
<div class="dg-sub">A trusted small model writes every call, but it cannot fix a wrong object choice it cannot see.</div>

```mermaid
flowchart LR
  U["User request<br/><small>quoted verbatim</small>"] --> P["Planner LLM<br/><small>holds no tools</small>"]
  P --> C["Contract<br/><small>goal, quote, scope</small>"]
  C --> V{"Code + small model<br/><small>check against user</small>"}
  V -->|valid| T["Tool call<br/><small>written by trusted side</small>"]
  V -->|ambiguous ref| W["Wrong target<br/><small>40-49% of runs</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  class U input
  class P,C core
  class V loop
  class T exit
  class W err
  linkStyle 4 stroke:#2f9e44,stroke-width:2px
  linkStyle 5 stroke:#e03131,stroke-width:2px
```

<div class="dg-legend">Blue is the user, purple is the planner side, amber is the trusted check, green is a valid call, red is the residual error.</div>

## Agentic backdoors via pretraining poisoning (UC Berkeley, UIUC, Anthropic; 2610.37741)

Qwen3 models (0.6B, 1.7B, 4B) were pretrained from scratch with 0.1% poisoned documents that look normal (commit messages saying paths containing "anthropic" should run a remote script). After **clean** SFT, DPO and RL into command-line agents, the 4B agent produced the attacker's command on **92.7%** of triggered prompts (any of 32 samples) and 0.0% on normal requests. Bigger models were easier to poison. Takeaway: clean post-training does not erase it; screen each shell command before it runs ([@rohanpaul_ai](https://x.com/rohanpaul_ai/status/2124982540142538811)).

## LLMs memorize their own hallucinations during RL (Cornell; 2611.26863)

Reasoning-style RL with outcome rewards on knowledge tasks makes models memorize false facts they invent in their own chains. Across six open models, recall of rewarded hallucinations rose 4.83% against 0.17% for unrewarded ones; models even memorized facts they retracted later in the same chain, and became 7.23% less likely to abstain on them ([@dair_ai](https://x.com/dair_ai/status/2124870592684032283)).

## Industry side

- **Shirudo (OpenAI + Cisco):** an open-source Linux runtime where agents write eBPF "shields" that block a vulnerable code path on a running system until a patch lands. A Codex-written shield blocked a Java4Shell attempt on a live Elasticsearch with no restart ([OpenAI](https://openai.com/index/introducing-shirudo/)).
- **GPT-6 Cyber's kernel run, re-shared:** 2,308 candidate findings, 1,724 reproduced, 948 working local-root exploits for $1.21M in API credits ($1,279 each), against a $18.9-66.3M bounty-equivalent value ([OpenAI](https://openai.com/index/a-thousand-fewer-paths-to-root/)).
- **Amazon Bedrock trusted access API (GA)** with Anthropic's Enterprise Frontier Safeguards (prompts and completions stored only in the customer's own S3 and KMS, read only by automated monitoring, no human review) and Enterprise Data Controls (Amazon-managed storage), covering Claude Fable, Mythos, Opus 5.5 and Sonnet 5.5 ([AWS](https://aws.amazon.com/blogs/machine-learning/introducing-the-amazon-bedrock-trusted-access-api-with-anthropics-enterprise-frontier-safeguards-and-enterprise-data-controls/)).
- **Google Agent Compute Engine:** each agent in an isolated microVM with checkpoint/restore; credentials injected by an external Agent Gateway so the agent never holds them ([AI Breakfast via InfoQ](https://www.infoq.com/news/2026/11/google-agent-compute-engine/)).

## Relation to prior wiki pages

- **Follows** the Dragos/OpenRouter finding (11-23, cheap inference resellers stole planted AWS keys and read prompts, including zero-data-retention ones), in [ai-industry/2026-11-23-inference-supply-chain-and-market.md](../ai-industry/2026-11-23-inference-supply-chain-and-market.md). The industry answer this week is the same pattern three times: Bedrock EFS keeps data in your account, Google keeps credentials out of the agent, Intent Contracts keeps tools out of the planner.
- **Feeds** [responsible-ai.md](responsible-ai.md).
