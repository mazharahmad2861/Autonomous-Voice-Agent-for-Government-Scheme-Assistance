import os
from typing import Tuple

# Try Vosk first (offline), fallback to SpeechRecognition (Google) if model missing

try:
    from vosk import Model, KaldiRecognizer
    import json
    VOSK_AVAILABLE = True
except Exception:
    VOSK_AVAILABLE = False

import speech_recognition as sr


class STT:
    def __init__(self, language: str = "hi-IN", vosk_model_path=r'C:\path\to\vosk-model'):
        self.language = language
        self.vosk_model = None
        if VOSK_AVAILABLE and vosk_model_path and os.path.exists(vosk_model_path):
            self.vosk_model = Model(vosk_model_path)

    def transcribe_from_audio_file(self, path: str) -> Tuple[str, float]:
        # Returns (transcript, confidence)
        if self.vosk_model:
            with open(path, "rb") as f:
                rec = KaldiRecognizer(self.vosk_model, 16000)
                data = f.read()
                rec.AcceptWaveform(data)
                res = json.loads(rec.Result())
                text = res.get("text", "")
                # Vosk doesn't always give confidence; use 0.9 if non-empty
                conf = 0.9 if text else 0.0
                return text, conf
        # Fallback: SpeechRecognition using Google Web Speech
        r = sr.Recognizer()
        with sr.AudioFile(path) as source:
            audio = r.record(source)
        try:
            text = r.recognize_google(audio, language=self.language)
            return text, 0.85
        except sr.UnknownValueError:
            return "", 0.0
        except Exception:
            return "", 0.0

    def transcribe_from_microphone(self, timeout: float = 5.0) -> Tuple[str, float]:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout=timeout)
        try:
            text = r.recognize_google(audio, language=self.language)
            return text, 0.85
        except sr.UnknownValueError:
            return "", 0.0
        except Exception:
            return "", 0.0
