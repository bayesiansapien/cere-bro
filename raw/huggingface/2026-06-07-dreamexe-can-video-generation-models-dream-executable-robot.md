---
source: farmer/huggingface
farmed: 2026-06-07T04:51:04Z
arxiv_id: 2606.04811
url: https://huggingface.co/papers/2606.04811
arxiv_url: https://arxiv.org/abs/2606.04811
date: 2026-06-07
---

# Dream.exe: Can Video Generation Models Dream Executable Robot Manipulation?

Video generation models have made impressive strides in synthesizing visually compelling content, yet their outputs remain confined to the virtual domain. A natural question follows: how well do these models reflect the physical world when their generated videos leave the screen and enter reality? We propose robotic manipulation as a concrete, measurable window onto this question: if a model has truly internalized physical laws, the motion it depicts should translate into executable robot behavior. We introduce Dream.exe, an evaluation framework that operationalizes this criterion through a video-to-execution pipeline. Given a scene image and a task description, Dream.exe synthesizes a manipulation video, converts the generated motion into robot trajectories, and executes them in a physics simulator, yielding a grounding signal that purely visual metrics cannot offer. Using this pipeline, we evaluate 8 models spanning frontier closed-source generators, open-source generators, and robot-specific models. Our benchmark covers 101 manually curated manipulation tasks at three levels of physical complexity, measured across visual quality, trajectory fidelity, and execution success. Encouragingly, several models achieve measurable execution success, suggesting that generative priors learned from internet-scale data already encode meaningful physical knowledge. Yet visual quality proves a poor predictor of executability, exposing a dimension of model capability that standard visual evaluations do not capture. Dream.exe will be open-sourced at https://github.com/showlab/Dream.exe.
