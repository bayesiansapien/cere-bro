---
source: farmer/huggingface
farmed: 2026-04-21T00:00:00Z
arxiv_id: "2604.08537"
url: https://huggingface.co/papers/2604.08537
arxiv_url: https://arxiv.org/abs/2604.08537
date: 2026-04-21
---

# Meta-learning In-Context Enables Training-Free Cross Subject Brain Decoding

Visual decoding from brain signals is a key challenge at the intersection of computer vision and neuroscience, requiring methods that bridge neural representations and computational models of vision. A field-wide goal is to achieve generalizable, cross-subject models. A major obstacle towards this goal is the substantial variability in neural representations across individuals, which has so far required training bespoke models or fine-tuning separately for each subject. To address this challenge, we introduce a meta-optimized approach for semantic visual decoding from fMRI that generalizes to novel subjects without any fine-tuning. By simply conditioning on a small set of image-brain activation examples from the new individual, our model rapidly infers their unique neural encoding patterns to facilitate robust and efficient visual decoding. Our approach is explicitly optimized for in-context learning of the new subject's encoding model and performs decoding by hierarchical inference, inverting the encoder. First, for multiple brain regions, we estimate the per-voxel visual response encoder parameters by constructing a context over multiple stimuli and responses. Second, we construct a context consisting of encoder parameters and response values over multiple voxels to perform aggregated functional inversion. We demonstrate strong cross-subject and cross-scanner generalization across diverse visual backbones without retraining or fine-tuning. Moreover, our approach requires neither anatomical alignment nor stimulus overlap. This work is a critical step towards a generalizable foundation model for non-invasive brain decoding. Code and models are publicly available at https://github.com/ezacngm/brainCodec.

**Authors:** Muquan Yu, Weijian Mai, Jacob S. Prince, Hossein Adeli, Rui Zhang, Jiahang Cao, Benjamin Becker, John A. Pyles, Margaret M. Henderson, Chunfeng Song, Nikolaus Kriegeskorte, Michael J. Tarr, Xiaoqing Hu, Andrew F. Luo (University of Hong Kong; Chinese University of Hong Kong; Harvard University; Columbia University; Shanghai Artificial Intelligence Laboratory; Carnegie Mellon University; University of Washington)

**Code:** https://github.com/ezacngm/brainCodec
