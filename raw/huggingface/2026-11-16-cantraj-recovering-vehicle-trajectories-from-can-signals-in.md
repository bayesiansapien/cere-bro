---
source: farmer/huggingface
farmed: 2026-11-17T08:29:02.000186+00:00
arxiv_id: 2611.18442
url: https://huggingface.co/papers/2611.18442
arxiv_url: https://arxiv.org/abs/2611.18442
date: 2026-11-16
---

# CANTraj: Recovering Vehicle Trajectories from CAN Signals in Naturalistic Driving

Open driving releases and usage-based insurance programs often claim to prevent privacy breaches by omitting GPS records when sharing or collecting vehicle data. However, removing GPS coordinates from driving logs does not erase the location information carried by vehicle signals. While prior route-inference attacks have demonstrated that speed, steering, and driving events can be matched to road networks to reconstruct trajectories, existing studies rely on inconsistent prior assumptions and evaluation metrics and are tested only on small, restricted datasets, making their results difficult to compare and their real-world effectiveness uncertain. We release CANTraj, a naturalistic driving dataset pairing decoded CAN events with time-aligned GNSS trajectories (3,940 drives, 454 drivers), and CANTraj-Bench for evaluating trajectory recovery (3,675 drives, 431 drivers, 1,380 hours, 85,919 km). On 776 evaluation drives from 94 unseen drivers, we compare six re-implemented attacks and benchmark baselines under explicit information-access protocols, paired comparisons, and metrics incorporating failures. Experiments show that combining steering signals with road-network constraints yields the largest gain: With a known start and heading, adding steering to speed raises the online map filter's five-minute route recovery from 56% to 87%, with a median average displacement error of 43 m versus 921 m for map-free dead reckoning. Offline beam search recovers 88% of test routes with the heading and 81% without it. Because methods fail on different windows, we also evaluate an LLM harness that selects among candidate routes on 659 five-minute windows; its best configuration recovers 79% of routes on test and 83% on few-shot, outperforming the best baseline on test and matching it on few-shot. Data and code at huggingface.co/datasets/HenryYHW/CANTraj and github.com/WangYuHang-cmd/GPS--CAN.
