import speech_recognition as sr
from pyaudio import *
from pocketsphinx import *

def listen():
    acoustic_parameters_directory = "pocketsphinx/acoustic-model"
    language_model_file = "pocketsphinx/1827.lm" 
    phoneme_dictionary_file = "pocketsphinx/1827.dic"
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source,duration=0.5)
        #r.energy_threshold = 4000
        r.dynamic_energy_threshold = True  
        print("say anything : ")
        audio= r.listen(source)
        try:
            text = r.recognize_sphinx(audio, language=(acoustic_parameters_directory, language_model_file, phoneme_dictionary_file))
        except:
            text = "sorry, could not recognise"
        return text
