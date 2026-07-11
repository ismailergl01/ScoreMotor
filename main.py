import streamlit as st
import requests

st.set_page_config(page_title="Score Motor", layout="wide")
st.title("⚽ Sezon Parametreli Kesin Çözüm")

API_KEY = "96805f1e5e0037781da5aeb07471a64e"

if st.button("🚀 2026 Sezonu ile Sorgula"):
    url = "https://v3.football.api-sports.io/fixtures"
    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    # Sezonu 2026 olarak net bir şekilde ekledik
    querystring = {"date": "2026-07-12", "league": "188", "season": "2026"}
    
    response = requests.get(url, headers=headers, params=querystring)
    
    st.write("Status Code:", response.status_code)
    st.write(response.json())
