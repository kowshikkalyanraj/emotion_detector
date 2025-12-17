import sys, os, base64, cv2, numpy as np
sys.path.append(os.path.join(os.path.dirname(__file__), "Project_Smart_Mental_Health"))

from utils.gemini_api import get_gemini_answer
from face_emotion import detect_emotion
from sentiment_analysis import analyze_sentiment
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

# 🧩 Chat Route — Handles both text and voice input
@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({"response": "Please enter a valid message."})

        # Analyze sentiment
        sentiment = analyze_sentiment(user_message)
        print(f"User message: {user_message} | Sentiment: {sentiment}")

        # Generate AI response
        prompt = (
            f"The user message shows {sentiment} sentiment. "
            f"Respond empathetically and helpfully to: '{user_message}'."
        )
        gemini_response = get_gemini_answer(prompt)

        if not gemini_response or gemini_response.startswith("Error:"):
            return jsonify({"response": "Sorry, I couldn't generate a response right now."})

        return jsonify({"response": gemini_response})

    except Exception as e:
        print(f"❌ Flask error in /chat: {e}")
        return jsonify({"response": "An error occurred while processing your request."})


# 🧩 Emotion Detection Route
@app.route("/detect_emotion", methods=["POST"])
def detect_emotion_route():
    try:
        data = request.get_json()
        image_data = data.get("image", "")

        if not image_data:
            return jsonify({"error": "No image received."})

        # Decode base64 image
        header, encoded = image_data.split(",", 1)
        image_bytes = base64.b64decode(encoded)
        np_arr = np.frombuffer(image_bytes, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        print("Analyzing emotion from image...")
        emotion, quote = detect_emotion(frame)
        print(f"Detected emotion: {emotion}")

        return jsonify({"emotion": emotion, "quote": quote})

    except Exception as e:
        print(f"❌ Flask error in /detect_emotion: {e}")
        return jsonify({"error": "Could not detect emotion. Please try again."})


if __name__ == "__main__":
    print("🚀 Smart Mental Health Companion running at: http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
