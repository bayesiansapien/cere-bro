# StateKV: Linear Scaling Video VLMs for Long Video Understanding

Video vision-language models (VLMs, models that read both pixels and text) use spatiotemporal self-attention, so compute and latency grow quadratically with the number of frames. Existing efficiency fixes such as dropping frames or tokens or using coarse attention all lose accuracy. StateKV is an inference-time method, with no fine-tuning and no architecture change, that adapts a pretrained long-video VLM to linear-time video prefill. It carries cross-frame context in a fixed-capacity, importance-based recurrent state, and pairs that with a second full per-frame cache used during decoding. Across three long-video benchmarks and seven models spanning three families and multiple scales, StateKV stays close to full self-attention and beats sliding-window and recency-streaming approximations. Because it cuts video-prefill FLOPs, at a fixed compute budget you can run a larger model for higher accuracy.

```
frames ──► spatiotemporal attention is O(n²) (the problem)

StateKV (training-free wrapper):
  frame_t ─► importance score ─► fixed-capacity RECURRENT STATE (cross-frame memory)
          └─────────────────────────────────────────────────► linear-time prefill
  decoding reads ─► full per-frame CACHE (kept separate, for generation)
```

## Key points

- **The cost is in prefill, and prefill is quadratic.** For long video the dominant expense is reading all frames through spatiotemporal self-attention before any answer is produced. StateKV attacks exactly that.
- **Two stores, two jobs.** A fixed-capacity recurrent state holds cross-frame context for prefill, scored by importance so the most useful frame information survives. A separate full per-frame cache is kept for the decoding phase. Splitting the roles is the core design choice.
- **Training-free and architecture-free.** StateKV wraps a pretrained quadratic VLM at inference time. No retraining, no new weights, no architecture surgery, which is what makes it immediately deployable.
- **Validated broadly.** Three long-video benchmarks, seven models, three model families, multiple scales. It stays close to full self-attention and beats sliding-window and recency-streaming baselines.
- **Compute saved buys accuracy.** Cutting prefill FLOPs lets you spend the freed budget on a larger model at the same total cost, which is the practical efficiency-for-quality trade.

## Gaps in the study

A fixed-capacity state may lose information on extremely long videos, where the importance scoring has to discard ever more. The overhead of computing the importance scores themselves is not fully characterized, and it could erode the linear-time win at scale. The benchmarks are understanding tasks, not generation, so the method's behavior on long-video generation is untested.

## How it relates to prior wiki pages

The kv-cache.md concept page tracks a strong "KV eviction as a quality decision" thread, and StateKV adds a distinct axis to it.

- **Conf-KV (2026-05-30)**, which sets a per-step cache budget driven by model confidence, decides how much to keep per step. StateKV instead fixes capacity up front and decides what to keep by importance.
- **Forcing-KV (2026-05-15)**, which compresses the cache by assigning heads static versus dynamic roles for video diffusion, splits the cache along the head axis. StateKV splits along a different line: a recurrent state for prefill memory versus a full cache for decoding.
- **WorldKV (2026-05-24)**, which treats evicted KV entries as a retrievable world memory for video, keeps evicted context recallable. StateKV instead folds cross-frame history into a single fixed state rather than a retrieval store.
- **EarlyTom (2026-05-30)**, which compresses video tokens inside the encoder before attention, reduces tokens upstream. StateKV leaves the tokens alone and reduces the attention cost downstream.

StateKV's new axis is the recurrent state: compress all cross-frame history into a fixed-capacity memory. That is the linear-attention and SSM idea (carry history in a fixed-size state instead of an ever-growing cache) applied not as a new architecture but as a training-free inference-time wrapper around a pretrained quadratic VLM. None of the prior video-KV work used a fixed recurrent state in this role.

## Industrial implication

Long-video and streaming-video agents are prefill-bound: the wall-clock cost is dominated by ingesting frames before responding. A training-free wrapper that turns that prefill linear is immediately deployable on existing pretrained VLMs, with no retraining bill. Expect this style of fixed-state prefill wrapper to show up fast in any product doing long or live video understanding, since it ships without touching the model.

## Links

- Paper: [arXiv 2605.31598](https://arxiv.org/abs/2605.31598)
- Related concept page: [KV cache](kv-cache.md)
- Related concept page: [Knowledge distillation](knowledge-distillation.md)

Raw source: [raw/huggingface/2026-06-01-linear-scaling-video-vlms-for-long-video-understanding.md](../../raw/huggingface/2026-06-01-linear-scaling-video-vlms-for-long-video-understanding.md)
