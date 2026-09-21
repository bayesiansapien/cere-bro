# Semiconductor process weekly: wafer-scale monolithic 3D, and three process wins that are cost stories

**Date:** 2026-09-20
**Topic:** hardware
**Source:** The Semiconductor Newsletter, *Weekly Monitor on Semiconductor Process Research and Manufacturing*
**Link:** [thesemiconductornewsletter.substack.com](https://thesemiconductornewsletter.substack.com/p/weekly-monitor-on-semiconductor-process-6ec)
**Raw:** `raw/gmail/2026-09-20-starred.md`

---

## TL;DR

Nine publications cleared the newsletter's technical-relevance screen this week. One is a genuine
scale-up result and the rest are process wins worth knowing about. No new standards or roadmap
updates passed.

**The headline: monolithic 3D integration of ALD oxide semiconductors on 200mm wafers** (Chang Niu
et al., *Nature Nanotechnology*, 15 September). Three tiers of atomic-layer-deposited indium-oxide
transistors stacked monolithically on 200mm silicon, **more than 100,000 devices fabricated**,
spanning ferroelectric, enhancement-mode and depletion-mode FETs. Threshold-voltage standard
deviation of **0.04 V** and average mobility as high as **91.6 cm²/V·s**. Cross-tier circuits worked.
A four-tier compute-in-memory accelerator designed against a custom InOx process design kit
delivered **modeled 1.4 to 2.9x speed improvements** with comparable energy-delay-product gains over
2D baselines.

---

## Why the M3D result matters to a reader who cares about inference cost

Monolithic 3D (M3D) means building device tiers sequentially on top of one another on the same wafer,
as opposed to fabricating dies separately and bonding them. Oxide-semiconductor M3D has existed as
isolated low-temperature device demonstrations for years. This is the first time it arrives with
**wafer-scale statistics, PDK support and working multilayer circuits**, which is the difference
between a physics result and something a design team could target.

The connection to everything on [the memory hierarchy page](memory-hierarchy.md) is the
compute-in-memory accelerator. [The 09-18 KV cache entry](../inference-efficiency/kv-cache.md)
recorded SemiAnalysis reporting NVIDIA despec'ing Rubin Ultra from 1024 GB to roughly 200 GB of HBM
per chip, and this wiki's read was that the cut converts cache compression from an optimisation into
an admission criterion. [Today's decode-inversion
entry](../inference-efficiency/2026-09-20-test-time-compute-decode-inversion.md) supplies the demand
side: decode runs at 1.0 to 2.5 FLOPs per byte, so the memory bus is the machine, and one 64k-token
reasoning request wants 18 GB. **Both halves of that squeeze are about the distance between compute
and memory.** Sequential integration above silicon logic is the structural answer to that distance,
and a 1.4 to 2.9x modeled gain is what the answer is currently worth. The word doing the work is
"modeled."

The newsletter's own engineering caveats are the right ones and worth carrying: cumulative thermal
exposure across tiers, inter-tier alignment, contact resistance, device drift, bias-stress
reliability, particle adders, and yield loss that compounds multiplicatively with tier count. A
three-tier process at 99% per-tier yield is a 97% process; at eight tiers the arithmetic stops being
friendly.

---

## The other eight, compressed

- **Low-GWP fluorocarbons for SiO₂ plasma etch** (*ECS JSS*, 15 Sept). C₄F₈O and C₅F₁₀O, with global
  warming potentials near or below 1, approach the etch performance of CHF₃, whose GWP is **14,600**.
  XPS showed steady-state fluorocarbon films under 4 Å for all gases, so the rate differences track
  radical populations rather than passivation thickness. This is a regulatory-cost story: fab
  emissions liability is a real line item and a drop-in replacement at 1/14,600th the GWP is worth
  a lot before it is worth anything technically.
- **Tone-switchable Sn-based MLD dry resist** (*ACS AMI*, 18 Sept). One molecular-layer-deposited
  resist that goes positive under ammonia wet development and negative under fluorine ICP dry
  development. Resolved a **7nm single line under 50-keV e-beam** and **18nm under EUV**. Note the
  gap between the title's "sub-7nm" language and the 18nm EUV number, which the newsletter flags
  honestly.
- **Dilute-HF pretreatment for wafer defect imaging** (*Semicond. Sci. Technol.*, open access, 14
  Sept). A brief HF dip before photoluminescence imaging makes sub-micron scratches visible;
  untreated imaging can miss microcracks extending ~150 µm deep. Timing also allows depth estimation.
  Nondestructive incoming inspection without Wright etching's material removal.
- **Nitrogen-plasma activation for low-temperature SiO₂ wafer bonding** (*Langmuir*, 16 Sept).
  Moderate N₂ exposure optimises bond strength; excess exposure causes reconstruction that hurts it.
  Directly relevant to the hybrid-bonding step that HBM stacking depends on.
- **Separating EUV emission from tin-ion debris via laser incidence angle.** Source lifetime and
  uptime economics.
- **PEALD Ga₂O₃ at 7.17 MV/cm intrinsic breakdown field.** Wide-bandgap power devices, which is the
  power-delivery side of datacenter economics.
- **Dual-task learning for imbalanced wafer-map defect classification** and **AI-enabled CVD
  manufacturing of 2D materials.** Both are ML-in-the-fab items rather than ML-from-the-fab, and both
  are the kind of yield-engineering work that never shows up in AI coverage despite being where a lot
  of the industry's actual machine learning runs.

---

## Relation to prior wiki pages

**Extends** [the memory hierarchy page](memory-hierarchy.md) with the first wafer-scale M3D datapoint
it carries. Prior entries there treat the memory-to-compute distance as fixed by packaging choices;
sequential integration is a different lever and the page had no instance of it.

**Confirms the direction in** [compute economics](compute-economics.md): three of the nine items
(low-GWP etch gases, EUV source debris, wafer-bonding activation) are cost and uptime results rather
than capability results. The fab-side story this quarter is margin, not nodes.

---

## Related pages

- [Memory hierarchy](memory-hierarchy.md)
- [Compute economics](compute-economics.md)
- [GPU kernels](gpu-kernels.md)
- [KV cache](../inference-efficiency/kv-cache.md)
- [The decode inversion (09-20)](../inference-efficiency/2026-09-20-test-time-compute-decode-inversion.md)
