---
source: farmer/huggingface
farmed: 2026-09-25T17:06:04.306887+00:00
arxiv_id: 2609.27284
url: https://huggingface.co/papers/2609.27284
arxiv_url: https://arxiv.org/abs/2609.27284
date: 2026-09-24
upvotes: 9
authors: ["Tencent Hunyuan Team", "Ao Liu", "Botong Zhou", "Can Xu", "Chayse Zhou", "ChenChen Zhang", "Chengcheng Xu", "Chenhao Wang", "Decheng Wu", "Dengpeng Wu", "Dian Jiao", "Dong Du", "Dong Wang", "Feng Zhang", "Fengzong Lian", "Guanghui Xu", "Guanwei Zhang", "Hai Wang", "Haipeng Luo", "Han Hu", "Huilin Xu", "Jiajia Wu", "Jianchen Zhu", "Jianfeng Yan", "Jiaqi Zhu", "Jihong Zhang", "Jinbao Xue", "Jun Xia", "Junqiang Zheng", "Kai Liu", "Kai Zhang", "Kai Zheng", "Kejiao Li", "Keyao Wang", "Lan Jiang", "Lixin Liu", "Lulu Wu", "Mengyuan Huang", "Peijie Yu", "Peiqi Wang", "Qian Wang", "Qianbiao Xiang", "Qibin Liu", "Qingfeng Sun", "Richard Guo", "Ruobing Xie", "Saiyong Yang", "Shaohua Chen", "Shihui Hu", "Shuai Li", "Shuaipeng Li", "Shuang Chen", "Suncong Zheng", "Tao Yang", "Tian Zhang", "Tinghao Yu", "Weidong Han", "Weijie Liu", "Weijin Zhou", "Weikang Wang", "Wesleye Chen", "Xiao Feng", "Xiaoqin Ren", "Xingwu Sun", "Xiong Kuang", "Xuemeng Huang", "Xun Cao", "Yanfeng Chen", "Yang Du", "Zhen Yang", "Yangyu Tao", "Yaping Deng", "Yi Shen", "Yigeng Hong", "Yiqi Chen"]
---

# Hunyuan-A13B Technical Report

**Authors:** Tencent Hunyuan Team, Ao Liu, Botong Zhou, Can Xu, Chayse Zhou, ChenChen Zhang, Chengcheng Xu, Chenhao Wang, Decheng Wu, Dengpeng Wu, Dian Jiao, Dong Du, Dong Wang, Feng Zhang, Fengzong Lian, Guanghui Xu, Guanwei Zhang, Hai Wang, Haipeng Luo, Han Hu, Huilin Xu, Jiajia Wu, Jianchen Zhu, Jianfeng Yan, Jiaqi Zhu, Jihong Zhang, Jinbao Xue, Jun Xia, Junqiang Zheng, Kai Liu, Kai Zhang, Kai Zheng, Kejiao Li, Keyao Wang, Lan Jiang, Lixin Liu, Lulu Wu, Mengyuan Huang, Peijie Yu, Peiqi Wang, Qian Wang, Qianbiao Xiang, Qibin Liu, Qingfeng Sun, Richard Guo, Ruobing Xie, Saiyong Yang, Shaohua Chen, Shihui Hu, Shuai Li, Shuaipeng Li, Shuang Chen, Suncong Zheng, Tao Yang, Tian Zhang, Tinghao Yu, Weidong Han, Weijie Liu, Weijin Zhou, Weikang Wang, Wesleye Chen, Xiao Feng, Xiaoqin Ren, Xingwu Sun, Xiong Kuang, Xuemeng Huang, Xun Cao, Yanfeng Chen, Yang Du, Zhen Yang, Yangyu Tao, Yaping Deng, Yi Shen, Yigeng Hong, Yiqi Chen

**Upvotes:** 9

**Links:** [HuggingFace](https://huggingface.co/papers/2609.27284) · [arXiv](https://arxiv.org/abs/2609.27284)

We present Hunyuan-A13B, an open-source large language model based on a Mixture-of-Experts architecture. It contains 80 billion total parameters but activates only 13 billion during inference, balancing model capability, computational efficiency, and deployment cost. The model is pretrained on a rigorously filtered 20T-token corpus with enhanced STEM data curation, improving factual reliability and reasoning ability. High-quality supervised fine-tuning and large-scale reinforcement learning further enhance its overall performance. Hunyuan-A13B also introduces a dual-mode Chain-of-Thought framework that adapts reasoning depth to task complexity: fast thinking for routine queries and slow thinking for complex, multi-step problems. Evaluations show competitive performance across mathematics, science, programming, general language understanding, and agent tasks, often approaching that of much larger models. Its high inference throughput makes it suitable for latency-sensitive applications. We release Hunyuan-A13B to support open research and practical LLM deployment.
