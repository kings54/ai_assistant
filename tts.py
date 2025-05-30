# tts.py
import pyttsx3
from gtts import gTTS
import os

engine = pyttsx3.init()

def speak(text, use_gtts=False):
    if use_gtts:
        tts = gTTS(text=text, lang='en')
        tts.save("response.mp3")
        os.system("start response.mp3")
    else:
        engine.say(text)
        engine.runAndWait()
