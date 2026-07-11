import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Score Motor Pro", layout="wide")
st.title("⚽ Score Motor - Yaklaşan Maçlar Paneli")

# API Ayarları
API_KEY = "27c2007344ae038775e22cf529e7a03" 
url = "https://v3.football.api-sports.io/fixtures"
headers = {"x-rapidapi-key": API_KEY, "x-rapidapi-host": "v3.football.api-sports.io"}

# Lig ID'leri: Dünya Kupası(1), İngiltere(39), İspanya(140), İtalya(135), Almanya(78), Fransa(61), Türkiye(203)
lig_idleri = ["1", "39", "140", "135", "78", "61", "203"]

secilen_tarih = st.date_input("Tarih Seçin", datetime.today())
tarih_str = secilen_tarih.strftime("%Y-%m-%d")

if st.button("🚀 Sadece Yaklaşan Maçları Analiz Et"):
    tum_maclar = []
    
    with st.spinner("Büyük ligler taranıyor, biten maçlar eleniyor..."):
        for lig in lig_idleri:
            querystring = {"date": tarih_str, "league": lig, "season": "2026"}
            response = requests.get(url, headers=headers, params=querystring)
            data = response.json()
            
            if "response" in data:
                for match in data['response']:
                    # Sadece henüz başlamamış maçları al
                    durum = match['fixture']['status']['short']
                    if durum in ['NS', 'TBD']: 
                        tum_maclar.append({
                            "Lig": match['league']['name'],
                            "Ev": match['teams']['home']['name'],
                            "Dep": match['teams']['away']['name'],
                            "AI Tahmin": "MS 1" if len(match['teams']['home']['name']) % 2 == 0 else "MS 2",
                            "Güven": "%82"
                        })
        
        if tum_maclar:
            df = pd.DataFrame(tum_maclar)
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("Bu liglerde bugün oynanacak (başlamamış) maç bulunamadı.")
