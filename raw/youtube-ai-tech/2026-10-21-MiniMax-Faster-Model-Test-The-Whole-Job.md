# Is a Faster Model Actually Faster? Test the Whole Job (Morgan Suo, MiniMax)

**Channel:** AI Engineer
**Published:** 2026-10-21
**Source:** https://www.youtube.com/watch?v=YvQ4BVTWfHI

## TL;DR
MiniMax previews M3.1 Flash (said to release "next week") and uses it to argue that every efficiency trick (sparse attention, 4-bit KV cache, 4-bit MoE experts, speculative decoding, reasoning-effort control) must be judged on the finished job: time and cost to a verifiable, usable output, including retries, tool calls and human fixes. The most useful content is the disclosed failure modes: a 6.6-point drop on one sub-score hidden by a flat average after KV4, P95 TTFT going ~8x when concurrency doubles, and an 80% to 68% accuracy fall when reasoning effort drops from max to high.

## Key Takeaways
- **Test task:** an analyst question across 14 PCB supplier reports ("is AI server demand turning into cash?"). Success requires the right sources, aligned reporting periods, separate business lines, and catching profit vs cash flow divergence in footnotes.
- **Sparse attention:** a cheap selection step scores text blocks, main attention runs on selected blocks plus a local window, selection is query-dependent. M3.1 Flash adds sparse attention to its first three layers. Passed 39/39 on a position-varied retrieval test up to ~830K tokens.
- **KV cache: Q8 / KV4.** Keys and values drop from 8-bit to 4-bit, queries stay 8-bit. Average score roughly flat, one sub-score falls 6.6 points, others rise. Averages hide user-relevant regressions.
- **MoE experts at 4-bit weights and activations.** Shared expert excluded. Placement of scale and rescale steps in the GEMM pipeline matters for correctness; "fast math still has to be corrected."
- **Speculative decoding:** count draft time, verify time and rejection cost; then count retrieval, tool calls and retries on top.
- **Concurrency 32 to 64:** throughput up ~1.9x, P95 time-to-first-token from ~1.5s to ~11.6s while the median looked fine.
- **Reasoning effort:** blank effort defaults to max. High uses fewer tokens but accuracy fell 80% to 68% on a coding test. Pick and record the budget per task.
- **Ship checklist:** fix the source set and info cutoff, define acceptance up front; measure trust (checkable sources and math), full job cost and time (including failed attempts and human repair), and reproducibility (pin model, runtime, prompts, sources); roll out small with rollback.

## Architecture & Optimization Mechanics
- **Sparse attention retrieval is a necessary but not sufficient check.** Needle tests at 830K say nothing about multi-hop reasoning across conflicting documents, which is the actual research failure mode. The talk acknowledges this but shows no such eval.
- **KV4 with Q8 queries** halves KV memory and bandwidth vs an 8-bit path, raising batch size and decode throughput. The cost lands unevenly across sub-tasks, which argues for per-capability eval slices whenever you quantize KV.
- **W4A4 routed experts with an unquantized shared expert** is the now-standard MoE compression split: shared expert carries common, outlier-heavy features; routed experts tolerate more aggressive quantization. Scale fusion order is where correctness bugs hide.
- **Throughput vs tail latency** is the classic serving trade: the 1.9x throughput gain at 64 concurrency is paid for in queueing, visible only at P95.
- **Reasoning budget is a routing dimension.** A 12-point accuracy drop from max to high effort means effort should be chosen per task class, not globally.

## Grounded Context (Web Enrichment)
As of 2026-10-22, M3.1 Flash is not formally released. Reports say MiniMax quietly put an M3.1-Flash-Preview into MiniMax Code with the API still gated, and leak trackers list no weights, model card or pricing. The leaked spec ("Q8KV4": FP8 queries, 4-bit E2M1 keys/values in blocks of 16; NVFP4 routed experts; a new speculative decoding head) matches what the talk describes, so the talk effectively confirms the leak. One discrepancy: leaks say M3.1 makes all layers sparse, while the talk says sparse attention was added to the "first three layers," which most plausibly means M3's remaining dense layers were converted. The base M3 (released 1 June 2026) has documented MSA block-sparse attention cutting per-token compute at 1M context to ~1/20th of M2; llama.cpp and TensorRT-LLM have added dedicated M3 sparse-attention support, and running it dense reportedly gives wrong answers.

Opinion: the "test the whole job" message is correct but generic, and the evidence is thin. The 39/39 retrieval result is a single small test, the KV4 table compares full setups without ablation (as the speaker admits), and none of the numbers are on the PCB research task itself. Treat the disclosed regressions as the real signal and the end-to-end claim as untested until M3.1 Flash ships with a model card.

## Real-World Application / Actionable Step
- **Quantization evals:** whenever you ship KV4 or W4A4 experts, report per-sub-task deltas and flag any slice dropping more than ~3 points even if the average is flat. Add a long-context, multi-document conflict test, not just needle retrieval.
- **MoE compression:** keep the shared expert at higher precision and audit scale/rescale placement in the fused expert kernel before blaming the format for accuracy loss.
- **Routing:** treat reasoning effort as a routing knob alongside model choice. Route to max effort only for task classes where the accuracy cliff exists; log the effort setting per request so cost attribution is reproducible.
- **Serving SLOs:** set admission control on P95 TTFT, not median or aggregate throughput. Raising concurrency from 32 to 64 is only a win if the tail stays inside the SLO.
- **Watch for the M3.1 Flash release** and benchmark it against your current long-context model on cost per accepted output, including retries.
