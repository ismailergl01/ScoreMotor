import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Score Motor", layout="wide")
st.title("⚽ API'nin İzin Verdiği Güncel Test")

API_KEY = "27c2007344ae038775e22cf529e7a03"
url = "https://v3.football.api-sports.io/fixtures"
headers = {"x-rapidapi-key": API_KEY, "x-rapidapi-host": "v3.football.api-sports.io"}

# API'nin istediği güncel tarih: 2026-07-12 (Bugün)
if st.button("🚀 Bugünü Sorgula (2026-07-12)"):
    # Sezon parametresini kaldırıyoruz, API tarihle eşleşen en güncel sezonu otomatik bulsun
    querystring = {"date": "2026-07-12", "league": "188"}
    response = requests.get(url, headers=headers, params=querystring)
    
    st.write("Status Code:", response.status_code)
    data = response.json()
    st.write(data)
