from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import tempfile
import os


def speak(text: str, lang: str = "hi"):
    """Synthesize Hindi speech and play it."""
    tts = gTTS(text=text, lang=lang)
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        tts.write_to_fp(f)
        tmp = f.name
    sound = AudioSegment.from_file(tmp, format="mp3")
    play(sound)
    os.remove(tmp)
