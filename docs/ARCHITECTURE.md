# Architecture — Voice-Agent-Hindi 🔧

## Overview
A voice-first agentic system that operates entirely in Hindi. Core components:
- STT (Vosk or Google SpeechRecognition) — transcribe Hindi speech
- LLM Adapter (OpenAI or fallback) — perform Hindi reasoning and planning
- Planner–Executor–Evaluator loop — agentic workflow
- Tools: eligibility engine (rule-based), mock government API (Flask), retrieval (sentence-transformers + FAISS)
- Memory (SQLite) — conversation history and contradiction handling
- TTS (gTTS) — Hindi voice output

## Agent Lifecycle
1. Listen (STT) → get user utterance in Hindi
2. Planner (LLM) → produce next step / query in Hindi
3. Executor → call tools (eligibility, retrieval) as needed
4. Evaluator → assess results and decide next action
5. Act → ask clarification, apply to scheme via mock API, or speak a response
6. Save to memory

## Failures & Recovery
- Low STT confidence → ask user to repeat
- Missing fields → ask targeted clarifying question (age, income, employment)
- Tool/API error → inform user and offer alternative

## Prompts
All prompts to the LLM are written in Hindi and request explicit short plans or actions.

## Diagram
(See docs/diagrams/ for sequence and component diagrams — simple ASCII for now)

