import os
import requests
from typing import Dict
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


class LLMAdapter:
    """
    LLM Adapter using Google Gemini 2.5 Flash (CORRECT API)
    """

    def __init__(self, model: str = "gemini-2.5-flash"):
        self.model = model

    def complete(self, prompt: str, **kwargs) -> Dict:
        # Hard fallback if key missing
        if not GOOGLE_API_KEY:
            return {
                "text": "कृपया अपनी जानकारी साझा करें।",
                "raw": None,
            }

        try:
            url = (
                f"https://generativelanguage.googleapis.com/v1beta/models/"
                f"{self.model}:generateContent?key={GOOGLE_API_KEY}"
            )

            payload = {
                "contents": [
                    {
                        "role": "user",
                        "parts": [{"text": prompt}],
                    }
                ],
                "generationConfig": {
                    "temperature": kwargs.get("temperature", 0.2),
                    "maxOutputTokens": kwargs.get("max_tokens", 512),
                },
            }

            resp = requests.post(url, json=payload, timeout=15)
            resp.raise_for_status()
            data = resp.json()

            text = ""
            if "candidates" in data and data["candidates"]:
                parts = data["candidates"][0].get("content", {}).get("parts", [])
                if parts and "text" in parts[0]:
                    text = parts[0]["text"]

            # Guaranteed non-empty response
            return {
                "text": text if text else "कृपया अपनी जानकारी साझा करें।",
                "raw": data,
            }

        except Exception as e:
            print(" Gemini API error:", e)
            return {
                "text": "कुछ तकनीकी समस्या आई है, कृपया फिर से प्रयास करें।",
                "raw": None,
            }
