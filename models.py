# models.py

import os
import tensorflow as tf


def load_generator(model_path):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at: {model_path}")

    generator = tf.keras.models.load_model(model_path, compile=False)
    print("✅ Generator model loaded successfully")

    return generator
