---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2611.31184
url: https://huggingface.co/papers/2611.31184
arxiv_url: https://arxiv.org/abs/2611.31184
date: 2026-11-25
---

# On-Policy Codec Distillation for Efficient All-in-One Video Generation

Modern visual generative models operate on tokens, and every visual asset they receive, whether an identity, a scribble, a depth map, or a motion video, is tokenized and appended to the input token sequence. Consequently, conditioning quickly dominates the computation cost. Yet most of these tokens carry redundant spatiotemporal information. Our key insight is that identifying what is genuinely new is exactly the problem that classical video codecs have long solved. Thus, we first introduce a codec-based token pruning method that discards redundant tokens. Then, we propose an on-policy self-distillation (OPSD) strategy to train a DiT adapter capable of learning the codec pruning pattern well without quality degradation. Together, they form On-Policy Codec Distillation (CodecOPSD). We scale CodecOPSD to 16 condition modalities on our own video diffusion model, where it prunes 66% of the condition tokens on average with almost no quality drop. Therefore, denoising becomes 2x faster, and the cache memory shrinks by up to 73% in KV cache mode. CodecOPSD also extends to other state-of-the-art pretrained image and video generative models, where its benefit grows further with more conditions, longer frames, and higher resolution.
