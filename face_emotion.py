import cv2
from deepface import DeepFace
from utils.gemini_api import get_gemini_answer
from response import get_motivational_quote

def detect_emotion(frame):
    try:
        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        if isinstance(result, list):
            emotion = result[0]['dominant_emotion']
        else:
            emotion = result['dominant_emotion']

        print(f"Detected emotion: {emotion}")

        # Combine with Gemini for motivational quote
        prompt = (
            f"The user appears {emotion}. "
            "Write a short, warm, and empathetic motivational quote or suggestion "
            "that encourages emotional balance."
        )

        gemini_msg = get_gemini_answer(prompt)
        if not gemini_msg or gemini_msg.startswith("Error:"):
            gemini_msg = get_motivational_quote(emotion)

        return emotion, gemini_msg

    except Exception as e:
        print(f"❌ Emotion detection error: {e}")
        return "unknown", "Couldn't detect emotion. Please try again."
