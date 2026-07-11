import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Score Motor", layout="wide")
st.title("⚽ API Anahtarını Temizleyerek Test Et")

# Boşlukları temizleyen .strip() ekledik
RAW_KEY = "96805f1e5e0037781da5aeb07471a64e"
API_KEY = RAW_KEY.strip()

url = "https://v3.football.api-sports.io/fixtures"
headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "v3.football.api-sports.io"
}

if st.button("🚀 Temizlenmiş Anahtarla Test Et"):
    querystring = {"date": "2026-07-12", "league": "188", "season": "2026"}
    response = requests.get(url, headers=headers, params=querystring)
    
    st.write("Status Code:", response.status_code)
    st.write("Gelen Veri:", response.json())
