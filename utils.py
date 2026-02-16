# utils.py

import tensorflow as tf
import numpy as np
import os
import matplotlib.pyplot as plt


def generate_latent_noise(n_samples, latent_dim):
    return tf.random.normal((n_samples, latent_dim))


def save_plot(signal, save_path, title="Synthetic ECG Signal"):
    plt.figure(figsize=(10, 3))
    plt.plot(signal)
    plt.title(title)
    plt.xlabel("Time")
    plt.ylabel("Amplitude")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(save_path)
    plt.close()


def save_raw_data(data, save_path):
    np.save(save_path, data)
