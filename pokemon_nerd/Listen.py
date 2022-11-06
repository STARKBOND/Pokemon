from paths import ACOUSTIC_DIRECTORY, LANGUAGE_MODEL_PATH, DICTIONARY_PATH
import speech_recognition as sr
from pyaudio import *
from pocketsphinx import *

def listen():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source,duration=0.5)
        r.energy_threshold = 4000
        r.dynamic_energy_threshold = True  
        print("say anything : ")
        audio= r.listen(source)
        try:
            text = r.recognize_sphinx(audio, language=(ACOUSTIC_DIRECTORY, LANGUAGE_MODEL_PATH, DICTIONARY_PATH))
        except:
            text = "sorry, could not recognise"
        return text
