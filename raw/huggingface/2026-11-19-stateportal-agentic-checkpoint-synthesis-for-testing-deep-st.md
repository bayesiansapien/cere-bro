---
source: farmer/huggingface
farmed: 2026-11-20T05:04:58.142626+00:00
arxiv_id: 2611.23257
url: https://huggingface.co/papers/2611.23257
arxiv_url: https://arxiv.org/abs/2611.23257
date: 2026-11-19
---

# StatePortal: Agentic Checkpoint Synthesis for Testing Deep States in Interactive Software

Large language models have reduced the effort to generate code for interactive software with graphical user interfaces (GUIs). For such software, a key testing bottleneck is reaching a deep state, one that requires a long interaction history. The cost of reaching it recurs across commits, and the GUI automation that could amortize it assumes a DOM or accessibility tree that self-rendered engines do not expose. We introduce StatePortal, an agent that synthesizes a checkpoint, an artifact that restores that state and can be versioned and replayed, from a natural-language functional test case and read-only access to the target's source code. The checkpoint is restored through a per-application hook that an onboarding agent binds or synthesizes once without hand-written hook code. Because a checkpoint can satisfy state checks while rendering incorrectly, checkpoints are scored by hybrid programmatic-state and visual evaluation: acceptance requires both a programmatic-state oracle and a visual oracle to pass. We calibrate the visual oracle against a blinded cross-VLM reference. We release DeepStateBench, 61 deep-state tasks across 10 interactive applications that span five language families and six rendering stacks, with source sizes from 874 to 7.2M lines. Across three registered models, a GUI agent seeded with synthesized checkpoints completes 10.4% of trials, compared with 0% without seeding under the same pixel action space, while StatePortal, which also delivers the target action through the hook, completes 27.5%. Over 1,361 replays of 112 checkpoints, 98.90% reproduce the original verdict with zero model calls, and the hybrid oracle detects 96.25% (77/80) of controlled visual faults invisible to programmatic-state checks alone. We open-source our code at https://github.com/pzy2000/State_Portal and website at https://stateportal.mineyosemite.chatgpt.site
