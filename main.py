import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Score Motor Pro", layout="wide")
st.title("⚽ Score Motor - 2026 Analiz")

API_KEY = "27c2007344ae038775e22cf529e7a03"
url = "https://v3.football.api-sports.io/fixtures"
headers = {"x-rapidapi-key": API_KEY, "x-rapidapi-host": "v3.football.api-sports.io"}

# İsveç (188) ve Norveç (103) liglerinin 2026 sezon ID'leri ile sorgu
lig_idleri = ["188", "103"]

secilen_tarih = st.date_input("Tarih Seçin", datetime.today())
tarih_str = secilen_tarih.strftime("%Y-%m-%d")

if st.button("🚀 Maçları Getir"):
    tum_maclar = []
    
    for lig in lig_idleri:
        # Season parametresini 2026 olarak netleştirdik
        querystring = {"date": tarih_str, "league": lig, "season": "2026"}
        response = requests.get(url, headers=headers, params=querystring)
        data = response.json()
        
        if "response" in data and len(data['response']) > 0:
            for match in data['response']:
                tum_maclar.append({
                    "Lig": match['league']['name'],
                    "Ev": match['teams']['home']['name'],
                    "Dep": match['teams']['away']['name'],
                    "Durum": match['fixture']['status']['short'],
                    "Saat": match['fixture']['date'][11:16]
                })
    
    if tum_maclar:
        df = pd.DataFrame(tum_maclar)
        st.dataframe(df, width=1500)
    else:
        st.info("⚠️ Bu tarih ve sezon (2026) için maç bulunamadı.")
