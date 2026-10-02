---
source: farmer/huggingface
farmed: 2026-10-02T10:34:13.347500+05:30
arxiv_id: 2609.38537
url: https://huggingface.co/papers/2609.38537
arxiv_url: https://arxiv.org/abs/2609.38537
date: 2026-10-01
---

# Systematically Exploring the Capabilities of GPT-6 Astra as Embodied Policies

GPT-6 Astra exhibits a remarkable ability to generate numerical robot actions, extending its role beyond high-level planning. To assess Astra's capabilities as general-purpose embodied policies, we conduct comprehensive evaluations across six domains, examining direct control, cooperation with learned policies, and feedback-driven adaptation. In gripper manipulation, Astra can correct task targets and prepare contact conditions for subsequent policy execution; hybrid control with π0.5 achieves 48% success on the evaluated RoboDojo subset. In dexterous manipulation, hybrid control achieves 50% success in ten experience-guided DexJoCo trials, while direct in-hand control struggles to coordinate finger contacts. In mobile manipulation, hybrid control reaches 38.7% success on the evaluated RoboCasa365. In navigation, Astra leads our local comparisons, reaching 92% success on RxR instruction following and 82% on HM3D object search, although search incurs substantial detours. In locomotion, dense motion-reference generation remains unreliable: none of five sequential attempts on a single obstacle course reaches the goal, despite improvements in stability and forward progress. In humanoid loco-manipulation, Astra exceeds baseline methods on 13 of 30 HumanoidBench tasks with pretrained whole-body controllers. These findings reveal a gap between useful task decisions and reliable physical control. Inference latency further constrains practical control: across 50 RoboDojo instances per condition, policy-assisted and direct control consume 624.8 million and 1.132 billion tokens. A 30-second locomotion run requires 250 model calls averaging 39.86 seconds each, with physics paused during inference.
