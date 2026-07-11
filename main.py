import streamlit as st
import requests
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Score Motor", layout="wide")
st.title("⚽ Score Motor - Bugünün Maçları")

API_KEY = "27c2007344ae038775e22cf529e7a03"
url = "https://v3.football.api-sports.io/fixtures"
headers = {"x-rapidapi-key": API_KEY, "x-rapidapi-host": "v3.football.api-sports.io"}

secilen_tarih = st.date_input("Tarih Seçin", datetime.today())
tarih_str = secilen_tarih.strftime("%Y-%m-%d")

if st.button("🚀 Tüm Maçları Getir"):
    # Lig ID'lerini çıkardık, direkt tarihe göre sorgu yapıyoruz
    querystring = {"date": tarih_str}
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()
    
    tum_maclar = []
    
    if "response" in data and len(data['response']) > 0:
        for match in data['response']:
            # Sadece senin ekran görüntüsündeki gibi futbol maçlarını al
            if match['fixture']['status']['short'] in ['NS', 'TBD']:
                tum_maclar.append({
                    "Lig": match['league']['name'],
                    "Ev": match['teams']['home']['name'],
                    "Dep": match['teams']['away']['name'],
                    "Saat": match['fixture']['date'][11:16]
                })
    
    if tum_maclar:
        df = pd.DataFrame(tum_maclar)
        st.dataframe(df, width=1500)
    else:
        st.info("Bu tarihte API üzerinden veri gelmedi. Lütfen tarih seçimini kontrol et.")
