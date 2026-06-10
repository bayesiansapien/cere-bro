---
source: farmer/huggingface
farmed: 2026-06-10T06:28:48Z
arxiv_id: 2606.10804
url: https://huggingface.co/papers/2606.10804
arxiv_url: https://arxiv.org/abs/2606.10804
date: 2026-06-10
---

# SCAIL-2: Unifying Controlled Character Animation with End-to-end In-Context Conditioning

Controlled character animation requires transferring motion from a driving sequence to a reference character. Prior works heavily rely on intermediate representations, including pose skeletons to represent motion or masked background to represent environment, which inevitably leads to information loss. To address this, we present SCAIL-2, an framework that bypasses those intermediates and achieves end-to-end character animation. By directly concatenating driving videos to the sequence, the model can obtain all the required visual information from the input video. To address lack of end-to-end data, we unify sub-tasks of character animation with decoupled conditions and then curate a pipeline to synthesize MotionPair-60K, an end-to-end motion transfer dataset containing heterogeneous tasks of character animation. To archive the unification, we utilize in-context mask conditioning and mode-specific RoPE as soft guidance beyond textual instructions and raw visual information. To address synthetic discrepancy in detailed regions, we propose Bias-Aware DPO to construct preference items to mitigate the errors. Extensive experiments demonstrate that our method substantially outperforms existing state-of-the-art approaches in various character animation tasks. A large subset of synthetic data as well as model weights will be released at our project page: https://teal024.github.io/SCAIL-2/.
