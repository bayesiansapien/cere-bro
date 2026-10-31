---
source: farmer/huggingface
farmed: 2026-10-31T08:06:35.162791+00:00
arxiv_id: 2609.05881
url: https://huggingface.co/papers/2609.05881
arxiv_url: https://arxiv.org/abs/2609.05881
date: 2026-10-30
---

# Broken on Arrival: Non-Functional Quantized LLM Artifacts in Public Model Registries and How to Catch Them

Developers download quantized large language models (LLMs) from public registries to run them locally. None of the registries we examined documented functional testing of their files. We tested all 305 eligible code-capable GGUF tags (the llama.cpp format) across 15 model lines in the official Ollama library, plus 22 popular Hugging Face community files. A 15-task code screen identified suspects, which we retested on all 164 HumanEval+ tasks. Seven official tags (2.3%) solved at most six of them. All were low-bit quantizations of models with at most four billion parameters. We rebuilt five suspect files from the original weights. All five registry files matched our uncalibrated rebuilds tensor for tensor, so none was corrupted. Exact reproducibility did not imply function. With the weights, toolchain and tensor mix held fixed, adding an importance matrix raised three Qwen2.5-Coder-3B builds from zero to 76-113 solved tasks. The same uncalibrated recipe left the smaller Qwen2.5-Coder-1.5B functional, showing that the recipe alone does not predict failure. None of 66 sampled tags that passed the screen was non-functional. We release the audit data and the quantcheck tool and recommend screening low-bit tags before publication, then calibrating or withholding failures.
