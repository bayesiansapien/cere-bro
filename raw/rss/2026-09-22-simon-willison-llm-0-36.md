---
source: farmer/rss
feed: simon-willison
farmed: 2026-09-23T07:54:51.609126+00:00
title: 'llm 0.36'
url: https://simonwillison.net/2026/Sep/22/llm/
published: 2026-09-22
---

# llm 0.36

Release: llm 0.36 

 
 
 New OpenAI models: gpt-6-sol for GPT-6 Sol and gpt-6-luna for GPT-6 Luna . #1702 
 Model plugins can now declare supports_conversation = False for models that only accept single-turn prompts. LLM raises llm.ConversationNotSupported when these models receive assistant or tool history, and llm chat rejects them before starting a session. See Models that do not support conversations . The first plugin to use this is llm-typesafe . #1692 
 Reasoning traces in the Markdown output of llm logs are now wrapped in <details><summary> tags. #1701 
 
 
 Plus bug fixes from five new contributors .

 
 
 Tags: openai , llm
