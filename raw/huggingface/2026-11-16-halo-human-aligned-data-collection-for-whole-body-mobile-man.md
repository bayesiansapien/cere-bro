---
source: farmer/huggingface
farmed: 2026-11-17T08:29:02.001965+00:00
arxiv_id: 2611.16439
url: https://huggingface.co/papers/2611.16439
arxiv_url: https://arxiv.org/abs/2611.16439
date: 2026-11-16
---

# HALO: Human-Aligned Data Collection for WhoLe-body MObile Manipulation

Learning whole-body mobile manipulation requires demonstrations that coordinate bimanual actions with locomotion across extended workspaces. However, existing interfaces trade off direct robot control, perception and action alignment, and natural operator mobility, making such demonstrations difficult to collect. We introduce HALO, a human-aligned data collection system for whole-body mobile manipulation. The system aligns the operator's perception and action space with the robot while preserving direct physical feedback and natural locomotion. Operators guide the robot end-effectors through kinesthetic teaching and move a low-resistance platform without the deployed mobile base while performing bimanual manipulation. This interface enables more natural whole-body demonstrations, but the close human-robot coupling introduces discrepancies between the demonstration and deployment settings. We address these discrepancies with deployment-aligned demonstration processing, which calibrates and temporally aligns platform motion with the deployed base response and masks and inpaints demonstrator hands in recorded observations. Compared with Mobile ALOHA and VR teleoperation, HALO enables up to 2.9x faster demonstration collection while maintaining comparable or higher success rates. Policies trained with HALO perform precise manipulation tasks, including zip-tie fastening, and achieve a 73.3% success rate on a six-stage long-horizon mobile manipulation task involving repeated coordinated base and arm motion. Project page: https://robbyant-research.github.io/Lingbot-ALOHA/
