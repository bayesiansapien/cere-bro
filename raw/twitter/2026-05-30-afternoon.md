# Twitter/X Digest | 2026-05-30 | AFTERNOON
> Scraped 2026-05-30 15:00 IST | Lookback: 24h | 3 tweets | 7 articles

---

## @bayesiansapien Retweets (Curated Signal)

*No retweets found in the past 24h*

## AI Account Feed

### @kilocode (Independent)
*3 AI-relevant tweets*

**@kilocode** (@kilocode) · 2026-05-29 19:03 UTC

> kilo.codes/gJBzwKp

[View tweet](https://nitter.net/kilocode/status/2060436821146742834#m)

**Article:** https://kilo.codes/gJBzwKp

Install Kilo Code in 60 Seconds — VS Code, JetBrains CLI Skip to main content Kilo Product Models Pricing Support Docs (opens in new tab) Blog (opens in new tab) GitHub Sign in Sign up Install Kilo Code Get started with AI coding in your CLI or preferred IDE Using Kilo for work? Create a team workspace . VS Code JetBrains CLI Slack Others VS Code Install Kilo Code for VS Code To install Kilo Code in VS Code, you need to have Visual Studio Code installed on your computer. 1. Install VS Code If you don&#x27;t have VS Code installed yet, download it here 2. Install the extension Click the button below to install Kilo Code directly in VS Code Install in VS Code Download VS Code Kilo Community Discord Discord GitHub GitHub Reddit r/kilocode 𝕏 @kilocode Product Hunt p/kilocode Product IDE CLI Slack Cloud Autocomplete Security Agent Customers Teams Enterprise Early Access Pricing Kilo Pass Learn Documentation Articles Kilo College (opens in new tab) Blog (opens in new tab) YouTube (opens in new tab) Changelog (opens in new tab) OpenClaw Workflows OpenClaw Guides OpenClaw Integrations KiloClaw Alternatives Company Careers (opens in new tab) About Open Source Events Kilo League Hackathons Partner Program Responsible Disclosure Compare Kilo Code All Alternatives vs Roo Code vs Cursor vs Windsurf vs GitHub Copilot vs Claude Code vs Cline vs Tabnine vs Replit vs Lovable vs CodeRabbit vs Augment Code Roo Migration Cursor Migration Compare KiloClaw All Alternatives vs xCloud vs MyClaw vs H

---

**@kilocode** (@kilocode) · 2026-05-29 19:01 UTC

> Three new arrivals in Kilo this week, all sharpening the price-to-performance trade. Opus 4.8 at the same price as 4.7. Step 3.7 Flash from StepFun. And Xiaomi just cut MiMo pricing by up to 99%.

[View tweet](https://nitter.net/kilocode/status/2060436411266769327#m)

---

**@kilocode** (@kilocode) · 2026-05-29 12:46 UTC

> StepFun’s Step 3.7 Flash is one of the best open-weight models you can run right now, and it’s live in Kilo. A multimodal agent model on open weights, running at 400 tok/s, now in Kilo. @StepFun_ai shipped Step 3.7 Flash with the weights and quants ready to go. StepFun (@StepFun_ai) ⚡️ Step 3.7 Flash is here: The new frontier is agent efficiency. #1 ClawEval-1.1 (67.1), #1 SimpleVQA Search (79.2), #2 SWE-PRO (56.3), 95.3 on V* Python. Open weights under Apache 2.0. Built for agentic, coding, search, and multimodal workflows — balancing speed, cost, and reliable execution. - 400 TPS. 198B spars

[View tweet](https://nitter.net/kilocode/status/2060341963119837635#m)

**Article:** http://github.com/stepfun-ai/Step-3.7-Flash

GitHub - stepfun-ai/Step-3.7-Flash · GitHub Skip to content Navigation Menu Toggle navigation Sign in Appearance settings Platform AI CODE CREATION GitHub Copilot Write better code with AI GitHub Spark Build and deploy intelligent apps GitHub Models Manage and compare prompts MCP Registry New Integrate external tools DEVELOPER WORKFLOWS Actions Automate any workflow Codespaces Instant dev environments Issues Plan and track work Code Review Manage code changes APPLICATION SECURITY GitHub Advanced Security Find and fix vulnerabilities Code security Secure your code as you build Secret protection Stop leaks before they start EXPLORE Why GitHub Documentation Blog Changelog Marketplace View all features Solutions BY COMPANY SIZE Enterprises Small and medium teams Startups Nonprofits BY USE CASE App Modernization DevSecOps DevOps CI/CD View all use cases BY INDUSTRY Healthcare Financial services Manufacturing Government View all industries View all solutions Resources EXPLORE BY TOPIC AI Software Development DevOps Security View all topics EXPLORE BY TYPE Customer stories Events webinars Ebooks reports Business insights GitHub Skills SUPPORT SERVICES Documentation Customer support Community forum Trust center Partners View all resources Open Source COMMUNITY GitHub Sponsors Fund open source developers PROGRAMS Security Lab Maintainer Community Accelerator GitHub Stars Archive Program REPOSITORIES Topics Trending Collections Enterprise ENTERPRISE SOLUTIONS Enterprise platform AI-pow

**Article:** http://huggingface.co/stepfun-ai/Step-3.7-Flash

stepfun-ai/Step-3.7-Flash · Hugging Face Hugging Face Models Datasets Spaces Buckets new Docs Enterprise Pricing Website Tasks HuggingChat Collections Languages Organizations Community Blog Posts Daily Papers Learn Discord Forum GitHub Solutions Team Enterprise Hugging Face PRO Enterprise Support Inference Providers Inference Endpoints Storage Buckets Log In Sign Up , eos_token : |im_end|> , pad_token : ｜end▁of▁sentence｜> , unk_token :null, use_default_system_prompt :false}, chat_template_jinja : {% macro render_message_content(message) %}{% if message.content is none %}{{- '' }}{% elif message.content is string %}{{- message.content }}{% elif message.content is mapping %}{{- message.content['value'] if 'value' in message.content else message.content['text'] }}{% elif message.content is iterable %}{% set ns = namespace(needs_text_separator=false) %}{% for item in message.content %}{% if item.type == 'text' %}{% if ns.needs_text_separator %}{{- ' ' }}{% endif %}{{- item['value'] if 'value' in item else item['text'] }}{% set ns.needs_text_separator = true %}{% elif item.type == 'image' %} im_patch>{% set ns.needs_text_separator = false %}{% endif %}{% endfor %}{% endif %}{% endmacro %}\n{{bos_token}}{%- if tools %}\n {{- ' |im_start|>system\\n' }}\n {%- if reasoning_effort is defined %}\n {{- \ Reasoning: \ + reasoning_effort + '\\n\\n' }}\n {%- endif %}\n {%- if messages[0].role == 'system' %}\n {{- render_message_content(messages[0]) + '\\n\\n' }}\n {%- endif %}\n {{- \ # Too

**Article:** http://huggingface.co/stepfun-ai/Step-3.7-Flash-GGUF

stepfun-ai/Step-3.7-Flash-GGUF · Hugging Face Hugging Face Models Datasets Spaces Buckets new Docs Enterprise Pricing Website Tasks HuggingChat Collections Languages Organizations Community Blog Posts Daily Papers Learn Discord Forum GitHub Solutions Team Enterprise Hugging Face PRO Enterprise Support Inference Providers Inference Endpoints Storage Buckets Log In Sign Up {% set ns.needs_text_separator = false %}{% endif %}{% endfor %}{% endif %}{% endmacro %}\n{{bos_token}}{%- if tools %}\n {{- ' |im_start|>system\\n' }}\n {%- if reasoning_effort is defined %}\n {{- \ Reasoning: \ + reasoning_effort + '\\n\\n' }}\n {%- endif %}\n {%- if messages[0].role == 'system' %}\n {{- render_message_content(messages[0]) + '\\n\\n' }}\n {%- endif %}\n {{- \ # Tools\\n\\nYou have access to the following functions in JSONSchema format:\\n\\n tools>\ }}\n {%- for tool in tools %}\n {{- \ \\n\ }}\n {{- tool | tojson(ensure_ascii=False) }}\n {%- endfor %}\n {{- \ \\n /tools>\\n\\nIf you choose to call a function ONLY reply in the following format with NO suffix:\\n\\n tool_call>\\n function=example_function_name>\\n parameter=example_parameter_1>\\nvalue_1\\n /parameter>\\n parameter=example_parameter_2>\\nThis is the value for the second parameter\\nthat can span\\nmultiple lines\\n /parameter>\\n /function>\\n /tool_call>\\n\\n IMPORTANT>\\nReminder:\\n- Function calls MUST follow the specified format: an inner function=...>\\n...\\n /function> block must be nested within tool_call>\\n...\\

**Article:** http://modelscope.cn/models/stepfun-ai/Step-3.7-Flash

Step-3.7-Flash

**Article:** http://platform.stepfun.ai

StepFun Open Platform API Platform Home Step Plan Documentation Experience Center Studio Experience Center StepFun Sign In Step 3.7 Flash A High-Efficiency Flash Model For Real-World Agents Multimodal Understanding Action / Web Visual Search Enhancement / Reliable Tool Use Orchestration / Agent Ecosystem Compatibility Learn More Start Now Step Plan Step Plan Build from Coding to Agents Smart Multi-model Routing / Multimodal / Compatible With Mainstream Agent Frameworks Learn More Start Now Step Image Edit 2 Image Editing Generation Model 19B lightweight architecture / Natural-language image editing / Leading open-source quality Learn More Start Now StepAudio 2.5 TTS Context-aware Speech Synthesis Model Dual-level Context Control / Zero-shot Voice Cloning / Human-like Voice Learn More Start Now Join partners. Accelerate AI application landing A Powerful Platform for Building AI Apps Step API · Stable · High-Performance · Easy Integration. Leading models and tools to accelerate the deployment of your next AI app. Language Models Audio Models Multimodal / GUI Models Large Language Model Step 3.7 Flash High-efficiency Flash model for production-grade agents Learn More Start Now Multimodal Understanding Action Understands images across the full range — product UIs, documents, charts, and natural scenes — then writes code or calls tools to act on what it sees. Web Visual Search Enhancement Web search reaches further — more sources, deeper follow-up. Visual search recognizes what ot

**Article:** http://static.stepfun.com/blog/step-3.7-flash/

Step 3.7 Flash â A high-efficiency Flash model for Real-World Gallery Agentic Coding Enterprise Search Agents That Can See Benchmarks Availability Join us Try Step 3.7 Flash 2026-05-29 Step 3.7 Flash The new frontier is agent efficiency. A high-efficiency Flash model for real-world agents. Multimodal Understanding & Actionï½Web & Visual Search Enhancementï½Reliable Tool Use & Orchestrationï½Agent Ecosystem Compatibility GitHub HuggingFace ModelScope Key Features Native Multimodal Understanding Acting Understands images across the full range â product UIs, documents, charts, and natural scenes â then writes code or calls tools to act on what it sees. Web Visual Search Enhancement Web search reaches further â more sources, deeper follow-up. Visual search recognizes what other systems don't â long-tail entities, freshly emerged concepts. Reliable Tool Use Orchestration Drives terminals, browsers, Office tools, search, and beyond â staying coherent however long the run gets. Less drift, fewer broken toolcalls, fewer failed runs. Agent Ecosystem Compatibility Works with mainstream harnesses (Claude Code, KiloCode, Hermes Agent, OpenClaw) and Skills â lower integration cost, less workflow rewiring. Agentic Coding SWE-Bench Pro 65 35 5 S ';"> 56.3 Step 3.7 Flash Score: 56.3 Params: 196B S ';"> 51.3 Step 3.5 Flash Score: 51.3 Params: 196B D ';"> 55.6 DeepSeek V4 Flash Score: 55.6 Params: 284B G ';"> 55.1 Gemini 3.5 Flash Score: 55.1 Params: Unknown G ';"> 58.6 GPT 5.

---


---
*Twitter farmer | 2026-05-30 AFTERNOON | 3 tweets | 7 articles*