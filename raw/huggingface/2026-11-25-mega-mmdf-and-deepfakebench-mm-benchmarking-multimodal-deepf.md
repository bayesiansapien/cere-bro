---
source: farmer/huggingface
farmed: 2026-11-26T10:35:42+05:30
arxiv_id: 2510.22622
url: https://huggingface.co/papers/2510.22622
arxiv_url: https://arxiv.org/abs/2510.22622
date: 2026-11-25
---

# Mega-MMDF and DeepfakeBench-MM: Benchmarking Multimodal Deepfake Detection Across Diverse Forgery Pipelines

Audio-visual deepfakes can spread misinformation and enable impersonation, undermining trust in digital media. However, existing datasets provide limited coverage of forgery operations and their combinations, constraining detector development and systematic evaluation. We introduce Mega-MMDF, containing 100,000 real and 1.2 million forged clips across 22 pipelines spanning modality-specific manipulations, stacked forgeries, and joint audio-video generation. To assess its training value and enable fair comparisons, we develop DeepfakeBench-MM, which standardizes training and evaluation across 8 datasets and 10 detectors. Training-based detectors achieve their highest mean AUC when trained on Mega-MMDF, with gains of up to 0.0784 over the best alternative training dataset for each detector. Experiments on data scale and pipeline coverage further support the value of large, diverse training data. Cross-pipeline evaluations reveal bidirectional and asymmetric generalization. Training on composite forgeries does not necessarily enable detection of their constituent operations in isolation. Our analysis of altered inputs shows that modality masking can increase false alarms and missed detections, and temporal misalignment can raise mean predicted forgery probabilities. Together, these resources provide a foundation for understanding and improving multimodal deepfake detection, with publicly available code and dataset access subject to application and usage terms.
