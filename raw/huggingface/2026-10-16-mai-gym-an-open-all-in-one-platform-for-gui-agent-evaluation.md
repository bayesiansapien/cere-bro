---
source: farmer/huggingface
farmed: 2026-10-17T12:02:29.883616+05:30
arxiv_id: 2610.20939
url: https://huggingface.co/papers/2610.20939
arxiv_url: https://arxiv.org/abs/2610.20939
date: 2026-10-16
---

# MAI-Gym: An Open All-in-One Platform for GUI Agent Evaluation and RL Training across Mobile and Computer Environments

Online reinforcement learning (RL) with verifiable rewards has driven rapid progress in mathematics, coding, and tool use, but scaling this success to GUI agents remains challenging due to the high cost of interactive environments and the scarcity of realistic training tasks. We introduce MAI-Gym, an open all-in-one platform that unifies GUI agent evaluation, data collection, and online RL training across mobile, computer, and web environments. Through a shared rollout pipeline, MAI-Gym ensures consistent agent behavior across evaluation and training, supports ten established benchmarks, and scales to 20,000 parallel environment instances. Beyond scalable infrastructure, MAI-Gym enables automated synthesis of diverse GUI applications and challenging tasks, including resettable mocked apps and coherent cross-app worlds with execution-validated task verifiers. Using MAI-Gym, we train MAI-Gym-9B, a unified 9B agent for mobile and computer use, achieving state-of-the-art performance among open GUI agents under 10B parameters: 78.4% on MobileWorld and 76.2% on OSWorld-Verified. Importantly, RL in a mocked train-ticketing app transfers to its real-world counterpart, improving task success on a phys- ical phone from 28.8% to 48.1%. We release the framework, synthesis skills, mocked apps, 2,000 verified tasks, and the model checkpoint to support repro- ducible research and further advances in scalable GUI agent training.
