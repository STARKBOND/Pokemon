import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
APP_DIR = os.path.join(ROOT_DIR,'src/pokemon_nerd')
DATA_DIR = os.path.join(APP_DIR, 'data')
CSV_PATH = os.path.join(DATA_DIR, 'pokemon.csv') 
DICTIONARY_PATH = os.path.join(DATA_DIR, 'pocketsphinx/1827.dic')
LANGUAGE_MODEL_PATH = os.path.join(DATA_DIR, 'pocketsphinx/1827.lm')
ACOUSTIC_DIRECTORY = os.path.join(DATA_DIR, 'pocketsphinx/acoustic-model')
