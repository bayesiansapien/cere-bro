---
source: farmer/rss
feed: pragmatic-engineer
farmed: 2026-09-23T07:54:50.952582+00:00
title: 'How will AI change operating systems? Part 2: Windows'
url: https://newsletter.pragmaticengineer.com/p/windows-and-ai
published: 2026-09-22
author: 'Gergely Orosz'
---

# How will AI change operating systems? Part 2: Windows

AI is changing how us software engineers build software, and developers’ tool preferences are rapidly evolving with it – like how AI coding harnesses have gotten very popular. Likewise, future versions of the world’s leading operating systems look certain to feature more support for agentic tools. 

 To find out how things are changing, we talked with the folks at tech giant Microsoft who shared in detail their plan for Windows, and how AI will play a part. It comes after the company’s previous AI efforts led to it being dubbed “Microslop” by some users online. 

 The Windows team’s vision is opinionated and includes building new agentic primitives, alongside reversing some decisions that have annoyed engineers. Microsoft wants developers who have shunned the system to return. The big question is: will it succeed? 

 For more, check out a previous article on how the leading Linux distribution, Ubuntu, is changing, thanks to AI , with a focus on hardware support for GPUs, NPUs and DPUs, a bet on local-first LLMs, and a focus on AI developer tools. 

 Today, we cover: 

 How many devs use Windows anyway? It’s hard to get exact numbers, but macOS appears far more popular at startups than Windows, while Linux may also be on track to overtake Microsoft’s OS in developer popularity. 

 Agent identity & discovery. Windows ships with native support for agent identification, plus a centralized registry of locally available MCP servers to be included with the OS. 

 Isolate agentic tools. Microsoft is building an OS-agnostic isolation mechanism that should make it easy for developers to build agents that run tools safely. 

 Running models locally : Windows is betting big on local models. WindowsML is a new hardware abstraction layer for building and running local AI models across GPU, NPU, and CPU. The OS aims to ship Small Language Models (SLMs) without requiring an NPU in the future. We’ve also seen an impressive demo of a local model running on a Surface laptop using NVIDIA chips. 

 Building agents on Windows: one goal of the OS is to allow building of agents with opinionated frameworks and libraries that devs can just assume are available. 

 More dev-friendly : Windows was plagued by questionable product decisions that resulted in a cluttered Start menu and search, to the chagrin of many developers who lost interest in the OS. Microsoft wants them back and is addressing criticisms – finally! 

 Linux on Windows (WSL): Windows ships with an embedded Linux called Windows Subsystem for Linux (WSL). It’s proving quite popular with devs. Windows embracing Linux might just be the strategy to get devs to switch from both native Linux and macOS, as counter-intuitive as this strategy sounds. 

 Windows & hardware: since its early days, Windows has gone out of its way to support a wide variety of hardware. The OS was x86-based from the beginning, but Windows on ARM is starting to finally look like a good alternative. A look into why ARM support took so long, and the upcoming NVIDIA collaboration. 

 We’ve talked with people on the Windows team to learn about the thinking behind Microsoft’s strategy for the operating system: Pavan Davuluri (EVP, Windows and Devices), Scott Hanselman (VP, Member of Technical Staff, Microsoft CoreAI and GitHub), and Logan Iyer, (CVP, Windows Platform and Developer). Many thanks for your time! 

 1. How many devs use Windows anyway? While Windows remains the most popular desktop operating system for mainstream computer users at around 63% market share as per Statcounter – the strong sense is that its popularity is down among developers. 

 Windows used to be popular with devs… A year ago, the 2025 Stack Overflow survey polled professional users’ choices of OS. It found that a minority of devs overall use Windows – although it remained the single most popular OS. Despite its top ranking in the survey, the number of devs using Windows was actually way down on Microsoft’s XP-era peak. Meanwhile, MacOS and various Linux distributions also showed considerable market share: 

 OS choice for professional use (49,000 respondents.) Source: Stack Overflow 2025 survey Then Mac started to catch up… Elsewhere, a JetBrains survey asked devs about their OS usage for developments, also last year. The results: 

 Source: State of Developer Ecosystem 2025 by JetBrains. Based on 24,500 responses Interestingly, half of devs use more than one OS for development. This JetBrains survey suggests that several devs jump between operating systems for their work. The survey also found macOS close to overtaking Windows as the most-used standalone OS for development work. 

 … and is Windows declining in developer market share? Only last week, myself and Ivan ran two social media surveys on X and on LinkedIn , most likely shown overwhelmingly to people who are also The Pragmatic Engineer readers. We offered a single choice – with no option to select multiple OS usage, Linux on Windows, or via WSL. We were surprised to find Windows in third place behind Linux, based on nearly 10,000 combined responses: 

 What OS are you using to build software on? Based on 9,937 responses, surveyed in Sep 2026 Based on current research, it’s likely that Windows’ share of the developer market is on the wane, but it’s hard to tell by how much. Inside VC-funded startups and Big Tech, it’s an open secret that Macs have been the most popular developer machine for some years now, partly thanks to the superior hardware performance of M-series CPUs, and also because these companies are not looking to save money when purchasing developer machines. It’s very likely that our own social media survey over-indexes on this group! 

 Either way, Microsoft has both market share and developer goodwill that it needs to win back. Based on what we’ve heard from them, Microsoft is attempting this. 

 But where is OS usage at with readers of The Pragmatic Engineer? To figure this out, please cast a vote on the primary operating system you use when developing software. After the vote, you can see the results: 

 With that, let’s get into how the next version of Windows intends to integrate AI agents at the OS level. 

 2. Agent identity & discovery At the operating system level, agents increasingly look like regular users. Their sessions can last hours, use multiple programs, and use OS resources like the UI and clipboard. Windows allows developers to build agentic programs that are distinguishable from users. 

 Agent identification is enabled through Entra ID , Microsoft’s tool for centralized identity management in Windows. When an agent has a local identity, it acts as if it is another user on the system as visible in the Task Manager. Below, tasks are grouped by user, and there are two users in the task manager: kirupach (a human) and V9-G4 (an agent). All observability of human users is now available for agent users as well. 

 Task Manager showing human & agent users (kirupach and V9-G4). Source: Microsoft Agents must be built with this agent identification capability in mind. Consider how a rogue agentic application can impersonate a user and not self-register as an agent – which in a sense is how viruses operate by using legitimate OS functionality for illegitimate purposes. That’s why Defender, Microsoft’s antivirus software, is becoming “agent aware” and scanning Windows for known local agent activity like it scans for viruses.

 Microsoft Defender’s AI Assets feature can scan for known agent activity. Source : Microsoft Agent discovery: agents are only as useful as the tools they’re able to interact with, and Windows On Device Agent Registry ( ODR ) is the centralized place where agents register and discover available MCP tools. ODR manages and runs MCP servers locally, and also comes with connectors for core operating system components like the File Explorer or System Settings. 

 Let’s say you want to build a specialized Photo Organizer Agent; the organizer agent organizes photos in the user’s Photos folders by theme and starts by running an image classifier to understand photos’ themes, then puts them in the relevant folder, such as ‘ parties ’, ‘ outdoors ’, ‘ baby photos ’, etc. 

 As such, the Photo Organizer Agent needs the ability to read and change the user’s local files, which starts with Windows ODR finding an MCP connector for the file access capability. After discovering File Explorer, the agent uses File Explorer MCP to access and modify files in the user’s Photo directory. 

 ODR and built-in MCPs when agents access dependencies ODR is still in development and available to beta testers, so little is known about its internals, but preliminary research by Origin Technology indicates an interesting implementation detail of ODR. By reverse engineering ODR behavior, researchers proved ODR puts itself as a proxy between the MCP client and its server. Here’s what that would look like in our updated Photo Organizer Agent example: 

 More than a registry: ODR also acts as a proxy between MCP clients and the server The Photo Organizer agent discovers the File Explorer MCP capability in the same way as in the dependencies diagram above. However, the process ID that ODR sends back to the agent is ODR itself: the Photo Organizer Agent talks to the File Explorer MCP through ODR! 

 By putting itself between the MCP client and server, ODR can inspect payloads going back and forth. This is a useful choke point because it enables Windows to detect potentially dangerous behavior. However, this proxying behaviour is as yet unconfirmed by Microsoft, so it remains to be seen how they use it. 

 3. Isolate agentic tools Tools are external programs that an agent uses to perform actions on the operating system, such as native OS tools, third-party app calls, or even programs written by an agent. Granting agents rights to execute tools potentially means code execution, so it’s essential the agent tools run in isolation to ensure the user’s files and session aren’t reachable by agentic tools. 

 Microsoft Execution Containers ( MXC ) is a new, in-development agent containment technology by Windows. Developers can use MXC to spawn agentic tools in isolated environments called sandboxes, and agent access within the sandbox environment is configured through MXC containment policies . 

 Containment policies are JSON-based config files that describe network, filesystem, UI, and execution restrictions. The image below illustrates how MXC works: 

 Agents run code with MXC in contained environments, with support for different containment tech & OSes Let’s say you’re building an agentic application like OpenClaw. This application will necessarily have to use tools to do its job and can use file operations, web operations, shell commands, and more. These are potentially dangerous operations, as OpenClaw executes them through MXC’s spawnSandboxFromConfig() method, which spawns a new contained process in which said tools can run safely. The process containment technology used depends on the containment policy config. MXC doesn’t do the containment itself and uses multiple existing containment technologies for that; for example, on a Mac, it would use seatbelt , a process containment layer built into the Mac OS. 

 Speed versus safety tradeoff: some containment mechanisms are faster to start and cheaper to run than others. For example, starting a new process is faster than starting a new Windows session or a new virtual machine. At the same time, running a new process in the existing user’s Windows session potentially exposes the user’s filesystem to the new process. 

 MXC allows developers to adapt the containment level to the sensitivity of the operation being run. Multiple containment levels are available in Windows: 

 Process containment 

 Session containment 

 Running WSL containers 

 Lightweight Hyper-V containers 

 Full virtual machines 

 Choosing the right level of containment is a trade-off between the blast radius and speed of execution. The simplified example below shows how it all comes together: 

 How developers can use MXC to contain agents The policy object specifies how the containerized workload should be constrained. It specifies network, UI, filesystem restrictions 

 The createConfigFromPolicy step configures the whole container. It takes the containment policy object, the chosen isolation level (“process”), and names the container. 

 The app then manipulates what gets executed in the “WHAT RUNS” step 

 Finally, spawnSandboxFromConfig() runs the container and processes its output. 

 OpenClaw for Windows ships as a native app and is one of the first agents to adopt MXC for isolation. Configuring the MXC containment in OpenClaw for Windows is packed as a standard windows settings screen. 

 OpenClaw Windows app containment config screen. Source: Microsoft MXC abstracts away process isolation for agents, so the OpenClaw agent in this example isn’t aware of all the restrictions its tools are running within. It can therefore encounter situations where it tries to do something its sandbox disallows. 

 OpenClaw agent describes lack of access to Windows resources like installed programs. Source: Microsoft Combined with agent identities, MXC will give enterprises fleet-wide control of their agents. For admins, Microsoft will offer MXC policy management through its Intune product for corporate device fleet management. 

 MXC enforcement isn’t broadly adopted yet, so we asked Microsoft for examples of how they use MXC internally to isolate autonomous agents. They shared some use cases with us: 

 How the Windows team uses MXC to isolate autonomous agents These cases illustrate how Microsoft is automating many internal developer chores, and how MXC provides finegrained control over agent isolation. MXC is under development, but already runs on Windows, Linux, and macOS. Developers therefore get a unified way of containing external tools across operating systems. 

 4. Running models locally Windows ML is a hardware-agnostic layer for running AI models locally on Windows. Its goal is to do for AI what DirectX did for computer graphics: abstract away hardware complexity, regardless of the underlying model’s architecture. 

 Windows ML is Microsoft’s second attempt at building a hardware-agnostic layer for running ML models. DirectML , the first attempt, is a library for running machine learning tasks on GPUs built on top of DirectX 12 , Microsoft’s graphics library used for running games on Windows, released in 2019. 

 So, an obvious question is how is Windows ML different? They say that Windows ML offers two improvements over DirectML: 

 #1: Higher level abstraction & better hardware coverage . DirectML is a low-level library where developers have to manually build the inference pipelines from simple mathematical operations, worry about memory layout, etc. Being based on DirectX, DirectML only worked with GPUs. 

 In contrast, Windows ML is based on the Open Neural Network Exchange format (ONNX), an open format for representing and running neural networks. Neural networks built with all popular machine learning frameworks can be converted into the ONNX format called ONNX graph and run on ONNX runtime . 

 ONNX runtime is an open source, cross-platform system for training and running neural nets defined in the ONNX format. Windows ML provides developers a framework that runs on a broader range of silicon, including GPUs, NPUs, and CPUs from all major vendors. 

 #2: No driver-update bottleneck: Windows ML wraps the ONNX runtime and abstracts away the hardware-specific runtime optimizations by providing hardware-agnostic APIs. Each hardware vendor implements this API for its own hardware through the Execution providers (EPs) concept. With DirectML, new runtime optimizations had to be done via driver updates which took six months to get meaningful adoption. 

 Windows ML loads EPs when they are needed, depending on the user’s hardware. For example, if a user has an NVIDIA GeForce RTX GPU, the NVIDIA Tensor RTX execution provider is downloaded and used to maximize GPU performance. Hardware vendors build and submit PEs to Microsoft for certification and testing before they can be used with Windows ML. Most execution providers available today are also available on GitHub. 

 Windows ML ecosystem layers Small language models (SLMs) are embedded within the operating system. Without them, developers would have to ship models with their apps, or call cloud-based models. Even if running local models should be easier with Windows ML, it’s still not worth the effort if you want to add simple functionalities to an app. 

 For example, running a sentiment analysis on some text in an application used to involve calling a hosted AI model in the cloud. On top of incurring app running costs, it can also add lag to the app, whereas with embedded models developers can assume the models are already there, and use them as any other local library. 

For example, the Aion-1.0-Instruct model is built into Edge, Microsoft’s web browser. Accessed through the Prompt API , Aion model allows developers to build apps like sentiment analysis with a few lines of code. Here’s an example from Microsoft’s website : 

 Local language model usage example in JavaScript ( Source ) Even a simple web application can now have LLM-powered features like sentiment analysis without having to continuously pay for tokens. The demo is JavaScript-only, but versions for native apps and other languages are also expected to be available when it’s released. 

 Teams being able to run their own models is becoming increasingly important, especially in the corporate sector, driven by escalating costs, mode availability questions such as those recently raised with Fable , and compliance issues. 

 Running models locally also unlocks a hybrid approach, which is well aligned with a trend among tech companies we recently covered , where tech companies have successfully shifted their LLM workloads to cheaper models for simpler requests, and only use frontier models for advanced reasoning. By running models locally, some agentic jobs could be executed with local LLMs, and more complex jobs delegated to a cloud-hosted frontier model. 

 Running local models on a next-gen Surface laptop with NVIDIA GPUs is impressive. At Microsoft, Scott Hanselman showed us a pre-release Surface laptop with NVIDIA GPUs running Qwen as a local model, hooked up to GitHub Copilot. This local model churned out tokens at a rate of ~40 tokens per second! Once such laptops become widely available, coding-related use cases could become a lot more viable, running locally. 

 5. Building agents on Windows Besides Windows being agent-friendly, Microsoft is also investing in the agent building toolchain to simplify agentic app development by providing a rich agent building framework. 

 
 
 Read more
