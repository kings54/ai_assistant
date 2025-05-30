# whisper_utils.py
import whisper
from config import WHISPER_MODEL

def listen_whisper(audio_file):
    model = whisper.load_model(WHISPER_MODEL)
    result = model.transcribe(audio_file)
    return result['text']
