---
source: farmer/huggingface
farmed: 2026-08-10T09:04:01.722687
arxiv_id: 2608.07051
url: https://huggingface.co/papers/2608.07051
arxiv_url: https://arxiv.org/abs/2608.07051
date: 2026-08-10
---

# YOLO-PEFT: Parameter-Efficient Fine-Tuning on YOLO Family

Generic parameter-efficient fine-tuning (PEFT) methods transferred from language models can fail silently on real-time detectors, whose heterogeneous operators and detection-specific components impose placement constraints absent from regular Transformer stacks. We propose YOLO-PEFT, a structure-aware framework that formulates adapter placement as an auditable constraint-planning problem. Given a detector graph, a PEFT request, and a resource budget, YOLO-PEFT assigns operator and semantic roles, evaluates explicit operator-validity, detector-semantic, graph-interface, and deployment predicates, records a reason code for each excluded module, and either emits a budgeted target-module plan or returns Refuse before training. Under the official VOC07+12 trainval-to-VOC07 test protocol, planner-selected RS-LoRA reaches 0.7138 and 0.7307 mAP50-95 on YOLO11s and YOLO12s, respectively, compared with 0.6428 and 0.6662 for Full-SFT. On RT-DETR-L, all seven evaluated LoRA-family configurations cross the predefined catastrophic threshold, supporting a calibrated Refuse-to-Full-SFT decision within the evaluated coverage. A controlled YOLO11 audit further shows that LoRA reduces peak training memory by 43.9 percent, although training takes 1.72 times longer. Within the evaluated detector families, placement policies, and calibration coverage, YOLO-PEFT replaces manual target-module trial and error with explicit, inspectable planning while preserving verified train-save-merge-export paths; refusal on unseen detector architectures remains an open validation problem. Project Page: github.com/Tencent/YOLO-Master
