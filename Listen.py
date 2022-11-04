import speech_recognition as sr
from pyaudio import *
from pocketsphinx import *

def listen():
    acoustic_parameters_directory = "/usr/local/lib/python3.10/site-packages/speech_recognition/pocketsphinx-data/en-US/acoustic-model"
    language_model_file = "1827.lm" 
    phoneme_dictionary_file = "1827.dic"
    # config = Config(lm="1827.lm", dict="1827.dic")
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source,duration=0.5)
        r.energy_threshold = 400
        print("say anything : ")
        audio= r.listen(source)
        try:
            text = r.recognize_sphinx(audio, language=(acoustic_parameters_directory, language_model_file, phoneme_dictionary_file))
            print(text)
        except:
            print("sorry, could not recognise")
pass
# Install a pip package in the current Jupyter kernel
# import sys
# !{sys.executable} -m pip install SpeechRecognition
# !{sys.executable} -m pip install PyAudio
# !{sys.executable} -m pip install google
# !{sys.executable} -m pip install --upgrade google-api-python-client
# !{sys.executable} -m pip install google-cloud-speech
# !{sys.executable} -m pip install pocketsphinx