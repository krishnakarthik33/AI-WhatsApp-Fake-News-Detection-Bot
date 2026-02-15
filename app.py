from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import joblib

# Load model and vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

app = Flask(__name__)

# ✅ ADD THIS PART HERE
@app.route("/")
def home():
    return "Fake News Detection App Running ✅"


# Your existing WhatsApp route
@app.route("/whatsapp", methods=["POST"])
def reply():
    incoming_msg = request.values.get("Body", "")

    vectorized_msg = vectorizer.transform([incoming_msg])
    prediction = model.predict(vectorized_msg)[0]
    probability = model.predict_proba(vectorized_msg).max()

    if prediction == 0:
        result = "⚠️ This news is likely FAKE"
    else:
        result = "✅ This news is likely REAL"

    response_msg = f"{result}\nConfidence: {round(probability*100,2)}%"

    resp = MessagingResponse()
    resp.message(response_msg)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
