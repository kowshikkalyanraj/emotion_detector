import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

def get_gemini_answer(prompt):
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            print("❌ GEMINI_API_KEY not found in .env file")
            return "Error: API key missing."

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-2.0-flash")

        print("📩 Sending prompt to Gemini:", prompt)
        response = model.generate_content(prompt)
        print("✅ Gemini response received")
        return response.text.strip()

    except Exception as e:
        print(f"❌ Gemini API Error: {e}")
        return "Error: Could not get response from Gemini API."
