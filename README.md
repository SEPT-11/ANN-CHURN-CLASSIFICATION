# 📊 ANN Churn Classification

This repository contains an **Artificial Neural Network (ANN)**-based churn classification model.  
It predicts whether a customer is likely to churn (leave) based on various features.  
The model is deployed with **Streamlit** for an interactive web-based experience.

---

## 🚀 Live Demo

🔗 **[Try the Churn Classification App Here](https://ann-churn-classification-yzq2dapzzw8x7appdawj3mg.streamlit.app)**  

> ⚠️ **Note:** Please explore the app thoroughly and test different inputs to see the model in action!

---

## 📌 Features
- **Data Preprocessing**: Handles missing values, categorical encoding, and feature scaling.
- **ANN Model**: Multi-layer architecture for binary classification.
- **Model Evaluation**: Accuracy.
- **Interactive UI**: Powered by **Streamlit** for easy input and real-time predictions.

---

## 🛠️ Tech Stack
- **Python**
- **TensorFlow / Keras**
- **Scikit-learn**
- **Pandas / NumPy**
- **Streamlit** for deployment

---

## 📂 Repository Structure
```bash
├── .devcontainer/ # Dev environment setup (if applicable)
├── Churn_Modelling.csv # Raw dataset used for training
├── Prediction.ipynb # Notebook for running predictions
├── annprojectimplement.ipynb # Notebook covering full pipeline (EDA, training, evaluation)
├── app.py # Streamlit application script
├── model.h5 # Pretrained ANN model
├── scaler.pkl # Preprocessing scaler object
├── label_encoder_gender.pkl # Label encoder for gender
├── one_hot_encoder_geo.pkl # One-hot encoder for geography
├── requirements.txt # Python dependencies
├── runtime.txt # Runtime specification (for platforms like Heroku)
└── README.md # Project documentation (you are here)

