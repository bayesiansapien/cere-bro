---
source: farmer/huggingface
farmed: 2026-10-16T11:32:11.227309+05:30
arxiv_id: 2610.15542
url: https://huggingface.co/papers/2610.15542
arxiv_url: https://arxiv.org/abs/2610.15542
date: 2026-10-15
---

# Apertus 1.5: From Open Text Models to Open Multimodal Reasoners

Language models are becoming infrastructure, and infrastructure built in the open, by public institutions, on documented data, is the alternative to dependence on a few providers; Apertus shows this is viable at scale. Apertus 1.5 extends the fully open Apertus family from text to multimodal reasoning. Continued pretraining of the Apertus 1.0 models, on 4T additional tokens for the 8B and 2T for the 70B, adds image and audio understanding and extends the context window fourfold to 262,144 tokens; multimodality enters through the tokenizer, the language-model head remains restricted to text, and the architecture is unchanged. Supervised finetuning, long-context finetuning, reinforcement learning with verifiable rewards, and preference alignment complete the released models. Thinking is a flag of the chat template rather than a separate model, and lifts mathematical reasoning by up to 20 points on the 8B model. The released models improve over their predecessors on nearly every benchmark; among fully open models of its class, the 8B leads on knowledge, instruction following, and cultural benchmarks, and its instruction following surpasses all compared models, including open-weight ones. On image and audio understanding, a first for the family, the models are competitive with fully open multimodal models, strongest on document understanding and long-form and lower-resource speech recognition, while specialized vision and audio models remain ahead on perception and transcription of English and other high-resource languages. As in Apertus 1.0, we train only on openly available data, respect crawler opt-outs retroactively, and exclude restrictively licensed material. We release the model weights, data preparation and training recipes, and evaluation suites under permissive licenses; openness extends to values, with the Apertus charter guiding alignment stages published alongside the models.
