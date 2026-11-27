---
source: farmer/huggingface
farmed: 2026-11-27T05:29:19.905784+00:00
arxiv_id: 2611.33925
url: https://huggingface.co/papers/2611.33925
arxiv_url: https://arxiv.org/abs/2611.33925
date: 2026-11-26
---

# Beyond the Happy Path: Generalizing Robot World Models from Simulated Failures

Robot world models are increasingly used to evaluate and plan policies, yet robot training data are dominated by successful demonstrations. Off the happy path, when a grasp is misaligned or mistimed and the object is pushed, tilted, or slips, their predictions break down. Across five pretrained action-conditioned models, object-motion error is at most 10.4% lower than that of a static baseline that copies the first frame, and two models are worse than this baseline. We present WorldReforge, which teaches world models what happens when manipulation goes wrong. We construct the Reforge dataset of 62k simulated trajectories by perturbing reference grasps in position, orientation, and closure timing, recording each resulting push, slip, or failed pickup with ground-truth object pose, contact, and surface points. WorldReforge turns this ground truth into two training signals without additional inference cost. Interaction Alignment focuses reconstruction on the small object and contact regions that a global loss underweights, and Surface Correspondence trains backbone features to follow the same physical surface points across frames. On Cosmos3 Nano, WorldReforge reduces object trajectory error by 28.2% overall and by 35.0% on unseen objects, and it lowers the error in predicting how two actions' outcomes diverge by 43.3%. Although trained only in simulation, it also improves reconstruction on DROID and on real failure videos. Controlled data studies show that failed contact and successful holding teach complementary physics: failed contact teaches how objects respond, and holding teaches how a grasped state persists. Our code, data, and models are available at aim-uofa.github.io/WorldReforge/.
