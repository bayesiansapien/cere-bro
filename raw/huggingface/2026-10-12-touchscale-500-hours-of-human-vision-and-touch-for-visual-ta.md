---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.222257+05:30
arxiv_id: 2610.10288
url: https://huggingface.co/papers/2610.10288
arxiv_url: https://arxiv.org/abs/2610.10288
date: 2026-10-12
---

# TouchScale: 500 Hours of Human Vision and Touch for Visual-Tactile Learning

Large-scale egocentric human interaction data is becoming an important source of physical supervision for embodied learning, yet video alone leaves the contact and pressure that characterize physical interaction unrecorded. Recent visual-tactile datasets provide this missing supervision, but their synchronized tactile data remain far smaller in volume than human video. Moreover, the largest resources often merge recordings from different sensors or annotation procedures, which makes the effect of data scale difficult to isolate. We therefore introduce TouchScale, a 500-hour dataset of contact-rich human interaction recorded with a single unified wearable setup. Its approximately 2K predefined task descriptions span everyday activities and structured manipulation, and each recording temporally aligns egocentric RGB-D video with wrist RGB video and dense full-hand bimanual tactile measurements. Compared with prior tactile data, training on the full TouchScale raises zero-shot contact IoU on data from an unseen tactile sensor from 0.134 to 0.383. Pretraining a visual encoder on TouchScale also yields the highest action recognition accuracy on three benchmarks among the compared visual-tactile datasets. Used for visual-tactile mid-training of a robot policy, TouchScale improves the average real-world success rate across four contact-rich manipulation tasks from 22.5% to 57.5%. With the sensor and collection protocol held fixed, both zero-shot tactile prediction and robot success show an overall upward trend as more TouchScale data is used. These results suggest that human visual-tactile data collected at scale with consistent sensing benefits both perception and robot manipulation. We will publicly release TouchScale, including all synchronized visual-tactile recordings and reconstructed object models, to support future research on scalable visual-tactile learning.
