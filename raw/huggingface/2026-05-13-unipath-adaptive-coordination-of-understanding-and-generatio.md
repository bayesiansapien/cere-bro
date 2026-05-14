---
source: farmer/huggingface
farmed: 2026-05-14T10:39:11Z
arxiv_id: 2605.11400
url: https://huggingface.co/papers/2605.11400
arxiv_url: https://arxiv.org/abs/2605.11400
date: 2026-05-13
---

# UniPath: Adaptive Coordination of Understanding and Generation for Unified Multimodal Reasoning

Unified multimodal models (UMMs) aim to integrate understanding and generation within a single architecture. However, it remains underexplored how to effectively coordinate these two capabilities for more effective and efficient reasoning. Existing coordination approaches either perform coupling during training, without explicit inference-time coordination, or impose a fixed coordination pattern for all inputs. In this work, we show that multimodal tasks exhibit substantial coordination-path diversity: different inputs favor different coordination paths. This suggests that exploiting such diversity is key to improving performance. We propose UniPath, a framework for adaptively modeling and exploiting coordination-path diversity. Instead of enforcing a single coordination pattern, we represent task solving as the selection and execution of a path, ranging from direct answering to textual inference, visual-thought construction, and hypothesis-based exploration. We construct role-aligned trajectories to train a path-conditioned executor and introduce a lightweight planner mechanism to enable input-dependent path selection. Experiments show that leveraging coordination-path diversity improves performance over fixed coordination strategies while providing interpretable intermediate behaviors. The code is available at:https://github.com/AIFrontierLab/TorchUMM/tree/main/src/umm/post_training/unipath.
