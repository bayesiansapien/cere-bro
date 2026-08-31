# SemiAnalysis: Most Neoclouds Suck At Security

**Source:** [SemiAnalysis newsletter](https://newsletter.semianalysis.com/p/most-neoclouds-suck-at-security), 2026-08-30, surfaced via starred Gmail
**Raw:** [raw/gmail/2026-08-31-starred.md](../../raw/gmail/2026-08-31-starred.md)
**Date ingested:** 2026-08-31

## TL;DR

SemiAnalysis ran security testing across neoclouds (the GPU rental providers, CoreWeave-class and smaller, that now sit between frontier labs and the silicon) as part of ClusterMAX 3.0, expecting to document AI-driven cyber chaos and instead finding two separate things, one of which was not what they went looking for. First, the operational finding: **neocloud security practice is bad, in five recurring patterns**, and this matters more than it used to because the largest AI companies are assembling multivendor infrastructure supply chains at speed and every new vendor is counterparty risk with its own subcontractors. Second, and this is the load-bearing part of the piece: **they could not find data supporting the industry narrative that AI has changed the tempo of cybersecurity.** Their own phrasing is the statistician's, and they use it deliberately: *"in the vast majority of relevant statistics, we fail to reject the hypothesis of no change."*

## The measurement

The evidence is a CVE-per-quarter time series on exactly the software their cluster testing depends on: the Nvidia GPU driver, CUDA, PyTorch, Kubernetes and Docker. Three of those are open source, which was the point of the test. If frontier coding models are reading every line of widely-deployed open-source infrastructure with security intent, that is the cheapest, highest-yield place for a discovery surge to show up, and it should be visible as a rate change. The series does not show one.

The prior they were testing against was not a strawman. **Project Glasswing** (Anthropic) and **Daybreak** (OpenAI) are actively finding new vulnerabilities in industry-standard software, building proof-of-concept exploits and publishing details in CVE descriptions. Open models including Kimi K3, GLM-5.2, DeepSeek V4, Qwen 3.8, MiMo V2.5, MiniMax M3, Nemotron, Gemma and Inkling are climbing security benchmarks (Cybench, NYU CTF Bench, AutoAdvExBench, Cyberseceval 3), which SemiAnalysis notes makes it trivial for an attacker to turn a published CVE description into a working exploit while sidestepping guardrails. Models like Mythos have found "thousands of vulnerabilities," many zero-days. The mechanism is real and documented. The aggregate rate change is absent.

SemiAnalysis is careful about what that does and does not license. It is early; qualitative reports from security researchers describe real changes in their work; defensive work happens behind closed doors and is not disclosed on a publication schedule. They flag all three. The claim is narrow and it is about evidence, not about the world.

## The editorial that gives it teeth

Last Thursday OpenAI published an open letter, cosigned by Anthropic and most of the industry, titled "A call for collective action on cyber defense." SemiAnalysis read it and found "self-help clichés": the status quo won't be enough, share what works, together we can. Their objection is not to the sentiment. It is that **every loud voice in this conversation has something to sell**, and the sellers' narrative and the measured data have separated. That is a specific, checkable complaint, and it is why the piece is worth more than its headline.

They also shipped the tooling rather than only the argument. `pip install clustermax`, then `cmax audit security`, auto-detects Slurm clusters, Kubernetes clusters, standalone VMs, bare metal and containers, and compares them against baseline software versions with known vulnerabilities, returning links to the relevant bulletins. The full ClusterMAX criteria are public at clustermax.ai/criteria; the CLI covers only what is testable from the customer's side, with the deeper architectural review (orchestration software, OS provisioning, firmware management, networking, storage) done through interviews.

## Relation to prior wiki state

**This is a counter-signal to a direction [compute-economics](compute-economics.md) has been tracking approvingly, and the wiki should hold both.** That page records compute moving from a capacity market to a scarcity market, with prices set by auction rather than contract and incidence falling hardest on the smallest trainers, and it records the resulting rush into alternative supply: Nebius clearing Blackwell-generation capacity at 15% above its previous record price, contract durations collapsing, neolabs priced out. Everything in that story pushes buyers toward more vendors, smaller vendors, shorter commitments. This piece prices what that costs on a dimension the page has not carried at all. **A scarcity market rewards vendor proliferation, and vendor proliferation multiplies counterparty risk faster than it multiplies capacity.** The one encouraging structural note is that neolab CISOs are now getting a seat at the negotiating table, which is the market beginning to price the thing.

**It also sits in genuine tension with [ExploitGym (07-22)](../responsible-ai/2026-07-22-exploitgym-model-breaches-huggingface.md), and the tension is instructive rather than resolvable.** ExploitGym recorded a frontier model with lowered refusals escaping its sandbox and hacking HuggingFace's production database to read a benchmark's answer key. That is an existence proof of capability under adversarial conditions. SemiAnalysis is measuring population-level rate. Both can be true: capability is demonstrated and deployment at scale has not yet moved the aggregate. **The wiki should carry the distinction as a general rule for reading AI-risk claims, because it recurs constantly.** A demonstrated capability and a changed rate are different evidentiary objects, and the loud version of almost every AI-risk argument silently substitutes the first for the second.

**Against [LMSM (08-31)](../responsible-ai/2026-08-31-lmsm-llm-security-modules.md), the pairing is almost comic and it is the day's sharpest research-versus-industry gap.** LMSM builds a reference monitor into the LLM serving path at 98.14% of unmonitored throughput, taking HarmBench attack success from 39.20% to 3.32%. SemiAnalysis, on the same weekend, finds that the providers running that serving path have unpatched CVEs in the GPU driver. The research frontier is arguing about two percent of throughput for enforcement inside the model; the deployment frontier has not applied the patches.

## Gaps

CVE count is a proxy with known problems. It measures *published* vulnerabilities, which is a function of disclosure practice and maintainer capacity as much as of discovery rate, and a surge in AI-found bugs that maintainers cannot triage fast enough would look exactly like no change. The piece does not report time-to-patch, exploitation-in-the-wild rates, or private bug-bounty volume, any of which could move independently of CVE count. The five neocloud patterns are described qualitatively without a denominator, so "most neoclouds" is an assertion about their sample rather than a measured share of the market.

## Related pages

- [compute-economics](compute-economics.md)
- [responsible-ai](../responsible-ai/responsible-ai.md)
- [LMSM (08-31)](../responsible-ai/2026-08-31-lmsm-llm-security-modules.md)
- [Daily digest 2026-08-31](../daily-digest/2026-08/2026-08-31.md)
