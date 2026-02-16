# config.py

import os

MODEL_PATH = r"D:\Downloads\Project4\CheckPoints\ECG_Generator_PhysioNet_Final.h5"
SAVE_DIR = r"D:\Downloads\Project4\Generated_Outputs"

LATENT_DIM = 100
SEQ_LEN = 1248
DEFAULT_SAMPLES = 5

os.makedirs(SAVE_DIR, exist_ok=True)
