---
source: farmer/huggingface
farmed: 2026-10-07T16:16:43+05:30
arxiv_id: 2610.04211
url: https://huggingface.co/papers/2610.04211
arxiv_url: https://arxiv.org/abs/2610.04211
date: 2026-10-06
---

# CurveCodec 2: Skeleton-agnostic animation compression with a learned entropy model

Skeletal motion is stored as every joint's transform at every frame, yet most of it is implied by the body rather than by what the motion is about. Compression is one way to ask what a motion must still say once the body is known, and a production codec must answer it for any skeleton with a stated error bound. Our earlier codec, CurveCodec, matched the mean error of ACL, the production library of modern game engines, with a learned prior over sparse anchors, but not ACL's worst case, and it counted its payload as floats rather than bits. Here we ask where the redundancy of skeletal motion lies and which part of a codec a learned model should take over. Measurements give three answers. At production precision the largest saving comes from predicting each quantized curve from its own past, the second from choosing per joint, in closed loop through the hierarchy, which samples not to code. On the gaps such an encoder leaves, a nearest-neighbour oracle over millions of training samples is no better than linear interpolation, and no learned in-betweener we tried paid for itself. What a network does learn is the distribution of the residuals the codec must send. CurveCodec 2 codes every sub-track as a curve in the log map, quantized in closed loop and thinned to rate-distortion-selected keys, with residuals entropy-coded under a small learned model whose integer inference is bit-exact across platforms. Two contracts are verified on every decoded clip: ACL's own worst case per joint within a stated tolerance, or ACL's mean error per clip. On a held-out test side of 4,472 clips from 33 datasets, CurveCodec 2 needs 0.37x ACL's bytes at ACL's default precision of 0.01 cm under the worst-case contract and 0.22x at 0.1 cm under the mean contract, decodes on one CPU core, and transfers without retraining to a species absent from training. Project page: https://rubbly.cn/publications/curvecodec/
