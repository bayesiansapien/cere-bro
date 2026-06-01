# Engineering Voice Agents: Latency, Quality, and Scale — Rishabh Bhargava (Together AI)

**Channel:** AI Engineer  
**Published:** May 31, 2026  
**Source:** https://www.youtube.com/watch?v=N7b1PJc7SFc  

## TL;DR
Rishabh Bhargava (Head of Voice AI at Together AI) outlines the engineering challenges of building high-performance voice agents, emphasizing that sub-500ms latency is the "north star" for natural interaction. While the industry is shifting toward end-to-end speech-to-speech models, the modular "cascaded" pipeline (STT → LLM → TTS) remains the production standard due to superior instruction following and tool-calling reliability.

## Key Takeaways
- **The 300ms Threshold:** Humans respond to cues in ~300ms. For AI, exceeding 500ms results in a disjointed "walkie-talkie" experience.
- **Pipeline Dominance:** The STT → LLM → TTS architecture allows for surgical optimization. Current state-of-the-art targets are ~100ms for STT, <300ms TTFT for LLMs (8B-30B parameters), and sub-100ms for TTS.
- **Co-location is King:** Network latency (e.g., US West to Europe) can add 75ms+ per hop. Moving the orchestrator and models into the same data center can reduce total latency by 30%.
- **Architectural Patterns:** The "Thinker-Talker" pattern (small LLM for conversational filler/guardrails, large LLM for tool execution) is emerging as a solution for balancing speed and intelligence.
- **Future Outlook:** Native speech-to-speech models (like OpenAI's Realtime API or Nvidia's Nemotron-3 VoiceChat) will eventually replace pipelines by enabling full-duplex communication and emotional nuance.

## Core Architecture & Research Claims
- **Streaming Native STT:** Moving away from 30s batch models (Whisper) to streaming encoders (like Nvidia Parakeet-TDT) that use minimal look-ahead (80ms) and cache activations to save compute.
- **LLM Size Sweet Spot:** Models between 8B and 30B parameters are ideal for voice. Larger models break the latency budget, while smaller ones struggle with complex tool-calling and instruction following.
- **Turn Detection:** Still an "unsolved" engineering problem. Relying on simple silence detection leads to awkward interruptions; the next frontier is using the LLM/S2S model to predict intent-to-pause vs. intent-to-end.

## Grounded Context (Web Enrichment)
As of June 1, 2026, the landscape has rapidly advanced since this talk was recorded. Together AI has formally integrated **Deepgram Nova-3** and optimized **Parakeet-TDT v3**, enabling transcribing 20 hours of audio in under 10 seconds. Their co-located stack now consistently achieves end-to-end latency below 300ms, effectively meeting Rishabh's "north star" for production agents.

Furthermore, the industry transition to speech-to-speech (S2S) mentioned as "future" is arriving faster than anticipated. Today (June 1, 2026), NVIDIA unveiled the **RTX Spark** chip at Computex, designed to run 12B-parameter S2S models like **Nemotron-3 VoiceChat** locally with sub-200ms latency. While Bhargava correctly noted that cascaded pipelines are better for tool-calling, newer models like **Gemini 3.1 Flash Live** and **GPT-Realtime-2** are closing the reasoning gap, suggesting that 2027 may see the final obsolescence of the cascaded architecture for high-end consumer applications.
