from voice_input import get_voice_input
from utils.sentiment_analysis import analyze_sentiment
from utils.response import get_motivational_quote

def main():
    print("🌸 Starting Smart Mental Health Companion...\n")

    # 🎙️ Voice Input
    voice_text = get_voice_input()
    print(f"\n🗣️ Voice input captured: {voice_text}")

    # 💬 Sentiment Analysis
    sentiment = analyze_sentiment(voice_text)
    print(f"💭 Sentiment detected: {sentiment}")

    # 💡 Response
    quote = get_motivational_quote(sentiment)

    print("\n✨ Final Response ✨")
    print(f"Detected Sentiment: {sentiment}")
    print(f"Motivational Quote: {quote}")

if __name__ == "__main__":
    main()
