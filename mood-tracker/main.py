import streamlit as st
import pandas as pd
import datetime
import csv
import os

MOOD_FILE = "mood_log.csv"

def load_mood_data():
    if not os.path.exists(MOOD_FILE):
        return pd.DataFrame(columns=["Date", "Mood"])
    return pd.read_csv(MOOD_FILE, encoding="utf-8")

def save_mood_data(date, mood):
    # Open the file in append mode with UTF-8 encoding
    with open(MOOD_FILE, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, mood])

st.title("🌈 Mood Tracker")

today = datetime.date.today()

st.subheader("How are your feeling today?")

mood = st.selectbox("Select your mood", ["Happy 😊", "Sad 😔", "Angry 😠", "Neutral 😐"])

if st.button("Log Mood"):
    save_mood_data(today, mood)
    st.success("Mood Logged Successfully!")

data = load_mood_data()

if not data.empty:
    st.subheader("Mood Trends Over Time 📈")
    data["Date"] = pd.to_datetime(data["Date"])
    mood_counts = data.groupby("Mood").count()["Date"]
    st.bar_chart(mood_counts)

st.write("Build with 🛠️❤️ by [Jawad Hassan](https://github.com/JawadJamro)")
