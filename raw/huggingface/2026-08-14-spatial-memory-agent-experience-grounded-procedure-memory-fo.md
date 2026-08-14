---
source: farmer/huggingface
farmed: 2026-08-14T11:17:27.766803
arxiv_id: 2608.12743
url: https://huggingface.co/papers/2608.12743
arxiv_url: https://arxiv.org/abs/2608.12743
date: 2026-08-14
---

# Spatial Memory Agent: Experience-Grounded Procedure Memory for Spatial Intelligence

Spatial intelligence is becoming a foundation for embodied agents, robotic planning, and multimodal assistants. To improve the spatial reasoning ability of VLM agents, existing work has mainly followed two lines. One line uses post-training methods, such as supervised fine-tuning and reinforcement learning. Another line adopts an agentic paradigm in which the model calls external spatial tools, such as depth estimation and 3D reconstruction tools, to gather intermediate spatial evidence. We study a complementary and underexplored route: Can a frozen VLM agent improve its spatial reasoning through parameter-update-free self-evolution, without depending on external expert spatial tools at inference time? We present Spatial Memory Agent (SMA), an experience-grounded runtime framework that converts verified spatial experience into reusable transferable lessons. In a verifiable spatial environment, SMA queries the frozen VLM, obtains a predicted answer and reward, and uses verifier-guided reflection to distill compact transferable lessons from spatial experience. SMA further assigns each lesson a Transfer Reliability Score (TRS), which is initialized uniformly and calibrated from later retrieval outcomes as visit evidence of future transfer reliability. During read-only deployment, SMA retrieves lessons by semantic filter and similarity-TRS combined ranking, allowing the retrieved memory to guide frozen model inference. Across five representative spatial benchmarks and four base VLMs, SMA achieves the highest macro average in every base-model block and the best accuracy among the evaluated methods in most of the 20 evaluations, establishing a practical parameter-update-free path for spatial self-evolution across the evaluated frozen model scales and environments.
