import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Score Motor", layout="wide")
st.title("⚽ Score Motor - API Bağlantı Testi")

# API Anahtarını en güvenli şekilde tanımlıyoruz
API_KEY = "27c2007344ae038775e22cf529e7a03"
url = "https://v3.football.api-sports.io/fixtures"
headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "v3.football.api-sports.io"
}

secilen_tarih = st.date_input("Tarih Seçin", datetime.today())
tarih_str = secilen_tarih.strftime("%Y-%m-%d")

if st.button("🚀 Sorgula"):
    # 188 numaralı lig için doğrudan sorgu
    querystring = {"date": tarih_str, "league": "188", "season": "2026"}
    response = requests.get(url, headers=headers, params=querystring)
    
    st.write("Bağlantı Durumu:", response.status_code)
    data = response.json()
    st.write(data)
