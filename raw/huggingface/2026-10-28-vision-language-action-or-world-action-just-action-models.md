---
source: farmer/huggingface
farmed: 2026-10-29T10:37:09.996148+05:30
arxiv_id: 2610.37219
url: https://huggingface.co/papers/2610.37219
arxiv_url: https://arxiv.org/abs/2610.37219
date: 2026-10-28
---

# Vision-Language-Action or World-Action? Just Action Models

The vision-language-action (VLA) and world-action model (WAM) communities debate whether control policies should inherit pretrained knowledge from vision-language models or from visual generators. The debate, however, bundles three separable choices: backbone initialization, the objective applied to future observations, and whether the machinery for that future loss is kept at inference. A gap between a VLA and a WAM therefore cannot simply be attributed to any one of them. We show that decoupling these choices yields a common framework for both families, which we term Just Action Model (JAM): a pretrained visual backbone with an action expert, trained with an action loss and a foresight loss. The foresight loss trains current-observation features to predict frozen encodings of the recorded future through a prediction head discarded after training, so no visual generation is involved in either training or inference, and the backbone can be chosen freely. We first compare objectives within fixed policy architectures, then evaluate the foresight recipe across backbone families. The resulting JAM policies outperform their matched FastWAM and ImageWAM counterparts on LIBERO and LIBERO-Plus, and achieve similar or slightly higher success rates on RoboTwin. Compared with FastWAM, JAM improves the success rates from 97.0%/55.3%/91.2% to 98.2%/64.5%/91.4%, respectively. With cached foresight targets, JAM reduces estimated online training FLOPs per sample per update by 73% relative to FastWAM. Our results show that future supervision improves control without visual generation or additional inference machinery, and strong foresight performance is attainable with either generator-initialized or vision-language backbones. Project Page: https://y0uroy.github.io/JAM
