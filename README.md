# 📰 Fake News Detection using LSTM (Deep Learning)

A deep learning-based web app to detect whether a news headline is **Fake** or **Real** using an LSTM neural network.  
Built with TensorFlow, Flask, and deployed locally with a clean Tailwind-powered UI.

## 🚀 Overview

Fake news is a rising concern in the digital era. This project aims to automatically classify news as *real* or *fake* using a Recurrent Neural Network (RNN) with LSTM layers, trained on a public dataset of news headlines.

## 📊 Model Performance

| Metric         | Score    |
|----------------|----------|
| Training Acc.  | 99.70%   |
| Validation Acc.| ~92%     |
| Test Accuracy  | 89.00%   |
| Model Type     | LSTM RNN |
| Dataset Used   | WELFake (Kaggle) |
| Input Type     | News Title |
| Preprocessing  | Stopwords Removal, Stemming, Tokenization, Padding |

📌 *Trained on ~62k news titles (balanced real/fake dataset)*

## 🧠 Tech Stack

- **Frontend:** HTML + Tailwind CSS
- **Backend:** Flask + REST API
- **ML/DL:** TensorFlow + Keras
- **Data:** Pandas, NLTK
- **Model:** LSTM with Embedding Layer

## 🗂️ Project Structure

fake-news-detector/
├── app.py # Flask API
├── model/ # Saved .keras model
├── templates/
│ └── index.html # UI with Tailwind
├── model.ipynb # Training notebook (LSTM)
├── requirements.txt
├── .gitignore
└── README.md

## 🔮Future Improvements
1) Replace LSTM with BERT/Transformers

2) Deploy via Render / HuggingFace Spaces

3) Train on a custom, current news dataset

4) Add explainable AI (XAI): Why was a news headline marked fake?

5) Add multilingual support (Hindi, etc.)

## 🧠 Author
Raghu Raj (NIT Jamshedpur)
Passionate about AI, ML, and building things that matter.