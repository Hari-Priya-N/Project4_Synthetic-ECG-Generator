# evaluate.py

import os
from config import SAVE_DIR, LATENT_DIM
from utils import generate_latent_noise, save_plot, save_raw_data


def generate_and_save_ecg(generator, n_samples):
    print(f"\n--- Generating {n_samples} ECG Samples ---")

    z = generate_latent_noise(n_samples, LATENT_DIM)
    generated_ecg = generator(z, training=False).numpy()

    # Save individual plots
    for i in range(n_samples):
        signal = generated_ecg[i].squeeze()

        plot_path = os.path.join(SAVE_DIR, f"sample_{i + 1}.png")
        save_plot(signal, plot_path,
                  title=f"Synthetic ECG Signal - Sample {i + 1}")

        print(f"Saved plot to: {plot_path}")

    # Save raw numpy batch
    data_path = os.path.join(SAVE_DIR, "generated_ecg_batch.npy")
    save_raw_data(generated_ecg, data_path)

    print(f"✅ Raw data saved to: {data_path}")
