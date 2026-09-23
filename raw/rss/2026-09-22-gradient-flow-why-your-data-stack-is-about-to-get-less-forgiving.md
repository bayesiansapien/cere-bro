---
source: farmer/rss
feed: gradient-flow
farmed: 2026-09-23T07:54:49.721281+00:00
title: 'why your data stack is about to get less forgiving'
url: https://gradientflow.substack.com/p/your-ai-might-be-fine-but-your-data
published: 2026-09-22
author: 'Ben Lorica 罗瑞卡'
---

# why your data stack is about to get less forgiving

Subscribe • Previous Issues 

 Stale Data Used to Be Annoying Imagine a procurement agent checking inventory and deciding that stock has fallen below the reorder threshold. It places another order. The problem is that a large delivery was recorded a few minutes earlier, and the copy of the data the agent queried has not caught up. A dashboard running on stale data might show you the wrong inventory number. An agent running on stale data can place the wrong order. 

 For years, many analytical systems could tolerate some delay, ambiguity, and imperfect data because a person sat between the result and the action. That person could wait for a slow query, notice that a number looked wrong, or ask which definition applied. Agents remove much of that buffer. They check the data, take an action, see what happened , and check again. 

 Subscribe now 

 Last week I wrote about the value of preserving the history of how work gets done. This week I want to look at what an agent needs to know while it’s carrying out a task.. 

 Relevant Is No Longer Enough The first wave of enterprise AI focused heavily on retrieval: find the information relevant to a question and put it in front of the model. Agents need to answer a different question. Not just what is relevant, but what is true right now . Did the payment clear? Is that inventory still there? Was the account suspended an hour ago? Did another process already touch the record? Information that is five minutes old may be fine for a research question and dangerously wrong for an action. 

 Freshness is not the only problem. Definitions matter too. Suppose two systems disagree about what counts as an active customer. An analyst who notices the ambiguity can stop and ask somebody. An agent may choose one definition and keep going. 

 A small benchmark illustrates the problem. When business definitions and relationships were modeled ahead of time, accuracy improved substantially. I find the failure mode more interesting than the scores. When the semantic layer, which encodes those definitions and relationships, could not answer a question, it said so. When the model wrote SQL directly against the data, it could return a perfectly plausible wrong number . 

 When data informed people, ambiguity produced bad analysis. When agents act on that data, the same ambiguity can produce bad operations. 

 Analytical Queries Become Production Dependencies Correct answers are not enough if they arrive too slowly or not at all. A human running an analytical query can usually wait. An agent may be waiting on that query before it takes the next step. 

 If a query is step seven of twenty, every extra second can delay the steps behind it. A timeout can stop a customer interaction or business process rather than merely leave someone staring at a dashboard. Software can also launch many tasks at once and revisit the same data as conditions change. 

 That puts different expectations on some analytical systems. Latency, availability, concurrency , and workload isolation start to matter in ways that look more like application infrastructure than traditional analytics. 

 Data Quality Matters More When AI Acts Stale records, duplicates, inconsistent definitions, and poorly documented fields are familiar data problems . Better models do not make them disappear. What is different is what can happen when an agent acts on them. 

 A duplicate record can trigger duplicate outreach or a second transaction. A bad entity match can cause an action against the wrong account. A poorly documented field can quietly change what an agent thinks it is measuring. 

 In one experiment, adding profiling and query history left an analytics agent around 40% reliable . Cleaning up the data model and improving the documentation brought it to roughly 90%. It is one specific result, not a benchmark, but the lesson is useful: basic data modeling and documentation mattered more than adding more context. 

 Some failures that look like AI failures are really old data failures whose consequences have become operational. 

 Permissions Have to Follow the Data Agents also make an old permissions problem harder. A single task may pull information from a warehouse, a search index, a SaaS application, a vector store, or a cache. Those systems do not necessarily enforce access in the same way. 

 Suppose a source system hides a document from a particular employee, but a search index built from that system does not preserve the same restriction. An agent retrieving from the index can now see something the employee could not have retrieved from the source. 

 This is why permissions cannot be treated as something checked only when data first enters the system. When information is copied, indexed, cached, or retrieved somewhere else, the access rules need to travel with it . 

 The practical question remains simple: when an agent reads a record, whose authority is it exercising? 

 Production Requires More Than Retrieval Some of the database architectures I wrote about last year make more sense in this context. Databricks is pushing this idea further with an architecture that lets transactional and analytical workloads operate over a unified storage layer instead of constantly copying operational data into a separate analytical system. Less copying can mean less lag between something changing in the business and that change becoming available to an application or agent. 

 But I think the broader lesson is more useful than any one architecture. A prototype can show that an agent can perform a task without proving that the surrounding data systems can support it reliably. 

 Production has to answer harder questions. Is the state authoritative? How does the agent learn that something changed? Do permissions survive when data is copied or indexed? What happens after a partial failure? Can a retry repeat an action? A working demo can hide how much data infrastructure still has to be built. 

 For years, the data stack mostly helped companies observe and understand themselves. Agents increasingly use the same information while doing work. 

 Once agents can act on the data they retrieve, the data stack becomes part of the application. 

 More Intelligence, Less Waiting, Less Power From Inside OpenAI’s First Chip Not Every AI Job Needs a Chatbot Learn more 👉 Laya the open source version of Jev 

 Ben Lorica edits Ethics.dev and the Gradient Flow newsletter , and he hosts the Data Exchange podcast . He helps organize the AI Conference and the Agent Conference . You can follow him on Linkedin , X , Mastodon , Reddit , Bluesky , YouTube , or TikTok . This newsletter is produced by Gradient Flow .
