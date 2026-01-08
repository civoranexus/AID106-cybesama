import whisper
import tempfile
import sounddevice as sd
from scipy.io.wavfile import write

model = whisper.load_model("small")

def record_audio(duration=5, fs=16000):
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    return fs, audio

def speech_to_text(audio_input=None, language="en"):
    """
    Records voice and converts to text
    """
    fs, audio = record_audio()

    with tempfile.NamedTemporaryFile(suffix=".wav") as f:
        write(f.name, fs, audio)
        result = model.transcribe(f.name, language=language)

    return result["text"]
