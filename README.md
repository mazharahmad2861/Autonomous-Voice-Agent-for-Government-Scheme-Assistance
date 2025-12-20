# Voice-Agent-Hindi

Voice-first, agentic AI assistant for Indian public welfare scheme identification and application — full voice pipeline in Hindi (STT → LLM → TTS) with Planner–Executor–Evaluator loop, tools, memory, and failure handling.

## 🎯 Problem Statement

In India, a large number of citizens are **unaware of government welfare schemes** they are eligible for. Even when information is available, users face several challenges:

- Most government portals are **text-heavy and English-centric**
- Eligibility rules are **complex and difficult to understand**
- Users must navigate multiple websites and forms
- Limited accessibility for **rural and non-technical users**
- No guided, conversational assistance for scheme discovery

As a result, many eligible citizens **fail to benefit from public welfare programs**.

### Proposed Solution

This project addresses the problem by building a **voice-first, agentic AI system** that:

- Allows users to **interact using spoken Hindi**
- Understands user intent through natural conversation
- Collects required information step-by-step
- Automatically checks eligibility using rule-based logic and APIs
- Guides users with clear, spoken responses
- Maintains conversational context and handles errors gracefully

The solution focuses on **accessibility, automation, and intelligent decision-making**, making public welfare information easier to discover and understand.


## Features
- Voice-first interaction in Hindi (input and output)
- Planner–Executor–Evaluator agent loop
- Tools: eligibility engine, mock government API, retrieval system
- Conversation memory (SQLite) and contradiction handling
- Failure and clarifying question handling

## 🔍 Architecture Explanation

### 1. Voice Interface
- Converts spoken **Hindi voice input** into text using **Speech-to-Text (STT)**
- Converts the final system response back into **Hindi speech** using **Text-to-Speech (TTS)**
- Ensures a complete **voice-first interaction pipeline**

---

### 2. Planner
- Uses a **Large Language Model (LLM)** to understand user intent
- Analyzes conversation context and identifies **missing or required information**
- Generates a **structured action plan** instead of producing a direct response

---

### 3. Executor
- Executes the plan created by the Planner
- Calls external tools such as:
  - Eligibility checking logic
  - Scheme databases or mock government APIs
- Maintains a clear separation between **reasoning (Planner)** and **execution (Executor)**

---

### 4. Memory Layer
- Stores user responses and conversation state using **SQLite**
- Enables **multi-turn conversations**
- Detects contradictions and avoids repeated questions
- Provides persistent conversational context

---

### 5. Evaluator
- Validates outputs received from tools
- Detects failures, incomplete information, or inconsistencies
- Triggers **re-planning or clarification questions** when needed
- Ensures robustness and fault tolerance in the agent workflow

---

## 🛠️ Technology Stack

- **Python**
- **Large Language Models (OpenAI / Google API with fallback support)**
- **Speech-to-Text (STT) & Text-to-Speech (TTS)**
- **SQLite** (Conversation memory storage)
- **Agentic AI Design Patterns (Planner–Executor–Evaluator)**
  

## Quickstart (dev)
1. Create a Python 3.10+ virtualenv
2. pip install -r requirements.txt
3. Download optional Vosk Hindi model (see `docs/setup.md`)
4. Run demo: `python run_demo.py --lang hi`

Note: Start the mock API first with `python -m src.agentic_hindi.tools.mock_api` in another terminal.

Google services: If you set `GOOGLE_API_KEY` in your environment or `.env`, the agent will prefer Google Generative API (Text-Bison) for reasoning and planning in Hindi. If `GOOGLE_API_KEY` is not present but `OPENAI_API_KEY` is set, the agent will use OpenAI as a fallback.


Tip: You can point the agent to another API for testing. Set `API_BASE_URL` in `.env` or as an environment variable. Example (PowerShell):

```powershell
$env:API_BASE_URL = 'https://httpbin.org'
python run_demo.py --lang hi
```

When `API_BASE_URL` points to `https://httpbin.org`, the agent will POST to `https://httpbin.org/post` for quick request tests.

Full setup, architecture docs, and evaluation transcripts are in `docs/`.
