import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle
import os

# Load dataset
df = pd.read_csv("combined_tweets_200.csv")

# Features and labels
X = df["tweet"]
y = df["label"]

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Convert text into feature vectors
vectorizer = CountVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)

# Train the Naive Bayes model
model = MultinomialNB()
model.fit(X_train_vec, y_train)

# Make sure the 'model' folder exists
os.makedirs("model", exist_ok=True)

# Save the trained model
with open("model/tweet_model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save the vectorizer
with open("model/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model and vectorizer saved successfully!")
