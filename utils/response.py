def get_motivational_quote(emotion):
    quotes = {
        "sad": [
            "It's okay to feel sad. Remember, every storm runs out of rain",
            "Tough times never last, but tough people do",
            "Even the darkest night will end and the sun will rise again"
        ],
        "happy": [
            "Keep shining, your happiness is contagious",
            "Stay grateful and keep spreading positivity",
            "Happiness looks good on you — wear it every day"
        ],
        "angry": [
            "Breathe deeply. Don’t let anger control your peace",
            "Channel your anger into something productive",
            "Let it go peace of mind is priceless"
        ],
        "tired": [
            "Rest when you need to. You’re doing your best",
            "Take a deep breath. You deserve a break",
            "Even small steps forward still count as progress"
        ],
        "stressed": [
            "You’re stronger than you think",
            "Take one thing at a time. You’ve got this",
            "Don’t let stress steal today’s peace"
        ],
        "neutral": [
            "Every day is a new chance to grow",
            "Stay focused, Stay kind, Stay you",
            "Balance is the key to happiness"
        ]
    }

    selected_quotes = quotes.get(emotion, quotes["neutral"])
    import random
    return random.choice(selected_quotes)