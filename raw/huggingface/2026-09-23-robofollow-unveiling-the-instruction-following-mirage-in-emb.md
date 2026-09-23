---
source: farmer/huggingface
farmed: 2026-09-23T14:55:25.993402
arxiv_id: 2609.25636
url: https://huggingface.co/papers/2609.25636
arxiv_url: https://arxiv.org/abs/2609.25636
date: 2026-09-23
---

# RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents

Modern embodied agents achieve impressive success rates, yet their actual instruction-following ability is far weaker than these numbers suggest. We trace this illusion to a structural property we term low scene entropy: when a visual scene admits only one valid task, language becomes redundant and a policy can score highly while barely using it. We introduce RoboFollow, a diagnostic benchmark with three principles: (1) High Scene Entropy: each training scene supports multiple kinematically distinct task branches, making vision alone insufficient and forcing reliance on language. (2) Hierarchical Diagnostic Protocol: a four-level protocol (L0--L3) progressively perturbs visual layout and semantics, probing whether equivalent instructions yield consistent behavior and distinct ones yield discriminable behavior across spatial relations, attributes, trajectory constraints, and logic. (3) Confound-Controlled Diagnosis: we simplify interaction objects, restrict actions to the trained repertoire and report stage-wise Intent and Execution scores, isolating comprehension from motor execution. Evaluation of nine VLA and WAM policies shows that strong L0 performance, where attained, does not reliably transfer to L1--L3 under our fine-tuning setup. Representative mitigations, including stronger VLM backbones, QA co-training, LangForce, and Classifier-Free Guidance, all fail to close this gap. RoboFollow exposes genuine instruction following as a critical, overlooked bottleneck. Code and dataset are available at https://github.com/AutoLab-SAI-SJTU/RoboFollow and https://huggingface.co/datasets/AutoLab-SJTU/robofollow-data.
