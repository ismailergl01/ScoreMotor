import streamlit as st
import requests

st.set_page_config(page_title="Score Motor", layout="wide")
st.title("⚽ Son Deneme: URL ile Sorgu")

API_KEY = "96805f1e5e0037781da5aeb07471a64e"
url = "https://v3.football.api-sports.io/fixtures"

if st.button("🚀 URL Üzerinden Sorgula"):
    # Anahtarı doğrudan parametre olarak ekliyoruz
    params = {
        "date": "2026-07-12",
        "league": "188",
        "key": API_KEY  # Anahtarı buraya ekledik
    }
    
    response = requests.get(url, params=params)
    
    st.write("Status Code:", response.status_code)
    st.write(response.json())
