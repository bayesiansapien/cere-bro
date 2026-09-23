---
source: farmer/huggingface
farmed: 2026-09-23T05:53:04.588715+00:00
arxiv_id: 2609.25270
url: https://huggingface.co/papers/2609.25270
arxiv_url: https://arxiv.org/abs/2609.25270
date: 2026-09-23
---

# RULER: Instance-aware Rubric Rewards for SVG Generation

Generating Scalable Vector Graphics (SVG) code from natural-language instructions is an open-ended task without absolute visual ground truth, leaving both evaluation and policy optimization without a faithful signal. Scalar metrics (CLIP, Aesthetic) calibrated on natural images transfer poorly to stylized vector content, and reusing them as RL rewards triggers reward hacking. We address both limitations with rubric-based scoring. We first establish empirically that prompting a vision-language judge with a multi-axis rubric correlates with human judgments far better than scalar metrics, both across samples and within instructions. Building on this finding, we introduce RULER (Instance-aware Rubric Rewards for Reinforcement Learning), which converts each instruction into an instance-aware rubric of six items spanning semantic, visual, and stylistic axes; a judge VLM scores rendered rollouts item-by-item, and the weighted satisfactions form a fine-grained reward optimized via Group Relative Policy Optimization. Because the rubric is derived from text alone, RULER requires neither paired SVG ground truth nor human preference labels. On MMSVG-Illustration and MMSVG-Icon, RULER lifts the rubric score from 0.432/0.395 to 0.693/0.683, surpassing dedicated SVG specialists and matching the substantially larger DeepSeek-V3, with ablations identifying rubric design as the active lever for RL on open-ended SVG generation. The project page is available at https://hangyuran.github.io/RULER/.
