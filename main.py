import streamlit as st
import requests

st.set_page_config(page_title="Score Motor", layout="wide")
st.title("⚽ Son Çare: Kesin Header Yapılandırması")

# Anahtarı buraya tırnaksız/boşluksuz yapıştır
API_KEY = "96805f1e5e0037781da5aeb07471a64e"

if st.button("🚀 Sorgula"):
    url = "https://v3.football.api-sports.io/fixtures"
    # API-Sports dokümantasyonunda tam olarak istedikleri header yapısı
    headers = {
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': 'v3.football.api-sports.io'
    }
    querystring = {"date": "2026-07-12", "league": "188"}
    
    response = requests.get(url, headers=headers, params=querystring)
    
    st.write("Status Code:", response.status_code)
    st.write(response.json())
