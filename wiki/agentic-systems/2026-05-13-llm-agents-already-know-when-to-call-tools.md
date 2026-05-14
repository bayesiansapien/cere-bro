# LLM Agents Already Know When to Call Tools — Even Without Reasoning (Probe&Prefill)

**Date:** 2026-05-13
**Source:** [arXiv 2605.09252](https://arxiv.org/abs/2605.09252) · HuggingFace Daily Papers
**Tier:** 2. Agentic tool calling, mechanistic interpretability of agent behavior
**Raw:** [`raw/huggingface/2026-05-13-llm-agents-already-know-when-to-call-tools-even-without-reas.md`](../../raw/huggingface/2026-05-13-llm-agents-already-know-when-to-call-tools-even-without-reas.md)

## TL;DR

Tool-augmented agents over-call tools, wasting fees and latency. The When2Tool benchmark (18 environments across 3 categories of tool necessity: computational scale, knowledge boundaries, execution reliability) shows that prompt-only suppression and Reason-then-Act baselines both fail. Probing the model's hidden states reveals that tool necessity is linearly decodable from the pre-generation representation with AUROC 0.89-0.96 across six models, substantially exceeding the model's own verbalized reasoning. The model already knows; it just fails to act on its own knowledge. Probe&Prefill uses a lightweight linear probe to read this signal and prefills the response with a steering sentence. Result: 48% reduction in tool calls with only 1.7% accuracy loss. Best baseline at comparable accuracy reduces only 6%, or at comparable reduction takes a 5x larger accuracy hit.

## Why it matters

Two findings stack into a load-bearing result: (1) verbalized reasoning underreports what the model already knows internally, and (2) a linear probe can extract that latent knowledge and use it to steer behavior at inference time. The first is a mechanistic claim about chain-of-thought being a degraded readout of internal state. The second is a deployable production tool. Together they argue that the right primitive for agent control is hidden-state probing plus prefix steering, not better prompts or longer reasoning.

## Mechanism

The benchmark separates "tool is needed" from "tool is unnecessary" with controlled difficulty. The probe is a linear classifier on the pre-generation hidden state, trained on a few hundred examples per environment. At inference, the probe outputs a single scalar; if above threshold, the response is prefilled with a steering sentence that directs the model toward tool use; otherwise the model proceeds directly.

The 0.89-0.96 AUROC is the structurally interesting number, the tool-necessity signal is linearly decodable from a single layer's hidden state. This rules out a story where the model needs deep reasoning to know that it knows; the signal is shallow and steerable.

## Relation to prior wiki

- **Massive Activations ME Layer (today)** — single-layer interpretability claim from the same week. Both papers say important behavioral structure is locatable in shallow representations. Pattern is forming: agentic and interpretability papers in May are converging on "shallow latent variables explain a lot."
- **Compliance vs Sensibility (2026-05-02)** — reasoning mode is a linear direction in activation space. Probe&Prefill is the agentic version: tool necessity is a linear direction in activation space. Two independent papers in 11 days locating actionable agent behavior on a linear axis.
- **Needle (r/LocalLLaMA 2026-05-13)** — distilled Gemini tool calling into a 26M attention-only model, claiming that tool calling is fundamentally retrieval-and-assembly, not reasoning. Probe&Prefill's hidden-state-decodability result is the mechanistic confirmation of Needle's design intuition: if the tool-necessity signal is linear, you do not need FFN capacity for the decision; cross-attention plus a probe suffices.
- **Tool-Calling concept page** — the standard agentic loop assumes the model decides via verbalized reasoning. This paper says the decision is mostly *not* verbalized; chains of reasoning are a verbose readout of an already-formed internal answer. Production agent systems should probe the hidden state directly when latency or token cost matters.

## Research angle

Two open questions. (1) Generalize the probe across environments. The paper trains per-environment probes; a universal tool-necessity probe across environment types would be a stronger result and a deployable artifact. (2) The probe-and-prefill primitive is generic. Refusal, format, calibration could all be amenable to the same approach. The natural next paper is the Kazemi-style single-neuron refusal install (12-May retweet) applied to tool-necessity, or vice versa.

## Why Tier 2

It is not Tier 1 because the gain (48% tool reduction at 1.7% accuracy loss) is per-environment and the deployment cost-saving has not been measured at production scale. But the mechanistic claim (verbalized reasoning is a degraded readout of latent state, which is linearly extractable) is structurally important across agents and interpretability.
