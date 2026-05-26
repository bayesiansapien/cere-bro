---
source: farmer/huggingface
farmed: 2026-05-26T06:42:03Z
arxiv_id: 2605.26095
url: https://huggingface.co/papers/2605.26095
arxiv_url: https://arxiv.org/abs/2605.26095
date: 2026-05-26
---

# Pixel-Level Pavement Distress Assessment Using Instance Segmentation

Automated pavement distress assessment requires more than image-level classification or coarse bounding box detection, demanding precise localization of thin, branching, and irregular cracks to achieve the geometric precision necessary for maintenance-relevant quantification. This paper presents a vision-based pavement distress analysis system based on Mask R-CNN instance segmentation and evaluates it on UWGB-StreetCrack, a custom field-collected roadway image dataset acquired with a vehicle-mounted smartphone and manually annotated with polygon labels for longitudinal cracks, transverse cracks, alligator cracks, and potholes. Five Detectron2-based Mask R-CNN backbone variants were considered under a consistent fine-tuning protocol. The best-performing model, Mask R-CNN with a ResNet-101 FPN backbone, achieved 84.23% precision, 90.04% recall, and an F1 score of 87.04% under the project-specific bounding-box matching protocol. The same model produced an aggregate predicted crack-area fraction of 2.164%, closely matching the 2.170% ground-truth crack-area fraction. To contextualize the segmentation system against a detector-oriented alternative, a CSPDarknet53-based YOLO detector was also adapted and retrained on the dataset, reaching 27.5% precision and 20.7% recall on the validation protocol. The results show that instance segmentation is a practical direction for field pavement imagery and aggregate crack-area estimation, while also exposing open challenges in annotation consistency, class imbalance, confounder rejection, and mask-level benchmarking.
