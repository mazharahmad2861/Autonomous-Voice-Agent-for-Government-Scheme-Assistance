# Setup instructions

1. Create virtualenv and install requirements:

   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt

2. Optional: Download Vosk Hindi model (offline STT)
   - Visit https://alphacephei.com/vosk/models and download a Hindi model (e.g., `vosk-model-small-hi-0.4`)
   - Extract and set path when constructing the STT class

3. Run mock API (in one terminal):
   python -m src.agentic_hindi.tools.mock_api

4. Run demo:
   python run_demo.py

Notes:
- If you want to use OpenAI, set OPENAI_API_KEY in `.env` file.
- gTTS requires internet.
