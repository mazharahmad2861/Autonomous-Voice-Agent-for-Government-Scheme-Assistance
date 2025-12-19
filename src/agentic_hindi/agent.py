from .llm import LLMAdapter
from .tools.eligibility import load_schemes, check_eligibility
from .memory import Memory
from .retrieval import Retriever
from .tts import speak
import requests
import os


class Agent:
    def __init__(self, lang='hi', api_base_url: str = None):
        self.llm = LLMAdapter()
        self.memory = Memory()
        self.retriever = Retriever()
        self.schemes = load_schemes()
        self.lang = lang
        # API base URL for submitting applications (can be overridden by env/API_BASE_URL)
        self.api_base_url = api_base_url or os.getenv('API_BASE_URL', 'http://localhost:5002')

    def planner(self, user_text: str) -> str:
        # Prompt in Hindi to ask what info is missing, propose steps
        prompt = f"आप यूजर के प्रश्न का सार लें और बताइए अगला आवश्यक कदम क्या है। यूजर: {user_text}"
        resp = self.llm.complete(prompt)
        return resp.get("text", "कृपया अपनी जानकारी साझा करें।")


    def executor(self, user_info: dict):
        # Check eligibility with tool
        matches = check_eligibility(user_info, self.schemes)
        return matches

    def evaluator(self, result):
        # Evaluate if result is conclusive in Hindi
        if not result:
            return "ऐसा लगता है कि आपके पाए गए किसी भी योजना के लिए आप अभी अर्ह नहीं हैं। क्या आप अपनी जानकारी अपडेट करना चाहेंगे?"
        return f"मुझे {len(result)} उपयुक्त योजनाएँ मिलीं। क्या मैं आपके लिए आवेदन कर दूँ?"

    def apply_scheme(self, scheme_id: str, applicant: dict):
        # call configured API (supports test endpoints like httpbin.org)
        try:
            if 'httpbin.org' in self.api_base_url:
                url = self.api_base_url.rstrip('/') + '/post'
            else:
                url = self.api_base_url.rstrip('/') + '/apply'
            r = requests.post(url, json={'scheme_id': scheme_id, 'applicant': applicant}, timeout=10)
            r.raise_for_status()
            data = r.json()
            # If using httpbin, the echoed JSON is under 'json' key — adapt response
            if 'httpbin.org' in self.api_base_url:
                return {'status': 'ok', 'application_id': 'httpbin-1', 'raw': data}
            return data
        except Exception as e:
            return {'status': 'error', 'message': str(e)}

    def handle_user(self, user_text: str, user_info: dict = None):
        # Planner
        plan_text = self.planner(user_text)
        # If user_info missing, ask for it
        if user_info is None:
            return plan_text
        matches = self.executor(user_info)
        eval_text = self.evaluator(matches)
        # Save to memory
        self.memory.add_turn(user_text, eval_text)
        return eval_text, matches
