import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("⚽ Score Motor: Kendi Verini Çek")

# Hedef site (Buraya maç skorlarının olduğu bir URL gelecek)
url = "https://www.mackolik.com/futbol/canli-sonuclar" # Örnek site

if st.button("🚀 Maçları Getir"):
    # Siteyi kandırmak için tarayıcı kimliği (User-Agent)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # BURASI KRİTİK: Sitedeki maçların olduğu kutucukları bulmalıyız
            # Örnek: Çoğu sitede maçlar 'div' veya 'li' içindedir
            maclar = soup.find_all('div', class_='mactablosu-class-adi') # class adını incelememiz lazım
            
            if maclar:
                for mac in maclar:
                    st.write(mac.text)
            else:
                st.warning("Veri bulunamadı. Sayfa yapısı değişmiş olabilir.")
        else:
            st.error(f"Siteye ulaşılamadı: {response.status_code}")
            
    except Exception as e:
        st.error(f"Hata: {e}")
