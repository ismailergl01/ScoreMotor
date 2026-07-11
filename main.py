import streamlit as st
import requests

st.set_page_config(page_title="Score Motor", layout="wide")
st.title("⚽ Son Deneme: 2026 Tarih ve Sezonu")

API_KEY = "96805f1e5e0037781da5aeb07471a64e"

if st.button("🚀 Sorgula"):
    url = "https://v3.football.api-sports.io/fixtures"
    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    # API'nin istediği güncel tarih ve 2026 sezonu
    querystring = {"date": "2026-07-12", "league": "188", "season": "2026"}
    
    response = requests.get(url, headers=headers, params=querystring)
    
    st.write("Status Code:", response.status_code)
    st.write(response.json())
