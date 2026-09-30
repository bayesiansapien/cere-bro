---
source: farmer/huggingface
farmed: 2026-09-30T05:05:05.936595+00:00
arxiv_id: 2609.31669
url: https://huggingface.co/papers/2609.31669
arxiv_url: https://arxiv.org/abs/2609.31669
date: 2026-09-29
---

# NanoForecast v0.5: Competitive Time Series Forecasting Through Training Pipeline Optimization

We present NanoForecast v0.5, a 6.5M-parameter forecaster that competes with models 31x its size (TimesFM, 200M parameters) after training pipeline fixes and no architecture change. Retraining the v0.3 architecture with corrected loss-scope handling, tensor shape alignment, and wider augmentation coverage cuts overall Mean Absolute Scaled Error by 43.8% under one fixed protocol (MASE 3.030 to 1.704) on the same data and compute budget. NanoForecast v0.5 beats TimesFM on all three ETT datasets (MASE 0.676/1.110/0.287 vs. 0.705/1.360/0.545) and on exchange rate (4.317 vs. 4.383); TimesFM keeps a clear lead on the high-cardinality electricity and traffic sets. Against PatchTST (15M+ parameters, official configuration), v0.5 wins all three ETT sets. Training takes about 12 hours on a single cloud GPU (NVIDIA T4, Google Colab) and inference needs no GPU (measurements in this paper are on an Apple M4 CPU). We release all code, pretrained checkpoints, and evaluation framework under Apache 2.0 at https://github.com/eulogik/NanoForecast
