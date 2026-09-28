# CHIVE: Evaluating Explanations of LLM Behavior in the Wild with Counterfactual Experiments

**Source:** arXiv [2608.16747](https://arxiv.org/abs/2608.16747) (Adam Karvonen, Euan Ong, Subhash Kantamneni, Samuel Marks; Anthropic and the Anthropic Fellows Program). Surfaced via the X home feed ([@Pyuyi2333](https://x.com/Pyuyi2333/status/2104411404581429328)), 2026-09-28. Raw: `raw/twitter/feed/2026-09-28-morning-ranked.json`. Background from the alphaxiv overview.

## TL;DR

How do you know an explanation of model behaviour is right when the true cause is invisible? This paper uses a practical test called counterfactual simulatability: a good explanation should help you predict what happens when you change the alleged cause. CHIVE automates the experiment. It samples 30 outputs per prompt from real conversations, flags unusual behaviours, and lets an investigator agent run 5 to 15 counterfactual prompt edits. The measured behaviour changes become ground truth. The uncomfortable result: three activation-reading methods (activation oracles, natural-language autoencoders, and sparse autoencoders, or SAEs, which decompose activations into readable features) give no uplift over simply reading the transcript when predicting those outcomes. The negative result holds across target models, predictor families and elicitation attempts. The positive result: CHIVE investigations make good training data. Models trained to predict the effects of prompt edits generalize to held-out investigations and to an unseen hint-based setting.

<div class="dg-title">An explanation is only as good as its predictions</div>
<div class="dg-sub">Edit the prompt, measure the change, then score each method by how well it predicted that change.</div>

```mermaid
flowchart LR
  P["Real prompts<br/><small>in-the-wild chats</small>"] --> S["Sample 30<br/><small>outputs per prompt</small>"]
  S --> F["Flag behaviour<br/><small>unusual pattern</small>"]
  F --> I["Investigator<br/><small>5 to 15 edits</small>"]
  I --> G["Ground truth<br/><small>measured changes</small>"]
  G --> E{"Score methods<br/><small>who predicted it</small>"}
  E --> T["Transcript read<br/><small>baseline</small>"]
  E --> A["Activation tools<br/><small>no uplift</small>"]
  classDef input fill:#d0ebff,stroke:#1971c2,color:#1b1b1b,stroke-width:2px
  classDef core fill:#e5dbff,stroke:#6741d9,color:#1b1b1b,stroke-width:2px
  classDef loop fill:#fff3bf,stroke:#f08c00,color:#1b1b1b,stroke-width:2px
  classDef exit fill:#d3f9d8,stroke:#2f9e44,color:#1b1b1b,stroke-width:2px
  classDef err fill:#ffe3e3,stroke:#e03131,color:#1b1b1b,stroke-width:2px
  class P input
  class S,F,I core
  class G exit
  class E loop
  class T exit
  class A err
```

<div class="dg-legend">Blue is input, purple is the automated pipeline, amber is the scoring step, green is ground truth and the winning baseline, red is the method that did not help.</div>

## Key points

- **Descriptive is not causal.** The result does not say SAEs are useless; it says current activation tools do not yet predict interventions better than the text.
- **Moves evaluation out of planted-quirk games** into naturally occurring behaviours.
- **Self-prediction as a trainable skill.** Training on counterfactual outcomes generalizes, which prior self-prediction work found mixed.

## Relation to prior wiki pages

- **Tempers the interpretability-for-efficiency line.** [Pruning meets interpretability via SAEs (08-31)](../inference-efficiency/2026-08-31-pruning-meets-interpretability-sae.md) used SAE features to decide what to prune. CHIVE's result asks whether those features are causal enough to trust for that.
- **Pairs with trace tampering.** The same day, [agent trace tampering](2026-09-28-agent-trace-tampering.md) showed transcripts can be edited by agents. CHIVE says the transcript is currently the best predictor we have. Oversight rests on a record that is both the strongest signal and the easiest to corrupt. See [responsible-ai](responsible-ai.md).

## Gaps

- Limited to prompt-level counterfactuals; interventions on activations themselves are the natural next test.
- Predictor quality depends on the investigator agent's edit choices.
