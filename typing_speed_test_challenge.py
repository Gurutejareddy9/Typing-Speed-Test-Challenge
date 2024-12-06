import random
import time
from typing import Dict

# Sample Quotes for Typing Test
quotes = [
    "The quick brown fox jumps over the lazy dog",
    "Python is a widely used general-purpose, interpreted, interactive and object-oriented scripting language",
    "Typing master is not just about speed, it's about accuracy and flow",
    # Add more quotes here as needed
]

# Badge Rewards
badges: Dict[float, str] = {
    0.95: "🏆 **Mastery** (95%+ Accuracy)",
    0.85: "🥇 **Expert** (85-94% Accuracy)",
    0.70: "🥈 **Pro** (70-84% Accuracy)",
    0.00: "🤖 **Newbie** (<70% Accuracy)"
}

def calculate_accuracy(input_text: str, original_text: str) -> float:
    """Calculate accuracy between input and original text."""
    # Simple accuracy checker, improve as needed
    correct_chars = sum(1 for a, b in zip(input_text, original_text) if a == b)
    return correct_chars / len(original_text)

def get_badge(accuracy: float) -> str:
    """Fetch badge based on accuracy level."""
    for threshold, badge in badges.items():
        if accuracy >= threshold:
            return badge
    return badges[0.00]  # Default to lowest badge

def typing_speed_test() -> None:
    """Conduct a typing speed test."""
    print("Typing Speed Test Challenge")
    print("-------------------------------")
    original_quote = random.choice(quotes)
    print(f"Type this: \n\n{original_quote}\n")
    
    # Start timer
    input("Press Enter when ready...")
    start_time = time.time()
    typed_quote = input()
    end_time = time.time()
    
    # Calculate elapsed time, speed, and accuracy
    elapsed_time = end_time - start_time
    accuracy = calculate_accuracy(typed_quote, original_quote)
    num_words = len(original_quote.split())
    speed_wpm = num_words / elapsed_time * 60 if elapsed_time > 0 else 0
    
    # Display results
    print("\nResults:")
    print(f"**Speed:** {speed_wpm:.2f} wpm")
    print(f"**Accuracy:** {accuracy*100:.2f}% - {get_badge(accuracy)}")
    print(f"**Elapsed Time:** {elapsed_time:.2f} seconds")

if __name__ == "__main__":
    typing_speed_test()