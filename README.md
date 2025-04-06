# Central-or-Centel
# 🏀 Central or Centel?

**Is that tweet real, or is it Ballsack?**

Central or Centel is a real-time tweet verification tool that helps users quickly determine whether an NBA-related tweet is from a trusted journalist or a parody account. Built using machine learning and a custom dataset, this project aims to fight misinformation in the sports world — especially on Twitter.

---

## 🚀 Features

- 🧠 Uses a **Multinomial Naive Bayes** model trained on real and fake NBA tweets
- 📊 Built with a **balanced dataset** of 1,000 tweets (500 real, 500 fake)
- 🌐 Streamlit web app that accepts tweet input and returns:
  - ✅ Real or Fake verdict
  - 🎯 Confidence score
- 📚 Viewable **prediction log** (log.csv) showing past inputs and model results
- 📝 Input validation to ensure tweet format starts with a Twitter handle (e.g., `@wojespn`)

---

## 🏗️ How It Works

1. Tweets are vectorized using `CountVectorizer`
2. The model analyzes word frequency patterns learned from the dataset
3. A prediction ("real" or "fake") is returned with a confidence score
4. The prediction is logged in a CSV for transparency

---

## 📁 File Structure

```
central-or-centel/
├── app.py                  # Streamlit app
├── main.py                 # Terminal version
├── ml_verify.py            # Loads model and predicts tweet label
├── train_model.py          # Trains and saves the ML model
├── log.csv                 # Log of all tweet predictions
├── model/
│   ├── tweet_model.pkl     # Trained Naive Bayes model
│   └── vectorizer.pkl      # Trained CountVectorizer
└── combined_tweets_1000.csv  # Dataset with 500 real, 500 fake tweets
```

---

## 🔧 Setup Instructions

1. Make sure you are using **Python 3.10** (important for compatibility!)

```bash
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

2. Train the model:
```bash
python train_model.py
```

3. Run the app:
```bash
streamlit run app.py
```

---

## 📦 Dependencies
- `scikit-learn`
- `pandas`
- `streamlit`

You can install them manually or via `requirements.txt`.

---

## 🧠 Future Enhancements

- Expand dataset to include all major sports (NFL, MLB, tennis, etc.)
- Add Twitter API integration to pull live tweets
- Include mobile-friendly view
- Integrate user feedback to improve model accuracy

---

## 🙌 Author
**Krishang Khandelwal**  
UC San Diego – Data Science Major

> "Fake or Facts lets you separate sports truth from trash in one click."

