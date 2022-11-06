import os, sys, pokemon_nerd
[sys.path.append(i) for i in ['.', '..']] # allow imports from root dir

ROOT_DIR =  os.path.abspath(os.path.join(pokemon_nerd.__file__ ,"../../.."))
if 'pokemon_nerd' not in ROOT_DIR: ROOT_DIR += '\\pokemon_nerd' # Windows 
APP_DIR = os.path.join(ROOT_DIR,'pokemon_nerd')
DATA_DIR = os.path.join(APP_DIR, 'data')
CSV_PATH = os.path.join(DATA_DIR, 'pokemon.csv') 
DICTIONARY_PATH = os.path.join(DATA_DIR, 'pocketsphinx/1827.dic')
LANGUAGE_MODEL_PATH = os.path.join(DATA_DIR, 'pocketsphinx/1827.lm')
ACOUSTIC_DIRECTORY = os.path.join(DATA_DIR, 'pocketsphinx/acoustic-model')
