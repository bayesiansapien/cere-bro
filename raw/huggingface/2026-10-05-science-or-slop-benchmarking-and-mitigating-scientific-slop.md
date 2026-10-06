---
source: farmer/huggingface
farmed: 2026-10-06T11:30:06.338949+05:30
arxiv_id: 2610.00531
url: https://huggingface.co/papers/2610.00531
arxiv_url: https://arxiv.org/abs/2610.00531
date: 2026-10-05
---

# Science or Slop?: Benchmarking and Mitigating Scientific Slop in AI-Generated Papers

AI-generated content, often called AI slop, is increasingly common everywhere, particularly in academia. Slop in AI-generated scientific papers, however, has more complex patterns that cannot be easily detected by existing token-based AI detectors. Each part of such a paper looks plausible while the scientific reasoning that connects the parts breaks down, which can mislead how readers assess the work. We benchmark these failures as scientific slop through six measures across Structure, Argument, and Artifacts. We construct SciSlopBench with 390 AI-generated papers, mostly in computer science but spanning the life, social, and natural sciences, each paired with a human-written paper matched by research problem and contribution type. Our measures identify the AI paper in each pair with 85.9% accuracy, compared with 68.7% for Binoculars. Higher scientific slop accompanies lower ICLR ratings and distinguishes rejected from accepted papers above chance in every year from 2017 to 2025. Reducing these patterns, however, is not as simple as directly optimizing the measures. We therefore propose SciSlopHarness, a harness-level framework that guides a fixed LLM to revise slop only where the experiment records support the change. While standard revisions leave residual slop and direct slop-aware prompting triggers reward hacking, SciSlopHarness reduces the remaining AI-human gap by 63% over the strongest revision baseline without requiring human reference targets. Overall, we demonstrate that AI-generated scientific papers leave fundamental traces in their global reasoning, and that responsible mitigation demands strict evidentiary grounding rather than mere prose refinement.
