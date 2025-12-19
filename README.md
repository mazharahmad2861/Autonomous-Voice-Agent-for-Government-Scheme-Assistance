# Voice-Agent-Hindi

Voice-first, agentic AI assistant for Indian public welfare scheme identification and application — full voice pipeline in Hindi (STT → LLM → TTS) with Planner–Executor–Evaluator loop, tools, memory, and failure handling.

## Features
- Voice-first interaction in Hindi (input and output)
- Planner–Executor–Evaluator agent loop
- Tools: eligibility engine, mock government API, retrieval system
- Conversation memory (SQLite) and contradiction handling
- Failure and clarifying question handling

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
