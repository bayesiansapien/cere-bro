---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.03607
url: https://huggingface.co/papers/2610.03607
arxiv_url: https://arxiv.org/abs/2610.03607
date: 2026-10-07
---

# World Action Learning via Interaction-Centric Spectral Latent Guidance

Learning general-purpose robot policies requires large-scale real-world interaction data, yet collecting robot demonstrations remains expensive and difficult to scale. Egocentric videos offer abundant human interaction experience with task-relevant semantics for robotic manipulation, but direct transfer is challenging for two reasons: latent actions inferred from frame reconstruction can be dominated by nuisance variation such as ego-camera motion, and human and robot behaviors often exhibit different temporal dynamics. We propose WING (World Action Learning via INteraction-Centric Spectral Latent Guidance), a framework for transferring interaction knowledge from egocentric videos to robot policies. WING first separates observer-induced motion from hand-object interaction and distills the interaction-centric component into latent actions. It then exploits the observation that cross-embodiment task semantics are concentrated in slowly varying temporal structures, identifying shared low-frequency components between egocentric latent actions and robot behaviors in the spectral domain and using them to guide action generation. WING achieves average success rates of 99.20% on LIBERO, 93.80% on RoboTwin 2.0, and 57.7% on RoboCasa-GR1, and also performs strongly across four real-world manipulation tasks under diverse generalization settings. These results show that interaction-centric spectral guidance provides an effective and scalable way to transfer physical interaction knowledge from human egocentric video to robot control. Project page: https://mikuz12.github.io/wing/
