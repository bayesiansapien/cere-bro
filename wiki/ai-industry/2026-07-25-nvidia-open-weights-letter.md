# The Open-Weights Letter: NVIDIA, Meta, Microsoft, and the Coalition Against Restriction

**TL;DR.** On 2026-07-24, Jensen Huang joined X for the first time to post an NVIDIA-signed open letter titled "Open Weights and American AI Leadership," co-signed by Meta, Microsoft, Andreessen Horowitz, and more than twenty other companies, as the Trump administration weighs restrictions on Chinese open-weight models. The letter's three load-bearing claims: closed models are single points of failure, relying solely on closed models is not inherently safe, and distillation "reflects a long tradition of learning from, building upon, and improving existing technologies." **OpenAI and Anthropic did not sign.** That absence, more than the letter, is the story: it puts the two labs with the strongest frontier positions on one side of an industry split and the entire compute-and-platform layer on the other.

## The alignment map

| Signed | Did not sign |
|---|---|
| NVIDIA, Meta, Microsoft, a16z, 20+ AI startups | OpenAI, Anthropic |
| Endorsed publicly: Elon Musk ("This has my full support. Jensen is right."), tinygrad, Google DeepMind researchers | — |

Sam Altman posted "i want the US to win in AI both in open source and proprietary models, and i am glad to see this" without signing, which drew immediate pushback on X pointing out that OpenAI has lobbied against open weights since DeepSeek R1. The Decoder reads Microsoft's participation as commercially transparent: **the more open models running on Azure, the less Microsoft depends on expensive OpenAI and Anthropic inference**, and Microsoft is already swapping external models for its in-house MAI family in Copilot despite MAI performing significantly worse in independent benchmarks.

## Why the distillation sentence is the sharp one

The letter defends distillation as normal engineering practice on the same day the administration is publicly accusing a Chinese lab of exactly that. OSTP director Michael Kratsios posted, without evidence, that "Moonshot AI distilled Anthropic's Fable for the development of its K3 model," using "a sophisticated internal platform to conduct large scale distillation against U.S. models, allowing them to quickly switch between multiple methods of access to avoid detection," plus acquiring GB300-equipped servers and accessing GB300s in Thailand. Kratsios drew the line explicitly: legitimate distillation for smaller efficient models is fine, "large-scale, covert industrial distillation aimed at stealing proprietary U.S. technology" is not. Treasury Secretary Scott Bessent's framing: "We support open-source AI and the innovation it unlocks. But open source is not open season."

So the same word, distillation, is a defended engineering tradition in NVIDIA's letter and an act of industrial theft in the OSTP statement, on the same day. The wiki has been tracking the technical side of this since the [Kimi K3 offensive-cyber result (07-24)](../responsible-ai/responsible-ai.md), where K3 scored 32% on ExploitBench against 76% for US frontier models despite strong general benchmarks, and UK AISI / US CAISI suggested distillation from Anthropic models could explain the shape of the gap. The technical claim, that a distilled model inherits the teacher's capability profile including its deliberate omissions, is now doing political work.

## The critical reads

Two opinion pieces landed against the policy direction the same day.

**Gary Marcus, "An open letter to David Sacks"** ([Marcus on AI](https://garymarcus.substack.com/p/an-open-letter-to-david-sacks)): Marcus does not dispute the CAISI report itself but objects to Sacks using it to champion US primacy and minimal AI regulation. His position is that the US should consider pivoting toward working with China on AI for global good rather than "creating a new cold war that is likely to end in an uncomfortable way for all, with no clear winners."

**Alberto Romero, "White House's Response to China Lacks Confidence in America"** ([Algorithmic Bridge](https://www.thealgorithmicbridge.com/p/white-houses-response-to-china-lacks)): the sharper argument. Romero's title is the thesis. Reaching for restriction rather than competition is a signal of weakness, not strength, and the Kratsios statement was published "without any evidence whatsoever."

## Relation to prior wiki

- **Escalates** the [07-21 prediction](../daily-digest/2026-07/2026-07-21.md) that "the Chinese open-source ban moves from discussion to a concrete proposal within 60 days." Signal to watch was a named executive order draft, NIST framework, or bill. What arrived instead is a *counter*-coalition forming before the proposal does, plus an on-record OSTP accusation. Partial resolution: the debate is now public and named, but no concrete legal instrument exists yet.
- **Extends** the [07-24 Silicon Valley split](../daily-digest/2026-07/2026-07-24.md) item (The Information: SV unites against Anthropic over Chinese AI restrictions) with the signature list that makes the split concrete.
- **Complicates** the sovereignty thread the wiki has tracked through [SLAI T-Rex (07-23)](../hardware/2026-07-23-slai-t-rex-deepseek-v4-ascend.md), which post-trained a 1.6T DeepSeek-V4 on Huawei Ascend at 34% MFU. If sovereign compute is viable at all, restriction buys less time than its advocates assume, and the letter's "enable sovereignty" line is arguing for the US being the supplier of open weights rather than ceding that role.

## Sources

- [Open Weights and American AI Leadership (NVIDIA, PDF)](https://images.nvidia.com/pdf/Open-Weights-and-American-AI-Leadership.pdf) · [@JensenHuang first post](https://x.com/JensenHuang/status/2080643682408321103)
- [Meta, Microsoft, Nvidia and Others Sign Letter Defending Open-Source AI (The Information)](https://www.theinformation.com/briefings/meta-microsoft-nvidia-others-sign-letter-defending-open-source-ai)
- [Microsoft's open-weight AI push is so obviously an Azure play it hurts (The Decoder)](https://the-decoder.com/microsofts-open-weight-ai-push-is-so-obviously-an-azure-play-it-hurts/)
- [An open letter to David Sacks (Gary Marcus)](https://garymarcus.substack.com/p/an-open-letter-to-david-sacks) · [White House's Response to China Lacks Confidence in America (Algorithmic Bridge)](https://www.thealgorithmicbridge.com/p/white-houses-response-to-china-lacks)
- Raw: `raw/twitter/2026-07-25-morning.md`, `raw/rss/2026-07-24-the-information-meta-microsoft-nvidia-and-others-sign-letter-defending.md`, `raw/rss/2026-07-24-algorithmic-bridge-white-house-s-response-to-china-lacks-confidence-in-ame.md`, `raw/gmail/2026-07-25-starred.md`
