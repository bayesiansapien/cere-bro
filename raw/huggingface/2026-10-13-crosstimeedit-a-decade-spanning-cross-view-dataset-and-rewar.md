---
source: farmer/huggingface
farmed: 2026-10-14T17:45:17.067247+05:30
arxiv_id: 2609.36616
url: https://huggingface.co/papers/2609.36616
arxiv_url: https://arxiv.org/abs/2609.36616
date: 2026-10-13
---

# CrossTimeEdit: A Decade-Spanning Cross-View Dataset and Reward-Guided Editing for Historical Street-View Generation

Historical street-view imagery records urban evolution, but uneven coverage leaves substantial gaps in historical records. Generating plausible past appearances requires restoring changed structures while preserving persistent scene content. We construct VIGOR-his, a decade-spanning cross-view dataset containing 43,653 location-level quadruplets across 11 cities on three continents. Its automated pipeline performs spatial pairing, consistency screening, change classification, and the generation and validation of satellite-based change descriptions and local editing instructions. Based on VIGOR-his, we propose CrossTimeEdit, a model that reformulates historical street-view generation as editing, using recent street views to constrain viewpoint and unchanged appearance and temporal satellite differences as change evidence. Starting from FLUX.2 [Klein] 4B, we train CrossTimeEdit through supervised fine-tuning (SFT) followed by online reinforcement learning (RL). We design three street-view editing criteria, namely Instruction Alignment (IA), Background Preservation (BP), and Quality and Physical Plausibility (QP), as both RL reward dimensions and evaluation metrics. We optimize this multi-reward objective using Within Group Relative Policy Optimization for flow-matching models (Flow-GRPO) with Group reward-Decoupled Normalization Policy Optimization (GDPO), which normalizes each reward dimension before aggregation. CrossTimeEdit improves overall performance across the three editing criteria by 17.12\% over the pretrained baseline and outperforms cross-view generation models in scene consistency, visual realism, and perceptual quality. The implementation code, dataset, and model weights are available at https://luhanwen67.github.io/CrossTimeEdit-release/.
