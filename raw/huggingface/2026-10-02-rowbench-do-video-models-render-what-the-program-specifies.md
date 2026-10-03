---
source: farmer/huggingface
farmed: 2026-10-03T05:03:51.818444+00:00
arxiv_id: 2610.02205
url: https://huggingface.co/papers/2610.02205
arxiv_url: https://arxiv.org/abs/2610.02205
date: 2026-10-02
---

# ROWBench: Do Video Models Render What the Program Specifies?

Programmable world models separate executable dynamics from visual generation, offering a promising foundation for next-generation game engines. However, their visual adherence to explicit rules and interactions remains insufficiently evaluated. Existing benchmarks assess visual quality, controllability, and instruction or physical adherence, but rarely test fidelity to fine-grained, program-specified world events. We introduce PROWBench, comprising 170 programmatically constructed episodes and 600 proxy videos covering diverse scenes and interactions. PROWBench logs entity states and timestamped events, including those outside the camera's field of view, as replayable world records, from which it renders synchronized views and proxy representations. This enables generated videos to be checked against the observable consequences of program execution. An extensible framework constructs scenes, controls behaviors, and can render each camera view in different representations, such as coarse 3D, and bounding boxes. The benchmark covers first- and third-person perspectives, with synchronized multi-view observations available for a subset of episodes. Grounded in these records, PROWBench evaluates entity control, long-horizon memory, and, with two VLM-based metrics, Logic-Render Alignment and Interaction Success Rate, adherence to the prescribed timeline and the visual realization of timestamped engine-recorded events.
