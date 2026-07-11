import streamlit as st
import requests

st.title("Score Motor - Maç Analiz Paneli")

# API Ayarları
url = "https://v3.football.api-sports.io/fixtures"
querystring = {"date": "2026-07-11"}
headers = {
    "x-rapidapi-key": "27c2007344ae038775e22cf529e7a032",
    "x-rapidapi-host": "v3.football.api-sports.io"
}

if st.button("Maçları Getir"):
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    
    if "response" in data:
        st.write(f"Toplam {len(data['response'])} maç bulundu.")
        for match in data['response']:
            home = match['teams']['home']['name']
            away = match['teams']['away']['name']
            st.write(f"⚽ {home} vs {away}")
    else:
        st.write("Veri alınamadı, API anahtarını kontrol et.")
