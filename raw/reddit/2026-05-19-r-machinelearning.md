# r/MachineLearning | 2026-05-19 IST | sort=top
> Scraped 2026-05-19 10:32 IST | lookback=24h | tier_default=2
> Filter to [R]/[P]/Research/Project flair only — drops the [D] discussion noise. Generic news is excluded.

### Reviving PapersWithCode (by Hugging Face) [P]

**Meta:** score=266 · comments=20 · tier=2 · flair=Research · posted=2026-05-18 13:37Z
**Author:** u/NielsRogge
**Reddit:** [https://www.reddit.com/r/MachineLearning/comments/1tgmwqr/reviving_paperswithcode_by_hugging_face_p/](https://www.reddit.com/r/MachineLearning/comments/1tgmwqr/reviving_paperswithcode_by_hugging_face_p/)

Hi,

Niels here from the open-source team at Hugging Face. Like many others, I was a huge fan of paperswithcode. Sadly, that website is no longer maintained after its acquisition by Meta.

Hence, I've been working on reviving it. I obviously use AI agents to parse papers at scale and automatically generate leaderboards (for now I'm the one verifying results). So far, I've only parsed high-impact papers for which I know they're SOTA, like Qwen 3.5 and 3.6, RF-DETR for object detection, DINOv3, SOTA embedding models from the MTEB leaderboard, the Open ASR Leaderboard for automatic speech recognition models, etc.

For now, it includes the following:

* trending papers by default based on Github star velocity
* categorization by domain, e.g., [OCR](https://paperswithcode.co/tasks/ocr)
* [methods](https://paperswithcode.co/methods), which PwC used to have, e.g., [RLVR](https://paperswithcode.co/methods/rlvr)
* eval results for high-impact papers, see e.g., [Qwen 3.5](https://paperswithcode.co/paper/83017) at the bottom
* leaderboards for each domain, e.g., [MMTEB](https://paperswithcode.co/benchmark/mmteb) or [COCO val 2017](https://paperswithcode.co/benchmark/coco-val2017)
* support for [citation counts](https://paperswithcode.co/?order_by=citation_count) (you can also see the most cited papers by domain!)
* automated linked Github, project page URLs, and artifacts (+ multiple repos are supported on a paper page)
* support for external papers beyond Arxiv, see e.g., [DeepSeek v4]

[…truncated, see permalink]

---

### Sub-JEPA: a simple fix to LeCun group's LeWorldModel that consistently improves performance [P]

**Meta:** score=57 · comments=14 · tier=2 · flair=Project · posted=2026-05-18 13:44Z
**Author:** u/kai-zhao
**Reddit:** [https://www.reddit.com/r/MachineLearning/comments/1tgn3bz/subjepa_a_simple_fix_to_lecun_groups_leworldmodel/](https://www.reddit.com/r/MachineLearning/comments/1tgn3bz/subjepa_a_simple_fix_to_lecun_groups_leworldmodel/)

**World models** learn compact latent representations for planning without pixel reconstruction. LeWorldModel (LeWM), from LeCun's group at NYU, achieves stable end-to-end JEPA training by enforcing an isotropic Gaussian prior over the full latent space.

**The flaw:** real environment dynamics live on low-dimensional manifolds, so a global high-dimensional Gaussian is an overly rigid prior — mismatched to the task geometry. LeWM itself struggles most on low-intrinsic-dimension tasks like Two-Room.

**Our fix (Sub-JEPA):** apply the Gaussian regularization inside multiple frozen random orthogonal subspaces instead. This relaxes the global constraint while keeping the anti-collapse benefit. No new hyperparameters, same two-term objective.

Sub-JEPA consistently outperforms LeWM across all four benchmarks, with up to +10.7 pp on Two-Room. We also observe straighter latent trajectories and better physical state decodability as emergent benefits.

![](https://kaizhao.net/images/projects/sub-jepa/overview.png)

![](https://kaizhao.net/images/projects/sub-jepa/cube.gif)


🌐 Project: [https://kaizhao.net/sub-jepa](https://kaizhao.net/sub-jepa)

💻 Code: [https://github.com/intcomp/sub-jepa](https://github.com/intcomp/sub-jepa)

📄 Paper: [https://arxiv.org/pdf/2605.09241](https://arxiv.org/pdf/2605.09241)

---
