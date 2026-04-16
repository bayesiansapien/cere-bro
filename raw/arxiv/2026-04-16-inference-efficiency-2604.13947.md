---
source: farmer/arxiv
farmed: 2026-04-16T05:29:34Z
arxiv_id: 2604.13947
category: cs.CV
concept: inference-efficiency
url: https://arxiv.org/abs/2604.13947
published: 2026-04-16
authors: Hamed Ouattara, Pierre Duthon, Pascal Houssam Salmane
---

# Heuristic Style Transfer for Real-Time, Efficient Weather Attribute Detection

**arXiv:** https://arxiv.org/abs/2604.13947
**Authors:** Hamed Ouattara, Pierre Duthon, Pascal Houssam Salmane

## Abstract

arXiv:2604.13947v1 Announce Type: new  Abstract: We present lightweight and efficient architectures to detect weather conditions from RGB images, predicting the weather type (sunny, rain, snow, fog) and 11 complementary attributes such as intensity, visibility, and ground condition, for a total of 53 classes across the tasks. This work examines to what extent weather conditions manifest as variations in visual style. We investigate style-inspired techniques, including Gram matrices, a truncated ResNet-50 targeting lower and intermediate layers, and PatchGAN-style architectures, within a multi-task framework with attention mechanisms. Two families are introduced: RTM (ResNet50-Truncated-MultiTasks) and PMG (PatchGAN-MultiTasks-Gram), together with their variants. Our contributions include automation of Gram-matrix computation, integration of PatchGAN into supervised multi-task learning, and local style capture through local Gram for improved spatial coherence. We also release a dataset of 503,875 images annotated with 12 weather attributes under a Creative Commons Attribution (CC-BY) license. The models achieve F1 scores above 96 percent on our internal test set and above 78 percent in zero-shot evaluation on several external datasets, confirming their generalization ability. The PMG architecture, with fewer than 5 million parameters, runs in real time with a small memory footprint, making it suitable for embedded systems. The modular design of the models also allows style-related or weather-related tasks to be added or removed as needed.
