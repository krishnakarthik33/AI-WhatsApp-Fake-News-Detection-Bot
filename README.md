# AI-WhatsApp-Fake-News-Detection-Bot
An AI-powered WhatsApp chatbot designed to detect fake news in real-time using Natural Language Processing and Machine Learning. The system leverages TF-IDF vectorization and a Logistic Regression model (~95% accuracy) to classify news as REAL or FAKE.
# 🤖 AI WhatsApp Fake News Detection Bot

An AI-powered WhatsApp chatbot that detects whether a news message is REAL or FAKE using Natural Language Processing (NLP) and Machine Learning.

---

## 🚀 Project Overview

This project integrates:

- Natural Language Processing (NLP)
- TF-IDF Vectorization
- Logistic Regression Classifier
- Flask REST API
- Twilio WhatsApp Sandbox
- Ngrok for local deployment

The bot receives a message on WhatsApp, processes it using a trained ML model, and responds with:

- Prediction (REAL / FAKE)
- Confidence Score

---

## 🧠 Model Details

- Algorithm: Logistic Regression
- Feature Extraction: TF-IDF
- Dataset: Fake & Real News Dataset (Kaggle)
- Accuracy: ~95%

---

## 🏗 Project Architecture

User → WhatsApp → Twilio → Flask API → ML Model → Prediction → WhatsApp Reply

---

## 📂 Project Structure

```
AI-WhatsApp-Fake-News-Detection-Bot/
│
├── app.py
├── model_training.ipynb
├── model.pkl
├── requirements.txt
├── README.md
└── result.img/
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

```bash
git clone https://github.com/yourusername/AI-WhatsApp-Fake-News-Detection-Bot.git
cd AI-WhatsApp-Fake-News-Detection-Bot
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Train Model

Run:

```
model_training.ipynb
```

This will generate:

- model.pkl
- vectorizer.pkl

---

## 📲 WhatsApp Integration

1. Create Twilio Account
2. Activate WhatsApp Sandbox
3. Install ngrok
4. Run:

```bash
python app.py
ngrok http 5000
```

5. Copy HTTPS link to Twilio webhook:

```
https://your-ngrok-url/whatsapp
```

Method: POST

---

## 🧪 Example Output

User Message:
```
Breaking news: Government launches secret alien program
```

Bot Response:
```
⚠️ This news is likely FAKE
Confidence: 97.45%
```

---

## 📊 Technologies Used

- Python
- Flask
- Twilio API
- Scikit-Learn
- NLTK
- Pandas
- Ngrok

---

## 💡 Future Improvements

- BERT Transformer Model
- Cloud Deployment (Render / AWS)
- Admin Dashboard
- Database Logging
- Multi-language Support

---

## 👨‍💻 Author

BATTULA VENKATA KRISHNA KARTHIK.

---

## 📜 License

This project is for educational and research purposes.
