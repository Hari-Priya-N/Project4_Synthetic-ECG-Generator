# Project-4_Synthetic-ECG-Generator 
## Group Project  
- Team Members:  Likitha , MD Lathif , Sruthika , Navadeep , Hari Priya 

---

## Overview  

This project focuses on generating synthetic ECG (Electrocardiogram) signals using a Vanilla Generative Adversarial Network (GAN).  
In medical AI systems, ECG datasets are often limited due to privacy concerns and data collection challenges. This project addresses that problem by learning the distribution of real ECG signals and generating realistic synthetic ECG waveforms for data augmentation and research purposes.
The generated synthetic signals can help improve the robustness and performance of ECG classification and anomaly detection systems.

---

## Project Objectives  

- Learn the distribution of real ECG signals  
- Generate realistic synthetic ECG waveforms  
- Augment limited medical datasets  
- Improve generalization of ECG classification models  
- Provide a reusable GAN-based ECG generation framework  

---
## Training Workflow  

1. Load ECG dataset  
2. Preprocess signals (normalize, reshape, scale)  
3. Initialize Generator and Discriminator  
4. Train GAN using adversarial learning  
5. Generate synthetic ECG samples  
6. Save trained generator model  

---

## Project Folder Structure  

Project4_Synthetic-ECG-Generator/

├── src/
│   ├── ecg_data_loader.py          
│   ├── preprocess_ecg.py           
│   ├── ecg_generator.py            
│   ├── ecg_critic.py              
│   ├── wgan_ecg_model.py           
│   ├── train_wgan_ecg.py           
│   ├── ecg_signal_metrics.py       
│   ├── clinical_validity_eval.py   
│   ├── ecg_classifier_train.py     
│   ├── ecg_classifier_eval.py      
│   ├── inference_ecg.py            
│   ├── app_ecg_wgan.py             
│   ├── api_ecg_wgan.py            
│   └── utils/
│       ├── metrics.py              # Loss & evaluation metrics
│       ├── logger.py               
│       └── visualizer.py           
│
├── checkpoints/                    
├── generated_ecg_samples/          # Generated synthetic ECG signals
├── figures/                        # Training plots & comparisons
├── configs/                        
└── docs/                         


---

## Module-Wise Description  

### 🔹 Module 1 — Data Pipeline & Preprocessing  
MD Lathif  

- Load ECG signals  
- Normalize signal amplitude  
- Reshape into fixed-length segments  
- Scale values to [-1, 1]  

---

### 🔹 Module 2 — Model Design  
Navadeep 

### Generator  
- Input: Random noise vector  
- Fully connected layers  
- ReLU activation  
- Tanh output layer  
- Generates synthetic ECG waveform  

### Discriminator  
- Binary classifier  
- Uses LeakyReLU activation  
- Distinguishes between real and synthetic ECG signals  

###  Loss & Optimization  

- Binary Cross Entropy (BCE) Loss  
- Adam Optimizer  
- Adversarial training approach
  
---

### 🔹 Module 3 — Training Pipeline  
Sruthika  

- Implement adversarial learning loop  
- Train Discriminator first  
- Train Generator to fool Discriminator  
- Monitor training loss  

---

### 🔹 Module 4 — Evaluation & QA  
Balusupalli Likitha

- Visual comparison of real vs synthetic ECG  
- Check waveform smoothness  
- Detect mode collapse  
- Evaluate diversity  

---

### 🔹 Module 5 — Deployment Layer  
Hari Priya  

- Load trained Generator model  
- Generate required number of ECG signals  
- Save generated ECG samples  
- Provide practical usability  

---

### 🔹 Module 6 — Monitoring & Updates  

- Real-time loss tracking  
- Performance monitoring  
- Model version tracking  
- Adaptive hyperparameter tuning  

---

## Dataset  
-  https://www.kaggle.com/datasets/taejoongyoon/mitbit-arrhythmia-database

ECG dataset used for training contains real electrocardiogram waveform recordings.  

The dataset is preprocessed before feeding into the GAN model to ensure stable training and realistic signal generation.

---

## Technologies Used  

- Python  
- PyTorch  
- NumPy  
- Matplotlib  
- OpenCV   
- Vanilla GAN  

---
#  Results
---
#  Conclusion
---


---
