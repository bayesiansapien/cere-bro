---
source: farmer/huggingface
farmed: 2026-10-13T10:40:18.215979+05:30
arxiv_id: 2610.12611
url: https://huggingface.co/papers/2610.12611
arxiv_url: https://arxiv.org/abs/2610.12611
date: 2026-10-12
---

# SoftwareGym: Scaling Computer-Use Agent Training with Diverse Synthesized Software Environments

Computer-use agents (CUAs) are rapidly improving, yet synthesizing diverse and reliable software environments at scale remains challenging. Native application environments require substantial construction and integration effort, which limits application coverage and increases the risk of application-specific overfitting. Browser-hosted environments provide limited interaction depth and workflow complexity. These limitations motivate SoftwareGym, an automated pipeline for synthesizing GUI software environments with diverse interfaces, executable functionality, and runtime-verified behavior. It generates structurally diverse designs, realizes them as runnable applications, and uses GUI evaluation with iterative repair to ensure functional reliability. Using SoftwareGym, we synthesize 182 applications across twelve categories and achieve a mean GUI task pass rate of 91.5%. We construct SoftwareGym-Bench, a 120-task evaluation suite spanning the same twelve categories, and use trajectories collected from these environments for CUA training. The resulting model improves Pass@3 from 41.39% to 56.97% on the strictly out-of-domain OSWorld benchmark and achieves 40.0% on SoftwareGym-Bench. These results demonstrate the potential of synthesized software environments as scalable and transferable supervision for CUA training.
