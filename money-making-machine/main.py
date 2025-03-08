import streamlit as st
import random
import time
import requests

st.title("💰 Money Making Machine")

def genrate_money():
    return random.randint(1, 1000)

st.subheader("Fast Money Maker")
if st.button("Genrate Money"):
    st.write("Counting your money...")
    time.sleep(1)
    amount = genrate_money()
    st.success(f"You made ${amount}!")

def fetch_side_hustle():
    try:
        response = requests.get("http://127.0.0.1:8000/side_hustles")
        if response.status_code == 200:
            hustles = response.json()
            return hustles["side_hustles"]
        else:
            return "Freelancing"
    except:
        return "Something went wrong!"

st.subheader("Side Hustle Ideas")
if st.button("Genrate Hustle"):
    ideas = fetch_side_hustle()
    st.info(ideas)

# Move this function outside the `if` block
def fetch_money_quote():
    try:
        response = requests.get("http://127.0.0.1:8000/money_quotes")
        if response.status_code == 200:
            quotes = response.json()
            return quotes["money_quotes"]
        else:
            return "Money is the root of all evil!"
    except:
        return "Something went wrong!"

st.subheader("Money Making Motivation")
if st.button("Get Inspired"):
    quote = fetch_money_quote()
    st.info(quote)
