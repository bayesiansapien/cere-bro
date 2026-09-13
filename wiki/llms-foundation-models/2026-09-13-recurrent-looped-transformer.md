# Recurrent Looped Transformer (RLT): latent reasoning with unbounded temporal depth

**Source:** Yifan Zhang, technical report, 2026-09-12. [Project page](https://yifanzhang-pro.github.io/recurrent-looped-tranformer/) · [GitHub](https://github.com/yifanzhang-pro/recurrent-looped-tranformer) (263 stars within a day) · [English paper PDF](https://github.com/yifanzhang-pro/recurrent-looped-tranformer/blob/master/Recurrent_Looped_Transformer.pdf). Surfaced via the X home feed, [@yifanzhang_](https://x.com/yifanzhang_/status/2098714303967871430), one of the day's most-shared research artifacts.

**TL;DR.** RLT pairs a causal encoder that builds global key-value memory with a **recurrent decoder that carries its final hidden state and its layerwise sliding-window attention cache across every prompt and response token, never resetting at the serving boundary.** After t tokens the recurrent path has traversed t x L_D decoder blocks while the per-token block count stays fixed at 96. The author's phrase "infinite depth" is carefully scoped in the abstract itself: it refers to an **extensible temporal path, not infinite work within a token**, and the report states outright that "realized reasoning gains, hardware efficiency, and RL scaling remain to be established." This is a design proposal with an honest epistemic label on it, which is rarer than it should be and is why it belongs in the wiki despite having no benchmark table.

---

![RLT architecture](../../raw/assets/2026-09-13-recurrent-looped-transformer-fig1.png)

---

## The mechanism

**State.** The carried state is a pair: `H_t = (s_t, C_t^D)`, where `s_t` is the recurrent output of the decoder and `C_t^D` is the layerwise decoder sliding-window KV cache. The transition is

`(s_t, C_t^D) = D_φ( Merge(e_t, s_{t-1}) ; M_{≤t}, C_{t-1}^D, t )`

with `M_{≤t}` the global encoder memory, and the output distribution read off `s_t` through an RMSNorm and an unembedding. A sliding window of W includes the current token and retains at most W-1 historical entries for the next update.

Three properties make this different from the looped architectures already on the [looped transformers page](looped-transformers.md).

1. **The loop is over time, not over layers within a token.** Prior looped work applies the same block k times to one token's representation. RLT applies the decoder once per token and threads the output of token t-1 into the merge for token t. Depth grows with sequence length, for free, because you were going to process those tokens anyway.
2. **Prompt and response share one state transition.** Encoder memory is prefix-restricted and decoder attention respects its local window, but **neither decoder state component resets at the serving boundary** between prompt processing and generation. In a standard stack, prefill and decode are the same computation run in two regimes. Here they are literally one continuous recurrence.
3. **The RL story is a consequence of the state design, not an add-on.** The report's third design principle is "one transition from sampling to replay": to do on-policy replay you rebuild the full history under current parameters, *including* prompt states and decoder SWA KV, while keeping recorded behaviour probabilities tied to the actual sampler. The stated concrete config is 48 encoder layers and 48 decoder layers with compatible attention and FFN weights shared across stages, so 96 logical blocks execute per token and the temporal path reaches 48t blocks after t tokens.

**The hardware principle is the interesting engineering claim.** A recurrence is serial, which is the standard reason nobody ships one at scale. RLT's answer is to batch everything that is not the recurrence: known-token encoder work runs in a causal batch, independent decoder updates run in parallel, weights and memory are reused, activations are checkpointed, all while preserving the reference computation. "Parallel work around a recurrent core" is the design sentence.

---

## How this relates to prior wiki pages

**It does not contradict this wiki's settled two-loop finding, and the reason it does not is the most useful thing to record.** The [looped transformers page](looped-transformers.md) carries a result the wiki treats as established: [LoopCoder-v2 (06-17)](../inference-efficiency/2026-06-17-loopcoder-v2-parallel-loop-transformer.md) found empirically that **two loops is optimal and three-plus regress**, and [SMELT (09-02)](2026-09-02-smelt-moe-looped-transformers.md) reproduced that loop count independently under simultaneously matched FLOPs, parameters and KV budget, and supplied a mechanism (the second visit reduces the attention sink, the pile-up of attention mass on a few early or delimiter tokens). RLT's "infinite depth" is on a **different axis entirely**: it does not revisit a token's representation more than once. So the two-loop ceiling, which is a statement about diminishing and then oscillatory returns from *re-reading the same input*, has nothing to say about a path that reads new input each step. **The page's headline should now read "two loops is optimal per token, and the depth-per-token ceiling does not bound depth-per-sequence."**

**The KV precondition SMELT established applies to RLT and RLT satisfies it by construction.** SMELT's contribution to this wiki was partly methodological: KV cache size bounds the longest servable context, so a looped model that quietly needs a bigger cache is not a drop-in replacement regardless of its loss curve, and matching KV is a precondition for the loop's benefit being well-defined at all. RLT's decoder uses sliding-window attention, so its decoder cache is **bounded by W rather than by sequence length**, while the encoder memory is the conventional growing one. That is the right side of SMELT's constraint, and it means RLT's depth growth genuinely is free of KV growth in the decoder.

**The unresolved axis this page named on 09-02 was latency, and RLT is aimed directly at it.** The page recorded that looping serializes computation, so matched FLOPs is not matched wall-clock, and that SMELT reported training-FLOP savings without addressing serving latency, while concurrent MoE-looping work matched wall-clock instead. RLT's entire second design principle is an answer to that: batch everything except the recurrent core. **It is the first entry on this page that treats serving latency as a first-class design constraint rather than a reported afterthought.** Whether the batching actually recovers the loss is exactly what is unmeasured.

**Relation to the KV cache page's placement thesis.** A carried recurrent state is a fixed-size alternative to a growing cache, which is the same structural bet as the KDA layers in [kimi-k3-in-c (09-12)](../inference-efficiency/2026-09-12-kimi-k3-in-c-nvme-expert-streaming.md), where 69 of 93 layers carry a fixed-size recurrent state instead of a KV cache and that is what kept the whole model inside 8 GB. **Two very different projects in two days both concluded that the way to make long contexts cheap is to stop storing per-token state.**

## Gaps

There are no experiments. No benchmark table, no loss curve, no ablation, no wall-clock measurement, no comparison against a matched-budget baseline. The report says so itself. Everything above is a description of a design and its relationship to prior results, and **none of the three claimed benefits (reasoning gains, hardware efficiency, RL scaling) has a single supporting number.** The specific thing that would settle it fastest is the one the looped-transformer literature keeps failing to publish: matched wall-clock throughput against a conventional decoder at equal quality. There is also an obvious risk the report does not address, which is that a state carried across every token with no reset is a state that can drift, and nothing in the transition is a contraction.

## Industrial implication

If the batching claim holds, the commercial consequence is a serving architecture where prefill and decode stop being two different optimization problems, which would invalidate a large amount of current infrastructure design including the prefill/decode disaggregation that most serving stacks converged on in 2025-2026. That is a big enough claim that the absence of measurement should be read as the headline rather than a footnote. Treat this as a direction to watch for a follow-up with numbers, not as a result.

## Related pages

- [Looped transformers / iterative latent depth](looped-transformers.md)
- [Attention mechanisms](attention-mechanisms.md)
- [KV cache](../inference-efficiency/kv-cache.md)
- [RL for LLMs](rl-for-llms.md)
