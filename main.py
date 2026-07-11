import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Score Motor", layout="wide")
st.title("⚽ Geçmiş Sezon Testi (2024)")

API_KEY = "96805f1e5e0037781da5aeb07471a64e"
url = "https://v3.football.api-sports.io/fixtures"
headers = {
    "x-rapidapi-key": API_KEY,
    "x-rapidapi-host": "v3.football.api-sports.io"
}

if st.button("🚀 2024 Sezonundan Maç Çek"):
    # API'nin izin verdiği 2024 sezonunu kullanıyoruz
    querystring = {"date": "2024-07-12", "league": "188", "season": "2024"}
    response = requests.get(url, headers=headers, params=querystring)
    
    st.write("Status Code:", response.status_code)
    data = response.json()
    st.write(data)
