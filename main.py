from ml_verify import verify_tweet_ml
import csv
import os

LOG_FILE = "log.csv"

def log_prediction(tweet, verdict, confidence):
    """Save the result to log.csv"""
    with open(LOG_FILE, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([tweet, verdict, confidence])

def print_log():
    """Print the saved log of all predictions."""
    if not os.path.exists(LOG_FILE):
        print("📭 No log file found yet.\n")
        return

    with open(LOG_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if not rows:
            print("📭 Log is empty.")
            return

        print("\n📚 Tweet Log:")
        print("-" * 60)
        for tweet, verdict, confidence in rows:
            print(f"📝 {tweet}")
            print(f"✅ Verdict: {verdict} ({confidence}% confidence)")
            print("-" * 60)

def main():
    print("🏀 Fake or Facts: Sports Tweet Verifier (ML Edition)")
    print("---------------------------------------------------")
    print("📌 Example: @wojespn LeBron James signs extension with Lakers\n")

    while True:
        print("Choose an option:")
        print("1️⃣  Analyze a new tweet")
        print("2️⃣  View past predictions")
        print("3️⃣  Exit")

        choice = input("\nEnter 1, 2, or 3:\n> ")

        if choice == "1":
            tweet = input("\nPaste a tweet (start with @handle):\n> ")
            if not tweet.startswith("@"):
                print("⚠️ Please include a Twitter handle (e.g., @wojespn)\n")
                continue

            verdict, confidence = verify_tweet_ml(tweet)
            print(f"\n✅ Verdict: {verdict}")
            print(f"📊 Confidence: {confidence}%")
            print("-" * 40 + "\n")
            log_prediction(tweet, verdict, confidence)

        elif choice == "2":
            print_log()

        elif choice == "3":
            print("👋 Thanks for using Fake or Facts!")
            break

        else:
            print("❌ Invalid option. Please enter 1, 2, or 3.\n")

if __name__ == "__main__":
    main()