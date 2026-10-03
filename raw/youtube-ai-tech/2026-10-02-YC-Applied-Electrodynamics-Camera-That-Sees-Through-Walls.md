# A camera that can see through walls

**Channel:** Y Combinator
**Published:** 2026-10-02
**Source:** https://www.youtube.com/watch?v=Lk_0TviLhnw

## TL;DR
A short YC founder clip. Bilgehan Avser (transcribed as "Bill Abster"), who led antenna work on four iPhone generations, is building WaveSight at Applied Electrodynamics (YC S26): a radio-frequency imager that produces a to-scale 3D point cloud of what sits behind drywall, marble, tile or brick. The enablers he cites are cheap high-frequency MIMO radar chipsets and GPUs fast enough to beamform the echoes in real time. The demo steps through depth planes (wall face, then studs and a junction box, then pipes and cable). Four months full-time, on hardware version three. Signal is moderate: a real product with a credible team, but the clip has no specs, no price and no comparison to existing wall scanners.

## Key Takeaways
- **Physics:** RF passes through common building materials; metal pipes, wiring and studs reflect it. A large antenna array at high frequency, plus time-of-flight processing, gives depth-resolved images rather than a stud-finder beep.
- **Why now:** commodity MIMO radar chipsets (the same class used in automotive mmWave) and GPU compute for real-time image formation.
- **Output is metric 3D.** Pixel measurements match physical dimensions; the company claims 1 mm accuracy.
- **Roadmap:** a handheld that fuses RF imaging with RGB and thermal cameras.
- **Hardware advice:** do not wait for a polished device. Ship revisions fast, find the bottleneck, parallelize paths. They are on v3 after four months.

## Architecture & Optimization Mechanics
The compute story is the relevant part for AI work. A MIMO array with N transmitters and M receivers yields N x M virtual channels, and 3D image formation (back-projection or a range-migration algorithm) is an embarrassingly parallel sum over channels, frequencies and voxels. That is a dense, regular GPU workload, essentially a large batched matrix-vector product per depth slice, which is why it only recently became real-time on a handheld budget. The depth-plane scrolling in the demo is just slicing the reconstructed volume. The obvious next step, which the clip does not mention, is a learned reconstruction or denoising model on top of the raw beamformed volume; through-wall RF imaging literature already uses deep networks to remove wall-induced distortion, and that model would need to run on an edge GPU, making it a classic quantization and distillation target.

## Grounded Context (Web Enrichment)
The company checks out. Applied Electrodynamics was founded in 2026 by Bilgehan Avser, Brian Huppi, Paul Leutheuser and George McLean, a team that has worked together 8+ years and holds 250+ patents; Avser has a PhD in electromagnetics and shipped Apple's first UWB and 5G mmWave phones. WaveSight claims instantly readable, to-scale point clouds at 1 mm accuracy through sheetrock, tile, marble, quartz, brick and insulation. No price has been announced; there is only a preorder list, and target buyers are contractors, industrial inspectors and security teams.

What the clip skips: this is not a new category. Vayyar's Walabot DIY has sold consumer UWB in-wall imaging (6 to 10 GHz) for years, but with 3 antennas, roughly 4 inches of depth and noisy output, so the gap WaveSight targets is resolution and readability, not existence. Regulation is the real risk for a consumer story. FCC Part 15.509 restricts "wall imaging systems" to law enforcement, firefighting, rescue, research, mining and construction users, while Walabot sells broadly by certifying under the handheld UWB rule (15.519). Which rule WaveSight certifies under will decide whether this is a pro tool or a home-renovation gadget, and the founder's own origin story (a remodel gone wrong) is a consumer use case.

Sources: [YC Launch: Applied Electrodynamics](https://www.ycombinator.com/launches/SAN-applied-electrodynamics-a-new-kind-of-camera-that-can-see-through-walls), [YC company page](https://www.ycombinator.com/companies/applied-electrodynamics-inc), [RuntimeWire: WaveSight](https://runtimewire.com/article/applied-electrodynamics-wavesight-see-through-walls), [RuntimeWire: handheld comes next](https://runtimewire.com/article/applied-electrodynamics-wavesight-wall-camera), [Interesting Engineering](https://interestingengineering.com/videos/this-yc-startup-built-a-camera-that-sees-through-walls-heres-how-it-works), [47 CFR 15.509](https://www.law.cornell.edu/cfr/text/47/15.509), [Walabot tech brief](https://cdn.sparkfun.com/assets/learn_tutorials/7/2/4/walabot-tech-brief-416.pdf), [Through-wall radar deep learning (arXiv 2102.07990)](https://arxiv.org/pdf/2102.07990)

## Real-World Application / Actionable Step
- Nothing to change in core work. Bookmark as an example of sensing workloads moving onto edge GPUs, where learned reconstruction models will need aggressive quantization to fit handheld power budgets.
- Personal: if renovating, a pro inspection with RF imaging before opening walls is becoming viable. Wait for WaveSight's FCC class and price before assuming it is a consumer purchase; Walabot DIY 2 is the cheap option today, with low resolution.
- Investment angle is premature: private, pre-revenue, no pricing.
