---
source: farmer/huggingface
farmed: 2026-11-14T05:10:36.531859+00:00
arxiv_id: 2611.00428
url: https://huggingface.co/papers/2611.00428
arxiv_url: https://arxiv.org/abs/2611.00428
date: 2026-11-13
---

# Do Multimodal Models Decide Consistently on Equivalent Optical Spectra?

A spectrum can be given to a model as a table in nanometers or as a plot in photon energy, and the decision should not depend on which one it sees. When the data needed for an answer are missing, the model should say so. We test representation invariance and abstention on measured optical spectra of silicon metasurfaces (MOCLIP) and gold nanoparticles, with labels computed from the data. Each spectrum is shown as four tables (nm, μm, scientific notation, eV) and two plots (nm, eV), and partial spectra remove data inside or outside the queried range. We evaluate the decision models d3-nano and Jev 1.13, three GPT-6 Luna configurations and the Qwen3.5-2B base model. Changing only the representation moves accuracy by up to 41 percentage points within one model, mostly on photon-energy tables and plots. With the same evidence, asking in photon energy instead of wavelength helps some model-view pairs by 16-50 points and hurts others by up to 25. When the relevant extremum is removed, unadapted models rarely answer "undetermined". LoRA fine-tuning of d3-nano improves comparisons on the trained table formats, but much of its gain on unanswerable questions comes from a shortcut: it abstains whenever the input is truncated. Training with answerable truncations avoids the shortcut in all six seeds, with a 90-100 point gap between abstention after inside and outside cuts on held-out structures; with the same amount of extra original-task data, five of six seeds keep the shortcut. On gold spectra the two training sets perform similarly. Multimodal language models used for scientific decisions should be tested on equivalent representations and on missing evidence, not only on average accuracy. We release the tasks, per-response results and analysis code.
