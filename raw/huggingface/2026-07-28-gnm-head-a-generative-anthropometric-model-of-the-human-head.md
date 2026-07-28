---
source: farmer/huggingface
farmed: 2026-07-28T09:26:01.339781
arxiv_id: 2607.23687
url: https://huggingface.co/papers/2607.23687
arxiv_url: https://arxiv.org/abs/2607.23687
date: 2026-07-28
---

# GNM Head: A Generative aNthropometric Model of the human head

Parametric models of the human head are essential tools traditionally used in computer vision and graphics for animation, rendering, and reconstruction. More recently, they serve as crucial conditioning signals within generative large vision models, allowing for tight spatial control of generated imagery. However, existing publicly available models are typically limited in anatomical scope, modeling only outer geometry while ignoring intra-oral and ocular structures, and frequently suffer from reduced geometric quality stemming from low-fidelity input datasets. In this report we introduce a new parametric model dubbed Generative aNthropometric Model (GNM), named as a homophone of the human genome. GNM encompasses the head, face, neck, eyeballs, teeth, and tongue, and it is built on an extensive database of high-resolution 3D scans combined with high-quality anatomy specific artist-made samples. This report details the data provenance, the model architecture including the specialized sub-models for the ocular and intra-oral structures, and shows its SotA performance on fitting target 3D face scans. To foster community innovation, the complete GNM framework is made publicly available.
