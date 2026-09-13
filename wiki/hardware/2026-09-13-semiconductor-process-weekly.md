# Semiconductor process weekly: humidity becomes a process-control parameter

**Source:** [Weekly Monitor on Semiconductor Process Research and Manufacturing](https://thesemiconductornewsletter.substack.com/p/weekly-monitor-on-semiconductor-process-327), The Semiconductor Newsletter, 2026-09-12. Eight publications met the technical-relevance threshold. Raw: [`raw/gmail/2026-09-13-starred.md`](../../raw/gmail/2026-09-13-starred.md).

**TL;DR.** An unusually strong week for plasma etching, with three results that each move a variable from "ambient condition" to "thing you have to control." The headline finding: **dry-etched silicon fins with 12 nm spaces bend when relative humidity exceeds roughly 60% at 25°C**, purely from air exposure, no wet step involved. Pattern collapse has always been a wet-clean-and-dry problem. This says nominally dry structures collapse in storage and transit, which turns humidity into a queue-time process parameter for advanced FinFET, gate-all-around and CFET flows. Two other results matter for HBM and advanced interconnect supply: high-aspect-ratio etch necking turns out not to be predictable from mask-loss rate, and ruthenium etching now has a validated combined transport-and-surface-kinetics model.

---

## The three that matter for AI compute supply

**1. Silicon-fin collapse caused by humidity after dry etching.** *J. Vac. Sci. Technol. B*, 8 September, Satake, Ohmori and Kofuji. Fins with 12 nm spaces began bending above approximately 60% relative humidity at 25°C. The effect appears when spacing falls below 15 nm and fin aspect ratio exceeds about 5. The proposed mechanism is capillary condensation between hydrophilic SiN hard masks, where the resulting attractive force exceeds the fins' elastic restoring force.

**Why this is the week's most consequential item.** It relocates a failure mode out of the process tool and into the fab's logistics. The engineering responses named are dry-purge transport, controlled queue-time environments, hydrophobic surface termination, or rapid hard-mask removal, and each of those is a change to *handling* rather than to a recipe. **Yield problems that live between tools are the hardest kind to attribute**, because nothing in the etch or inspection data records the hour the wafer spent in a humid corridor.

**2. Plasma chemistry controls ACL necking during high-aspect-ratio SiO₂ etching.** *J. Phys. D*, 11 September, Wei, Yang and Kwon. Increasing the oxygen-containing C₃F₆O fraction enlarged the amorphous-carbon-layer entrance and moved the neck toward the mask surface; oxygen-free C₃F₆ produced less lateral contraction. At fixed composition, **higher source power reduced the minimum neck critical dimension and moved the constriction deeper**, despite nearly constant ion-acceleration energy. The load-bearing claim: neck position and severity **cannot be described by mask-loss rate alone**, so source power and fluorocarbon oxygen content need optimizing against depth-resolved mask contour rather than against selectivity or bulk plasma density.

**This is directly an HBM and 3D-NAND constraint.** ACL necking restricts reactant and ion transport into high-aspect-ratio contacts and memory structures, which is the etch that gates DRAM capacitor and memory-channel formation. The [compute economics page](compute-economics.md) carries SemiAnalysis's 09-12 disclosure that Nvidia's supply commitments through fiscal 2029 are "primarily memory." **Memory capacity is bounded by exactly this etch**, and the paper says the field has been optimizing it against the wrong observable.

**3. Ruthenium plasma etching, experiment plus model.** *Physics of Plasmas*, 10 September, Amirov et al. A 2D inductively-coupled-plasma fluid model coupled to a zero-dimensional multisite surface model, validated against new experiments in ternary 50% Ar/O₂/Cl₂ plasma and against independent published measurements. Ru is increasingly relevant to advanced interconnects and electrodes, where copper's resistivity scaling has run out, but its low volatility and the competition between oxidation and chlorination make anisotropic removal hard. The model separates transport limitations from surface kinetics and identifies usable O₂/Cl₂ operating windows. Numerical etch rates were not in the accessible abstract.

## The other five, briefly

- **Hydrogen-flow optimization for tin contamination in EUV sources** (*Physics of Fluids*, 10 September, Chen et al.): bulk hydrogen can hold tin mass fraction near EUV mirrors to roughly 10⁻³-10⁻⁵, but poorly configured inlets generate vortices that redirect tin **toward** the optics. Optimizing three inlets cut three vortices to two smaller off-centre ones and lowered modelled mirror contamination below 5 x 10⁻⁶. The useful lesson is counterintuitive and general: **more total flow is not the control variable, inlet momentum distribution and residence-time topology are.** EUV source uptime is a direct input to leading-edge wafer supply.
- **Plasma-enhanced atomic-layer etching review** (*Adv. Mater. Interfaces*, 11 September, open access): organizes PEALE into thermally activated isotropic and low-energy-ion anisotropic modes. Its stance is integration-oriented and worth noting because it is the sober one: **ALE is a finishing and correction step, not a replacement for productive reactive-ion etching.** Hybrid RIE-ALE is the credible high-volume-manufacturing path.
- **Pretreatment-free Al₂O₃ ALD on oxide-bearing 2D materials** (*Nano Express*, 8 September): the same process across inert MoS₂, native-oxide-forming TaS₂ and intrinsically oxidic RuO₂, with MoS₂ showing strongly suppressed nucleation. Relevant to whether 2D-channel devices ever get a manufacturable gate dielectric.
- **Large-area optical-to-AFM hybrid metrology** and **noise-robust wafer-map defect classification** round out the eight. The second is a machine-learning result inside the fab rather than a fab result about machine learning, and it is the quiet direction worth watching.

---

## How this relates to prior wiki pages

**It continues the patterning thread this page opened on 09-06** with [the previous weekly monitor](2026-09-06-semiconductor-patterning-weekly.md). The two issues together make a point neither makes alone: **the leading-edge bottleneck being reported week over week is etch and handling, not lithography.** EUV gets one item out of eight and it is about keeping the mirrors clean rather than about resolution. If you were sizing a constraint on AI compute supply from these newsletters, you would size it on high-aspect-ratio etch control and on wafer handling discipline.

**The humidity result is a new kind of entry for this wiki.** Every supply-constraint item this page carries is either a capacity number (fab starts, HBM lines, packaging slots) or a physics limit (resolution, thermal, bandwidth). This is neither. It is a **latent defect mechanism that would show up in yield data as unexplained variance** and is invisible to every tool log. The analogue on the software side of this wiki is the [prefix-stability argument (09-13)](../inference-efficiency/2026-09-13-prefix-stable-kv-caching-claude-md.md), where a line-ending change costs real money and nothing in the system reports it. Both are cases where the instrument does not exist because nobody thought the variable mattered.

## Gaps

These are abstracts and summaries of peer-reviewed papers, several behind paywalls, with numerical values withheld in at least the ruthenium case. Nothing here has been reproduced across reactors, and the newsletter itself flags that reactor-to-reactor transfer of the ACL necking result requires matching radical ratios, ion flux and mask temperature. The humidity threshold (60% RH, 25°C, sub-15 nm spacing, aspect ratio above 5) is one group's measurement on one geometry.

## Industrial implication

If the humidity mechanism generalizes, the near-term consequence is boring and expensive: controlled-environment handling between etch and downstream processing at the leading edge, which is a capex and cycle-time cost that shows up in wafer price rather than in any published spec. The ACL necking result is the one to watch commercially, because if neck control genuinely requires depth-resolved mask contour metrology rather than mask-loss rate, that is a new inline measurement requirement and therefore a metrology equipment opportunity.

## Related pages

- [Memory hierarchy](memory-hierarchy.md)
- [Compute economics](compute-economics.md)
- [Semiconductor patterning weekly (09-06)](2026-09-06-semiconductor-patterning-weekly.md)
