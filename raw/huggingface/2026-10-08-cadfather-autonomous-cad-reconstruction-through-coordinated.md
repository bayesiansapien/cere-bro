---
source: farmer/huggingface
farmed: 2026-10-09T11:51:45.308358+05:30
arxiv_id: 2610.09127
url: https://huggingface.co/papers/2610.09127
arxiv_url: https://arxiv.org/abs/2610.09127
date: 2026-10-08
---

# CADFather: Autonomous CAD Reconstruction through Coordinated Tool Use

Reconstructing an editable CAD model from a 3D shape remains a challenging engineering task. Existing methods can propose CAD operations, but no single source of proposals works equally well across different part geometries and stages of reconstruction. We introduce CADFather, an autonomous agentic system that coordinates complementary tools to recover parametric CAD programs from 3D meshes. A vision-language assistant inspects renders of the target and intermediate reconstructions, then decides which candidate CAD programs to extend, which tools to invoke, how many proposals to generate, and when to finish. Learned and algorithmic tools propose CAD operations, while numerical optimization refines the parameters of existing programs. Proposed or refined programs are executed and evaluated to provide feedback for subsequent decisions. The agent maintains alternative candidate programs for each target part and preserves the best valid result throughout reconstruction. CADFather uses pretrained generation and assistant models without additional training. We evaluate reconstruction quality and execution validity on the full DeepCAD, Fusion360, and MCB test sets, as well as on CADENA-Bench, CADBench, and BenchCAD. We additionally analyze computational cost and the trade-off between cost and reconstruction quality.
