import os, sys
[sys.path.append(i) for i in ['.', '..']] # allow imports from root dir

# print os.path.abspath(os.path.join(yourpath, os.pardir))

ROOT_DIR = os.path.dirname(os.path.abspath('pokemon_nerd'))
APP_DIR = os.path.join(ROOT_DIR,'pokemon_nerd')
DATA_DIR = os.path.join(APP_DIR, 'data')
CSV_PATH = os.path.join(DATA_DIR, 'pokemon.csv') 
DICTIONARY_PATH = os.path.join(DATA_DIR, 'pocketsphinx/1827.dic')
LANGUAGE_MODEL_PATH = os.path.join(DATA_DIR, 'pocketsphinx/1827.lm')
ACOUSTIC_DIRECTORY = os.path.join(DATA_DIR, 'pocketsphinx/acoustic-model')
