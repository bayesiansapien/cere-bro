# Lambert: Notes from inside China's AI labs

**Source:** [Interconnects AI](https://www.interconnects.ai/p/notes-from-inside-chinas-ai-labs) (Nathan Lambert, 2026-05-07)
**Tier:** 2 — AI industry essay

## TL;DR

Six labs visited in 36 hours (Z.ai, Moonshot AI, Tsinghua, Meituan, Xiaomi, 01.ai), plus Alibaba Beijing. Six concrete differences from Western labs: students integrated as peers, less ego in org charts, Chinese devs are Claude-pilled despite the ban, build-not-buy on RL data, tech-ownership mentality at non-AI companies, Nvidia chip desperation. The most striking observation: extreme philosophical humility. Western preoccupation with how-models-should-behave does not exist as a research-shaping force in Chinese labs.

## The six structural differences

### 1. Students integrated as peers

Chinese AI labs are quite young. A large proportion of core contributors are active students, treated as peers and directly integrated into the LLM team. Lambert compares to Ai2's setup. Western counter-example: OpenAI, Anthropic, and Cursor offer no internships at all. Google has Gemini-related internships but with concerns about siloing.

### 2. Less ego in the org chart

"More willingness to do non-flashy work in order to improve the final model. Less ego enabling org charts to scale slightly, as there's less gamifying the system." The Llama-org collapse at Meta is the U.S. counter-example, "heavily rumored to have collapsed under the political weight of these interests embedding themselves in a hierarchical organization." Lambert reports having heard from labs that "it can be needed to pay off a top researcher to get them to stop complaining about their idea not making it in the final model."

### 3. Most Chinese developers are Claude-pilled despite the ban

Direct quote: "Most of the AI developers in China are obsessed with Claude and how it's changed how they build software, despite Claude nominally being banned in China." This is the single most important sentence in the piece. It reframes the Anthropic-capacity-crunch story (see today's [Anthropic-Colossus deal coverage](2026-05-08-anthropic-colossus-deal-capacity.md)). If Chinese demand is real and Claude is the bottleneck globally, the inference market is bigger than the public posture admits.

A subtle observation: "There were also surprisingly few mentions of Codex, which is definitely surging in popularity in the Bay Area." OpenAI's coding agent is winning the U.S. dev market but not the Chinese one. Geographic split in coding-agent adoption is worth tracking.

### 4. Build-not-buy on RL data and environments

"The data industry was relatively poor quality and it is often better to build the environments or data in-house. Researchers themselves spend meaningful time making the RL training environments. Some of the bigger companies like ByteDance and Alibaba can have in-house data labelling teams." This contrasts with Anthropic and OpenAI spending "$10M+ for single environments, with cumulative spend on the order of hundreds of millions per year to push the frontier of RL."

### 5. Tech-ownership mentality at non-AI companies

Meituan (food delivery), Xiaomi (consumer tech), and Ant Group (fintech) all ship open-weight LLMs. Western equivalents would buy services. Lambert: "These companies aren't building LLMs out of a race to be relevant with the hot new thing, but a deep fundamental yearning to control their own stack and develop the most important technologies of the day."

### 6. Nvidia chip desperation

"Nvidia compute is the gold-standard for training and everyone is limited in progress by not having more of it. If supply was there, it is obvious that they would buy it." Huawei chips are "spoken positively of for inference" but not training.

## The philosophy gap

The most striking observation is on philosophy. "Trying to get Chinese scientists to comment on the coming economic uncertainty fueled by AI, questions beyond the capabilities of simple AGI, or moral debates on how models should behave all served to capture the extreme humility of these scientists." Lambert reports Chinese researchers hear questions about long-term AI risk and respond with "simple confusion. It's a category error to them." One researcher quoted Dan Wang's "China is run by engineers, U.S. by lawyers" frame.

For the wiki's [responsible-ai topic](../responsible-ai/responsible-ai.md), this is a falsifiable claim: the entire alignment / interpretability / safety preoccupation may be a structurally Western preoccupation, not a global one. If true, it changes the political-economy story of the field.

## Industry-level take-aways from Lambert's six bullets

1. **Early signs of domestic AI demand.** The hypothesis that Chinese AI market will be smaller because Chinese companies don't pay for software is "only true for software spend that maps to the SaaS ecosystem." The cloud market is fundamental, and AI is trending closer to cloud than SaaS.
2. **Most developers are Claude-pilled.**
3. **Tech-ownership mentality.** No master plan. The industry is a practical equilibrium of many technology businesses.
4. **Government aid is real, but unclear how big.** Decentralized across many levels. Bureaucratic-red-tape removal is certain. Chip smuggling and direct technical influence are unclear.
5. **Data industry is far less developed.**
6. **Desperation for more Nvidia chips.**

## How this relates to prior wiki work

- **Direct connection to today's [ResRL paper](../llms-foundation-models/2026-05-08-resrl-negative-sample-projection-rl.md).** ResRL's first author Zihan Lin is interning at Meituan. Lambert visited Meituan this week. ResRL is exactly the kind of methodologically-deep work that the build-not-buy + tech-ownership culture produces.
- **Continuation of [DeepSeek V4 architecture](../llms-foundation-models/2026-04-24-deepseek-v4-architecture.md)** thread. Lambert: "DeepSeek as the lab with the best research taste in execution. They set the direction, but aren't set up to win economically." Confirms the wiki's prior framing.
- **Continuation of [Distillation Panic](../inference-efficiency/2026-05-04-distillation-panic-lambert.md)** (05-04, also Lambert). Same author, two pieces in one week, both arguing that the Western framing of Chinese AI work misses the mark.
- **Lateral to [Anthropic-Colossus capacity story](2026-05-08-anthropic-colossus-deal-capacity.md)** today. The "Chinese devs are Claude-pilled despite the ban" line is demand evidence for the capacity-crunch reading.

## What's surprising

The convergence between Lambert's qualitative ethnography and today's quantitative paper output. Lambert says Chinese labs are culturally optimized for fast-following. ResRL is exactly the kind of incremental-but-deep methodological work that fast-followers produce. Lambert says Chinese labs build their own RL data. ResRL works on the core gradient mechanism of RL. Lambert says the philosophical-AI-debate doesn't shape Chinese research. ResRL doesn't mention safety or alignment once.

## Worth Watching

- **First Chinese lab to ship work the U.S. ecosystem cannot reproduce in 6 months.** Lambert hypothesizes Chinese models will continue to look like the U.S. frontier of 3-9 months ago. ResRL is a candidate for refuting that (open code, but the SVD-projection mechanism is non-obvious enough to delay reproduction). 6-month window from publication.
- **xAI/Anthropic Colossus deal demand-side reading.** Lambert's "Claude-pilled despite the ban" line is the demand evidence Pragmatic Engineer's piece needed.
- **Coding-agent adoption split (Claude in China vs Codex in the Bay Area).** Falsifiable: if Codex penetrates Chinese dev tooling within 90 days, the geographic split is temporary. If it doesn't, there's a real lock-in story.
