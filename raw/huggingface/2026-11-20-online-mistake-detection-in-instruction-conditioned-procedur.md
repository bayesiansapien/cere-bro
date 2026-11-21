---
source: farmer/huggingface
farmed: 2026-11-21T10:04:29.385819+00:00
arxiv_id: 2611.25567
url: https://huggingface.co/papers/2611.25567
arxiv_url: https://arxiv.org/abs/2611.25567
date: 2026-11-20
---

# Online Mistake Detection in Instruction-Conditioned Procedural Video

An assistant monitoring a person performing a procedure is most useful when it can detect mistakes while there is still time to recover. This requires judging actions against task instructions as the video unfolds, identifying the attempted step, locating it in time, and assessing its execution. Existing online detectors do not use the instruction text, while instruction-conditioned methods operate offline. In this paper, we study online, instruction-conditioned mistake detection in egocentric videos. Using only observed video, task instructions, and prior predictions, our model identifies and localizes completed action attempts and classifies them as correct, modified, slip, corrections, or additions; omitted steps are determined after the video ends. We compare a modular pipeline, with separate step identification, temporal localization, and execution verification, to a joint model that predicts all outputs in a single step. To support supervised learning from mistakes, we repartition EgoPER to include erroneous videos in all splits. The approaches achieve similar step-segmentation F1@0.5 (93.6% and 92.1%), while the joint model achieves higher binary mistake-detection F1@0.5 (84.1% vs. 80.7%), with its largest gain on slips (56.4% vs. 37.5%). Component-level analysis suggests that error propagation between stages contributes to the modular approach's lower detection score. On test videos containing mistakes, both designs outperform released AEM and ESTANet checkpoints under our evaluation protocol.
