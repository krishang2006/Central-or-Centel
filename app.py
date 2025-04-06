import streamlit as st
from ml_verify import verify_tweet_ml
import csv
import os
import pandas as pd

LOG_FILE = "log.csv"

def log_prediction(tweet, verdict, confidence):
    """Save the prediction to log.csv."""
    with open(LOG_FILE, "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([tweet, verdict, confidence])

def load_log():
    """Load the prediction log as a DataFrame."""
    if not os.path.exists(LOG_FILE):
        return pd.DataFrame(columns=["Tweet", "Verdict", "Confidence"])
    return pd.read_csv(LOG_FILE, header=None, names=["Tweet", "Verdict", "Confidence"])

# Streamlit app layout
st.set_page_config(page_title="Central or Centel?", page_icon="🏀")

st.title("🏀 Central or Centel?")
st.markdown("---")

st.subheader("📝 Instructions")
st.markdown(
    "Paste a sports-related tweet starting with a **Twitter handle**.  \n\n"
    "**Example:**  \n"
    "`@wojespn LeBron James signs a 3-year deal with the Lakers`"
)

st.markdown("---")

tweet = st.text_area("📥 Enter tweet below:", height=150)

if st.button("🔍 Analyze Tweet"):
    if tweet.strip() == "":
        st.warning("🚫 Please enter a tweet.")
    elif not tweet.startswith("@"):
        st.warning("⚠️ Tweet must start with a Twitter handle (e.g., @wojespn)")
    else:
        verdict, confidence = verify_tweet_ml(tweet)
        st.success(f"✅ Verdict: **{verdict.upper()}**")
        st.info(f"📊 Confidence: **{confidence}%**")
        log_prediction(tweet, verdict, confidence)

# Optional log viewer
if st.checkbox("📚 Show Prediction Log"):
    df_log = load_log()
    if df_log.empty:
        st.info("No predictions logged yet.")
    else:
        st.markdown("### 🧾 Prediction Log")
        st.dataframe(df_log[::-1].reset_index(drop=True), use_container_width=True)
