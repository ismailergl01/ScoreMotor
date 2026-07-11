import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Score Motor Pro", layout="wide")
st.title("⚽ Debug Mode: API Yanıtı")

API_KEY = "27c2007344ae038775e22cf529e7a03"
url = "https://v3.football.api-sports.io/fixtures"
headers = {"x-rapidapi-key": API_KEY, "x-rapidapi-host": "v3.football.api-sports.io"}

# Lig ID'leri
lig_idleri = ["188", "103"]

secilen_tarih = st.date_input("Tarih Seçin", datetime.today())
tarih_str = secilen_tarih.strftime("%Y-%m-%d")

if st.button("🚀 Ham Veriyi Çek"):
    for lig in lig_idleri:
        # Önce 2026, olmazsa 2025 ile deneyeceğiz
        for sezon in ["2026", "2025"]:
            querystring = {"date": tarih_str, "league": lig, "season": sezon}
            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()
            
            st.write(f"Lig: {lig} | Sezon: {sezon}")
            st.write(data) # API'den dönen her şeyi ekrana dökecek
            
            if "response" in data and len(data['response']) > 0:
                st.success(f"MAÇ BULUNDU! Sezon: {sezon}")
                break
