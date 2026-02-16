# main.py

from config import MODEL_PATH, DEFAULT_SAMPLES
from models import load_generator
from evaluate import generate_and_save_ecg


def main():
    generator = load_generator(MODEL_PATH)
    generate_and_save_ecg(generator, DEFAULT_SAMPLES)
    print("\n✅ Process Complete.")


if __name__ == "__main__":
    main()
