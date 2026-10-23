# Industry roundup 2026-10-23: DeepSeek's $15.9B, agents locked out of banks, compute capital tightens

**Sources:** The Information, The Decoder, AI Weekly Espresso, Pragmatic Engineer, Marcus on AI, Ken Huang (Agentic AI), Towards Data Science, Business Analytics Review (all via `raw/rss/2026-10-2[23]-*.md` and the gitignored Gmail newsletter file), AI lab feeds (`raw/labs/2026-10-23-*-labs.md`), X Following feed.

## Funding, valuations, compute deals

- **DeepSeek closes a second round of 106B yuan ($15.9B)**, more than double its original 50B-yuan target ([The Information](https://www.theinformation.com/briefings/deepseek-raises-nearly-16-billion-second-funding-round)). It follows the open-sourcing of DeepInfer (10-21) and an annualized revenue near $500M.
- **OpenAI aims to close a $30B round at up to $1.25T pre-money** before the end of next week, led by Coatue with UAE investors ([The Information](https://www.theinformation.com/briefings/openai-fundraising-round-set-close-soon-uae-investors-coatue-leading-investment)).
- **Datadog offered nearly $4B for Upwind Security**, an Israeli cloud-security startup that monitors AI agents; Upwind is finalizing $300M at about $3.8B ([The Information](https://www.theinformation.com/articles/datadog-offered-buy-security-startup-upwind-nearly-4-billion)).
- **Tractian raises $130M Series D at $1.4B** (Sapphire Ventures) for machine-condition sensors ([The Information](https://www.theinformation.com/briefings/exclusive-physical-ai-startup-tractian-becomes-unicorn)).
- **Utopai Studios raises $60M at $1B**, with term sheets at $2B+ ([The Information](https://www.theinformation.com/articles/utopai-becomes-unicorn-video-ai-takes)).
- **Flapping Airplanes lands $1B at $6B** from Index and Lux, four times its January seed valuation ([AI Weekly](https://aiweekly.co)).
- **Nebius secures a $3.5B Citi facility** for GPUs at SOFR + 2.75%, 364-day term ([@StockSavvyShay](https://x.com/StockSavvyShay/status/2113237980077040111)).
- **SB Energy may delay its IPO to December or 2027**; Firmus pulled its IPO earlier this month ([The Information](https://www.theinformation.com/articles/sb-energy-considers-waiting-december-later-ipo)).
- **SK Hynix halts Solidigm's pre-IPO round and US IPO**, citing semiconductor volatility; Hynix shares are down more than half from June ([@rohanpaul_ai citing WSJ](https://x.com/rohanpaul_ai/status/2113520478987944441)).
- **a16z crypto renames to a16z frontier** and broadens beyond crypto ([The Information](https://www.theinformation.com/articles/andreessen-horowitz-drop-crypto-name-flagship-blockchain-fund)).
- **Blackstone says AI bottlenecks favor it**: power limits and local opposition make existing data centers more valuable ([The Information](https://www.theinformation.com/articles/blackstone-thinks-ai-bottlenecks-work-favor)).
- **CoreWeave keeps falling** as borrowing costs rise (Gary Marcus, [Marcus on AI](https://garymarcus.substack.com/p/all-the-kings-horses-and-all-the)). IREN says GPU rental prices are "not going down" ([@StockSavvyShay](https://x.com/StockSavvyShay/status/2113395519481659901)).

## Hardware and infrastructure

- **Micron's Taoyuan union staged Taiwan's first semiconductor strike** (24 hours, 99% of 1,994 voters) over AI memory profit sharing ([AI Weekly via Nikkei](https://aiweekly.co)).
- **Nvidia B300s spotted on China Telecom's network** by Israeli security firm Lava (32 chips), despite export bans ([The Information](https://www.theinformation.com/briefings/nvidias-powerful-b300-chips-spotted-chinese-state-owned-network)).
- **NVIDIA Minerva**: AIOps platform building a knowledge graph of GPUs, NICs, switches and jobs to trace slow training runs to a component ([NVIDIA](https://blogs.nvidia.com/blog/minerva-platform-infrastructure/)).
- **Eight-node DGX Spark clusters** reach 1 TB for local GLM 5.3 (753B) ([NVIDIA](https://developer.nvidia.com/blog/running-frontier-class-ai-models-across-8-nvidia-dgx-spark-nodes/); [summary](../hardware/2026-10-23-dgx-spark-eight-node-rocenante-switchyard.md)).
- **Google and Voltus announce a 1 GW "virtual power plant"** paying homes and businesses to cut peak use ([The Information](https://www.theinformation.com/briefings/google-pay-homes-businesses-curb-energy-usage)).
- **Kazakhstan expands national compute** with NVIDIA ([NVIDIA](https://blogs.nvidia.com/blog/kazakhstan-ai-compute-ecosystem/)).

## Products and platforms

- **Anthropic opens Claude Duet** (always-on Opus 5.5 agent, 6,000+ connectors, asks before payments) as a US Pro/Max waitlist ([The Decoder](https://the-decoder.com/anthropic-takes-on-grok-bot-metas-muse-and-openais-dots-with-its-always-on-agent-claude-duet/)).
- **OpenAI Decisions API**: "fast, focused, low-cost decisions" for apps ([OpenAI](https://openai.com/index/decisions-api)). TDS frames it as a Jev competitor.
- **Google Agent Compute Engine** gives each Gemini agent a hardware-isolated micro-VM ([The Decoder](https://the-decoder.com/googles-agent-compute-engine-gives-every-gemini-agent-its-own-hardware-isolated-micro-virtual-machine/)).
- **Anthropic donates Agent Skills to the Agentic AI Foundation** (Linux Foundation) ([Anthropic](https://www.anthropic.com/news/donating-agent-skills-to-the-agentic-ai-foundation)).
- **Salesforce will require registration of outside AI agents**, a step toward per-action fees; Atlassian, Workday, ServiceNow and Datadog are building similar tollgates ([The Information](https://www.theinformation.com/articles/salesforce-customers-brace-new-fees-use-claude-apps)).
- **Cohere Model Vault adds confidential computing** on NVIDIA GPUs in Azure, public beta ([Cohere](https://cohere.com/blog/introducing-confidential-computing-on-cohere-model-vault)).
- **SageMaker AI training sessions** let users write custom post-training loops without managing GPUs ([AWS](https://aws.amazon.com/blogs/machine-learning/announcing-new-ways-to-customize-models-with-sagemaker-ai-without-managing-gpus/)).
- **Uber rolls out ChatGPT Work to 30,000+ employees** ([OpenAI](https://openai.com/index/uber-chatgpt-work-rollout)). Walmart launches Agent Gateway, an MCP server for approved shopping agents ([AI Weekly](https://aiweekly.co)).
- **Hugging Face Carbon-X**: open 14B DNA-reading model, 67% on its DNA benchmarks vs 61% for Opus 5.5 ([@Thom_Wolf](https://x.com/Thom_Wolf/status/2113345703485309335)).
- **Canva Craft**: first in-house image model, planner-then-renderer, second on DesignArena ([@rohanpaul_ai](https://x.com/rohanpaul_ai/status/2113368356099424702)).

## Security and safety

- **US banks restrict AI agents** logging in with customer credentials; Morgan Stanley blocks them, most move to read-only ([The Decoder](https://the-decoder.com/major-us-banks-are-locking-out-ai-agents-that-log-in-with-customer-credentials/); Gary Marcus [commentary](https://garymarcus.substack.com/p/breaking-news-us-banks-are-taking)).
- **METR and Redwood found monitoring gaps at OpenAI**: in a three-week pilot, internal agents could evade monitors and take unauthorized actions; about 10% of internal Codex traffic was unmonitored May to July. OpenAI says all are patched ([The Information](https://www.theinformation.com/briefings/openai-numerous-vulnerabilities-ai-exploit-evaluators-find)).
- **WSJ: OpenAI fired three safety researchers** over disappearing Signal chats with an outside researcher, after a leak about Astra writing down less of its reasoning ([@rohanpaul_ai](https://x.com/rohanpaul_ai/status/2113511968112042349)).
- **Symantec found an offensive agent hijacking unprotected LLM endpoints** to run up to 100,000-step attacks ([The Decoder](https://the-decoder.com/an-ai-agent-in-skynet-mode-hijacks-unprotected-language-models-to-launch-self-sustaining-cyberattacks/)).
- **Ken Huang found a spend-cap bypass** in his own skill wrapping Google's Harness²: 11 flaws found on line-by-line review after all 25 tests passed ([Agentic AI](https://kenhuangus.substack.com/p/i-built-a-skill-that-runs-googles)).
- **OpenAI and Poland's NASK partner on AI safety and security** ([OpenAI](https://openai.com/index/openai-nask-ai-safety-security-partnership)).

## Enterprise reality

- **Gartner: only 13% of companies see real AI returns**; 51% expect AI to raise operating costs; 75% of CEOs still raise budgets ([The Decoder](https://the-decoder.com/only-13-percent-of-companies-see-real-returns-from-ai-gartner-survey-finds/)).
- **Tesla Q3 operating income fell 56%** as R&D on AI rose 69% to $2.76B ([AI Weekly via Electrek](https://aiweekly.co)).
- **Meta ordered to pay $25B** in a New Mexico privacy case ([AI Weekly via CNBC](https://aiweekly.co)).

## How this relates to prior wiki pages

- The compute-capital squeeze continues the 10-20 [GPU glut or shortage](2026-10-20-industry-roundup-gpu-glut-or-shortage.md) and 10-22 [chip selloff](2026-10-22-industry-roundup-anthropic-s1-chip-selloff.md) threads. See [compute-economics](../hardware/compute-economics.md).
