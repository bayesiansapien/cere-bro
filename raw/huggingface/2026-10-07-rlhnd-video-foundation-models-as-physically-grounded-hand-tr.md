---
source: farmer/huggingface
farmed: 2026-10-08T11:34:10+05:30
arxiv_id: 2610.09455
url: https://huggingface.co/papers/2610.09455
arxiv_url: https://arxiv.org/abs/2610.09455
date: 2026-10-07
---

# RLHND: Video Foundation Models as Physically Grounded Hand Trackers for Robot Learning

Recently, approaches that leverage human video datasets for robot policy training have become increasingly prevalent. However, most existing hand trackers regress pose from cropped frames with limited priors on hand motion and object interaction, resulting in inaccurate and physically inconsistent estimates. Moreover, the lack of physical cues, e.g., contact and force, limits the use of human videos for robot policy training. To this end, we propose RLHND, a video foundation model-based hand tracking model that jointly estimates hand pose and realistic tactile information from monocular egocentric videos. RLHND turns the pre-trained Cosmos 3 video diffusion backbone into a deterministic clip-level feature extractor via clean-latent conditioning, carrying its learned priors on hand motion and hand-object interaction into tracking. For pose estimation, RLHND (i) predicts hand poses with anatomically plausible joint angles and (ii) enables optional conditioning on the shape parameter to maintain consistent hand shape within the same video and even across videos recorded by the same actor. For tactile estimation, a separate tactile expert stream, trained with the pose stream frozen, predicts dense contact and force over the hand surface. We further adopt LBS-based feature spreading to enable vertex-wise feature extraction without costly per-vertex attention. RLHND achieves state-of-the-art performance across various benchmark datasets for pose estimation, while also achieving state-of-the-art performance in contact and force estimation. Moreover, we demonstrate the utility of RLHND for robot learning through retargeting results and real-world robot experiments. The code will be publicly available at https://seungjun-moon.github.io/rlhnd/.
