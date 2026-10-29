# Q3 cloud earnings, GB300 rents and packaging price hikes (2026-10-28)

**Sources:** The Information (Google Q3, Microsoft Q3, Google Cloud vs Azure, Oracle capex cap, Marvell-Lumentum, Malaysia chip seizure), AI Breakfast (TSMC CoWoS, CXMT HBM3E, AWS sold out), X feed (Deutsche Bank GB300 rents, Google Cloud detail, IREN, Cerebras packaging, Jensen Huang). raw: `raw/rss/2026-10-2[89]-the-information-*.md`, `raw/gmail/2026-10-29-newsletters.md`, `raw/twitter/feed/`.

**TL;DR.** The compute market's prices are all going up at once, and the cloud numbers show why.
- **Google Cloud** revenue +103% YoY to $30.7B, operating income tripled to $11.1B; Google's model APIs process ~32B tokens per minute (4x a year ago); TPU sales contributed, but Google expects most TPU revenue in 2027. AI data-center spend pushed free cash flow to -$9B+. Alphabet revenue grew 25% to $127.6B, short of expectations, and it sold $12.4B of stock via an ATM program. Google Cloud is now close to Azure in revenue ([The Information](https://www.theinformation.com/articles/google-cloud-closes-azure-microsoft-wins-day-investors)).
- **Microsoft** revenue +19% to $92.3B; Azure accelerated partly on OpenAI server rentals; data-center spend dampened cash flow.
- **Oracle** rose 10%+ after calling FY2028-29 "peak capex" and projecting positive cash flow, 34% operating margins and a 28% five-year ROI on AI compute.
- **AWS**: Andy Jassy says capacity is sold out through 2027 with parts of 2028 committed.
- **Rents**: Deutsche Bank estimates GB300 rents up to ~$14/hour vs $3.50 for H100, with some contracts at ~$60M per MW per year (~$48B per GW).
- **Packaging and memory**: TSMC is weighing a 10-20% CoWoS (the advanced packaging that joins GPU dies to HBM) price rise and 3-6% on wafers from January 2027. CXMT starts limited HBM3E production at 20-30% yields vs ~70% at SK hynix.
- **Deals**: Marvell in talks to buy optics maker Lumentum (market cap $80B+). IREN raised $363M against GPUs already earning under contracts. Malaysia seized ~$12M of smuggled AI chips.
- **Cerebras packaging**: an analysis of its S-1 says Cerebras runs non-functional background work to keep wafers warm and avoid damaging thermal cycles, despite claiming "thermal expansion-tolerant packaging."

## Relation to prior wiki
- **Extends** [compute economics](compute-economics.md) and the 10-28 summary (TPUs leave Google; SK hynix pre-sold half of 2027-28). Every layer of the stack (memory, packaging, GPUs, cloud capacity) is now pre-sold or repricing upward.
- **Rents ratio**: GB300 at ~4x H100 hourly echoes the 10-24 finding that H200 rents rose 160% against 40% for H100. Newer, memory-richer parts are capturing the margin.
- **Why software efficiency pays now**: Jensen Huang argued the same day that doubling model speed doubles a lab's revenue while demand exceeds capacity. With capacity sold out to 2027-28, kernel and cache work is the only near-term way to serve more tokens.
