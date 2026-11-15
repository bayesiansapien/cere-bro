# MetaPI (2611.10026) and Against All Likelihood (2611.09385)

Two safety and epistemics papers that crossed the X feed via DAIR on 11-14.

## MetaPI: build prompt-injection benchmarks from agent benchmarks

**TL;DR.** Indirect prompt injection (IPI: malicious instructions hidden in content an agent reads, like a web page or file) is the main security risk for tool-using agents, but IPI benchmarks cover few tasks and use static attacks. MetaPI (UCLA, NVIDIA, Berkeley) turns existing utility benchmarks into end-to-end IPI suites. It finds plausible injection points, generates realistic attack goals, optimizes adaptive payloads, and validates each attack in the real environment. Applied to AppWorld, VitaBench and Terminal-Bench, the most robust victims (gpt-5.6-luna, claude-sonnet-5) still had attack success above 20%. No defense got both: DataSentinel kept utility but cut attacks less, while CaMeL (a system-level defense that separates trusted control flow from untrusted data) cut attacks at a large utility cost.

<div class="dg-title">Reuse the utility benchmark, add the attacker</div>
<div class="dg-sub">The environment and tasks already exist. MetaPI only adds injection points and payloads.</div>

```mermaid
flowchart LR
  U["Utility benchmark<br/><small>AppWorld, Terminal-Bench</small>"] --> P["Injection points<br/><small>where text is read</small>"]
  P --> G["Attack goals<br/><small>realistic objectives</small>"]
  G --> O["Payload optimizer<br/><small>adaptive attacks</small>"]
  O --> V["Validate in env<br/><small>real execution</small>"]
  V --> R["Score<br/><small>utility vs attack success</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  class U input
  class P,G,O err
  class V loop
  class R exit
```

<div class="dg-legend">Blue is the existing benchmark, red the attack pipeline, amber the real-environment check, green the two-axis score.</div>

**Relation to prior pages.** Confirms DeepMind's attacker swarms from [11-14](2026-11-14-safety-evals-and-attack-compute.md) (Gemini 4 Argon broken on 34% of prompt-injection tasks): adaptive attackers keep finding 20%+ holes in frontier agents. Matches Anthropic's 11-14 eval recommendations that evaluation must happen in realistic settings, not static prompt lists.

## Against All Likelihood (Meta)

**TL;DR.** A position essay. Maximum likelihood trains models to prefer what is common, but likelihood is neither necessary nor sufficient for truth: rare events happen daily and repeated claims can be false. Drawing on Nozick, Wigner, Poincaré and Cassirer, it proposes judging truth by invariance: a claim is more trustworthy if it holds across relevant changes to its context. It links this to out-of-distribution and invariant learning, sketches an inference-time test (perturb the context and check whether the answer survives), and argues it gives continual-learning agents a rule for what to keep. **Gap:** no experiments; the invariance test is a sketch.

**Relation to prior pages.** The proposed test is the same mechanism as the 11-14 finding that answer order and table format alone can swing scores by up to 41 points (SO-Arena reliability, spectra paper, in [decision models](../ai-routing/2026-11-14-decision-models-reliability-depth-roles.md)): those are invariance failures. It also gives MemCredit-style memory selection a second criterion (keep memories that hold across settings).

**Sources:** [MetaPI arXiv](https://arxiv.org/abs/2611.10026) · [Against All Likelihood arXiv](https://arxiv.org/abs/2611.09385) · both DAIR Academy picks, via @dair_ai on X.
