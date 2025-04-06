import pickle

# Load the trained model and vectorizer
with open("model/tweet_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

with open("model/vectorizer.pkl", "rb") as vectorizer_file:
    vectorizer = pickle.load(vectorizer_file)

def verify_tweet_ml(tweet):
    """
    Predict if a tweet is real or fake using the trained model.
    Returns the label and confidence score.
    """
    tweet_vector = vectorizer.transform([tweet])
    prediction = model.predict(tweet_vector)[0]
    proba = model.predict_proba(tweet_vector)[0]
    confidence = max(proba)  # Confidence of the predicted label
    return prediction, round(confidence * 100, 2)  # Return percentage

