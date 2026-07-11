import streamlit as st
import requests

st.set_page_config(page_title="Score Motor", layout="wide")
st.title("⚽ Lig Değiştirerek Test Et")

API_KEY = "96805f1e5e0037781da5aeb07471a64e"

if st.button("🚀 Premier Lig (ID: 39) Dene"):
    url = "https://v3.football.api-sports.io/fixtures"
    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    # İsveç (188) yerine İngiltere (39) deniyoruz
    querystring = {"date": "2026-07-12", "league": "39", "season": "2026"}
    
    response = requests.get(url, headers=headers, params=querystring)
    
    st.write("Status Code:", response.status_code)
    st.write(response.json())
