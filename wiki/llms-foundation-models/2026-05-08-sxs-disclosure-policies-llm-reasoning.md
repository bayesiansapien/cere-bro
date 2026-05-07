# When to Think, When to Speak: Learning Disclosure Policies for LLM Reasoning

**arXiv:** [2605.03314](https://arxiv.org/abs/2605.03314)
**Tier:** 2 — LLMs / streaming reasoning / responsible-ai overlap

## TL;DR

In single-stream autoregressive generation, the same tokens both update the model's internal state and constitute irreversible public commitment. SxS (Side-by-Side) Interleaved Reasoning makes the timing of disclosure a learned dual-action policy. The model interleaves partial disclosures with continued private reasoning in the same context, releasing content only when supported by reasoning so far. SFT acquires the dual-action semantics from entailment-aligned trajectories; RL recovers reasoning performance. Pareto improvements on accuracy-content-latency on AIME25 (in-domain) and GPQA-Diamond (out-of-domain), across MoE Qwen3-30B-A3B and dense Qwen3-4B.

## The conceptual frame

```
Standard autoregressive:
  token t  ────►  updates state  +  commits publicly
                       │                  │
                  (entangled — no way to think more before speaking)

The "silence tax":
  Wait longer → first relevant content arrives later.
  Speak early → premature commitments bias subsequent generation.

SxS dual-action:
  At each step, the model picks:
     (a) "think" — emit a private reasoning token (state-update only)
     (b) "speak" — emit a public-commitment token (entered into the disclosed answer)

  Constraint: only "speak" content that is entailment-supported by the reasoning so far.
```

## Training pipeline

1. **Construct entailment-aligned interleaved trajectories.** Match answer prefixes to supporting reasoning prefixes, pairing private reasoning with the public disclosure it justifies.
2. **SFT the model on dual-action semantics.** Acquire the think-vs-speak distinction within standard autoregressive generation.
3. **RL recovers reasoning performance** under the new format. The new format should not impose a tax on reasoning quality.

## Result summary

Reported as Pareto improvements on the accuracy-content-latency triple under token-level proxies (e.g., inter-update waiting time):
- AIME25 (in-domain): improved
- GPQA-Diamond (out-of-domain): improved
- Both Qwen3-30B-A3B (MoE) and Qwen3-4B (dense)

The paper does not report a single headline number but a Pareto frontier shift. The accuracy-vs-time-to-first-content trade-off improves at multiple operating points.

## How this relates to prior wiki work

- **First time the wiki has tracked the silence-tax / premature-commitment trade-off as a learnable variable.** Prior work treated streaming as an architectural constraint.
- **Connection to today's [First Token Knows](../responsible-ai/2026-05-08-first-token-knows-hallucination-detection.md)** paper. Both operate on the question "when does an LLM commit to an answer?" First Token Knows reads commitment from logit entropy. SxS makes commitment a learned action. Two framings of the same underlying unbundling.
- **Lateral to [Step-Level Optimization](../ai-routing/2026-05-02-step-level-optimization-computer-use-agents.md)** (05-02), which detects trajectory stalls at inference. Step-Level Optimization is a stall detector. SxS is a controlled-disclosure policy. They could compose.
- **Streaming analog to [Stream-T1](../inference-efficiency/2026-05-07-stream-t1-test-time-scaling-streaming-video.md)** (05-07), which works on video streaming. Different modality, similar problem of when-to-commit during generation.

## What's surprising

Most "controlled generation" work imposes external constraints (regex, grammar, etc.) on the output. SxS makes the disclosure timing itself an internal action of the model, learnable via SFT+RL. This is a different kind of unbundling than the constrained-decoding literature. It does not constrain *what* the model says, it makes *when* the model says it a controllable variable.

## Open questions

1. **Tool-calling generalization.** In tool-using agent loops, "speaking" is invoking a tool, and a wrong tool call is the irreversible commitment. Does SxS's dual-action distinction transfer? This is the obvious next setting.
2. **Entailment-trajectory scale.** The SFT stage requires entailment-aligned interleaved trajectories matched by hand or by automated entailment checking. Whether this scales to broad-domain training corpora vs the specific reasoning-benchmark distribution used here is unclear.
3. **Disclosure-as-control on adversarial inputs.** Premature commitment is the failure mode that [tool-chaining attacks](../agentic-systems/2026-05-05-academiclaw-student-tasks.md) exploit. Whether SxS is robust to adversarial inputs that try to force early commitment is open.

## Why it matters

For agent systems with long reasoning chains (the [Stream-T1 video analog](../inference-efficiency/2026-05-07-stream-t1-test-time-scaling-streaming-video.md) from yesterday's digest), the disclosure-policy frame is the abstraction that survives across modalities. Both papers say "the streaming version of generation is not just a UX wrapper over single-shot generation." SxS gives that claim a learnable form.
