---
source: farmer/huggingface
farmed: 2026-09-25T17:06:04.306887+00:00
arxiv_id: 2609.24308
url: https://huggingface.co/papers/2609.24308
arxiv_url: https://arxiv.org/abs/2609.24308
date: 2026-09-24
upvotes: 40
authors: ["Zhiqi Bai", "Junai Cai", "Yixin Chen", "Jingrun Du", "Tao Feng", "Wei Gong", "Siyuan Huang", "Xiao Lin", "Jiaheng Liu", "Jun Luo", "Yongzhe Lyu", "Liya Ma", "Zenan Meng", "Lin Qu", "Wenbo Su", "Jiaming Wang", "Qinghe Wang", "Shaofei Wang", "Yanghai Wang", "Zequn Wang", "Ziming Wang", "Hu Wei", "Jiangtao Wu", "Ruiqi Wu", "Jiaxin Xie", "Yuchi Xu", "Ze Xu", "Chengting Yu", "Liangyu Yuan", "Gang Zeng", "Yawen Zeng", "Xingyao Zhang", "Zizheng Zhang", "Bo Zheng", "Jiancheng Zhu", "Song-Chun Zhu"]
---

# HappyWorld-Bench

**Authors:** Zhiqi Bai, Junai Cai, Yixin Chen, Jingrun Du, Tao Feng, Wei Gong, Siyuan Huang, Xiao Lin, Jiaheng Liu, Jun Luo, Yongzhe Lyu, Liya Ma, Zenan Meng, Lin Qu, Wenbo Su, Jiaming Wang, Qinghe Wang, Shaofei Wang, Yanghai Wang, Zequn Wang, Ziming Wang, Hu Wei, Jiangtao Wu, Ruiqi Wu, Jiaxin Xie, Yuchi Xu, Ze Xu, Chengting Yu, Liangyu Yuan, Gang Zeng, Yawen Zeng, Xingyao Zhang, Zizheng Zhang, Bo Zheng, Jiancheng Zhu, Song-Chun Zhu

**Upvotes:** 40

**Links:** [HuggingFace](https://huggingface.co/papers/2609.24308) · [arXiv](https://arxiv.org/abs/2609.24308)

Evaluating world models requires assessing both the quality of the worlds they generate and their consistency and responsiveness under exploration, interaction, and modification. We introduce HappyWorld-Bench, a comprehensive benchmark that evaluates whether generated worlds remain reliable as agents interact with them. Our design is built on a hierarchical capability framework of six world capabilities (W1-W6), from generative construction to unified world modeling, instantiated across three independent evaluation tracks: video world models, spatial world models, and embodied world models. HappyWorld-Bench comprises 1,138 video prompts, 300 spatial scenes, and 254 embodied test cases. Across all three tracks, we build and operate HappyWorld-Arena to organize human A/B comparisons and derive model-level Elo ratings, which complement newly designed automated metrics that capture behavioral correctness. We evaluate 14 video world models, 9 spatial systems, and 8 embodied candidates under this unified framework. Results reveal remaining reliability gaps across all three tracks: video models exhibit reduced consistency during extended rollouts and revisits, spatial models achieve at best 70.14% placement accuracy and 73.33% edit execution, and embodied models struggle to preserve state across multi-step actions and respond precisely to altered action conditions and physical rules. These findings highlight the need to evaluate world models not only by visual quality, but also by state consistency and the correctness of their responses to actions and interventions.
