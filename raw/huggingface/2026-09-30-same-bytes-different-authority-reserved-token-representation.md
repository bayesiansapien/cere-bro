---
source: farmer/huggingface
farmed: 2026-10-01T10:34:02.070906+05:30
arxiv_id: 2609.35932
url: https://huggingface.co/papers/2609.35932
arxiv_url: https://arxiv.org/abs/2609.35932
date: 2026-09-30
---

# Same Bytes, Different Authority: Reserved-Token Representations in Chat-Template Prompt Injection

Prompt injection against LLM agents becomes much stronger when the injected instruction is wrapped in the model's own chat template. A forged template marker such as <|im_start|> can reach the model either as a single reserved control token or as a sequence of ordinary subword tokens. The two decode to exactly the same text, and because tokenization runs on the server, the defender rather than the attacker decides which one the model receives. We use this to measure how much of the injected instruction's authority comes from the reserved token's learned representation. Encoding the forged markers as subwords, with the text held fixed and a control for the extra tokens this adds, lowers attack success on the InjecAgent benchmark by 39 to 66 percentage points on three of four open-weight families, and the gap carries over to multi-turn agent tasks in AgentDojo. On Qwen3-8B the gap is 8 points, because without reserved ids the model still recognises the forged turn from its text by reasoning; suppressing the reasoning block widens the gap to 50. The authority sits in the single learned vector at the marker position: the mean of the marker's subword vectors does not reproduce it, the vector of the nearest ordinary token restores the attack on Llama-3.1, and an adaptive attacker who searches for non-reserved markers finds such embedding neighbours on three of four families. In every base and instruction-tuned pair we test, instruction tuning strengthens the model's preference for reserved markers. The standard mitigation, a tokenizer option that encodes special tokens as ordinary subwords, applies only to tokens a configuration declares special, so in 33 of 67 distinct tokenizer configurations, covering 255 of the 400 most-downloaded chat models on Hugging Face, it leaves intact the tool-protocol tokens through which agents read untrusted tool output, and the gap persists on that channel.
